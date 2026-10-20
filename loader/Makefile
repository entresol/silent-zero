# SPDX-License-Identifier: BSD-2-Clause
# Needs clang with the RISC-V target and ld.lld; QEMU (qemu-system-riscv64) only for `make test`.
CC      := clang --target=riscv64-unknown-elf -march=rv64imac_zifencei -mabi=lp64 -mcmodel=medany
CFLAGS  := -Os -ffreestanding -fno-builtin -fno-pic -fno-stack-protector -ffunction-sections -fdata-sections -Wall -Wextra -I. -I../splash
LD      := ld.lld --gc-sections -nostdlib

all: loader.elf kernel.zimg

sha256_tables.h: gen_sha_tables.py
	python3 -I gen_sha_tables.py

sha256.o: sha256.c sha256.h sha256_tables.h
	$(CC) $(CFLAGS) -c $< -o $@
loader.o: loader.c sha256.h
	$(CC) $(CFLAGS) -c $< -o $@
splash.o: ../splash/splash.c ../splash/glyphs.h
	$(CC) $(CFLAGS) -c $< -o $@
start.o: start.S
	$(CC) -c $< -o $@

loader.elf: start.o loader.o sha256.o splash.o loader.ld
	$(LD) -T loader.ld -o $@ start.o loader.o sha256.o splash.o

kernel_start.o: kernel_start.S
	$(CC) -c $< -o $@
kernel_stub.o: kernel_stub.c
	$(CC) $(CFLAGS) -c $< -o $@
kernel.elf: kernel_start.o kernel_stub.o kernel.ld
	$(LD) -T kernel.ld -o $@ kernel_start.o kernel_stub.o
kernel.bin: kernel.elf
	llvm-objcopy -O binary $< $@
kernel.zimg: kernel.bin mkimage.py
	python3 -I mkimage.py kernel.bin $@
test: all
	python3 -I test.py

test-sha:
	cc -O2 -Wall -Wextra -I. test_sha.c sha256.c -o test_sha && python3 -I test_sha.py

clean:
	rm -f *.o *.elf *.bin *.zimg *.ppm *.log *.sock test_sha sha256_tables.h bad-*.png
