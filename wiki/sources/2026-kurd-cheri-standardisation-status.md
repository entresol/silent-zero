---
type: source
id: 2026-kurd-cheri-standardisation-status
status: reviewed
read: full
kind: progress
sources: [2026-kurd-cheri-standardisation-status]
updated: 2026-11-23
---

# Kurd 2026: CHERI standardisation status

Tariq Kurd (Codasip), "Standardisation Status: Where the specification is now", slides dated 6 April 2026, from CHERI Blossoms 2026 (event name from the pool entry; the slides show only the date and the CHERI Alliance as copyright holder). [Slides](https://cheri-alliance.org/wp-content/uploads/2026/04/D1-3.6-Tariq-Kurd-CHERI-Standardisation-Status-CHERI-Blossoms-2026.pdf). Read in full: the text of the slides, which has no speaker notes; the talk itself was not heard.

## What it shows

- **The path to a RISC-V standard.** The slides list the stages of RISC-V's ratification flow: inception, plan, develop, freeze, public review (about 40 days) and ratification by the Board of Directors.
- **Where the CHERI specification stood.** The specification was trying to reach the freeze. The slides call it the key development milestone: after it only serious bugs allow a change, and all encodings and mnemonics are final. Version 0.9.7 had been submitted for architecture review, "the main hurdle". Earlier versions had changed after review feedback: simpler exception reporting, no exceptions from branches and jumps, and new names for all mnemonics and CSRs.
- **What was still missing.** Three points were awaited: confirmation of how multiple capability encoding formats are declared, final instruction encodings, and final CSR addresses.
- **The rest of the freeze checklist.** The document is complete and all opcodes are specified, none in the custom space. Simulators exist in Sail and QEMU and need updating for all capability formats. LLVM support is available. The ABI is a draft with "maybe more work needed". Tests wait for frozen encodings. A proof of concept needs at least one core updated to the approved specification.
- **The timetable.** The slide is titled "out of date". It gives ratification as intended for the second quarter of 2026 with the third more likely. The plan: finish the architecture review in April, update the tools, hold the public review from early June to July, be ratification-ready in August 2026 and be ratified at the next board meeting.

## How

A conference status talk in slides. It reports the state of a specification, not a measurement, and it counts as `progress` for that reason.

## Limits

A careful reader adds:

- The state is that of 6 April 2026, and the slide itself marks its timetable as out of date. The slides say nothing on whether the freeze, the public review or the ratification happened afterwards, and the pool holds no later source. Whether the standard is ratified today is open.
- The slides call the document complete and the encodings not yet final; they do not say how much of the specification a change of encodings would touch.
- The author's affiliation is a company; the slides name no product or core and do not say what proof of concept is planned.
- The slides do not give the name of the base the specification defines. [[2025-cheriot-cheriot-isa-1]] calls the RISC-V CHERI base "tentatively named Y". That both describe the same effort is our reading.

## Against the wiki

- [[2026-moore-cheri-is-being]]: **extends**. Moore's slides give the criteria and the status "being standardised" and point to this talk for the details. These slides give the stage: architecture review pending, ratification intended for the second quarter and thought more likely in the third.
- [[cheriot]]: **extends**. The open question on standardisation now has a stage and a dated estimate, and still no ratification.

## For zOS

- [[root-of-trust]]: the paper says CHERI is being standardised for RISC-V and that the work is under way. These slides agree for April 2026 and give no basis for a firmer statement. They also give no basis for relying on ratified CHERI hardware in a first zOS board.
