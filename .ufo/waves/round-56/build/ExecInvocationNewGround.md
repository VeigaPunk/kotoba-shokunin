Result: DONE — v3 of `verifiers/check_explicit_invocation.py` (round-55 routed defect 2) delivered as a patch: new ground counts DISTINCT normalised forms against the whole base tree; self-test 0 failures over 50 assertions; `--fetch` receipts 96155796 `5 of 5; new ground 2` exit 0, f9244c6c `5 of 5; new ground 2` exit 0, b0b7140b `5 of 5; new ground 2` exit 0, f0e5de82 `0 of 0; new ground 0` exit 1 (v2 beside them: 4 / 4 / 4 / 0).

Seat: KotobaR56.ExecInvocationNewGround (executor, round-56 BUILD wave). No lane file was edited: every run and the patched file live in sandbox clone `/fast/scratch/hyaku/kotoba-r56/KotobaR56.ExecInvocationNewGround` (checkout `e02f5f5d`, sandbox commit `5f10480e8a61bbee5626a3beefc372e847d4c280`). No tools installed or updated. No client CLI was run.

## Deliverables (written by this seat, lane-relative)

- `.ufo/waves/round-56/build/ExecInvocationNewGround.patch` — the v3 patch for `verifiers/check_explicit_invocation.py`; sha256 `591f585831676928d74293afed289b400f9259b4a39b1cecc95ae630706c6715`; 263 lines; `git diff e02f5f5d2f37427e8a77b1c3efb45f84b78c67c8 HEAD -- verifiers/check_explicit_invocation.py` from the sandbox (130 insertions, 51 deletions, one file).
- `.ufo/waves/round-56/build/ExecInvocationNewGround.md` — this report.

Apply-check on a second fresh clone of the lane at `e02f5f5d`:

```
$ git -C scratch/applycheck apply --check .../ExecInvocationNewGround.patch
apply-check exit=0
$ git -C scratch/applycheck apply .../ExecInvocationNewGround.patch   # applied
$ sha256sum scratch/applycheck/verifiers/check_explicit_invocation.py
49b8069c72484fa5e7179028244d1b0b5c98e0ad2552ac2e9e931249e598f8a0  scratch/applycheck/verifiers/check_explicit_invocation.py
$ cd scratch/applycheck && python3 -B verifiers/check_explicit_invocation.py --self-test
self-test: 0 failure(s) over 50 assertions
self-test exit=0
```

The applied file is byte-identical to the sandbox v3 (same sha256).

## What v3 changes

