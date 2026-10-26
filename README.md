# Silent Zero OS

**Bare minimum. Verified. Real-time. An OS for the AI era.**

Every change in substance is listed in [`CHANGELOG.md`](CHANGELOG.md) and at the end of the page; every change at all in the commit history.

> Imagine it's 1991. We are about to release a few lines of code into a world that will be very different from today.

Silent Zero is an operating system reduced to what cannot be removed: a bootloader, a formally verified microkernel, and the bare minimum needed to run AI agents safely and in real time. Nothing at its base is new; the seL4 microkernel, its system framework and drivers, open roots of trust and open agent protocols all exist as open-source work. What has to be built is the layer between agents and the world: a broker that turns human intent into bounded authority, and a safety path that keeps every motion under a verified loop. Silent Zero starts where agents act physically: one robot, one task.

First light: [a boot screen](splash/) and a [loader](loader/) that checks the kernel image before starting it, 9 KB on RISC-V, tested in QEMU. The paper proposes what we intend to build and where it can fail.

- Read the paper: https://silentzero.ooo
- Download the PDF: [`zos-zero-os.pdf`](zos-zero-os.pdf) (always the newest version)
- Every version as its own file: [`versions/`](versions/), named `zos-zero-os-YYYY-MM-DD-vX.Y.pdf`
- The paper's source and the build for PDF and page: [`paper/`](paper/)
- Red-team report on an earlier draft (German): [`review/red-team-2026-10-18.md`](review/red-team-2026-10-18.md)

Criticism and support are warmly welcome as [issues](https://github.com/entresol/zero-os/issues). To change something yourself, see [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Licence

Code, including the build scripts: [BSD-2-Clause](LICENSE). Fonts: [SIL Open Font License 1.1](assets/fonts/). Paper, texts and figures: [CC BY 4.0](LICENSE-CC-BY-4.0.txt).
