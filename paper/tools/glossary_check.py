#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-2-Clause
"""Checks that the paper explains a glossary term where a reader first meets it.

The reader's complaint behind it (zOS paper, October 2026): "WCET" stood in the text with
"worst-case execution time" written out one sentence earlier, and nothing said that the two
were the same. The glossary and the links on the page help only readers who look them up.

Usage:
  python3 -I glossary_check.py [SRC] [GLOSSARY]     (defaults: ../src.md, ../glossary.md)

Two rules, see CONTRIBUTING.md, "Writing the paper":
1. An abbreviation whose glossary term reads "Expansion (ABBR)" is spelled out at its first
   use anywhere, In brief and Abstract included, as "expansion (ABBR)". This is checked.
2. Every term is explained at its first use in the body, from the Prologue on. Whether a
   sentence explains a term is for a reader to judge, so the script prints each first use in
   the order of the text. It warns only about terms the body never uses, and about entries
   without words to link, which neither the page nor this check can find.
It also lists abbreviations in the text that the glossary does not cover, at their first use,
leaving out everyday ones such as AI or CPU.
Warnings only, like the other scripts here.
"""
import re
import sys
from pathlib import Path

here = Path(__file__).resolve().parent
sys.dont_write_bytecode = True  # no __pycache__ in paper/
sys.path.insert(0, str(here.parent))
import glossary  # noqa: E402  (paper/glossary.py, the parser the build uses)

FRONT = {"In brief", "Abstract"}
# abbreviations a reader of this paper knows without help
COMMON = {"AI", "CPU", "GPU", "OS", "PC", "US", "EU", "KB", "MB", "VM", "GNU", "AT"}

src_path = Path(sys.argv[1]) if len(sys.argv) > 1 else here.parent / "src.md"
gl_path = Path(sys.argv[2]) if len(sys.argv) > 2 else here.parent / "glossary.md"
src = src_path.read_text(encoding="utf-8")
src = src[:src.index("## References")] if "## References" in src else src

# sections as (heading, text); headings, figures and table rules are not prose
sections = []
for block in re.split(r"\n(?=## )", src):
    head, _, body = block.partition("\n")
    body = "\n".join(l for l in body.splitlines() if not re.match(r"\s*(#|&#91;embedded|\| ---)", l))
    sections.append((head.lstrip("# ").strip(), body))
front = "\n".join(b for h, b in sections if h in FRONT)
body = "\n".join(b for h, b in sections if h.startswith(("Prologue",)) or h[:1].isdigit() or h == "Epilogue")
full = "\n".join(b for _, b in sections)


def find(text, word):
    """First match as the page links it: case-sensitive, whole word."""
    return re.search(r"(?<![\w-])" + re.escape(word) + r"(?![\w-])", text)


def sentence(text, start, end):
    a = max(text.rfind(". ", 0, start), text.rfind("\n", 0, start)) + 1
    b = min((i for i in (text.find(". ", end), text.find("\n", end)) if i >= 0), default=len(text))
    return text[a:b + 1].strip()


warnings = 0
entries = [e for _, es in glossary.parse(gl_path) for e in es]
covered = set()
print(f"=== {src_path.name}: {len(entries)} glossary terms\n")

print("1. Abbreviations spelled out at first use")
for e in entries:
    m = re.fullmatch(r"(.+?) \(([A-Z][A-Z0-9-]+)\)", e["term"])
    if not m:
        continue
    abbr = m.group(2)
    covered.add(abbr)
    hit = find(full, abbr)
    if not hit:
        print(f"   ok    {abbr}: not used in the text")
    elif full[hit.start() - 1:hit.end() + 1] == f"({abbr})":
        print(f"   ok    {abbr}")
    else:
        warnings += 1
        print(f"   WARN  {abbr}: first use without its expansion\n         {sentence(full, hit.start(), hit.end())}")

print("\n2. Terms at their first use in the body (Prologue on), in the order of the text")
firsts = []
for e in entries:
    if not e["matches"]:
        warnings += 1
        print(f"   WARN  {e['term']}: no words to link in glossary.md, so neither the page nor this check finds it")
        continue
    covered.update(t for w in e["matches"] for t in re.findall(r"\b[A-Z][A-Z0-9]+(?:-[A-Z0-9]+)?\b", w))
    hits = [h for h in (find(body, w) for w in e["matches"]) if h]
    if not hits:
        where = "only in In brief or Abstract" if any(find(front, w) for w in e["matches"]) else "not in the text"
        warnings += 1
        print(f"   WARN  {e['term']}: {where}")
        continue
    h = min(hits, key=lambda h: h.start())
    firsts.append((h.start(), f"   read  {e['term']}\n         {sentence(body, h.start(), h.end())}"))
print("\n".join(line for _, line in sorted(firsts)))

print("\n3. Abbreviations the glossary does not cover (first use)")
seen = set()
for m in re.finditer(r"(?<![\w-])([A-Z][A-Z0-9]{1,}(?:-[A-Z0-9]+)?)s?(?![\w-])", full):
    w = m.group(1)
    if w in seen or w in covered or w in COMMON or len(re.sub(r"[^A-Z]", "", w)) < 2:
        continue
    seen.add(w)
    spelled = full[m.end():m.end() + 1] == ")" and full[m.start() - 1] == "("
    print(f"   {'ok  ' if spelled else 'info'}  {w}: {sentence(full, m.start(), m.end())[:110]}")

print(f"\n{warnings} warning(s); the 'read' lines need a reader's judgement.")
