# Kb81S09SkillRule — seat report (round 81, w1)

Role: scribe. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, base `b284223105f4d106f7e8f56ed4fd296c643cda0e`.
Item: draft the SKILL.md edits for C2 — the SDK-channel line in the `allowed-tools` author-facing rule area, and the exact `## Gate registry` row for the new counter — and prove the registry gate accepts the row.
Full technical draft (exact text, column map, all worlds, evidence tables): `build/Kb81S09SkillRule.md`. This report is the seat-level summary.

## Behavior delivered

**(1) SDK-channel line** — one sentence, appended as the final sentence of the paragraph at `SKILL.md:164` (0 new source lines, 233 chars, 25 words; ≤3 lines satisfied):

> Claude Agent SDK — query-config `allowedTools` (`allowed_tools` in Python) grants the same pre-approval the frontmatter field does; managed settings can ignore both (S248/S249; entry `corpus/knowledge/allowed-tools-sdk-round81.md`).

Citations resolve, measured: the entry path is `git cat-file -e` exit 0 at `F` (my SKILL.md edit + E08's real entry); S248 is a committed row at `corpus/SOURCES.md:189` (`used-by` `—` at base, S05's patch moves it); S249 is the row S05's published patch adds with the same pin. The line's claims are in the page's own bytes — my independent fetch is 28395 B, sha256 `ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2`, byte-identical to E08's committed `snapshots/S249.md`: `allowedTools` ×5, `allowed_tools` ×4, `allowManagedPermissionRulesOnly` ×1, "ignores both" ×1 (page line 348).

**(2) Registry row** — one line, appended after the `check_allowed_tools.py` row (`SKILL.md:518`), 8 columns matching the header: `gate` · `python3 -B verifiers/check_sdk_allowed_tools.py --rev <rev>` · `0=clean, 1=failed, 2=could-not-evaluate` + the frozen-line note · `--self-test` · `in-file` · `none (reads committed bytes via git show; a --self-test writes fixture trees under $TMPDIR, removed)` · `kotoba`.

**(3) Acceptance measurement.** `python3 -B verifiers/check_gate_registry.py --rev <rev>` in a scratch clone:

| World | State | Result | Exit |
|---|---|---|---|
| base | untouched | `63 of 63; phantom 0` | 0 |
| B | counter, **no row** | `63 of 64`, `no registry rows naming it: 0 (need 1)` | 1 |
| C | row with self-test **`—`** | `63 of 64`, `no self-test cell names no backticked flag` | 1 |
| D | row (`--self-test`) + line + placeholder counter | **`64 of 64; phantom 0`** | **0** |
| F | D + **E08's real entry** | `64 of 64` | 0 |
| G | F + E09's counter, **mid-build copy** (`cac15f36…`, later revised) | **`64 of 64; phantom 0`** | **0** |
| E | row, counter deleted | `PHANTOM verifiers/check_sdk_allowed_tools.py; phantom 1` | 1 |
| **L** | fresh clone from base + this patch + **final** counter (`739a7181…`) + E08 entry + S249 snapshot + S05/S08/S10 + S01 lesson | **`64 of 64; phantom 0`** | **0** |

**(4) Claim-side attribution.** On an integration preview (`J` = my edits + E08 entry + S249 snapshot + S05/S08/S10 patches + S01 lesson body, all `git apply` clean), E09's mid-build counter prints `sdk allowed-tools surface documented 1 of 1`, `conjuncts: a ok, b ok, c ok, d ok, e ok, f ok, g ok`, exit 0. With only `SKILL.md` reset to base (`K`), the same tree prints `0 of 1` and conjunct (f) fails twice (`no line … names the SDK channel`, `no conformant gate row`). World `L` repeats the `1 of 1` / all-conjuncts-ok result on E09's **final** counter bytes (`739a7181…`), and E09's own candidate world independently records `skill sdk channel ok`, `registry home ok`, `1 of 1`. The two edits in this seat are exactly conjunct (f).

## Gates run (my own exits)

- `check_gate_registry.py` — base 0, B 1, C 1, D 0, E 1, F 0, G 0 (mid-build counter), H 0, **L 0 (final counter bytes `739a7181…`)**.
- `check_allowed_tools.py` (r80 counter) at base and at `D`: exit 0 both, `skill rule line ok`, `registry home ok`, form target `6 of 6` — the added sentence does not disturb the r80 gate.
- `check_assertion_floors.py` and `verify_skill_checklist.py` at base vs `D`: exit 1 at both, same failure classes (clone directory name; pre-existing `../` tokens in LOG/SKILL), checklist evaluated citations 212 → 217 with no new failure. At `E` (row without counter) the checklist gains a real new failure — `line 519: 'verifiers/check_sdk_allowed_tools.py' does not resolve` — which is the plan's same-commit rule (R6) seen from a second gate.
- `git apply --check` of `Kb81S09SkillRule-SKILL.patch` against base: exit 0.
- E09's counter run: the **mid-build** copy still carried the placeholder `SELF_SHA` and exited 2 `counter drifted`; E09's **final** bytes (`739a7181…`, blanked self-sha `38ac8513…`) already carry the refilled constant, so world L ran with no edit. I refilled only a scratch copy of the mid-build file (blanked sha `4811c7ee…`, superseded); the lane `build/` copy has never been touched.

