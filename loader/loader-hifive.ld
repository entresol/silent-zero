/* SPDX-License-Identifier: BSD-2-Clause */
/* The loader behind OpenSBI on the HiFive Unleashed model: OpenSBI starts its payload at 0x80200000. */
ENTRY(_start)
MEMORY { RAM (rwx) : ORIGIN = 0x80200000, LENGTH = 0x100000 }   /* loader and its stack: 1 MiB */
SECTIONS {
  .text   : { *(.text.start) *(.text .text.*) } > RAM
  .rodata : { *(.rodata .rodata.*) } > RAM
  .data   : { *(.data .data.*) } > RAM
  .bss    : { . = ALIGN(8); _bss_start = .; *(.bss .bss.*) *(COMMON) . = ALIGN(8); _bss_end = .; } > RAM
  _stack_top = ORIGIN(RAM) + LENGTH(RAM);
  /DISCARD/ : { *(.comment) *(.note*) *(.riscv.attributes) }
}
