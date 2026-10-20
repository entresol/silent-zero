/* SPDX-License-Identifier: BSD-2-Clause */
ENTRY(_start)
MEMORY { RAM (rwx) : ORIGIN = 0x80000000, LENGTH = 0x100000 }   /* loader and its stack: 1 MiB */
SECTIONS {
  .text   : { *(.text.start) *(.text .text.*) } > RAM
  .rodata : { *(.rodata .rodata.*) } > RAM
  .data   : { *(.data .data.*) } > RAM
  .bss    : { . = ALIGN(8); _bss_start = .; *(.bss .bss.*) *(COMMON) . = ALIGN(8); _bss_end = .; } > RAM
  _stack_top = ORIGIN(RAM) + LENGTH(RAM);
  /DISCARD/ : { *(.comment) *(.note*) *(.riscv.attributes) }
}
