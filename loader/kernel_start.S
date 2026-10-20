# SPDX-License-Identifier: BSD-2-Clause
        .section .text.start
        .global _kstart
_kstart:
        li      sp, 0x80600000
        call    kernel_main
