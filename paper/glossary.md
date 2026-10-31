# Glossary

Source for the glossary. The build adds it to the PDF as an appendix and to the page, where the first use of each term in a section links to its entry.

Format: `## Group`, then one entry per block. First line: `**Term**`, optionally followed by ` | ` and the words in the text that should link to it (separated by semicolons, matched case-sensitively as whole words). Second line: what it means, in plain words. Third line: `In Silent Zero:` and its role here. An optional fourth line, `Short:` and at most 50 characters, puts the term into the lexicon (`paper/lexicon.py`).

## Trust and proof

**Byzantine component** | Byzantine
A part that may fail in any way at all, including by lying or acting against the system on purpose.
In Silent Zero: the assumption made about every agent (Section 1).
Short: A part that may fail in any way, even lying

**Formal verification** | formally verified; formal verification; machine-checked proof
Proving with mathematics, checked by a computer, that a program does what its specification says, for every possible input.
In Silent Zero: the standard for the parts a guarantee depends on; seL4's kernel already meets it (Sections 2.3, 3).
Short: Machine-checked mathematical proof about code

**Functional correctness** | functional correctness
The proven statement that an implementation behaves exactly as its specification describes.
In Silent Zero: what seL4 has proven for its verified configurations (Section 3).
Short: Code proven to do exactly what its spec says

**Proven, tested, assumed** | proven, tested or assumed
Three levels of knowledge about a part: shown for every case its specification covers, shown to hold under defined load or attack, or simply trusted.
In Silent Zero: every part of the trusted base carries one of these labels (Section 1).
Short: Three levels of knowledge about a part

**Reference monitor** | reference monitor
The mechanism that checks every access; it must always be invoked, be tamper-proof and be small enough to analyse and test.
In Silent Zero: the reason the system must stay small (Section 1).
Short: Checks every access and cannot be bypassed

**Seam** | seams
The place where a proven part meets an unproven one, and where the assumptions of one must match the guarantees of the other.
In Silent Zero: kept to a minimum on the two critical paths, and each one is specified (Section 6).
Short: Where a proven part meets an unproven one

**Trusted base** | trusted base
The parts that must work correctly for a guarantee to hold; if one of them fails, the guarantee fails with it.
In Silent Zero: kept small and listed part by part (Sections 1, 3).
Short: The parts a guarantee depends on

## Kernel and time

**Microkernel** | microkernel
A kernel that does only what must run with full privilege, such as isolation, messages and scheduling, and leaves everything else to ordinary programs.
In Silent Zero: seL4 (Section 3).
Short: Kernel that does only what needs full privilege

**seL4** | seL4
A microkernel from the L4 family and the first general-purpose kernel with a machine-checked proof of functional correctness.
In Silent Zero: the kernel (Sections 2.1, 3).
Short: Microkernel with a machine-checked proof

**Mixed criticality (MCS)** | mixed-criticality; MCS
Running parts that matter to different degrees on one machine, so that a less important part can never take time from a more important one.
In Silent Zero: seL4's MCS extensions make processor time a protected resource (Sections 3, 4).
Short: Critical and uncritical code on one machine

**Scheduling context** | scheduling contexts
In seL4 MCS, a kernel object that grants a program a budget of processor time per period; the kernel enforces it.
In Silent Zero: limits how much time an agent can use (Sections 3, 4).
Short: Kernel-enforced budget of processor time

**Real time** | real time
Computing in which a result is only correct if it arrives before its deadline.
In Silent Zero: required for every loop that moves something; provable timing is a goal, not yet a property (Sections 1, 4).
Short: A result counts only if it arrives on time

**Worst-case execution time (WCET)** | WCET; worst-case execution time
The longest a piece of code can take to run; a safe upper bound on it is needed to prove that deadlines hold.
In Silent Zero: exists for seL4 only on an old Arm core; being rebuilt for RISC-V (Section 4).
Short: Upper bound on how long code can take

**Timing channel** | timing side channels
A leak in which one program learns secrets from how long another program's operations take.
In Silent Zero: closed only with hardware support that exists as prototypes on open RISC-V cores (Section 4).
Short: Secrets leaking through how long things take

**Protection domain** | protection domains
An isolated program in a static seL4 system, with its own memory and only the access it was given.
In Silent Zero: every agent and every component runs in its own (Section 3).
Short: An isolated program in a static seL4 system

**Static system** | static system
A system whose structure, programs, channels and shared memory are fixed when the image is built and cannot change at run time.
In Silent Zero: the whole system is declared in one description (Section 3).
Short: Structure fixed when the image is built

**Microkit** | Microkit
seL4's framework for building static systems from protection domains, channels and shared memory.
In Silent Zero: turns the system description into the bootable image (Section 3).
Short: Builds static seL4 systems from one description

**LionsOS** | LionsOS
A modular, static operating system on seL4 and Microkit from the group behind seL4.
In Silent Zero: the base to start from (Section 5).
Short: Modular, static operating system on seL4

