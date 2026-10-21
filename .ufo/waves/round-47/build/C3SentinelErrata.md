verdict: HIGH conditional design blocker — do not ship a generic author-writable exception list; at BASE the gate still fails closed on the one recorded missing runner, and no erratum-registry implementation is present to test.

## Axes

- **Calibration (primary):** an exception can make the gate green without establishing that the absence was true. Bind only the recorded Round-46 miss; do not grant a general waiver mechanism.
- **Operability:** the current gate names the exact failing token and prints counts. Keep those properties, and make malformed, stale, unused, or over-cap registry rows fail closed.
- **Freshness:** this is a historical Round-46 draft path, not a currently available runner. A round-scoped entry must expire rather than silently carrying forward.

## Findings

### F1 — HIGH, conditional: a self-authored registry row can launder an arbitrary dead citation

**Exploit path.** If the proposed gate merely skips any unresolved token named in a registry row, an author can add a row for a different dead path with a plausible non-empty reason. Requiring the source line to contain the word “absent” still permits an author to append a new line that asserts that path is absent, then calculate and store its own line hash. A per-round cap of one only limits the number of fabricated exceptions; it does not bind that one exception to the observed Round-46 event. A hash stored only beside the row is likewise self-asserted. Reason, round, hash, and cap are useful validation fields, but none authenticates the exception on its own.

**Evidence at BASE.** `plans/round-47.md:34-39` scopes C3 to the governance citation at `LOG.md:2111`. That line records that `python3 .ufo/round-45/drafts/v10/post-r44-hunt.py` exited 2 because the referenced runners were absent. At BASE, `verifiers/verify_skill_checklist.py:1454-1495` extracts the governance subjects and fails any unresolved subject; it contains no errata registry. The live read-only reproduction below identifies exactly that token. The line itself therefore records an absence, but it is not an independent proof that an arbitrary future registry row is justified.

The logged supporting report is hash-pinned in `LOG.md:2110`; the local `.ufo/round-46/scouts/U1.md` digest matches that recorded SHA-256. However, `git ls-tree` at the historical observation commit `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` returns no tracked U1 report entry. Do not make a clean-checkout gate depend on that untracked artifact being available. The append-only, committed LOG line is the durable recorded claim; any stronger claim of independent authentication needs durable evidence.

**Impact.** A broad or self-pinned row turns calibration into self-exemption: the reported count may look healthy while an arbitrary dead citation is no longer checked. Even a strict schema cannot establish that an author’s assertion is true; the policy must limit which fact can be exempted and make any change visible for review.

**Smallest remediation.** Implement only the one Round-47 exception for the exact normalized tuple `(LOG.md, 2111, .ufo/round-45/drafts/v10/post-r44-hunt.py)`. Put its allowed tuple and registry SHA-256 in a separately checked-in, review-visible pin (for example, the verifier’s existing pinned baseline), not solely in the registry. Store the exact source-line SHA-256, `round: 47`, a mandatory non-empty typed reason plus explanatory text, and—if available—a digest/reference to durable evidence. Enforce a hard active-row cap of **1** for this round, justified by the single baseline failure, and require the line to contain the exact token and an unambiguous same-line absence statement. Match the token through the existing extractor’s canonical form; an entry may suppress only that one subject, never other citations on the line. Recheck that the target is genuinely absent; existence, a symlink (including a dangling symlink), permission/read errors, or ambiguous path resolution must not be treated as absence. Reject every unconsumed/stale/duplicate entry and every unregistered dead token. Never execute a command or path read from the registry.

The registry parser should reject invalid JSON, duplicate object members, duplicate entries, unknown keys, wrong types (including booleans where integers are expected), invalid hashes, and paths outside the exact allowlisted root set. Round mismatch, wrong line/hash/token, missing reason, and count above the pinned cap must fail rather than be ignored or truncated. Print separate raw-candidate, resolved/checked, and registered-exception counts plus the exact excluded `(source, line, token)`; retain the existing non-vacuity rule that at least one non-exempt subject is actually checked. A local SHA pin detects drift; it is not cryptographic proof against a contributor who also changes the pin or verifier, so such changes still require normal independent review.

### F2 — MEDIUM, existing adjacent laundering surface: quotes and schematics already bypass resolution

**Exploit path.** An author can put a dead backticked path inside a same-line double-quoted span so the governance parser classifies it as a quoted meta-finding. A token containing an ellipsis or literal `round-N` is likewise classified as schematic. These are current intentional exclusions, not behavior introduced by the planned registry, but they mean an arbitrary dead token can already be made uncounted by changing its presentation.