## Findings worth the L1's attention

1. **The brief's `—` self-test cell cannot ship.** A `gate` row with `—` is nonconformant under the frozen checker (`clean("—") != "none"`, no backticked flag → "self-test cell names no backticked flag"); measured, not argued (world C). E09 confirmed, and the bytes show, the counter's exact `ap.add_argument("--self-test", action="store_true")` (line 1563 of the final file), so the row names `--self-test`.
2. **Row and counter must land in one commit.** Row without counter → phantom, exit 1; and `verify_skill_checklist.py` flags the row's path citation as dead. Both measured.
3. **Wording note.** The line says "managed settings can ignore both" — the page's literal words. S248's committed `teaches` cell says "managed settings can override both". Both are sourced; if byte-symmetry between line and row is preferred, swap the verb.
4. **`S248` stays `queued`** in S05's patch (the counter reports `S248 status queued; used-by corpus/knowledge/allowed-tools-sdk-round81.md`). C2 conjunct (e) reads only that row's `used-by` cell, so this is not a defect — E09 confirmed the intent explicitly (the counter refuses only when the cell omits the entry or the lesson does not log the old→new move). No action for the L1.
5. **Counter revision, and why the receipts are dated.** E09 published a mid-build counter (`cac15f36…`, placeholder `SELF_SHA`, `--self-test` at line 1495) and then revised it to the final bytes (`739a7181…`, blanked self-sha `38ac8513…`, `--self-test` at line 1563). World G measured the mid-build copy; world L re-ran the acceptance on the final bytes from a fresh clone and repeats `64 of 64, exit 0`, with the C2 counter at `1 of 1`. Cite L, not G, as the acceptance run.
6. **Process slip (this seat's own).** One revision of this report was issued through a Python string replacement instead of the `edit` tool — content-equivalent, build-side only, no lane file involved — and one earlier scratch run of the counter exited 2 because I edited the comment beside `SELF_SHA`, changing the blanked sha; both are recorded rather than hidden, and the cited runs are the corrected ones.

## Out of scope (not touched)

- No lane file written: no edit to `SKILL.md`, `corpus/`, `verifiers/`, `PROVINCE.md`, `README.md`, `plans/`; no commit, index write, stash or checkout in the lane (read-only git only).
- S05's SOURCES rows, E08's entry/snapshot, S08's README row, S10's PROVINCE cells, S01's lesson: consumed from `build/`, not authored or rewritten. In preview `J` I applied their patches verbatim to show composition; `J` is labelled a preview in the draft and is not a claim measurement.
- No claim after-value scored by this seat; no-control/no-harm battery and the tip battery belong to the L1.
- Tooling: nothing installed or upgraded; scratch under `/fast/scratch/hyaku/kotoba-r81/Kb81S09SkillRule` removed before yield.

## Artifact paths

`build/Kb81S09SkillRule.md` (draft), `build/Kb81S09SkillRule-SKILL.patch` (2 hunks, 21 lines, sha256 `77649aeb…`), `build/Kb81S09SkillRule-registry-at-{base,D,F-realentry,G-realcounter,L-finalbar,phantom-arm}.txt`, `build/Kb81S09SkillRule-registry-counter-no-row.txt`, `build/Kb81S09SkillRule-variantC-dash-selftest.txt`, `build/Kb81S09SkillRule-c2counter-at-{I-snapshot,J-integration-preview,K-no-skill-edits,L-finalbar}.txt`, `build/Kb81S09SkillRule-c2counter-pre-{freeze-drift-guard,snapshot-commit}.txt` (exit-2 probes), `build/Kb81S09SkillRule-{floors,checklist}-at-{base,D}.txt`, `build/Kb81S09SkillRule-r80-counter-at-D.txt`, `build/Kb81S09SkillRule-fetched-S249.md`.

VERDICT: Row drafted and measured conformant (`gate`, `--rev`, `0=clean, 1=failed, 2=could-not-evaluate`, `--self-test`, `in-file`, `kotoba`) at **64 of 64, exit 0** against E09's **final** counter bytes `739a7181…` (world L), the brief's `—` self-test cell falsified by measurement (63 of 64, exit 1), and the SDK-channel line drafted with resolving entry path and page-verified tokens; both edits together move the C2 counter's conjunct (f) FAIL→ok and the integration preview 0 of 1→1 of 1, on the mid-build and the final counter, plus E09's independent run.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81S09SkillRule.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S09SkillRule.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S09SkillRule-SKILL.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S09SkillRule-registry-at-L-finalbar.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S09SkillRule-c2counter-at-L-finalbar.txt
