/* SPDX-License-Identifier: BSD-2-Clause */
/*
 * zOS boot splash, prototype.
 *
 * Draws one frame of the first screen a person sees after power-on: a grey
 * panel in four shades, bevelled edges, crisp grey-scale type, and the boot
 * report of what was loaded and what we know about each part.
 *
 * Freestanding: no libc, no heap, no floating point. The caller hands in a
 * framebuffer of one byte per pixel holding a shade 0..3 (black, dark grey,
 * light grey, white) and the boot step to show. Mapping shades to the real
 * display format is the job of the (isolated) display driver, not of this file.
 */
#include <stdint.h>

struct glyph { uint8_t ch, w, adv; int8_t left; uint16_t off; };
struct font { uint8_t height, count; const struct glyph *g; const uint8_t *data; };
#include "glyphs.h"

enum { BLACK, DARK, LIGHT, WHITE };

struct fb { uint8_t *px; int w, h; };

static void rect(struct fb *f, int x, int y, int w, int h, uint8_t c) {
    for (int j = y; j < y + h; j++)
        if (j >= 0 && j < f->h)
            for (int i = x; i < x + w; i++)
                if (i >= 0 && i < f->w) f->px[j * f->w + i] = c;
}

/* raised (out = 1) or sunken (out = 0) edge, two pixels deep */
static void bevel(struct fb *f, int x, int y, int w, int h, int out) {
    uint8_t hi = out ? WHITE : DARK, lo = out ? BLACK : WHITE;
    rect(f, x, y, w, 1, hi);         rect(f, x, y, 1, h, hi);
    rect(f, x, y + h - 1, w, 1, lo); rect(f, x + w - 1, y, 1, h, lo);
    if (out) { rect(f, x + 1, y + h - 2, w - 2, 1, DARK); rect(f, x + w - 2, y + 1, 1, h - 2, DARK); }
    else     { rect(f, x + 1, y + 1, w - 2, 1, BLACK);    rect(f, x + 1, y + 1, 1, h - 2, BLACK); }
}

static const struct glyph *find(const struct font *fo, uint8_t ch) {
    for (int i = 0; i < fo->count; i++)
        if (fo->g[i].ch == ch) return &fo->g[i];
    return 0;
}

/* blend a 2-bit coverage value over the pixel below, in the 4-shade space */
static void plot(struct fb *f, int x, int y, uint8_t a, uint8_t c) {
    if (!a || x < 0 || y < 0 || x >= f->w || y >= f->h) return;
    uint8_t *p = &f->px[y * f->w + x];
    *p = (uint8_t)((c * a + *p * (3 - a) + 1) / 3);
}

static int text_width(const struct font *fo, const char *s) {
    int w = 0;
    for (; *s; s++) { const struct glyph *g = find(fo, (uint8_t)*s); w += g ? g->adv : 4; }
    return w;
}

static void text(struct fb *f, const struct font *fo, int x, int y, const char *s, uint8_t c) {
    for (; *s; s++) {
        const struct glyph *g = find(fo, (uint8_t)*s);
        if (!g) { x += 4; continue; }
        const uint8_t *d = fo->data + g->off;
        int n = 0, total = g->w * fo->height;
        while (n < total) {
            uint8_t v = *d >> 6, run = (uint8_t)((*d & 63) + 1);
            d++;
            for (; run; run--, n++) plot(f, x + g->left + n % g->w, y + n / g->w, v, c);
        }
        x += g->adv;
    }
}

static const char *const parts[] = {
    "firmware \xb7 root of trust", "bootloader \xb7 measured image", "seL4 microkernel \xb7 MCS",
    "static system description", "safety controller", "capability broker", "agents",
};
static const char *const know[] = { "assumed", "assumed", "proven", "tested", "tested", "tested", "untrusted" };
enum { NPARTS = 7 };

/* step 0 .. NPARTS: how many parts have reported in */
void zos_splash(uint8_t *px, int w, int h, int step) {
    struct fb f = { px, w, h };
    const int pw = 560, ph = 404, px0 = (w - pw) / 2, py0 = (h - ph) / 2;

    rect(&f, 0, 0, w, h, DARK);                                   /* workspace */
    rect(&f, px0 + 4, py0 + 4, pw, ph, BLACK);                    /* hard shadow */
    rect(&f, px0, py0, pw, ph, LIGHT);                            /* panel */
    bevel(&f, px0, py0, pw, ph, 1);
    rect(&f, px0 + 2, py0 + 2, pw - 4, 22, BLACK);                /* title bar */
    text(&f, &font_semibold, px0 + (pw - text_width(&font_semibold, "zOS")) / 2, py0 + 5, "zOS", WHITE);

    text(&f, &font_thin, px0 + (pw - text_width(&font_thin, "zOS")) / 2, py0 + 34, "zOS", BLACK);
    const char *tag = "Bare minimum. Verified. Real-time. An OS for the AI era.";
    text(&f, &font_regular, px0 + (pw - text_width(&font_regular, tag)) / 2, py0 + 118, tag, DARK);

    const int bx = px0 + 24, by = py0 + 150, bw = pw - 48, bh = NPARTS * 20 + 16;
    rect(&f, bx, by, bw, bh, WHITE);                              /* report well */
    bevel(&f, bx, by, bw, bh, 0);
    for (int i = 0; i < NPARTS && i < step; i++) {
        int y = by + 9 + i * 20;
        text(&f, &font_regular, bx + 14, y, parts[i], BLACK);
        text(&f, &font_semibold, bx + bw - 14 - text_width(&font_semibold, know[i]), y, know[i], i == 2 ? BLACK : DARK);
    }

    const int gx = bx, gy = by + bh + 16, gw = bw, gh = 14;     /* progress */
    rect(&f, gx, gy, gw, gh, LIGHT);
    rect(&f, gx + 2, gy + 2, (gw - 4) * step / NPARTS, gh - 4, DARK);
    bevel(&f, gx, gy, gw, gh, 0);

    if (step >= NPARTS) {
        const char *s = "the agent proposes. the loop disposes.";
        text(&f, &font_regular, px0 + (pw - text_width(&font_regular, s)) / 2, gy + gh + 12, s, BLACK);
    }
}
