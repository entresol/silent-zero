---
type: source
id: nd-linux-landlock-unprivileged-access
status: reviewed
read: partial
kind: report
sources: [nd-linux-landlock-unprivileged-access]
updated: 2026-11-03
---

# Linux kernel documentation: Landlock

Mickaël Salaün, "Landlock: unprivileged access control", [Linux kernel user-space API documentation](https://docs.kernel.org/userspace-api/landlock.html), dated October 2026 on the page and built for kernel 7.4.0-rc1, as saved on 2 November 2026. Read in part: the introduction, the example, the compatibility section, the current and previous limitations and the kernel-support section. The reference for each system call and access right was not read line by line.

## What it shows

- **Purpose.** Landlock lets a set of processes restrict their own ambient rights, such as global filesystem or network access. It is a stackable Linux security module, so a sandbox adds a layer to the system-wide access controls, and any process, including an unprivileged one, can restrict itself. The text says such a sandbox is "expected to help mitigate" the effects of bugs or malicious behaviour in user-space applications.
- **Rules.** A ruleset aggregates rules that name a resource and the allowed actions: file hierarchies, TCP ports (ABI 4) and UDP ports (ABI 10), Linux capabilities and namespace types (both ABI 12). The ruleset must name every access right it handles, to keep kernel and user space compatible, and handled rights that no rule allows are denied. A ruleset restricts the thread that enforces it and its future children.
- **Compatibility.** The interface is versioned (ABI numbers) and the documentation recommends a best-effort approach: detect the version at run time and enforce the supported subset.
- **Privilege rule.** An unprivileged process must set `no_new_privs`. The text warns that leaving it unset lets a sandboxed process run set-user-ID programs that would then become confused deputies.
- **Limits it states.** Threads sandboxed with filesystem restrictions cannot change the filesystem layout with `mount` or `pivot_root`, but `chroot` is not denied. Pipes, sockets reached through `/proc/<pid>/fd` and some special filesystems cannot be restricted explicitly, though ptrace restrictions automatically limit access to the sensitive `/proc` files according to the domain hierarchy. At most 16 rulesets can be stacked. Landlock appeared in Linux 5.13 and needs a build option and boot-time enabling.

## How

Reference documentation for developers, with a worked C example. It reports no measurements and no analysis of the module's own security.

## Limits

The page describes the interface, not its assurance. Our reading: Landlock runs inside the Linux kernel, for which the page claims no verification; it restricts what a process may name and do, but the kernel that enforces it stays in the trusted base, as does everything a permitted action can reach.

## Against the wiki

- [[landlock]]: created with this source.
- [[object-capabilities]], [[confused-deputy]]: our reading: Landlock rules are ambient-authority restrictions by path and port, not unforgeable references; the page's own warning about set-user-ID programs is the confused-deputy problem.
- [[broker]]: a candidate mechanism for a hardened-Linux agent, which the paper names as the main alternative to zOS.

## For zOS

Section 6 of the paper says Linux restricts processes with Landlock, citing this page. That is confirmed. The paper's hardening alternative is accurate as far as the source goes; whether it suffices is argued in the paper, not here. No `design/` page changes state.
