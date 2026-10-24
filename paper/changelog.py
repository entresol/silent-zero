# SPDX-License-Identifier: BSD-2-Clause
"""Reads ../CHANGELOG.md for build_paper.py and build_site.py: the entries, and the current paper version."""
import re
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "CHANGELOG.md"
SCOPES = ("Paper", "Site", "Project")


def parse(path=PATH):
    """Returns [(version, scope, text), ...], newest first; a version without -vX.Y is a date only."""
    entries = []
    for block in re.split(r"\n## ", Path(path).read_text(encoding="utf-8"))[1:]:
        head, _, text = block.partition("\n")
        m = re.fullmatch(r"(\d{4}-\d{2}-\d{2}(?:-v\d+\.\d+)?) · (\w+)", head.strip())
        assert m and m.group(2) in SCOPES, head
        entries.append((m.group(1), m.group(2), " ".join(text.split())))
    return entries


def has_pdf(version):
    return "-v" in version


def current(entries):
    """The newest paper version: the one printed on the paper and offered as the PDF."""
    return next(v for v, _, _ in entries if has_pdf(v))
