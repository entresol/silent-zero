#!/bin/sh
# SPDX-License-Identifier: BSD-2-Clause
# Fetches the official seL4 sources the demo is built from, at fixed commits, into deps/. Nothing is changed in them;
# the commit hash is the check that they are exactly these versions.
set -eu
here=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$here/deps"
get() {   # name, repository, commit (seL4 17.0.0 and the seL4_tools and util_libs its release manifest names)
  dir="$here/deps/$1"
  if [ ! -d "$dir/.git" ]; then git init -q "$dir"; git -C "$dir" remote add origin "$2"; fi
  git -C "$dir" fetch -q --depth 1 origin "$3"
  git -C "$dir" checkout -q --detach FETCH_HEAD
  test "$(git -C "$dir" rev-parse HEAD)" = "$3" || { echo "$1: not at $3" >&2; exit 1; }
  test -z "$(git -C "$dir" status --porcelain)" || { echo "$1: has local changes" >&2; exit 1; }
  echo "$1 $3"
}
get seL4       https://github.com/seL4/seL4.git       62e345c240a15671484530b4e6e069ce266c28d7
get seL4_tools https://github.com/seL4/seL4_tools.git 6493e0c6fab360eb81a8115a49c9ca7bc280c48a
get util_libs  https://github.com/seL4/util_libs.git  ef49a397b7044fc38b609a99a8c6265a97913b8e
