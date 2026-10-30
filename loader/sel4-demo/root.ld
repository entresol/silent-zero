/* SPDX-License-Identifier: BSD-2-Clause */
/* The root task is linked at 0x10000, where the ELF loader maps it. */
ENTRY(_sel4_start)
SECTIONS {
 . = 0x10000;
 .text : { *(.text.start) *(.text .text.*) }
 .rodata : { *(.rodata .rodata.*) }
 .data : { *(.data .data.*) }
 .sdata : { __global_pointer$ = . + 0x800; *(.sdata .sdata.*) }
 .bss : { *(.bss .bss.*) *(.sbss .sbss.*) *(COMMON) }
 . = ALIGN(4096);
 /DISCARD/ : { *(.eh_frame*) *(.comment) }
}
