# zOS loader (prototype, QEMU RISC-V)

The first code that runs. It draws the boot screen, checks the kernel image against the hash in the image's header, shows the verdict, and starts the kernel only if the hash matches.

![the loader after a matching hash](good.png)
![the loader after a tampered image](bad-payload.png)

## What it checks, and what it does not

- **Checked:** that the image is the one its header describes. The header (magic, version, length, entry offset) and the payload are hashed together with SHA-256 and compared with the hash stored in the header. Flipping one bit anywhere in the header or the payload stops the boot; `test.py` does this six ways.
- **Not checked: who made the image.** A hash stored next to the image protects against accidents, not against someone who can rewrite both. Authenticity needs a signature verified against a key that lives in the loader. That is the next step; nothing here claims it, and the screen says only "hash matches".
- **Not done: finding the image on a storage device.** QEMU puts the image at `0x80400000` before the loader starts. A storage driver or a platform loader (U-Boot) is a separate module.
- **Not measured: the loader itself.** The screen says "assumed" for firmware and loader, because that is what it is.

## Image format

Little endian, 64-byte header, payload follows.

| offset | size | field |
|---|---|---|
| 0 | u32 | magic `zOSK` (0x4b534f7a) |
| 4 | u32 | version, 1 |
| 8 | u64 | payload length (at most 8 MiB) |
| 16 | u64 | entry point, offset from the image start (at least 64, inside the payload) |
| 24 | 32 | SHA-256 over header bytes 0..23 followed by the payload |
| 56 | 8 | reserved, zero |

Hashing the header fields as well as the payload means length, version and entry point cannot be changed without breaking the hash. The loader hashes the copy in memory that it then starts, not a copy on a medium.

## Modules

- `start.S`: entry, one hart, stack, clears `.bss`.
- `loader.c`: serial output, the display (fw_cfg and the ram framebuffer), the checks, the jump. The display is the only platform-specific part: it obtains a framebuffer and converts the splash's four shades to its pixel format. Other platforms (a framebuffer from the device tree, UEFI, the Raspberry Pi's GPU firmware) add a module of their own behind the same two functions; the renderer does not change.
- `sha256.c`: SHA-256, incremental. The constants are computed by `gen_sha_tables.py` rather than typed, and the implementation is compared against Python's `hashlib` by `test_sha.c` for lengths around the block boundaries.
- `../splash/splash.c`: the renderer.
- `kernel_stub.c`, `kernel_start.S`, `kernel.ld`: a stand-in kernel that prints one line and stops QEMU, to prove that control was handed over.
- `mkimage.py`: wraps a flat binary in the header.

## Build and test

```
make           # needs clang with the RISC-V target and ld.lld
make test      # needs qemu-system-riscv64 and Pillow; writes a screenshot per case
make test-sha  # our SHA-256 against Python's hashlib
```

`make test` boots the loader in QEMU's `virt` machine with a ram framebuffer, once with the good image and five times with a flipped bit (payload, stored hash, entry point, length, magic). For each run it reads the serial verdict, takes a screenshot through the QEMU monitor and checks that the screenshot holds exactly the four grey shades. The good image must reach the kernel stub; every other image must not. Disabling the hash comparison in `loader.c` turns the four hash cases red, so the test can fail.

## Size

`clang -Os`, `rv64imac`, text + data. Whole loader: 8,896 bytes.

| part | bytes |
|---|---|
| `start.S` | 52 |
| `loader.c` (display, checks, jump) | 2,190 |
| `sha256.c` including its constants | 1,000 |
| `splash.c` including its glyphs | 6,435 |
