/*
 * SPDX-License-Identifier: BSD-2-Clause
 *
 * The demo's root task: the first and only user program. It builds a UART frame and page tables from untyped
 * capabilities, maps them, prints five heartbeats with seL4_Yield in between, and suspends itself. The kernel has no
 * debug console in its verified configuration, so everything after "Jumping to kernel-image entry point" comes from here.
 */
#include <sel4/sel4.h>

volatile seL4_Word boot_stage;
static seL4_CPtr next_slot, ram_ut;
static volatile unsigned int *uart;

static void stop(seL4_Word stage)
{
    boot_stage = stage;
    seL4_TCB_Suspend(seL4_CapInitThreadTCB);
    for (;;) {}
}

static seL4_CPtr retype(seL4_CPtr ut, seL4_Word type, seL4_Word bits, seL4_Word count)
{
    seL4_CPtr slot = next_slot;
    next_slot += count;
    if (seL4_Untyped_Retype(ut, type, bits, seL4_CapInitThreadCNode, 0, 0, slot, count)) {
        stop(0xe100 + type);
    }
    return slot;
}

static void putc_uart(char c)
{
    while (*uart & 0x80000000u) {}
    *uart = (unsigned char)c;
}

static void puts_uart(const char *s)
{
    while (*s) {
        if (*s == '\n') putc_uart('\r');
        putc_uart(*s++);
    }
}

static void decimal(seL4_Word n)
{
    char digits[24];
    int i = 0;
    do { digits[i++] = '0' + n % 10; n /= 10; } while (n);
    while (i) putc_uart(digits[--i]);
}

static seL4_Word ticks(void)
{
    seL4_Word t;
    __asm__ volatile("rdtime %0" : "=r"(t));
    return t;
}

int main(seL4_BootInfo *bi)
{
    boot_stage = 1;
    seL4_SetIPCBuffer(bi->ipcBuffer);
    next_slot = bi->empty.start;
    seL4_CPtr device_ut = 0;
    seL4_Word device_base = 0, device_bits = 0;
    const seL4_Word uart_phys = 0x10010000;
    for (seL4_Word i = 0; i < bi->untyped.end - bi->untyped.start; i++) {
        seL4_UntypedDesc d = bi->untypedList[i];
        if (!d.isDevice && d.sizeBits >= 18 && !ram_ut) ram_ut = bi->untyped.start + i;
        if (d.isDevice && d.paddr <= uart_phys && uart_phys - d.paddr < (1ul << d.sizeBits)) {
            device_ut = bi->untyped.start + i;
            device_base = d.paddr;
            device_bits = d.sizeBits;
        }
    }
    if (!ram_ut || !device_ut) stop(0xe001);
    boot_stage = 2;
    while (device_bits > 12) {
        device_bits--;
        seL4_CPtr children = retype(device_ut, seL4_UntypedObject, device_bits, 2);
        if (uart_phys >= device_base + (1ul << device_bits)) {
            device_ut = children + 1;
            device_base += 1ul << device_bits;
        } else device_ut = children;
    }
    seL4_CPtr frame = retype(device_ut, seL4_RISCV_4K_Page, 0, 1);
    const seL4_Word uart_virt = 0x40000000;
    int error;
    for (int attempt = 0; attempt < 3; attempt++) {
        error = seL4_RISCV_Page_Map(frame, seL4_CapInitThreadVSpace, uart_virt,
                                  seL4_AllRights, seL4_RISCV_Default_VMAttributes);
        if (!error) break;
        if (error != seL4_FailedLookup) stop(0xe200 + error);
        seL4_CPtr pt = retype(ram_ut, seL4_RISCV_PageTableObject, 0, 1);
        error = seL4_RISCV_PageTable_Map(pt, seL4_CapInitThreadVSpace, uart_virt,
                                       seL4_RISCV_Default_VMAttributes);
        if (error) stop(0xe300 + error);
    }
    if (error) stop(0xe400 + error);
    uart = (volatile unsigned int *)uart_virt;
    uart[2] |= 1; /* Enable SiFive UART transmitter. */
    boot_stage = 3;
    puts_uart("\nUSERSPACE: Hello from seL4 17.0.0 on RISC-V 64!\n");
    puts_uart("USERSPACE: Root task is running in U-mode.\n");
    puts_uart("CAPABILITIES: UART frame and page tables created and mapped.\n");
    puts_uart("KERNEL: official RISCV64_MCS_verified configuration, 58,428 bytes; no debug console.\n");
    puts_uart("BOOTINFO: CPUs exposed to seL4 = "); decimal(bi->numNodes); puts_uart("\n");
    for (int i = 1; i <= 5; i++) {
        seL4_Word start = ticks();
        while (ticks() - start < 750000) seL4_Yield();
        puts_uart("RUNNING: heartbeat "); decimal(i); puts_uart("/5 -- seL4_Yield returned\n");
    }
    puts_uart("BOOT SUCCESS: kernel -> root task -> capability calls -> UART.\n");
    puts_uart("Demo complete. Root task suspends; kernel stays in idle.\n");
    stop(4);
    return 0;
}
