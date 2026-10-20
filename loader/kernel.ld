/* SPDX-License-Identifier: BSD-2-Clause */
ENTRY(_kstart)
/* image at 0x80400000, 64-byte header, payload from 0x80400040 */
SECTIONS { . = 0x80400040; .text : { *(.text.start) *(.text .text.*) } .rodata : { *(.rodata .rodata.*) } /DISCARD/ : { *(.comment) *(.note*) *(.riscv.attributes) } }
