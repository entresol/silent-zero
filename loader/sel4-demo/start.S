/* SPDX-License-Identifier: BSD-2-Clause */
/* Entry of the root task: global pointer, stack, main. */
.section .text.start,"ax"
.global _sel4_start
_sel4_start:
 .option push
 .option norelax
 la gp, __global_pointer$
 .option pop
 la sp, stack_top
 call main
1: j 1b
.section .bss
.balign 16
stack_bottom:
 .space 16384
stack_top:
