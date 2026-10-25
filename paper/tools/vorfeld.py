#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-2-Clause
"""Measures how long a reader waits for the main verb: words before it, per sentence.

The reader's complaint behind it (zOS paper, October 2026): "You only learn at the end of a
long sentence what it is about." Gopen and Swan, The Science of Scientific Writing (1990):
put first what the sentence is about, and follow the subject with its verb as soon as possible.
In German the same fault is called an overloaded Vorfeld.

Run (spaCy needs pinned versions; Python 3.14 does not work yet):
  uv run -q -p 3.12 --with spacy==3.8.7 --with click --with preshed==3.0.9 --with cymem==2.0.10 \
    --with murmurhash==1.0.12 \
    --with "en_core_web_sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl" \
    python -I vorfeld.py FILE [--worst N]
For German add the de_core_news_sm wheel and pass --lang de.
Sentences joined by a semicolon are counted by the verb the parser picks as root, which is
sometimes the second clause; read the worst list, do not trust single numbers.
"""
import argparse, re, statistics as st
import spacy

ap = argparse.ArgumentParser()
ap.add_argument("file"); ap.add_argument("--worst", type=int, default=12); ap.add_argument("--lang", default="en")
a = ap.parse_args()
nlp = spacy.load("de_core_news_sm" if a.lang == "de" else "en_core_web_sm")
t = open(a.file, encoding="utf-8").read()
if "## References" in t:
    t = t[:t.index("## References")]
t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
t = re.sub(r"\(([A-Z][^()]*?(?:\d{4}[a-z]?|n\.d\.(?:-[a-z])?))\)", "", t)
paras = [re.sub(r"[*_]", "", p) for p in t.split("\n\n") if p.strip() and not p.startswith(("#", "|", "&#91;", "**Keywords"))]
rows = []
for p in paras:
    for s in nlp(" ".join(p.split())).sents:
        words = [w for w in s if not w.is_punct]
        if len(words) < 6:
            continue
        rows.append((sum(1 for w in words if w.i < s.root.i), len(words), s.text.strip()))
b = [r[0] for r in rows]
print(f"{len(rows)} sentences, words before the main verb: median {st.median(b)}, mean {st.mean(b):.1f}")
for k in (8, 12, 16):
    n = sum(x >= k for x in b)
    print(f"  {k:2d} or more: {n:3d} ({100 * n / len(b):.0f} %)")
print(f"\nworst {a.worst}:")
for before, n, s in sorted(rows, reverse=True)[: a.worst]:
    print(f"  {before:2d}/{n:2d}  {s[:150]}")
