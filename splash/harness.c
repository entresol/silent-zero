/* Host harness: renders every boot step of the splash into PGM files. */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

void zos_splash(uint8_t *px, int w, int h, int step);

int main(void) {
    const int w = 1120, h = 832;           /* the screen size of 1991's grey-scale workstations */
    static const uint8_t shade[4] = { 0, 85, 170, 255 };
    uint8_t *fb = malloc((size_t)w * h);
    for (int step = 0; step <= 7; step++) {
        zos_splash(fb, w, h, step);
        char name[32];
        snprintf(name, sizeof name, "frame%d.pgm", step);
        FILE *o = fopen(name, "wb");
        fprintf(o, "P5 %d %d 255\n", w, h);
        for (long i = 0; i < (long)w * h; i++) fputc(shade[fb[i]], o);
        fclose(o);
    }
    free(fb);
    return 0;
}
