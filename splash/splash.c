/* SPDX-License-Identifier: BSD-2-Clause */
/*
 * zOS boot splash, prototype.
 *
 * Draws the first screen a person sees after power-on: a grey panel in four
 * shades, bevelled edges, crisp grey-scale type, and the boot report of what
 * was loaded and what we know about each part.
 *
 * Freestanding: no libc, no heap, no floating point. The caller hands in a
 * framebuffer of one byte per pixel holding a shade 0..3 (black, dark grey,
 * light grey, white). Mapping shades to the real display format is the job of
 * whoever owns the display, not of this file.
 *
 * Two ways to use it. zos_splash() shows the fixed demonstration report.
 * The loader instead draws the frame once and fills the report row by row
 * with what it has really measured: zos_splash_frame(), zos_splash_row(),
 * zos_splash_progress(), zos_splash_footer().
 */
#include <stdint.h>

struct glyph { uint8_t ch, w, adv; int8_t left; uint16_t off; };
struct font { uint8_t height, count; uint16_t size; const struct glyph *g; const uint8_t *data; };
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
        const uint8_t *d = fo->data + g->off, *end = fo->data + (g + 1 < fo->g + fo->count ? g[1].off : fo->size);
        for (int n = 0; d < end; d++) {                   /* see gen_glyphs.py, encode() */
            uint8_t v = *d >> 6, skip = *d & 63;
            if (!v) { n += skip + 1; continue; }
            n += skip;
            plot(f, x + g->left + n % g->w, y + n / g->w, v, c);
            n++;
        }
        x += g->adv;
    }
}

/* layout, derived from the screen size */
enum { NROWS = 7, PW = 560, PH = 404 };
struct geo { int px0, py0, bx, by, bw, bh, gx, gy, gw, gh; };

static struct geo geometry(int w, int h) {
    struct geo g;
    g.px0 = (w - PW) / 2; g.py0 = (h - PH) / 2;
    g.bx = g.px0 + 24; g.by = g.py0 + 150; g.bw = PW - 48; g.bh = NROWS * 20 + 16;
    g.gx = g.bx; g.gy = g.by + g.bh + 16; g.gw = g.bw; g.gh = 14;
    return g;
}

/* panel, title, name, tagline, empty report well and empty progress bar */
void zos_splash_frame(uint8_t *px, int w, int h) {
    struct fb f = { px, w, h };
    struct geo g = geometry(w, h);

    rect(&f, 0, 0, w, h, DARK);                                   /* workspace */
    rect(&f, g.px0 + 4, g.py0 + 4, PW, PH, BLACK);                /* hard shadow */
    rect(&f, g.px0, g.py0, PW, PH, LIGHT);                        /* panel */
    bevel(&f, g.px0, g.py0, PW, PH, 1);
    rect(&f, g.px0 + 2, g.py0 + 2, PW - 4, 22, BLACK);            /* title bar */
    text(&f, &font_semibold, g.px0 + (PW - text_width(&font_semibold, "zOS")) / 2, g.py0 + 5, "zOS", WHITE);

    const char *name = "silent zero OS", *tag = "Bare minimum. Verified. Real-time. An OS for the AI era.";
    text(&f, &font_thin, g.px0 + (PW - text_width(&font_thin, name)) / 2, g.py0 + 50, name, BLACK);
    text(&f, &font_regular, g.px0 + (PW - text_width(&font_regular, tag)) / 2, g.py0 + 96, tag, DARK);

    rect(&f, g.bx, g.by, g.bw, g.bh, WHITE);                      /* report well */
    bevel(&f, g.bx, g.by, g.bw, g.bh, 0);

    rect(&f, g.gx, g.gy, g.gw, g.gh, LIGHT);                      /* progress */
    bevel(&f, g.gx, g.gy, g.gw, g.gh, 0);
}

/* one line of the report: what, and what we know about it (strong = black, else dark grey) */
void zos_splash_row(uint8_t *px, int w, int h, int row, const char *left, const char *right, int strong) {
    struct fb f = { px, w, h };
    struct geo g = geometry(w, h);
    int y = g.by + 9 + row * 20;
    text(&f, &font_regular, g.bx + 14, y, left, BLACK);
    text(&f, &font_semibold, g.bx + g.bw - 14 - text_width(&font_semibold, right), y, right, strong ? BLACK : DARK);
}

void zos_splash_progress(uint8_t *px, int w, int h, int step, int total) {
    struct fb f = { px, w, h };
    struct geo g = geometry(w, h);
    rect(&f, g.gx, g.gy, g.gw, g.gh, LIGHT);
    rect(&f, g.gx + 2, g.gy + 2, (g.gw - 4) * step / total, g.gh - 4, DARK);
    bevel(&f, g.gx, g.gy, g.gw, g.gh, 0);
}

/* one centred line below the progress bar */
void zos_splash_footer(uint8_t *px, int w, int h, const char *s) {
    struct fb f = { px, w, h };
    struct geo g = geometry(w, h);
    text(&f, &font_regular, g.px0 + (PW - text_width(&font_regular, s)) / 2, g.gy + g.gh + 12, s, BLACK);
}

static const char *const parts[] = {
    "firmware \xb7 root of trust", "bootloader \xb7 measured image", "seL4 microkernel \xb7 MCS",
    "static system description", "safety controller", "capability broker", "agents",
};
static const char *const know[] = { "assumed", "assumed", "proven", "tested", "tested", "tested", "untrusted" };

/* the fixed demonstration report; step 0 .. NROWS: how many parts have reported in */
void zos_splash(uint8_t *px, int w, int h, int step) {
    zos_splash_frame(px, w, h);
    for (int i = 0; i < NROWS && i < step; i++)
        zos_splash_row(px, w, h, i, parts[i], know[i], i == 2);
    zos_splash_progress(px, w, h, step, NROWS);
    if (step >= NROWS) zos_splash_footer(px, w, h, "the agent proposes. the loop disposes.");
}
