# SPDX-License-Identifier: BSD-2-Clause
# Entry of the zOS loader on QEMU "virt" (-bios none): machine mode, a0 = hart id, a1 = device tree.
        .section .text.start
        .global _start
_start:
        bnez    a0, park                # one hart runs the loader, the others wait
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
