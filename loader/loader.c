/* SPDX-License-Identifier: BSD-2-Clause */
/*
 * zOS loader, prototype for two QEMU RISC-V machines: "virt" (the default) and,
 * built with -DPLAT_HIFIVE, the model of the HiFive Unleashed, the platform of
 * seL4's verified RISC-V configurations.
 *
 * Shows the boot screen, checks the kernel image against the hash in its
 * header, shows the result, and starts the kernel only if the hash matches.
 *
 * What this checks: that the image is the one the header describes. A hash
 * stored next to the image protects against accidents, not against someone who
 * can rewrite both. Authenticity needs a signature checked against a key that
 * lives in the loader; that is the next step and is not part of this file.
 *
 * What this does not do: find the image on a storage device. In this prototype
 * QEMU puts the image at IMG_BASE before the loader starts.
 *
 * Image layout (little endian), the header is 64 bytes and the payload follows:
 *   0  u32 magic    "zOSK"
 *   4  u32 version  1
 *   8  u64 length   payload bytes
 *  16  u64 entry    offset of the entry point from the image start
 *  24  u8[32]       SHA-256 over header bytes 0..23 followed by the payload
 *  56  u8[8]        reserved, zero
 */
#include <stdint.h>
#include "sha256.h"

void zos_splash_frame(uint8_t *px, int w, int h);
void zos_splash_row(uint8_t *px, int w, int h, int row, const char *left, const char *right, int strong);
void zos_splash_progress(uint8_t *px, int w, int h, int step, int total);
void zos_splash_footer(uint8_t *px, int w, int h, const char *s);

#ifdef PLAT_HIFIVE
/* Runs in supervisor mode as OpenSBI's payload. The board has no display, and QEMU's model cannot be given one, so the
 * loader draws into memory only; a recorder reads the picture there at every update (see zos_frame_shown). The image
 * header sits 64 bytes before 0x82000000, so that a payload linked there, such as seL4's ELF loader, starts in place. */
#define UART      0x10010000UL      /* SiFive UART: txdata +0, bit 31 = full */
#define IMG_BASE  0x81ffffc0UL
#else
#define UART      0x10000000UL      /* ns16550a */
#define FWCFG     0x10100000UL      /* QEMU fw_cfg: data +0, selector +8, DMA +16 */
#define IMG_BASE  0x80400000UL      /* where QEMU puts the kernel image */
#endif
#define FB_ADDR   0x81000000UL      /* 32-bit pixels the display scans out */
#define SHADE_BUF 0x81800000UL      /* one shade 0..3 per byte, what the splash draws into */
#define MAX_PAYLOAD (8UL << 20)
enum { W = 1120, H = 832, STEPS = 4 };

struct zimg { uint32_t magic, version; uint64_t length, entry; uint8_t sha256[32]; uint8_t reserved[8]; };
#define ZIMG_MAGIC 0x4b534f7aU      /* "zOSK" */

/* ---- serial ---- */
static void putc_(char c) {
#ifdef PLAT_HIFIVE
    while (*(volatile uint32_t *)UART & 0x80000000U) {}
    *(volatile uint32_t *)UART = (uint8_t)c;
#else
    while (!(*(volatile uint8_t *)(UART + 5) & 0x20)) {}
    *(volatile uint8_t *)UART = (uint8_t)c;
#endif
}
static void puts_(const char *s) { for (; *s; s++) putc_(*s); }
static void hex(const uint8_t *p, int n) {
    for (int i = 0; i < n; i++) { putc_("0123456789abcdef"[p[i] >> 4]); putc_("0123456789abcdef"[p[i] & 15]); }
}

#ifndef PLAT_HIFIVE
/* ---- fw_cfg and the ram framebuffer ---- */
static void fw_select(uint16_t sel) { *(volatile uint16_t *)(FWCFG + 8) = __builtin_bswap16(sel); }
static uint8_t fw_byte(void) { return *(volatile uint8_t *)FWCFG; }
static uint32_t fw_be32(void) { uint32_t v = 0; for (int i = 0; i < 4; i++) v = v << 8 | fw_byte(); return v; }

static int fw_find(const char *name, uint16_t *sel) {     /* the file directory is selector 0x19 */
    fw_select(0x19);
    uint32_t count = fw_be32();
    while (count--) {
        fw_be32();                                          /* size */
        uint16_t s = (uint16_t)(fw_byte() << 8); s |= fw_byte();
        fw_byte(); fw_byte();                               /* reserved */
        int same = 1, end = 0;
        for (int i = 0; i < 56; i++) {                      /* always consume the whole 56-byte name field */
            uint8_t c = fw_byte();
            if (end) continue;                              /* padding after the terminator */
            if (c != (uint8_t)name[i]) same = 0;
            if (!c) end = 1;
        }
        if (same) { *sel = s; return 1; }
    }
    return 0;
}

struct fwdma { uint32_t control, length; uint64_t address; };   /* big endian on the wire */

