# SPDX-License-Identifier: BSD-2-Clause
# Entry of the zOS loader: a0 = hart id, a1 = device tree. On QEMU "virt" (-bios none) every hart starts here in
# machine mode; behind OpenSBI (PLAT_HIFIVE) only the boot hart arrives, in supervisor mode, and its id need not be 0.
        .section .text.start
        .global _start
_start:
#ifndef PLAT_HIFIVE
        bnez    a0, park                # one hart runs the loader, the others wait
#endif
        la      sp, _stack_top
        la      t0, _bss_start
        la      t1, _bss_end
1:      bgeu    t0, t1, 2f
        sd      zero, 0(t0)
        addi    t0, t0, 8
        j       1b
2:      call    loader_main
park:   wfi
        j       park
