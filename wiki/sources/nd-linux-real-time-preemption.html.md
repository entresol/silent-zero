# Linux kernel documentation: real-time preemption

> PREEMPT_RT in the kernel documentation: sleeping locks, threaded interrupts, shared-hardware limits. report, partly read.

Source · LLM reviewed · updated 2026-11-03 · https://silentzero.ooo/wiki/sources/nd-linux-real-time-preemption.html

[Real-time preemption](https://docs.kernel.org/core-api/real-time/index.html), core API documentation of the Linux kernel (page footer: kernel 7.4.0-rc1), saved on 2 November 2026. Three of its chapters were also read, as saved on 3 November 2026: "Theory of operation" (Sebastian Andrzej Siewior), "How realtime kernels differ" (same author) and "Considering hardware" (same author). The chapters on porting an architecture and on kernel configuration were not read.

## What it shows

- **What PREEMPT_RT does.** It makes the kernel real-time by replacing locking primitives such as `spinlock_t` with preemptible locks that donate priority to the owner (priority inheritance), and by forcing interrupt handlers into threads. The kernel becomes fully preemptible apart from a few critical paths, among them entry code, the scheduler and low-level interrupt handling. The stated effect is a shorter delay between a high-priority task becoming runnable and its running on the CPU.
- **Forced-threaded interrupts.** A short primary handler wakes a handler thread, which by default runs under the `SCHED_FIFO` policy at priority 50; the interrupt source stays masked until the thread has finished.
- **Hardware is shared.** The chapter on hardware says that heavy use of a shared resource by one application can affect the deterministic handling of others. Caches and main memory are shared, including with devices that use DMA; buses such as USB add variable delay; cache partitioning exists (Intel CAT, AMD PQoS, Arm MPAM) and is configured through resource control.
- **Virtualization and firmware.** A real-time guest needs care: host threads for guest CPUs, emulated devices and idle handling add latency. Firmware can interrupt the kernel, for example for memory scrubbing, and a hardware latency detector can make long interruptions visible.

## How

Developer documentation. It describes mechanisms and advice and gives no worst-case bounds. The firmware section mentions, for one case, a world-switch overhead of typically a few microseconds, which it does not present as a bound.

## Limits

The chapters read give no worst-case execution time for any path and claim none; the chapters on porting and configuration were not read. Our reading: what the chapters read offer is a design that is fully preemptible apart from a few critical paths, not a proven bound. In places they advise testing, for example that a real-time guest CPU thread should be tested to sustain its behaviour over extended periods.

## Against the wiki

- [PREEMPT_RT](https://silentzero.ooo/wiki/systems/preempt-rt.html.md): created with this source.
- [WCET analysis](https://silentzero.ooo/wiki/concepts/wcet-analysis.html.md): the chapters read give PREEMPT_RT no static bound; seL4's analysis aims at one.
- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md), [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md): the hardware chapter names shared caches and memory as a source of interference, which is the problem that [Time protection](https://silentzero.ooo/wiki/concepts/time-protection.html.md) addresses at the kernel level.

## For Silent Zero

Section 6 of the paper says Linux supports real time with PREEMPT_RT, citing this page. Confirmed. The chapters read promise no latency bound. No `design/` page changes state.

## Related pages

- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md)
- [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md)
- [Time protection](https://silentzero.ooo/wiki/concepts/time-protection.html.md)
- [WCET analysis](https://silentzero.ooo/wiki/concepts/wcet-analysis.html.md)
- [PREEMPT_RT](https://silentzero.ooo/wiki/systems/preempt-rt.html.md)