**Evidence at BASE.** `verifiers/verify_skill_checklist.py:1384-1427` applies the quoted and schematic exclusions; `:1454-1495` reports those counts but resolves only the remaining subjects. Its self-test at `:2023-2043` writes a quoted dead citation and expects a passing governance result alongside a live control. The live reproduction below reports `9 quoted meta-finding(s), 3 schematic token(s) excluded`.

**Impact.** A registry-only fix must not be described as closing every citation-laundering route. These existing exclusions are broad syntactic classifications; their counts make them visible, but do not establish that every quoted or schematic-looking reference is truly historical context.

**Smallest remediation.** Keep registry accounting disjoint from both existing exclusion classes and do not let an erratum change their counts or semantics. Wave 2 should include a planted quoted dead control and a literal `round-N` control; if the intended security claim is that no author can hide a dead citation by formatting alone, that claim additionally requires narrowing or evidence-binding these existing exclusions.

## Wave-2 probes

1. **Honest pinned control:** exact BASE tuple only; expected `[INFERENCE]` raw candidates 805, one registered exception, 804 remaining checked, zero unresolved, PASS; output names the exception and prints all three counts. An absent registry or removed row must leave the original citation failing.
2. **Same cap, different target:** replace the allowed token with a second dead path while keeping `round: 47`, a non-empty reason, and an entry count of one. Expect FAIL because the external pin/tuple differs.
3. **Self-issued absence:** add an unrelated line stating that a fabricated dead path is absent, then add a matching row and freshly computed line hash. Expect FAIL; this discriminates an exact event pin from “line says absent + self-hash.”
4. **Binding mutations:** wrong source file/line/token, off-by-one line, stale or altered line hash, normalized-path alias, a second token on the same line, and a changed target that now exists must each fail; the unregistered/adjacent token must remain checked.
5. **Bad registry data:** missing/blank reason, wrong type, unknown key, invalid JSON/hash, duplicate JSON member, duplicate row, unused row, and more than one row all fail closed with a named diagnostic; do not last-win parse or silently truncate to the cap.
6. **Round and absence semantics:** entries for rounds 46 or 48 do not apply to Round 47; an expired row is not silently carried. A dangling symlink, unreadable path, or resolver error is not proof of absence. No registry-supplied command is executed.
7. **Existing exclusion controls:** retain and report the quoted-dead and `round-N` schematic cases separately. Confirm neither is counted as a registry exception, and decide explicitly whether those existing syntactic exclusions remain within the security claim.

## Commands and observations

- `git diff --quiet c61a973b2e02e1ded169703ddcb06466f4edd8bd -- LOG.md verifiers/verify_skill_checklist.py corpus/lessons/round-46-verifier-spotcheck.md` — exit **0**; these three inspected tracked files matched BASE at check time.
- `PYTHONDONTWRITEBYTECODE=1 python3 -B verifiers/verify_skill_checklist.py --repo . --skill SKILL.md --check governance.citation_resolves --json` — exit **1**; `evaluated: 805`, `FAIL`, `LOG.md:2111: '.ufo/round-45/drafts/v10/post-r44-hunt.py' does not resolve`, with 9 quoted and 3 schematic subjects excluded.
- `test ! -e .ufo/round-45/drafts/v10/post-r44-hunt.py` — exit **0**; absent in the current working tree.
- `git ls-tree -r c61a973b2e02e1ded169703ddcb06466f4edd8bd -- .ufo/round-45/drafts/v10/post-r44-hunt.py` — exit **0**, no tree entry. The same query at recorded observation commit `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` — exit **0**, no tree entry.
- `git ls-tree -r 055d3b9a3f7eb28d13452a0d26853ef4feabf2ae -- .ufo/round-46/scouts/U1.md` — exit **0**, no tree entry. `sha256sum .ufo/round-46/scouts/U1.md` — exit **0**, local digest `d8d137d24d24f1605f5d6164b761d33fbdbcd403ae1a8ee43227b28b218e1388`, matching the digest recorded at `LOG.md:2110`.
- `git cat-file -e c61a973b2e02e1ded169703ddcb06466f4edd8bd:.ufo/round-45/drafts/v10/post-r44-hunt.py` — exit **128**, Git printed that the path does not exist in the commit; the clean `git ls-tree` query above was used for the tree-presence observation.

## Not checked

No registry implementation exists at BASE, so I did not execute an arbitrary-entry exploit or claim the proposed design is verified. I did not run `--self-test`, the full checklist, corpus gates, or the historical missing-runner commands; I did not authenticate the local U1 report as a tracked artifact or independently reproduce its historical run. No production files were changed; only this scoped report was written.