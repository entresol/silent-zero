/* SPDX-License-Identifier: BSD-2-Clause */
/* SHA-256 (FIPS 180-4), freestanding, incremental. */
#include <stdint.h>
#include "sha256.h"
#include "sha256_tables.h"

static uint32_t ror(uint32_t x, int n) { return x >> n | x << (32 - n); }

static void block(struct sha256 *s, const uint8_t *p) {
    uint32_t w[64], a[8];
    for (int i = 0; i < 16; i++)
        w[i] = (uint32_t)p[4 * i] << 24 | (uint32_t)p[4 * i + 1] << 16 | (uint32_t)p[4 * i + 2] << 8 | p[4 * i + 3];
    for (int i = 16; i < 64; i++) {
        uint32_t s0 = ror(w[i - 15], 7) ^ ror(w[i - 15], 18) ^ (w[i - 15] >> 3);
        uint32_t s1 = ror(w[i - 2], 17) ^ ror(w[i - 2], 19) ^ (w[i - 2] >> 10);
        w[i] = w[i - 16] + s0 + w[i - 7] + s1;
    }
    for (int i = 0; i < 8; i++) a[i] = s->h[i];
    for (int i = 0; i < 64; i++) {
        uint32_t t1 = a[7] + (ror(a[4], 6) ^ ror(a[4], 11) ^ ror(a[4], 25)) + ((a[4] & a[5]) ^ (~a[4] & a[6])) + sha_k[i] + w[i];
        uint32_t t2 = (ror(a[0], 2) ^ ror(a[0], 13) ^ ror(a[0], 22)) + ((a[0] & a[1]) ^ (a[0] & a[2]) ^ (a[1] & a[2]));
        for (int j = 7; j > 0; j--) a[j] = a[j - 1];
        a[4] += t1;
        a[0] = t1 + t2;
    }
    for (int i = 0; i < 8; i++) s->h[i] += a[i];
}

void sha256_init(struct sha256 *s) {
    for (int i = 0; i < 8; i++) s->h[i] = sha_h0[i];
    s->len = 0;
}

void sha256_update(struct sha256 *s, const uint8_t *p, uint64_t n) {
    for (; n; n--, p++) {
        s->buf[s->len++ & 63] = *p;
        if ((s->len & 63) == 0) block(s, s->buf);
    }
}

void sha256_final(struct sha256 *s, uint8_t out[32]) {
    uint64_t bits = s->len * 8;
    uint8_t pad = 0x80;
    sha256_update(s, &pad, 1);
    pad = 0;
    while ((s->len & 63) != 56) sha256_update(s, &pad, 1);
    for (int i = 7; i >= 0; i--) { uint8_t b = (uint8_t)(bits >> (8 * i)); sha256_update(s, &b, 1); }
    for (int i = 0; i < 8; i++) {
        out[4 * i] = (uint8_t)(s->h[i] >> 24); out[4 * i + 1] = (uint8_t)(s->h[i] >> 16);
        out[4 * i + 2] = (uint8_t)(s->h[i] >> 8); out[4 * i + 3] = (uint8_t)s->h[i];
    }
}
