/* SPDX-License-Identifier: BSD-2-Clause */
/* Stand-in kernel: proves that the loader handed over control, then stops QEMU. */
#include <stdint.h>
void kernel_main(unsigned long hartid, unsigned long dtb) {
    (void)dtb;
    const char *s = "kernel stub reached\n";
    for (; *s; s++) {
        while (!(*(volatile uint8_t *)(0x10000000UL + 5) & 0x20)) {}
        *(volatile uint8_t *)0x10000000UL = (uint8_t)*s;
    }
    (void)hartid;
    *(volatile uint32_t *)0x100000UL = 0x5555;           /* QEMU test finisher: exit with success */
    for (;;) __asm__ volatile("wfi");
}
