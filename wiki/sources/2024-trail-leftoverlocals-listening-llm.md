---
type: source
id: 2024-trail-leftoverlocals-listening-llm
status: reviewed
read: partial
kind: test
sources: [2024-trail-leftoverlocals-listening-llm]
updated: 2026-11-03
---

# Khlaaf and Sorensen 2024: LeftoverLocals

Heidy Khlaaf and Tyler Sorensen, Trail of Bits blog, 16 January 2024: [LeftoverLocals: Listening to LLM responses through leaked GPU local memory](https://blog.trailofbits.com/2024/01/16/leftoverlocals-listening-to-llm-responses-through-leaked-gpu-local-memory/). Read from the page as saved on 23 October 2026. Read in part: the summary, the exploit brief, the vulnerability section and the sections on LLM security, GPU vendors and the way forward. The background on GPU architecture and the per-device test table were not read in detail.

## What it shows

- **The flaw.** On several GPUs, one program can read values that another program left in the GPU's local memory, an optimised memory region. The authors name Apple, Qualcomm and AMD GPUs as affected from their own tests; they did not observe the leak on the Imagination GPUs they tested, but Google confirmed that some Imagination GPUs are affected; the flaw is tracked as CVE-2023-4969.
- **The attack.** A co-resident attacker needs only to run GPU compute programs, for example through OpenCL, Vulkan or Metal. The attack kernel can be under ten lines. The authors built a proof of concept that listens to another user's interactive LLM session (llama.cpp) across process or container boundaries.
- **Amount.** On an AMD Radeon RX 7900 XT the flaw leaks about 5.5 MB per GPU invocation, which for a 7B model on llama.cpp adds up to about 181 MB for each LLM query, enough in the authors' words to reconstruct the response with high precision.
- **Vendor status at publication.** NVIDIA and Arm said their devices are not affected, and the authors saw no effect on the Intel GPU they tested. AMD confirmed its devices remained affected. Apple had patched some devices and not others (the MacBook Air M2 still appeared affected on 10 January 2024). Qualcomm had a firmware patch for some devices. Imagination had released a fix in December 2023. Browser GPU frameworks such as WebGPU appear unaffected because they insert dynamic memory checks.
- **Mitigation.** Without vendor patches, the user must clear the local memory in every GPU kernel before it ends and keep the compiler from removing that clearing. The authors call this hard to verify, since GPU binaries are rarely stored and few analysis tools exist.
- **A specification gap.** The authors know of no unified security specification for how GPUs handle sensitive data and no portable test suite for simple leaks like this one. They quote the Vulkan specification's requirement that operating-system guarantees about memory visibility between processes not be violated.

## How

Testing of GPUs from many vendors with a listener and a writer program, a proof of concept on an LLM session, and coordinated disclosure since September 2023 through CERT/CC with all major GPU vendors and the Khronos Group.

## Limits

What the authors say themselves: the proof of concept targets one application; other attacks would likely need the victim's kernel code to reveal where it uses local memory. The authors also say attackers could likely target many GPU applications. A careful reader adds:

- **Dated.** The status is that of January 2024. We did not check current patch levels, and the page cannot say whether the 181 MB figure holds on other devices.
- **Vendor statements.** For NVIDIA and Arm the "not affected" status is the vendors' word, as the authors say, and for Intel their own limited test.

## Against the wiki

- [[drivers]]: adds a measured case of an accelerator that leaked data between processes, which bears on the "assumed" hardware layer.
- [[iommu]]: the leak happens inside the GPU, below anything an IOMMU mediates; our reading, as the source does not discuss IOMMUs.
- [[prompt-injection]], [[broker]]: unrelated mechanisms; this is a hardware isolation failure, not an attack through the model's input.

## For zOS

Section 6 of the paper writes that GPUs "have leaked memory between processes, and one flaw exposed about 181 MB per query of a running language model (Trail of Bits 2024)". Confirmed, with two qualifications the paper's sentence leaves out: the figure was measured on an AMD Radeon RX 7900 XT running a 7B model in llama.cpp, and 5.5 MB per invocation is the unit it adds up from. No `design/` page changes state.
