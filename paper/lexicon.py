# SPDX-License-Identifier: BSD-2-Clause
"""The lexicon: one line per term, collected from the glossary and the wiki, nothing written for it alone.

A glossary entry joins with a fourth line `Short: ...`. A wiki concept or system page joins with `short:` in its front
matter, or, if the term has a glossary entry, links to it with `glossary: <Term>` and takes the short line from there.
Each entry then points to the glossary (G) and the wiki (W) wherever it has a place there."""
import re
from pathlib import Path

import glossary

LIMIT = 50   # characters of a short line


def _front(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    return dict(re.findall(r"^(\w+):\s*(.*)$", m.group(1), re.M)) if m else {}


def collect(root):
    """Returns (entries, problems); an entry has term, short, glossary (anchor or None) and wiki (url or None)."""
    root = Path(root)
    entries, problems = {}, []
    for _, es in glossary.parse(root / "paper" / "glossary.md"):
        for e in es:
            if e.get("short"):
                entries[e["term"]] = {"term": e["term"], "short": e["short"], "glossary": e["id"], "wiki": None}
    for f in sorted((root / "wiki").glob("*/*.md")):
        meta = _front(f.read_text(encoding="utf-8"))
        if meta.get("type") not in ("concept", "system"):
            continue
        url = "/" + f.relative_to(root).with_suffix(".html").as_posix()
        if meta.get("glossary"):
            term = meta["glossary"].strip()
            if term in entries:
                entries[term]["wiki"] = url
            elif meta.get("short"):
                problems.append(f"{f.name}: glossary term '{term}' has no Short line, the page's own is not used")
            continue
        if meta.get("short"):
            title = re.search(r"^# (.+)$", f.read_text(encoding="utf-8"), re.M)
            term = title.group(1).strip() if title else f.stem
            entries[term] = {"term": term, "short": meta["short"].strip(), "glossary": None, "wiki": url}
    for _, es in glossary.parse(root / "paper" / "glossary.md"):
        problems += [f"glossary: '{e['term']}' has no Short line" for e in es if not e.get("short")]
    for f in sorted((root / "wiki").glob("*/*.md")):
        meta = _front(f.read_text(encoding="utf-8"))
        if meta.get("type") in ("concept", "system") and not (meta.get("short") or meta.get("glossary")):
            problems.append(f"wiki/{f.parent.name}/{f.name}: neither short: nor glossary: in its front matter")
    for e in entries.values():
        if len(e["short"]) > LIMIT:
            problems.append(f"{e['term']}: short line has {len(e['short'])} characters, more than {LIMIT}")
    out = sorted(entries.values(), key=lambda e: re.sub(r"[^a-z0-9]", "", e["term"].lower()))
    return out, problems


def letter(e):
    c = re.sub(r"[^A-Za-z]", "", e["term"])[:1].upper()
    return c or "#"


def az_bar(entries, base):
    """The A-Z line; letters with entries link to base#<letter>."""
    have = {letter(e) for e in entries}
    cells = [f'<a href="{base}#{c.lower()}">{c}</a>' if c in have else f'<span aria-hidden="true">{c}</span>'
             for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    return '<nav class="az" aria-label="Lexicon A to Z">' + "".join(cells) + "</nav>"
