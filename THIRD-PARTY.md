# Third-party code and its licences

Every piece of someone else's work this project uses, where it comes from, under which licence, and whether we pass it on. The rule: we use only open-source work, we name every source, and whatever we pass on in binary form we pass on with its source.

Our own code is [BSD-2-Clause](LICENSE), the paper and texts are [CC BY 4.0](LICENSE-CC-BY-4.0.txt). Licence identifiers follow [SPDX](https://spdx.org/licenses/).

## Passed on

What ends up in a file we publish: in this repository, or attached to a release.

| Component | Source, exact version | Licence | Where it ends up |
| --- | --- | --- | --- |
| seL4 kernel 16.0.0 | [github.com/seL4/seL4](https://github.com/seL4/seL4), commit `6e7c3b733d296cfd88d5fbf635c96e447a882374` (tag 16.0.0) | kernel code: GPL-2.0-only (a few files BSD-2-Clause, BSD-3-Clause, GPL-2.0-or-later, MIT, as their headers say) | `kernel.elf` inside the boot image `sel4.zimg` (release) |
| libsel4, the system-call library | same repository and commit, `libsel4/` | BSD-2-Clause | linked into the demo root task, inside `sel4.zimg` |
| HiFive Unleashed device tree | same repository and commit, `tools/dts/hifive.dts`, copyright SiFive, Inc. | the file carries two SPDX lines: Apache-2.0 and GPL-2.0-or-later | compiled as `kernel.dtb`, inside `sel4.zimg` |
| seL4 ELF loader | [github.com/seL4/seL4_tools](https://github.com/seL4/seL4_tools), commit `6493e0c6fab360eb81a8115a49c9ca7bc280c48a`, `elfloader-tool/` | GPL-2.0-only (a few files BSD-2-Clause, BSD-3-Clause) | the program `sel4.zimg` starts, which unpacks kernel and root task |
| libcpio | [github.com/seL4/util_libs](https://github.com/seL4/util_libs), commit `ef49a397b7044fc38b609a99a8c6265a97913b8e`, `libcpio/` | BSD-2-Clause | linked into the ELF loader |
| Inter (Thin) | [rsms/inter](https://github.com/rsms/inter), the variable font in `assets/fonts/` | SIL Open Font License 1.1 ([text](assets/fonts/LICENSE-Inter.txt)) | the page; rasterised glyphs of "silent zero OS" in `splash/glyphs.h` and so in the loader |
| Nunito Sans | [Fonthausen/NunitoSans](https://github.com/Fonthausen/NunitoSans), the variable font in `assets/fonts/` | SIL Open Font License 1.1 ([text](assets/fonts/LICENSE-NunitoSans.txt)) | the page; rasterised glyphs in `splash/glyphs.h` and so in the loader |

seL4 licenses kernel code under GPL-2.0 and user-level code under BSD-2-Clause. Its [licence note](https://github.com/seL4/seL4/blob/6e7c3b733d296cfd88d5fbf635c96e447a882374/LICENSE.md) says, as the Linux syscall note does, that the GPL "does *not* cover user-level code that uses kernel services by normal system calls". So the GPL binds the kernel and the ELF loader we pass on. It does not bind our loader, which starts the image, nor the root task, nor anything else that runs on seL4. More on this: [sel4.systems/Legal/license.html](https://sel4.systems/Legal/license.html).

**Source for every binary.** A release that contains GPL code carries, as attachments, the complete source of exactly the commits above (`git archive` of each repository), the licence texts of seL4's `LICENSES/` directory, and our build scripts, which are in this repository at the release's tag. `loader/release.sh` assembles this. Nobody has to trust that the sources will still be online somewhere.

## Used, not passed on

| Tool | Version | Licence | What for |
| --- | --- | --- | --- |
| QEMU | 11.1.3 | GPL-2.0 (QEMU's own terms) | the emulated HiFive Unleashed and `virt` machines |
| OpenSBI | v1.8.1, as built into QEMU (`-bios default`) | BSD-2-Clause | firmware in machine mode before our loader; comes with QEMU, not with us |
| xPack RISC-V GCC | 15.2.0-1 | GPL-3.0 with GCC runtime library exception | compiler and linker; `libgcc.a` is linked into the `virt` build of the loader, which the runtime library exception permits |
| CMake, Ninja, Python packages of the seL4 build | pinned in `loader/sel4-demo/requirements.txt` | their own | building seL4 |
| pandoc, LaTeX, Pillow, fontTools, ffmpeg | as installed | their own | building the paper and the page, rasterising glyphs, rendering the video |

Add a line here in the same change that takes in someone else's code, font, image or data.
