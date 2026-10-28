# Kb81S09SkillRule — SKILL.md edits draft (round 81, w1)

Seat: scribe. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Base: `b284223105f4d106f7e8f56ed4fd296c643cda0e`.
Scope: **no lane file edited**; all measurement in the scratch clone `/fast/scratch/hyaku/kotoba-r81/Kb81S09SkillRule/clone` (removed before yield). The integration patch and every receipt are under `.ufo/waves/round-81/build/`.
Inputs read: `plans/round-81.md` § C2 (conjuncts a–g), `SKILL.md:150-180` (allowed-tools rule area), `SKILL.md:511-519` (registry table style incl. the r80 `check_allowed_tools.py` row), `verifiers/check_gate_registry.py` (frozen rules, lines 3–58 and 194–241), `corpus/SOURCES.md:189` (S248 row).

---

## 1. SDK-channel line for the `allowed-tools` author-facing rule area

### Exact text (append to the paragraph at `SKILL.md:164`)

```
Claude Agent SDK — query-config `allowedTools` (`allowed_tools` in Python) grants the same pre-approval the frontmatter field does; managed settings can ignore both (S248/S249; entry `corpus/knowledge/allowed-tools-sdk-round81.md`).
```

Placement: append as the **final sentence** of the existing paragraph that begins `Treat \`allowed-tools\` as pre-approval, never as a sandbox` (`SKILL.md:164`), i.e. directly after `…but use the client's actual permission mechanism when the policy must restrict tools.` — this keeps the SDK channel inside the same author-facing "pre-approval, never a sandbox" area the claim names, and it adds **0 new source lines** (the paragraph grows by 233 characters, one space plus a 232-character sentence, 25 words; the line was already long). ≤3 lines satisfied.
If the L1 wants the channel visible as its own block, the same single sentence stands as its own paragraph immediately after line 164: 1 blank line + 1 text line = **2 source lines**, still ≤3.
House-style variant only if desired: the lane's existing cite order is entry-then-ids — `(entry \`corpus/knowledge/allowed-tools-sdk-round81.md\`, S248/S249)`. The literal text above is the brief's; both forms are one line.

### Citation resolution (measured, not assumed)

| Citation | State at base `b284223` | Resolution evidence |
|---|---|---|
| entry `corpus/knowledge/allowed-tools-sdk-round81.md` | absent | `git cat-file -e <F>:corpus/knowledge/allowed-tools-sdk-round81.md` → exit **0**, where `F` = `41683f39846b43aaeba68dc7c8a64b45cc7ff86e` is commit `D` with **E08's real entry** (`build/allowed-tools-sdk-round81.md`, two `source:` lines S249/S248, `verified-at`, runnable `recheck:`) copied in. Earlier, at `D`, a clearly-labelled placeholder stood in for the then-unpublished entry; `F` supersedes it as the evidence tree. Registry gate at `F`: `gate registry rows conformant 64 of 64 lane verifiers; phantom 0`, exit **0** (`Kb81S09SkillRule-registry-at-F-realentry.txt`). |
| `S248` | row at `corpus/SOURCES.md:189`, status `queued`, `used-by` `—` | row resolves at base (`grep -c '^| S248 '` = 1 at `D`). C2 conjunct (e) — S248 `used-by` old→new to the entry — is another seat's edit; the line is truthful only in the tree where that lands. |
| `S249` | no row | `grep -c '^| S249 '` = **0** at base and at `D`. Created by plan § Frontier / C2 conjunct (b); the line's citation is resolved by the row the claim ships. |

Both S-citations are *scheduled to land in this wave*: S05's published patch `build/Kb81S05SourcesEdits.patch` adds `| S249 | Claude Code Agent SDK — Skills | … | docs | A |` with the same `ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2` / 28395 B pin and rewrites S248's row (`used-by` moves off `—`). I read those two hunks rather than deriving them; they are S05's product, and my line is the SKILL.md side that must be consistent with them.

