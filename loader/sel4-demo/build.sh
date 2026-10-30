#!/bin/sh
# SPDX-License-Identifier: BSD-2-Clause
# Builds the boot image with the official preset RISCV64_MCS_verified and checks that the kernel inside it is the
# expected one, byte for byte. Needs the xPack RISC-V GCC 15.2.0-1 (riscv-none-elf-*) on PATH, dtc, uv and the sources
# from fetch.sh. Python packages, CMake and Ninja come in pinned versions from requirements.txt.
set -eu
here=$(cd "$(dirname "$0")" && pwd)
deps="$here/deps"
build="$here/build"
test -d "$deps/seL4/.git" || { echo "run fetch.sh first" >&2; exit 1; }
[ -x "$deps/venv/bin/python3" ] || { uv venv -q --python 3.12 "$deps/venv"; uv pip install -q --python "$deps/venv/bin/python3" -r "$here/requirements.txt"; }
PATH="$deps/venv/bin:$PATH"; export PATH
rm -rf "$build"
# Three options outside the kernel, as in the first demo; build.sh checks below that the kernel is unaffected:
#   LibSel4UseThreadLocals=OFF  the toolchain has no thread-local storage; the root task has one thread anyway
#   IMAGE_START_ADDR            where the ELF loader runs, out of the way of the images it unpacks
#   UseRiscVOpenSBI=OFF         QEMU brings OpenSBI; the image is the ELF loader only
cmake -S "$here" -B "$build" -G Ninja \
  -C "$deps/seL4/configs/RISCV64_MCS_verified.cmake" \
  -DCMAKE_TOOLCHAIN_FILE="$deps/seL4/gcc.cmake" -DCROSS_COMPILER_PREFIX=riscv-none-elf- \
  -DElfloaderImage=elf -DLibSel4UseThreadLocals:BOOL=OFF -DIMAGE_START_ADDR=0x82000000 -DUseRiscVOpenSBI=OFF >/dev/null
cmake --build "$build" >/dev/null
riscv-none-elf-objcopy -O binary "$build/kernel/kernel.elf" "$build/kernel.bin"
python3 -I - "$here/expected.json" "$build" <<'PY'
import hashlib, json, re, sys
from pathlib import Path
want, build = json.loads(Path(sys.argv[1]).read_text()), Path(sys.argv[2])
cache = (build / "CMakeCache.txt").read_text()
for k, v in want["preset"].items():   # every setting of the official preset, as the build really used it
    m = re.search(rf"^{k}:[A-Z]+=(.*)$", cache, re.M)
    if not m or m.group(1) != v:
        sys.exit(f"{k}: expected {v}, build has {m and m.group(1)}")
kernel = (build / "kernel.bin").read_bytes()
digest = hashlib.sha256(kernel).hexdigest()
if (len(kernel), digest) != (want["kernel_bytes"], want["kernel_sha256"]):
    sys.exit(f"kernel differs: {len(kernel)} bytes, {digest}")
image = build / "images" / "boot-demo-image-riscv-hifive"
print(f"preset: {len(want['preset'])} settings as expected")
print(f"kernel: {len(kernel)} bytes, sha256 {digest}, as expected")
print(f"image:  {image.stat().st_size} bytes, sha256 {hashlib.sha256(image.read_bytes()).hexdigest()}")
PY
