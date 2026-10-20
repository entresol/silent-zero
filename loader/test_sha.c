/* SPDX-License-Identifier: BSD-2-Clause */
/* Host check: hash a file in odd-sized chunks with our SHA-256 and print the digest. */
#include <stdio.h>
#include <stdint.h>
#include "sha256.h"
int main(int argc, char **argv) {
    (void)argc;
    FILE *f = fopen(argv[1], "rb"); uint8_t b[37], d[32]; size_t n; struct sha256 s;
    if (!f) return 1;
    sha256_init(&s);
    while ((n = fread(b, 1, sizeof b, f)) > 0) sha256_update(&s, b, n);
    sha256_final(&s, d);
    for (int i = 0; i < 32; i++) printf("%02x", d[i]);
    printf("\n");
    return 0;
}
