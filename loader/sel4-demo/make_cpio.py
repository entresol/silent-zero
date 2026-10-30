# SPDX-License-Identifier: BSD-2-Clause
"""Packs kernel and root task into the newc CPIO archive the seL4 ELF loader reads, and writes the assembler stub
that embeds it. Replaces the cpio tool, which the macOS host lacks; the ELF loader itself is unchanged."""
import os
from pathlib import Path
import sys

archive = bytearray()
def append(name, data, ino):
    encoded = name.encode() + b'\0'
    fields = [ino, 0o100644, 0, 0, 1, 0, len(data), 0, 0, 0, 0, len(encoded), 0]
    archive.extend(('070701' + ''.join(f'{v:08x}' for v in fields)).encode())
    archive.extend(encoded)
    archive.extend(b'\0' * (-len(archive) % 4))
    archive.extend(data)
    archive.extend(b'\0' * (-len(archive) % 4))

for i, filename in enumerate(sys.argv[2:], 1):
    p = Path(filename)
    append(p.name, p.read_bytes(), i)
append('TRAILER!!!', b'', 0)
Path(sys.argv[1]).write_bytes(archive)
Path('archive.S').write_text('.section ._archive_cpio,"aw"\n.global _archive_start, _archive_start_end\n_archive_start:\n.incbin "archive.cpio"\n_archive_start_end:\n')
