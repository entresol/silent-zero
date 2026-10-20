# zOS – Zero OS

**Bare minimum. Verified. Real-time. An OS for the AI era.**

Working paper 2026-10-20-v0.4 by Tobias von Dewitz, Susann Mürling, Stefan Probst and Daniel Strecker. Every revision is listed on the page and in the commit history.

> Imagine it's 1991. We are about to release a few lines of code into a world that will be very different from today.

zOS is an operating system reduced to what cannot be removed: a bootloader, a formally verified microkernel, and the bare minimum needed to run AI agents safely and in real time. Nothing at its base is new; the seL4 microkernel, its system framework and drivers, open roots of trust and open agent protocols all exist as open-source work. What has to be built is the layer between agents and the world: a broker that turns human intent into bounded authority, and a safety path that keeps every motion under a verified loop. zOS starts where agents act physically: one robot, one task.

Nothing is built yet. The paper proposes what to build first and states where it can fail.

- Read the paper: https://entresol.github.io/zero-os/
- Download the PDF: [`zos-zero-os.pdf`](zos-zero-os.pdf) (always the newest version)
- Every version as its own file: [`versions/`](versions/), named `zos-zero-os-YYYY-MM-DD-vX.Y.pdf`
- Red-team report on an earlier draft (German): [`review/red-team-2026-10-18.md`](review/red-team-2026-10-18.md)

Comments and criticism are welcome as [issues](https://github.com/entresol/zero-os/issues).