**Multikernel** | multikernel
A configuration that runs one separate kernel instance per processor core instead of one kernel for all cores.
In Silent Zero: how a proven system will later use several cores (Section 6).
Short: One kernel instance per processor core

## Agents and authority

**Agent** | agent; agents
A program that reads, decides and acts on its own, usually driven by a language model.
In Silent Zero: an untrusted tenant with a time budget (Sections 1, 3).
Short: A program that reads, decides and acts on its own

**Capability** | capabilities
An unforgeable token that both names a resource and grants a specific right to it; whoever does not hold it cannot use the resource.
In Silent Zero: the only way authority is passed (Sections 2.4, 3).
Short: Unforgeable token that names and grants a right

**Capability broker** | broker
The single component that hands out authority: limited, time-bound and revocable.
In Silent Zero: part of the trusted base; tested first, proven later (Sections 3, 5).
Short: The one component that hands out authority

**Confused deputy** | confused deputy
A program that misuses authority given to it by one party while acting on behalf of another.
In Silent Zero: the old name for what prompt injection does to agents (Section 2.4).
Short: Misusing one party's authority for another

**Prompt injection** | prompt injection
Instructions hidden in data, such as a web page or an email, that steer an agent reading it.
In Silent Zero: not solved, but limited in what it can reach (Sections 2.4, 6).
Short: Hidden instructions in data that steer an agent

**Information-flow control** | information-flow control
Tracking where data comes from and where it may go, so that it cannot leave through a channel that is otherwise allowed.
In Silent Zero: needed in addition to capabilities (Section 6).
Short: Tracking where data may come from and go

**Model Context Protocol (MCP)** | Model Context Protocol; MCP
An open protocol that connects agents to tools and data sources.
In Silent Zero: the way agents reach tools, always through the broker (Section 3).
Short: Open protocol connecting agents to tools

## Robots and safety

**Action model (VLA)** | action model; action models
A model that turns what a robot sees and is told into motor commands; VLA stands for vision-language-action.
In Silent Zero: plays the complex, unproven controller (Sections 2.4, 4).
Short: Model that turns sight and words into motion

**Action chunking** | chunks
Emitting several motor commands at once, so that the robot keeps moving while the model computes the next ones.
In Silent Zero: why the motion path needs real time (Section 2.4).
Short: Several motor commands from one model call

**Simplex architecture** | Simplex
A safety pattern in which a complex controller runs the system while a simple, trustworthy one takes over before the system leaves a safe region.
In Silent Zero: the agent proposes, the verified loop disposes (Section 4).
Short: A simple safe controller guards a complex one

**Safety controller** | safety controller
The simple controller in the Simplex pattern, with the last word over every motion.
In Silent Zero: part of the trusted base, at the highest criticality (Sections 3, 4).
Short: The simple controller with the last word

**ROS 2** | ROS 2
The Robot Operating System, the most common middleware that connects the software parts of a robot.
In Silent Zero: shown running on seL4 in proofs of concept (Section 2.4).
Short: Common middleware linking a robot's software

## Hardware

**RISC-V and CVA6** | RISC-V; CVA6
RISC-V is an open instruction set anyone may implement; CVA6 is an open-source RISC-V core whose timing can be fully inspected.
In Silent Zero: the first platform, because only there is a timing proof within reach (Sections 4, 7).
Short: Open instruction set; an open core built on it

**Root of trust** | root of trust
A small piece of hardware that is trusted to measure and check the first code a machine runs.
In Silent Zero: the bottom of the trusted base; OpenTitan is an open one (Section 3).
Short: Hardware that checks the first code to run

**OpenTitan** | OpenTitan
An open-source silicon root of trust, in production since 2026.
In Silent Zero: the open option for the root of trust (Sections 3, 5).
Short: Open-source silicon root of trust

**IOMMU** | IOMMU
Hardware that restricts which memory a device may read and write directly (DMA, direct memory access).
In Silent Zero: without a proven IOMMU configuration, a driver with such a device joins the trusted base (Sections 3, 7).
Short: Limits which memory a device may access

**Firmware** | firmware
Code that runs below or before the operating system, often with more privilege than the kernel.
In Silent Zero: trusted and assumed; it cannot be confined by any kernel (Sections 3, 6).
Short: Code below or before the operating system

**CHERI** | CHERI
A hardware extension that makes pointers unforgeable, so that memory errors are caught by the processor.
In Silent Zero: used where available (Sections 3, 5).
Short: Hardware that makes pointers unforgeable

**Driver island** | driver island
A Linux virtual machine that runs drivers Silent Zero cannot replace, such as those for graphics and AI accelerators.
In Silent Zero: on the agent's side, outside the trusted base where an IOMMU confines its devices (Section 3).
Short: Linux VM for drivers that cannot be replaced
