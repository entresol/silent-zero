# Use Silent Zero

> Silent Zero is a small operating system for machines where AI acts in the physical world. You cannot install it yet. This page says what you can look at today and what is still to come.

- **What it is for** (available now): AI agents that deliver work and, increasingly, move arms or wheels. Silent Zero treats every agent as untrusted, whatever model drives it, and keeps the agent's authority and the machine's safety beneath it. [The paper](https://silentzero.ooo/silent-zero.pdf)
- **See it boot** (available now): A graphical loader checks the seL4 kernel image, shows the result and starts the kernel. 24 seconds of video. [Watch](https://silentzero.ooo/assets/video/loader-sel4-boot.mp4)
- **What verification gives you** (available now): The proven part of the kernel does what its specification says. Everything else is labelled tested or assumed and never passed off as proven; firmware and graphics hardware stay trusted. [Which is which](https://silentzero.ooo/wiki/design/kernel.html)
- **What real-time gives you** (in progress): By design, processor time is held like memory: an agent cannot starve the control loop, and a small deterministic loop has the last word on every motion. Timing bounds for modern processors are not yet proven. [The design](https://silentzero.ooo/wiki/design/safety-path.html)
- **Open and free** (available now): The code is BSD-2-Clause, the paper and the texts CC BY 4.0. [Licence](https://github.com/entresol/silent-zero/blob/main/README.md#licence)
- **Ask a question** (available now): Discussions for questions and ideas, Issues for a flaw or a wrong claim. [Discussions](https://github.com/entresol/silent-zero/discussions)
- **Try it** (planned): A bootable image, first in an emulator.
- **Check your download** (planned): Checksums and signatures, and how to verify them before you boot.
- **Which hardware** (planned): A first board, then a list of what runs on what.
- **Is it certified?** (open question): Not yet. Today's commercial robot stacks list certificates (PikeOS) or work towards them (NVIDIA Halos); the seL4 Foundation's own page names none. How a proof becomes evidence for a certification body is open, and we promise no route to a certificate. [Safety certification in the wiki](https://silentzero.ooo/wiki/concepts/safety-certification.html)

Looking for the other door? [Developers](https://silentzero.ooo/devel/index.html.md)
