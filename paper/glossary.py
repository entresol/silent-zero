# SPDX-License-Identifier: BSD-2-Clause
"""Reads glossary.md for build_paper.py and build_site.py: the appendix as Markdown, and the terms the page links."""
import re
from pathlib import Path


def slug(term):
    return "gl-" + re.sub(r"[^a-z0-9]+", "-", term.lower()).strip("-")


def parse(path):
    """Returns [(group, [entry]), ...]; an entry has term, matches, meaning, role and id."""
    text = Path(path).read_text(encoding="utf-8")
    groups = []
    for block in re.split(r"\n## ", text)[1:]:
        name, _, rest = block.partition("\n")
        entries = []
        for chunk in re.split(r"\n\s*\n", rest.strip()):
            lines = [l.strip() for l in chunk.strip().splitlines() if l.strip()]
            head = re.match(r"\*\*(.+?)\*\*(?:\s*\|\s*(.+))?$", lines[0])
            role = lines[2]
            assert head and role.startswith("In Silent Zero:"), chunk
            term = head.group(1)
            matches = [m.strip() for m in head.group(2).split(";")] if head.group(2) else []
            entries.append({"term": term, "matches": matches, "meaning": lines[1],
                            "role": role[len("In Silent Zero:"):].strip(), "id": slug(term)})
        groups.append((name.strip(), entries))
    return groups


def markdown(groups, anchors):
    """The appendix; with anchors, each term carries the id the page links to."""
    out = ["## Glossary", ""]
    for name, entries in groups:
        out += [f"### {name}", ""]
        for e in entries:
            term = f"[**{e['term']}.**]{{#{e['id']}}}" if anchors else f"**{e['term']}.**"
            out += [f"{term} {e['meaning']} *In Silent Zero:* {e['role']}", ""]
    return "\n".join(out) + "\n"