static int fw_write(uint16_t sel, const void *buf, uint32_t len) {
    volatile struct fwdma d;
    d.control = __builtin_bswap32((uint32_t)sel << 16 | 0x08 | 0x10);    /* select + write */
    d.length = __builtin_bswap32(len);
    d.address = __builtin_bswap64((uint64_t)(uintptr_t)buf);
    __sync_synchronize();
    *(volatile uint64_t *)(FWCFG + 16) = __builtin_bswap64((uint64_t)(uintptr_t)&d);
    while (__builtin_bswap32(d.control) & ~1U) {}                          /* bit 0 is the error flag */
    return !(__builtin_bswap32(d.control) & 1);
}

struct ramfb { uint64_t addr; uint32_t fourcc, flags, width, height, stride; } __attribute__((packed));

static int ramfb_init(void) {
    uint16_t sel;
    if (!fw_find("etc/ramfb", &sel)) return 0;
    struct ramfb c;
    c.addr = __builtin_bswap64(FB_ADDR);
    c.fourcc = __builtin_bswap32(0x34325258);              /* 'XR24': 8 bits each of x, r, g, b */
    c.flags = 0;
    c.width = __builtin_bswap32(W); c.height = __builtin_bswap32(H); c.stride = __builtin_bswap32(W * 4);
    return fw_write(sel, &c, sizeof c);
}
#endif

/* Called after every finished picture. It does nothing; a recorder sets a breakpoint here and reads FB_ADDR. */
__attribute__((noinline)) void zos_frame_shown(void) { __asm__ volatile(""); }

/* four shades to real pixels: the thin layer between the splash and the display */
static void present(int have_display) {
    if (!have_display) return;
    static const uint32_t pal[4] = { 0x000000, 0x555555, 0xAAAAAA, 0xFFFFFF };
    const uint8_t *s = (const uint8_t *)SHADE_BUF;
    volatile uint32_t *d = (volatile uint32_t *)FB_ADDR;
    for (long i = 0; i < (long)W * H; i++) d[i] = pal[s[i] & 3];
    zos_frame_shown();
}

static void halt(void) { for (;;) __asm__ volatile("wfi"); }

void loader_main(unsigned long hartid, unsigned long dtb) {
    uint8_t *px = (uint8_t *)SHADE_BUF;
    const struct zimg *img = (const struct zimg *)IMG_BASE;
    uint8_t digest[32];
    char line[36];

    puts_("zOS loader\n");
#ifdef PLAT_HIFIVE
    int disp = 1;
    puts_("display: memory only\n");
#else
    int disp = ramfb_init();
    puts_(disp ? "display: ramfb\n" : "display: none\n");
#endif

    zos_splash_frame(px, W, H);
    zos_splash_row(px, W, H, 0, "firmware \xb7 root of trust", "assumed", 0);
    zos_splash_row(px, W, H, 1, "bootloader", "assumed", 0);
    zos_splash_progress(px, W, H, 1, STEPS);
    present(disp);

    int ok = img->magic == ZIMG_MAGIC && img->version == 1 && img->length <= MAX_PAYLOAD &&
             img->entry >= sizeof *img && img->entry < sizeof *img + img->length;
    zos_splash_row(px, W, H, 2, "kernel image header", ok ? "well-formed" : "malformed", ok);
    zos_splash_progress(px, W, H, 2, STEPS);
    puts_(ok ? "header: ok\n" : "header: bad\n");

    int match = 0;
    if (ok) {
        struct sha256 s;
        sha256_init(&s);
        sha256_update(&s, (const uint8_t *)img, 24);
        sha256_update(&s, (const uint8_t *)img + sizeof *img, img->length);
        sha256_final(&s, digest);
        uint8_t diff = 0;
        for (int i = 0; i < 32; i++) diff |= digest[i] ^ img->sha256[i];
        match = diff == 0;

        puts_("sha256: "); hex(digest, 32); puts_("\n");
        zos_splash_row(px, W, H, 3, "kernel image \xb7 SHA-256", match ? "hash matches" : "hash differs", 1);
        int n = 0;
        for (int i = 0; i < 16; i++) {
            if (i && i % 4 == 0) line[n++] = ' ';
            line[n++] = "0123456789abcdef"[digest[i] >> 4]; line[n++] = "0123456789abcdef"[digest[i] & 15];
        }
        line[n] = 0;
        zos_splash_row(px, W, H, 4, line, "first 128 bits", 0);
        zos_splash_progress(px, W, H, 3, STEPS);
    }
    present(disp);

    if (!ok || !match) {
        zos_splash_footer(px, W, H, "boot halted. the kernel was not started.");
        present(disp);
        puts_("halt: image rejected\n");
        halt();
    }

    zos_splash_progress(px, W, H, STEPS, STEPS);
    zos_splash_footer(px, W, H, "starting the kernel.");
    present(disp);
    puts_("jump\n");
    __asm__ volatile("fence.i");
    ((void (*)(unsigned long, unsigned long))(IMG_BASE + img->entry))(hartid, dtb);
    halt();
}