Claim tokens against the fetched page bytes (my own `curl -sS -L`, HTTP 200, **28395 B**, sha256 `ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2` — byte-identical to E08's `.ufo/waves/round-81/snapshots/S249.md`, same sha256, and to its `S249.fetch.json`):

```
allowedTools 5   allowed_tools 4   allowManagedPermissionRulesOnly 1   "ignores both" 1   "pre-approve tools for a project or personal skill" 1
```

The "ignore both" clause is the page's own wording, snapshot line 348: *"If your organization sets `allowManagedPermissionRulesOnly` in managed settings, Claude Code ignores both."* Note for the reviewer: S248's committed `teaches` cell says **"managed settings can override both"**; if the L1 prefers the SKILL line to reuse the row's verb, `override both` is equally sourced — `ignore both` is literal to the page. Located-quote candidate for the entry (≤25 words, contains `allowedTools`): *"In SDK sessions, you can pre-approve tools for a project or personal skill with the skill's allowed-tools frontmatter or with the allowedTools option"* — **23 words**, starts at byte **19713** of the snapshot, line 348.

No-regression on the r80 gate: `python3 -B verifiers/check_allowed_tools.py --repo <clone> --rev <D>` → exit **0**, prints `skill rule line ok`, `registry home ok`, form target `6 of 6` (receipt `Kb81S09SkillRule-r80-counter-at-D.txt`; base run also exit 0). The added sentence does not disturb the r80 counter's SKILL.md line check.

---

## 2. The exact `## Gate registry` row

One line, appended **after** the `verifiers/check_allowed_tools.py` row (the table's current last row, `SKILL.md:518`, immediately before `## Sources`). Same 8 columns as the header at `SKILL.md:454`.

```
| `verifiers/check_sdk_allowed_tools.py` | gate | `python3 -B verifiers/check_sdk_allowed_tools.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — round-81 C2 counter (depth): the Agent SDK documents a second grant channel for the field, a query-config `allowedTools` option (`allowed_tools` in Python) beside the skill's `allowed-tools` frontmatter, with the managed-settings `allowManagedPermissionRulesOnly` override; committed bytes only — the entry `corpus/knowledge/allowed-tools-sdk-round81.md` carries the provenance trio and a located quote, `corpus/SOURCES.md` row S249 is `mined` tier-A/B naming the entry with the sha256-pinned snapshot, row S248's `used-by` names the entry, the quote occurs in the snapshot's text view after the first heading, `SKILL.md` names the SDK channel and this row exists; `sdk allowed-tools surface documented N of 1` | `--self-test` | in-file | none (reads committed bytes via `git show`; a `--self-test` writes fixture trees under `$TMPDIR`, removed) | kotoba |
```

Column map (frozen rules: `verifiers/check_gate_registry.py` docstring, lines 21–53):

| Column | Value | Rule it satisfies |
|---|---|---|
| Name | `verifiers/check_sdk_allowed_tools.py` | exactly one row, name cell equals the universe path |
| Kind | `gate` | one of `gate`/`probe`; `probe` is rejected for a script with a `--self-test` handler |
| Entry command | `python3 -B verifiers/check_sdk_allowed_tools.py --rev <rev>` | cell contains `verifiers/check_sdk_allowed_tools.py`; `--rev` is the invocation E09's counter documents |
| Verdict map | `0=clean, 1=failed, 2=could-not-evaluate` + frozen-line note | a gate needs `0=clean` and `1=failed`; no code twice; `PAIR_RE` sees no other `code=class` pair in the prose |
| Self-test | `` `--self-test` `` | gate may not say `none`; flag must be an exact active `add_argument("--self-test")` (E09 confirmed the exact string by message; placeholder fixture carries it) |
| Pinned values | `in-file` | gate may not say `none`; in-file pin table lives in the counter |
| Write scope | `none (reads committed bytes via git show; a --self-test writes fixture trees under $TMPDIR, removed)` | non-empty, not a dash; matches the lane's `check_cn_vendor_surfaces.py`/`check_spec_craft.py` style |
| Owner | `kotoba` | required constant |

### Self-test cell: the brief's `—` cannot ship — measured, not argued

The seat brief asks for self-test flag `—`. Under the frozen checker a `gate` row with `—` is **nonconformant**, and the row must be conformant (plan C2 conjunct (f)). I measured it instead of deciding it:

```
variant C row (self-test cell `—`)          → verifiers/check_sdk_allowed_tools.py  no  self-test cell names no backticked flag
                                              gate registry rows conformant 63 of 64 lane verifiers; phantom 0   EXIT=1
                                              (receipt: Kb81S09SkillRule-variantC-dash-selftest.txt, commit da8d7d6)
same row with self-test cell `--self-test`  → verifiers/check_sdk_allowed_tools.py  OK
                                              gate registry rows conformant 64 of 64 lane verifiers; phantom 0   EXIT=0
                                              (receipt: Kb81S09SkillRule-registry-at-D.txt, commit e81277e)
```

Cause: `clean("—") != "none"`, so the checker enters the flag branch, `FLAG_RE` finds no backticked `--flag`, and it records `self-test cell names no backticked flag` (`check_gate_registry.py:202-210`). E09 (`Kb81E09C2Counter`) confirmed by message that the counter exposes `ap.add_argument("--self-test", action="store_true")` exactly — so naming it is also the truthful value. **The row above therefore carries `--self-test`, and the `—` in the brief is superseded.**

---

## 3. Registry-gate acceptance measurement (the requested verification)

Scratch clones: one clone at base; commits built in it. Commands run with `cwd` = the clone (the counter derives `LANE` from `__file__`, so the clone's copy measures the clone) — `python3 -B verifiers/check_gate_registry.py --rev <rev>`.

| World | Tree state | Output tail | Exit | Receipt |
|---|---|---|---|---|
| base | `b284223…` untouched | `gate registry rows conformant 63 of 63 lane verifiers; phantom 0` | 0 | `Kb81S09SkillRule-registry-at-base.txt` |
| B `e385c3a` | counter file added, **no row** | `verifiers/check_sdk_allowed_tools.py  no registry rows naming it: 0 (need 1)`; `63 of 64` | 1 | `Kb81S09SkillRule-registry-counter-no-row.txt` |
| C `da8d7d6` | counter + row with self-test `—` | `… no self-test cell names no backticked flag`; `63 of 64` | 1 | `Kb81S09SkillRule-variantC-dash-selftest.txt` |
| D `e81277e` | counter + **this row** + the SDK-channel sentence | `verifiers/check_sdk_allowed_tools.py  OK`; `gate registry rows conformant 64 of 64 lane verifiers; phantom 0` | **0** | `Kb81S09SkillRule-registry-at-D.txt` |
| F `41683f3` | `D` + E08's real entry (placeholder replaced) | `verifiers/check_sdk_allowed_tools.py  OK`; `64 of 64`; entry `git cat-file -e` exit 0 | **0** | `Kb81S09SkillRule-registry-at-F-realentry.txt` |
| G `ca3a0ec` | `F` + E09's counter **mid-build copy** (sha256 `cac15f36…`, exact `add_argument("--self-test")` at its line 1495; later revised by E09) | `verifiers/check_sdk_allowed_tools.py  OK`; `64 of 64` | **0** | `Kb81S09SkillRule-registry-at-G-realcounter.txt` |
| E `a7505dc` (row, counter deleted) | phantom arm | `PHANTOM verifiers/check_sdk_allowed_tools.py`; `63 of 63 … phantom 1` | 1 | `Kb81S09SkillRule-registry-phantom-arm.txt` |
| **L `7222e3c`** | **fresh clone from base** + this patch + **final** counter (`739a7181…`, blanked `38ac8513…`, `add_argument("--self-test")` line 1563) + E08 entry + S249 snapshot + S05/S08/S10 patches + S01 lesson | `verifiers/check_sdk_allowed_tools.py  OK`; `gate registry rows conformant 64 of 64 lane verifiers; phantom 0` | **0** | `Kb81S09SkillRule-registry-at-L-finalbar.txt` |

Reading: B proves the row is load-bearing (the counter alone fails the registry gate); C proves the brief's `—` cell is rejected; D is the acceptance run the brief asks for (row + counter present at one rev → **64 of 64, exit 0**); E proves the row and the counter must land in the **same commit** (plan R6 — otherwise the row is a phantom and the gate is red).

Fixture honesty: B–F ran while E09's counter was unpublished, so those trees carried my placeholder `verifiers/check_sdk_allowed_tools.py` (flagged in its docstring; same flag surface, prints the frozen line, always `0 of 1`). E09 then published a **mid-build** copy (sha256 `cac15f36bf4df2f6a7caba6ed61d52e76f369cf045eda6a71637e767a1d1c297`) — world **G** measured that copy — and **then revised the counter to its final bytes** (sha256 `739a71810453f83c94468db25fc39c55f3bfbfdb224894a630d91e5aea86f985`, blanked self-sha `38ac8513c8f693c58b9f4b4a582471bc41ee3c6e7072f1b5cec06f07b17c53b5`, `ap.add_argument("--self-test", action="store_true")` at line 1563). World **L** is the acceptance run on **those final bytes**, in a fresh clone from base with this patch applied: `64 of 64, exit 0`. The row is therefore measured against the counter file that will ship, not a stand-in and not a revision.

Note for the L1's freeze step: the drift guard (`_blanked_sha(src) != SELF_SHA` → exit 2, `environment error: counter drifted`) fired on the mid-build copy, whose `SELF_SHA` was still the placeholder; I refilled it only in a scratch copy (blanked sha `4811c7ee…`, superseded) to reach the two named preconditions below. The **final** file already carries its correct `SELF_SHA`, so world L needed no refill and the lane copy under `build/` has never been touched.

---

## 4. Lane-side gate deltas at the SKILL.md edit (measured base vs D)

Two cheap gates were run in the clone at base and at `D` to show the edit adds no new failure (receipts `Kb81S09SkillRule-floors-at-{base,D}.txt`, `Kb81S09SkillRule-checklist-at-{base,D}.txt`):

| Gate | base `b284223` | `D` (`e81277e`) | Delta |
|---|---|---|---|
| `check_assertion_floors.py` | 16 PASS, `FAIL checklist observed=1863 floor=1863 self_test_failures=2`, exit 1 | identical 16 PASS, same single FAIL, exit 1 | **none** — the failure is pre-existing in a clone whose directory is `clone` (the checklist self-test checks the skill directory name), not caused by the row |
| `verify_skill_checklist.py` | 3 FAIL (`trigger.name_directory` name `kotoba-shokunin` ≠ directory `clone`; `trigger.citation_resolves` line 586 `../.ufo/…`; `governance.citation_resolves` LOG.md `../` tokens), evaluated 212, exit 1 | same 3 FAIL classes, evaluated **217**, exit 1 | **no new failure**; the 5 extra evaluated citations are the row's and the new sentence's, and every one resolves at `D` |

The citation arm is the sharp one: at commit `E` (row kept, counter deleted) `trigger.citation_resolves` gained a *new* failure — `line 519: 'verifiers/check_sdk_allowed_tools.py' does not resolve` — which disappears at `D` where the counter is present. That is the same-commit requirement (plan R6) measured from a second gate, not just from `check_gate_registry.py`'s phantom arm.

## 5. Conjunct-(f) evidence: these two edits are load-bearing for C2, and nothing else

The C2 counter's conjunct (f) is exactly "`SKILL.md` names the SDK channel in the `allowed-tools` author-facing rule area **and** carries a conformant registry row for the counter". I ran the real counter on an **integration preview** and on the same tree with my SKILL.md edits reverted:

| Tree | Contents | Counter line | (f) | Exit | Receipt |
|---|---|---|---|---|---|
| `I` `d2f3ec9` | my SKILL.md edits + E08 entry + S249 snapshot committed | `0 of 1` | **f ok** (a ok, d ok; b/c/e/g FAIL — S05/S08/S10 not applied) | 1 | `Kb81S09SkillRule-c2counter-at-I-snapshot.txt` |
| `J` `ff02cf9` | `I` + S05 `Kb81S05SourcesEdits.patch` + S08 `Kb81S08ReadmeRows.patch` + S10 `Kb81S10Province.patch` + S01's lesson body as `corpus/lessons/round-81.md` (all applied cleanly with `git apply -p1`) | **`sdk allowed-tools surface documented 1 of 1`**, `conjuncts: a ok, b ok, c ok, d ok, e ok, f ok, g ok`, `skill sdk channel ok`, `registry home ok` | **ok** | **0** | `Kb81S09SkillRule-c2counter-at-J-integration-preview.txt` |
| `K` `112e23b` | `J` with **only** `SKILL.md` reset to base (`git checkout b284223 -- SKILL.md`) | `0 of 1`, `(f) no line in the allowed-tools rule area names the SDK channel (SDK plus allowedTools/allowed_tools)`, `(f) SKILL.md carries no conformant gate row for verifiers/check_sdk_allowed_tools.py`, `skill sdk channel MISSING`, `registry home MISSING` | **FAIL** | 1 | `Kb81S09SkillRule-c2counter-at-K-no-skill-edits.txt` |
| `L` `7222e3c` | same composite as `J` but with **E09's final counter bytes** (`739a7181…`), fresh clone from base + this patch | **`sdk allowed-tools surface documented 1 of 1`**, `conjuncts: a ok, b ok, c ok, d ok, e ok, f ok, g ok`, `skill sdk channel ok`, `registry home ok` | **ok** | **0** | `Kb81S09SkillRule-c2counter-at-L-finalbar.txt` |

`J` vs `K` differ in one file and move `0 of 1 → 1 of 1`: the claim's SKILL.md side is carried by exactly the two edits in this draft, and neither edit is decorative. `L` re-confirms the same at the counter bytes that will ship (E09 revised the counter after `J`; the revision does not change conjunct (f)'s verdict).

Peer cross-check: E09 (`Kb81E09C2Counter`) ran this seat's SKILL patch plus the gate row inside its own candidate world and recorded `skill sdk channel ok`, `registry home ok`, `sdk allowed-tools surface documented 1 of 1`, `conjuncts: a ok … g ok` in `build/Kb81E09C2Counter-candidate.txt` — an independent run of the same two edits, agreeing with `J`/`L`.

Disclosure (do not read `J` as a claim after-value): `J` is a **composite integration preview** built from *other seats' published build outputs*, which I applied rather than rewrote — S05's SOURCES patch (S249 row + S248 old→new + S250), S08's README coverage row, S10's PROVINCE cells, S01's lesson body. It exists only to show my two edits compose with theirs and to attribute conjunct (f) to my patch. It is not a measurement of the lane, and it does not score any claim.

Two exit-2 probes are kept, named for what they are rather than for a revision: `Kb81S09SkillRule-c2counter-pre-freeze-drift-guard.txt` (the mid-build counter copy, whose `SELF_SHA` was still the placeholder → `counter drifted`) and `Kb81S09SkillRule-c2counter-pre-snapshot-commit.txt` (the snapshot not yet committed in the tree → the counter refuses to evaluate). Neither is a pass and neither is a claim measurement; they document the two preconditions the freeze step and the wave's snapshot commit satisfy — both absent from world `L`, which needed no refill.

## Out of scope / not done (deliberately)

- No lane edit, no commit, no index/stash: the SKILL.md change ships as `Kb81S09SkillRule-SKILL.patch` (2 hunks: the SDK-channel sentence at line 164, the registry row after line 518).
- S248 `used-by`, the S249 row, the entry body, the `README.md` coverage-map row and the `PROVINCE.md` § Core cell belong to S05/E08/S08/S10 — not duplicated here. The line's citations are only truthful once those land (stated in §1).
- I did not run the plan's no-harm battery or the tip battery; that is the L1's integration step.
- Tooling: nothing installed or upgraded this seat.

## Provenance

- Base: `b284223105f4d106f7e8f56ed4fd296c643cda0e`. Scratch clone commits (clone 1): B `e385c3ae69c1be3b026b9ffc5b75971f59b2a462`, C `da8d7d640e4547cd0cf8151acece56e8c6ba8c41`, D `e81277e3fb9278a6278cf4ea9b2e7ba89a4dca04`, E `a7505dc1852fcb2c8fc1295f1b9396aae1247124` (phantom arm, dangling after the seat branch was cut from `D`), F `41683f39846b43aaeba68dc7c8a64b45cc7ff86e` (D + E08's real entry), G `ca3a0ec2a490fa3177fef80d8bfc357fbfcb2ace` (F + E09's **mid-build** counter `cac15f36…`), H `dcddc75370584836e1b6ae0a8f5dd08708732e4d` (G + `SELF_SHA` refilled, scratch only), I `d2f3ec90bbd6b77a158ab7fd81d10f14082473e0` (H + committed S249 snapshot), J `ff02cf9bafb0d3e4dfc2dfd5d628bb93f7da9054` (I + S05/S08/S10 patches + S01 lesson body — integration preview), K `112e23baf570b77c70bb1ae6f6d920a1d4efa65a` (J with `SKILL.md` reset to base — conjunct-f control). Clone 2 (fresh, from base): L `7222e3c317f35f1f9635cc6fff7b0247a90b58e4` (this patch + **E09's final counter** `739a71810453f83c94468db25fc39c55f3bfbfdb224894a630d91e5aea86f985` + E08 entry + S249 snapshot + S05/S08/S10 + S01 lesson — the final-bytes acceptance run).
- Patch: `Kb81S09SkillRule-SKILL.patch`, 21 lines, sha256 `77649aeb5a2eddd2777dc4fc877de44fc895273cc6ad002df60a9bce0120999f`.
- Fetched page copy (my fetch, for token counts; the claim snapshot is E08's): `Kb81S09SkillRule-fetched-S249.md`, 28395 B, sha256 `ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2` — same digest E08 committed as `snapshots/S249.md`.
- `check_assertion_floors.py` and `verify_skill_checklist.py` were run at base and at `D` in the clone (§4): both exit 1 at both revisions, with the same failure classes; the only counts that move are the checklist's evaluated citations (212 → 217). Nothing in this seat's change turns a passing gate red.
- Tooling: nothing installed or upgraded; no host service touched.

VERDICT: Row delivered as `gate` / `--rev` invocation / `0=clean, 1=failed, 2=could-not-evaluate` / `--self-test` / `in-file` / none-reads-committed-bytes / `kotoba` — measured conformant **64 of 64, exit 0** against E09's **final** counter bytes `739a7181…` (world L, fresh clone from base + this patch), while the brief's `—` self-test cell is rejected `63 of 64, exit 1` (world C); SDK-channel line appended to `SKILL.md:164` with the entry path resolving (`git cat-file -e` exit 0) and every claim token present in the 28395 B / `ac62c2df…` page bytes; the two edits alone move the C2 counter's conjunct (f) from FAIL to ok and the integration preview from `0 of 1` to `1 of 1` (also on the final counter, world L, and independently in E09's candidate world), and the patch applies cleanly to base (`git apply --check` exit 0).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S09SkillRule.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S09SkillRule-SKILL.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S09SkillRule-registry-at-base.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S09SkillRule-registry-counter-no-row.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S09SkillRule-variantC-dash-selftest.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S09SkillRule-registry-at-D.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S09SkillRule-registry-at-F-realentry.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S09SkillRule-registry-at-G-realcounter.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S09SkillRule-registry-phantom-arm.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S09SkillRule-r80-counter-at-D.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S09SkillRule-c2counter-at-I-snapshot.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S09SkillRule-c2counter-at-J-integration-preview.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S09SkillRule-c2counter-at-K-no-skill-edits.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S09SkillRule-registry-at-L-finalbar.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S09SkillRule-c2counter-at-L-finalbar.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S09SkillRule-floors-at-base.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S09SkillRule-floors-at-D.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S09SkillRule-checklist-at-base.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S09SkillRule-checklist-at-D.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S09SkillRule-fetched-S249.md
