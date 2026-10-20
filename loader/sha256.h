/* SPDX-License-Identifier: BSD-2-Clause */
#ifndef ZOS_SHA256_H
#define ZOS_SHA256_H
#include <stdint.h>

struct sha256 { uint32_t h[8]; uint8_t buf[64]; uint64_t len; };

void sha256_init(struct sha256 *s);
void sha256_update(struct sha256 *s, const uint8_t *p, uint64_t n);
void sha256_final(struct sha256 *s, uint8_t out[32]);

#endif
