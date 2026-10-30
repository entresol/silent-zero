#!/bin/sh
# SPDX-License-Identifier: BSD-2-Clause
# Builds the paper PDF from src.md and the landing page into the repository root.
# Needs Python 3 and pdfLaTeX (TeX Live with charter, helvet, microtype, titlesec, fancyhdr, xurl, booktabs).
set -eu
here=$(cd "$(dirname "$0")" && pwd)
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
cp "$here/src.md" "$here/figs/fig1.png" "$here/figs/fig2.png" "$here/figs/stations.json" "$work/"
python3 -I "$here/build_paper.py" "$work" >/dev/null
for pass in 1 2; do
  (cd "$work" && pdflatex -interaction=nonstopmode -halt-on-error paper.tex >/dev/null)
done
python3 -I "$here/build_site.py" "$work" "$here/.." >/dev/null
python3 -I "$here/build_wiki.py" "$here/.." >/dev/null
echo "paper: $(pdfinfo "$work/paper.pdf" | awk '/^Pages/ {print $2}') pages; site: index.html, wiki"
