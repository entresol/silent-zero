#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-2-Clause
"""The mechanical half of the wiki's lint (wiki/CLAUDE.md, "Lint"): what a script can find without reading a page.

Links to pages that do not exist, pages missing from the catalogue, pages no other page links to, sources named in
front matter without a page of their own, and drafted pages older than a month. The build prints what it finds as
warnings; run on its own (python3 paper/wiki_lint.py [root] [YYYY-MM-DD]) it exits with 1 when it finds anything.
Contradictions, claims a newer source has replaced, and concepts without a page need reading; the weekly run does
that part."""
import datetime
import re
import sys
from pathlib import Path

STALE_DAYS = 30
LINK = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")


def _front(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    return (dict(re.findall(r"^(\w+):\s*(.*)$", m.group(1), re.M)), text[m.end():]) if m else ({}, text)


def check(root, today=None):
    """Returns a list of problems, one line each."""
    wiki = Path(root) / "wiki"
    today = today or datetime.date.today()
    pages = {}
    for f in sorted(wiki.rglob("*.md")):
        meta, body = _front(f.read_text(encoding="utf-8"))
        if meta.get("type") or f == wiki / "index.md":
            pages[f.stem] = (f.relative_to(wiki.parent).as_posix(), meta, body)
    catalogue = {t.strip() for t in LINK.findall(pages["index"][2])}
    problems, linked = [], set()
    for name, (path, meta, body) in pages.items():
        for target in sorted({t.strip() for t in LINK.findall(body)}):
            if target not in pages:
                problems.append(f"{path}: [[{target}]] has no page")
            elif target != name and name != "index":
                linked.add(target)
        if name == "index":
            continue
        for s in re.findall(r"[\w.-]+", meta.get("sources", "").strip("[]")):
            if s not in pages:
                problems.append(f"{path}: source {s} in its front matter has no page")
        if meta.get("status") == "drafted":
            try:
                age = (today - datetime.date.fromisoformat(meta.get("updated", ""))).days
            except ValueError:
                problems.append(f"{path}: drafted, without a valid updated: date")
            else:
                if age > STALE_DAYS:
                    problems.append(f"{path}: drafted for {age} days, more than {STALE_DAYS}")
    for name, (path, *_) in pages.items():
        if name == "index":
            continue
        if name not in catalogue:
            problems.append(f"{path}: not in the catalogue (index.md)")
        if name not in linked:
            problems.append(f"{path}: no other page links to it")
    return problems


if __name__ == "__main__":
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    day = datetime.date.fromisoformat(sys.argv[2]) if len(sys.argv) > 2 else None
    found = check(root, day)
    for p in found:
        print(p)
    print(f"wiki lint: {len(found)} found", file=sys.stderr)
    sys.exit(1 if found else 0)
