---
type: source
id: nd-sel4-microkit-user-manual
status: reviewed
read: partial
kind: report
sources: [nd-sel4-microkit-user-manual]
updated: 2026-10-29
---

# seL4 Microkit: User Manual, v2.3.0

The manual of the seL4 Microkit, version 2.3.0, undated, read as it stood on 23 October 2026. [Manual](https://docs.sel4.systems/projects/microkit/manual/2.3.0/). The concepts, configurations, system description file, rationale and internals were read in full; the board-specific instructions and the API reference were skimmed.

## What it shows

- **What Microkit is.** A small operating system on [[sel4]] for systems with a *static architecture*, "one where system resources are assigned up-front at system initialisation time" (Introduction). Its targets are IoT, cyber-physical and other embedded systems, and it should be "in principle, amenable to formal analysis of system safety and security properties (although such analysis is beyond the initial scope)" (Purpose).
- **A single description.** The whole system is declared in an XML system description: protection domains, memory regions, channels, interrupts. On Arm and RISC-V the Microkit tool turns it into one bootable image; on x86-64 it produces a kernel image and a boot module for a Multiboot loader (Overview).
- **Protection domains.** A protection domain (PD) is a single-threaded program in its own address space with up to four entry points: `init`, `notified`, `protected` and `fault`. A system holds at most 63 PDs (Protection Domains). The computational model is a set of isolated components reacting to events (Entry points).
- **Paths between PDs.** A channel connects exactly two PDs; through channels a PD can refer to another PD only by a channel identifier (Channels). PDs exchange notifications in either direction, or one calls the other's protected procedure with up to 64 words of arguments. Beyond channels, a memory region can be mapped into several PDs (Memory Regions), and the description's `cspace` element can place another PD's thread, scheduling-context or address-space capability in a PD's capability space (System Description File). All of these are fixed in the description.
- **Rules that serve real time.** A protected procedure may only be called by a PD of strictly lower priority, and the call graph must be acyclic. The rationale: no deadlocks, and resource servers under the immediate priority ceiling protocol without unbounded priority inversion (Rationale). Protected procedures "must execute in bounded time"; the manual says a future version may check this by static analysis, and that for now the caller must trust the callee (Protected procedures).
- **Time.** Each PD has a priority (0 to 254), a budget and a period in microseconds, and can be passive (Scheduling). A passive PD runs on the notification's scheduling context when notified; for protected calls and child faults the manual says it runs "on the scheduling context of the callee", which in our reading means the caller, since the passive PD is itself the callee. Microkit always uses the MCS configuration of seL4 (Proofs). A domain scheduler can switch between groups of PDs on a fixed cyclic schedule (Domain Scheduling), but seL4 supports it only on single-core configurations (System Description File, `domains`). Microkit "does not provides [sic] timers, nor any sleep API"; all activity after initialisation starts from an interrupt (Interrupts).
- **Interrupts and devices.** A hardware interrupt can be associated with at most one PD (Interrupts). Device registers are memory regions; the manual does not restrict them to one PD.
- **Virtual machines.** A VM is always the child of a PD, and a PD can manage only one VM (Virtual Machines).
- **IO address spaces.** The manual describes IO address spaces enforced by an "IOMMU or SMMU" in general terms; the mapping of memory regions into them (`iomap`) is stated explicitly only for x86 (IO Address Spaces, Memory Regions).
- **Build-time checks.** On Arm and RISC-V the tool emulates the kernel's boot to check that the generated capDL specification can be set up on the board, for example that no frame lies outside device or normal memory and that there is enough memory for all kernel objects; if the tool produces an image, "there should be no errors upon initialising the system". The manual ties this to the static architecture (Internals, Arm and RISC-V specific).
- **Boot chain.** The Microkit loader starts seL4, and seL4 starts the capDL initialiser, which creates all kernel objects and capabilities from the specification and starts the PDs; the loader "will never be executed again" (Internals).
- **Viper output.** The tool can write each PD's capability table in the Viper verification language "for verification purposes" (Microkit Tool).
- **Multicore** configurations exist alongside the single-core default (Multi-core).

## How

A user manual: concepts, tools, API and rationale. It makes no measurements.

## Limits

The manual states:

- Verification applies to specific seL4 configurations only, so a release build of a Microkit system does not imply a verified kernel. In version 2.3.0 the MCS configuration was "still undergoing verification, scheduled to complete for RISC-V in 2026 and AArch64 in 2027" (Proofs).
- The bounded-time rule for protected procedures is not enforced.
- On Arm, a PD allowed to make secure monitor calls voids the kernel's WCET properties, since the kernel cannot preempt the secure monitor (`microkit_arm_smc_call`).

A careful reader adds:

- The proof status in the manual is older than the announcement of 29 June 2026 ([[2026-sel4-functional-correctness-proof]]).
- The manual claims no verification of Microkit's own tool, loader or initialiser.
- A parent can stop, restart and resume child PDs. These calls run code already in the image; nothing new is loaded.

## Against the wiki

- [[mixed-criticality]]: **confirms** the passive-server model at the level of the system description.
- [[nd-sel4-verified-configurations]], [[2026-sel4-functional-correctness-proof]]: the manual's proof status is the oldest of the three.
- [[microkit]]: created with this source.

## For zOS

- [[static-system]]: the paper says the whole system is declared in one description and Microkit turns it into the bootable image (Section 3). The manual confirms it.
- [[kernel]]: since Microkit always uses MCS, a Microkit system runs only on a kernel configuration whose proofs exist where MCS is proved. Our reading: on the Raspberry Pi 4, verified only without MCS ([[nd-sel4-verified-configurations]]), a Microkit system has no verified kernel configuration today.
- [[real-time-loops]]: without timers or a sleep API in Microkit, a periodic control loop needs a timer driver of its own.
- Our reading: two rules bear on the broker. Calls go only upwards in priority, and the callee must finish in bounded time, unchecked. A broker called by agents would sit above them in priority, and its bounded time is an obligation zOS has to discharge itself.
