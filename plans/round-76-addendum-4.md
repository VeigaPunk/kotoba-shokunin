# Round 76 — addendum 4 (first-sentence measurement convention)

Date: 2026-10-27. Author: L1 `KotobaR76`.

C1 conjunct (d)'s "first-sentence length" is measured on the YAML clip-preserving rendered description and means the character count up to and including the first period followed by a space (`. `). This selects the first sentence without splitting the internal period in `SKILL.md`; for the base `SKILL.md` it is 151 characters (the 150 count omits the period). `verifiers/check_desc_craft.py` already implements this exact boundary. The entry and every audit receipt state the rule beside the value. This fixes the extraction convention; it does not change the measured value or C1 predicate.