The v2 rule (round-55 erratum) counted new ground per matched **example token** against base `SKILL.md` + base `corpus/knowledge/*.md` only, so `$setup-demo-app` and `/frontend-design` — renamed examples of forms the lane held (`$skill` at `corpus/knowledge/skill-overlap-levers-round51.md:26`; `/SKILL-NAME` in base `corpus/SOURCES.md` row S031's teaches cell) — scored as new ground.

v3 (documented in the docstring as `CORRECTION v3 (round 56; the fix round-55 routed defect 2 asks for -- a correction of the new-ground rule, never a re-claim of round 55)`):

- `form_shape(token)` = the token's sigil + the placeholder `<name>` — the example name is not part of the form (`/skill-name`, `/frontend-design`, `/<skill-name>` are one form `/<name>`; `$setup-demo-app` and `$<skill-name>` are `$<name>`).
- `base_form_count(form)` = `git grep -i -F -c -e <form> <BASE> -- . ':!.ufo'`, counts summed over the tree (SOURCES anchor/teaches cells, lessons and seat reports included); `git grep` exit 1 = 0 hits, other non-zero exit = could-not-evaluate (exit 2).
- `new_ground(token, counts, url, base_urls)` = the token's form has count 0 in that whole-tree haystack AND the row's URL is not a base row URL. `G` = number of DISTINCT forms among the counted clients that are new ground.
- Removed as now-dead: `git_ls()` and `base_texts()` (the old two-file haystack). Judge/backing rules, output labels and the exit rule (`value >= 4 and G >= 2`) are unchanged.

## Receipts (sandbox clone; `--fetch` is the declared predicate form)

v3 at 96155796, 2026-10-23 02:55:56–02:55:57Z:

```
$ timeout 300 python3 -B verifiers/check_explicit_invocation.py --rev 96155796 --fetch
Claude Code  BACKED token=/skill-name form=/<name> new=False found=yes base_count=9
Codex        BACKED token=$setup-demo-app form=$<name> new=True found=yes base_count=0
VS Code      no quote does not contain the word skill
Copilot CLI  BACKED token=/frontend-design form=/<name> new=False found=yes base_count=9
Gemini CLI   no SKILL.md form cell has no backticked invocation token
Cursor       BACKED token=/skill-name form=/<name> new=False found=yes base_count=9
opencode     BACKED token=@skill-id form=@<name> new=True found=yes base_count=0
user-typed invocation forms found on the live page 5 of 5; new ground 2
exit=0
```

v2 (saved copy, sha256 `e13eb88d8cfc32fc8975968280aa5a0055416fb07e43facbf1f585d951787e5a`, the sha recorded for the frozen v2) at the same revision, same minute: `user-typed invocation forms found on the live page 5 of 5; new ground 4`, exit 0 (the defect reproduced).

v3 at f9244c6c (02:56:03Z) and at b0b7140b (02:56:04Z): identical per-client lines, `user-typed invocation forms found on the live page 5 of 5; new ground 2`, exit 0. v2 at both: `5 of 5; new ground 4`, exit 0 (02:56:54–02:56:55Z).

v3 at f0e5de82 (02:56:04Z), `--fetch`: every client `no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)`; `user-typed invocation forms found on the live page 0 of 0; new ground 0`, exit 1. Without `--fetch`: `user-typed invocation forms backed 0 of 7 clients; new ground 0`, exit 1.

Self-test (both the sandbox v3 and the applied patch copy): `self-test: 0 failure(s) over 50 assertions`, exit 0.

## Arms that fail on the v2 behaviour

Three arms were added to the self-test (`v3: form held in the base tree is not new ground`; `v3: example rename of a held form is not new ground (v2 counted it)`; `v3: two example names of one form are one form (v2 counted two)`), plus `v3: form absent from the base tree is new ground` as the direction control. Replayed against the saved v2 module (02:56:29Z):

```
arm: form held in the base tree is not new ground (form /<name>, base count 9)
  v2: new_ground('/frontend-design', base SKILL+knowledge) = True
  v3: new_ground('/frontend-design', {'/<name>': 9})       = False
arm: example rename of a held form is not new ground (form $<name>, base count 2)
  v2: new_ground('$setup-demo-app', base SKILL+knowledge)  = True
  v3: new_ground('$setup-demo-app', {'$<name>': 2})        = False
arm: two example names of one form are one form
  v2: distinct case-folded tokens = 3
  v3: distinct forms              = 2
arm: form absent from the whole tree is new ground (form $<name>, count 0)
  v2: new_ground('$setup-demo-app', base SKILL+knowledge)  = True
  v3: new_ground('$setup-demo-app', {})                    = True
```

## Base-tree counts behind the receipts (sandbox; `git grep -i -F -c`, summed, `.ufo/` excluded)

| needle | base count | note |
|---|---|---|
| `/<name>` | 9 | held: `corpus/knowledge/instruction-surface-census-round13.md:475` records a user-invoked `/<name>` command form; skill-path templates (`.claude/skills/<name>`) match too |
| `$<name>` | 0 | not held → Codex's form counts |
| `@<name>` | 0 | not held → opencode's form counts |
| `/skill-name` | 2 | held case-insensitively (S031 `/SKILL-NAME`); not the unit any more |
| `@<id>`, `$<app>`, `/<design>`, `$<skill-name>`, `/<skill-name>`, `@skill-id`, `$setup-demo-app`, `/frontend-design` | 0 | |

## Risks and limits (for the L1)

- **Attribution, not count.** v3 names the two new forms `$<name>` (Codex) and `@<name>` (opencode); the spot-check's substantive reading names Cursor and opencode. The count (2) is what the routed defect asks for ("so that `new ground` equals the substantive count (2, not 4)"); the per-client heldness behind the spot-check reading (Codex held via its own S021, Copilot via its own S031) is not reproducible by a mechanical counter, as `CriticNewGround.md` itself concluded ("no placeholder-aware check is possible without a reviewer").
- **`/<name>` heldness is literal but has a substantive site** (the `/<name>` command form at `instruction-surface-census-round13.md:475`); the other 8 matches are path templates. A reviewer who wants heldness to be invocation-only would make `/<name>` count 0 and G 3, not 2 — the rule is documented, the number is not robust to that reading.
- **The example token is no longer consulted.** A world where the form string `/<name>` is absent while an example token of that form occurs at base would count the form as new ground; no such case exists at the four receipt revisions (the counted sets at 96155796 / f9244c6c / b0b7140b are strict subsets of v2's).
- The assignment's illustration `@<id>` was not adopted: the implemented shape is uniform `sigil + <name>` (`@skill-id` → `@<name>`), because a per-token "last word" shape would make the form depend on which example the quote matched (Codex: `$<name>` from the cell vs `$<app>` from the quote). Both strings have base count 0, so G is 2 under either reading at all four revisions (counts above).
- Round-55's records keep the value v2 measured; v3 is a later instrument and these runs are correction receipts, not a re-measurement or re-claim (Q28).

## Blockers

None. The L1 still has to: apply `ExecInvocationNewGround.patch` to the lane's `verifiers/check_explicit_invocation.py`, run the counter's self-test there, and record the correction receipt (and, per the round-56 plan § Frontier step, the lesson-mistake entry). The lane working tree has no other change to that file (verified against `e02f5f5d` before this report was written).
