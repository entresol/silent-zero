#!/bin/sh
# SPDX-License-Identifier: BSD-2-Clause
# Assembles the files of a release into release/<version>/: the loader and boot image for QEMU's HiFive Unleashed
# model, the video, the complete source of the seL4 commits inside the boot image, the licence texts, and SHA-256 sums.
# Run `make hifive` first (and sel4-demo/fetch.sh and build.sh before it). See ../THIRD-PARTY.md.
set -eu
version=${1:?usage: release.sh <version>}
here=$(cd "$(dirname "$0")" && pwd)
deps="$here/sel4-demo/deps"
out="$here/release/$version"
mkdir -p "$out/licenses"
cp "$here/hifive/loader.elf" "$out/zos-loader-hifive.elf"
cp "$here/hifive/sel4.zimg" "$out/sel4-mcs-hifive.zimg"
cp "$here/recording/loader-sel4-boot.mp4" "$out/"
for r in seL4 seL4_tools util_libs; do          # the exact commits fetch.sh pins, as source archives
  c=$(git -C "$deps/$r" rev-parse HEAD)
  test -z "$(git -C "$deps/$r" status --porcelain)" || { echo "$r has local changes" >&2; exit 1; }
  git -C "$deps/$r" archive --format=tar --prefix="$r-$c/" HEAD | gzip -n -9 > "$out/source-$r-$c.tar.gz"
done
cp "$deps"/seL4/LICENSES/*.txt "$out/licenses/"
cp "$here/../LICENSE" "$out/licenses/silent-zero-BSD-2-Clause.txt"
cp "$here/../THIRD-PARTY.md" "$out/"
cp "$here/../assets/fonts/LICENSE-Inter.txt" "$here/../assets/fonts/LICENSE-NunitoSans.txt" "$out/licenses/"
(cd "$out" && find . -type f ! -name SHA256SUMS | sort | xargs shasum -a 256 > SHA256SUMS)
echo "release files in $out:"; ls -l "$out"
