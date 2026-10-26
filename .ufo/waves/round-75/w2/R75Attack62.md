# R75Attack62 — independent falsification of facet 62

## Verdict
**Survived attack on its central operational defect; partly overstates current impact.** At pinned HEAD `65a5c7a663249e0522cc49e4a148424200d9ddfe`, Q73's actual pasted detector is broken under rendered-Markdown interpretation: its alternation is escaped into a literal pipe. The report also correctly identifies a live omission of the existing JSON checklist pin from the command's file universe. But the cited checklist pin does not establish a current r75 Q73 event: Q73 is expressly about sections/files a historical counter pins byte-identical, whereas the checklist's normalized text hashes are a separate pin mechanism. Treat that as a design/coverage gap under a broader intended scope, not confirmed present Q73 violation. The proposed four-arm control is design, not evidence of an existing project failure.

## Independent checks
- Re-opened `corpus/QUALITY.md:89`: raw row contains `\|` in the command and has an extra pipe byte versus ordinary rows. At the rendered-command form, `grep -n 'differs from the base|byte-identical' verifiers/*.py` returned no output and exit 1; the raw source form returned **16 matches**. Thus the command as authored and as rendered do not behave equivalently. This materially supports the report's command-escaping finding.
- Executed the cited counter self-test safely: `python3 -B verifiers/check_province_core.py --self-test` exited successfully, reporting `self-test: 0 failure(s) over 12 assertions`. Its output proves the positive ledgered and negative unledgered fixture arms pass, but it does not test preservation of the committed ledger entry. The inspected `:158-172` code injects a test hash and clears the entire dict in `finally`, consistent with that limitation.
- Reopened `verifiers/check_province_core.py:45-51,100-109,158-180` and `verifiers/checklist-baseline.json:1-15`. The counter has a committed SHA-256 exception entry and the JSON baseline has per-box `text_sha256` entries. The quoted `SKILL.md` checklist rationale says reword/add/remove fails; that is an independent pin family not searched by the Q73 `verifiers/*.py` command. It is credible evidence of limited coverage, not proof that such pins are in Q73's literal scope.
- The report's strictest scope argument is explicitly conditional (intent versus literal wording), and its own risk section says it does not claim r75 has a pin conflict. No current defect in a claim's behavior is established by the checklist example alone. Q73's explicit criterion still includes a pre-freeze sweep and a named touch-list; those controls are not demonstrated by the current implementation or the historical counter self-test.

## Evidence state
Measured revision: `65a5c7a663249e0522cc49e4a148424200d9ddfe`. `git status --short` showed pre-existing modifications in lane files and untracked round-75 material; none were edited by this probe. Hashes observed: `corpus/QUALITY.md` `6ed3a9ae6595a9292b24d6fb9594c0704a482b3c`; `verifiers/check_province_core.py` `0cd12b31fae6814321a2f27a1a65eb26477d577b`; `verifiers/checklist-baseline.json` `99dcf89654c81157158a2beda63b2d0161d8fd5d`.

No lane source changes made. No scratch copy or mutation was necessary; this was a safe read/command probe. No restoration operation required.

Report: .ufo/waves/round-75/w2/R75Attack62.md
