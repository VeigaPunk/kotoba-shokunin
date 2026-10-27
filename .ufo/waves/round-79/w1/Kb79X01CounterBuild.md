# Kb79X01CounterBuild — C2 counter (build), kotoba round 79 w1

Seat: `Kb79X01CounterBuild` (executor). Scope: build the r79 C2 counter to the frozen predicate of
`plans/round-79.md` § C2, with its self-test, its conjunct map and receipts. Draft only: the L1
copies it to `verifiers/check_allowed_tools.py` at freeze 2 and no claim data is scored here.

## Delivered

| File | Role | Bytes / sha256 |
|---|---|---|
| `.ufo/waves/round-79/build/check_allowed_tools.py` | the counter (2,288 lines, stdlib only, `python3 -B`) | `74e067ccad7813d91826ee503c8ee93ba47d3a4a05b12ec67a82791d93f722a6` |
| `.ufo/waves/round-79/build/X01-conjunct-map.md` | plan conjunct → counter function → failing self-test arm | 8.5 kB |
| `.ufo/waves/round-79/build/X01CounterBuild-receipts.txt` | every command below with its own exit status | 3.6 kB |
| `.ufo/waves/round-79/build/X01-counterbuild-receipts.sh` | re-runs the receipts (read-only over the lane) | 3.6 kB |
| `.ufo/waves/round-79/build/selftest.txt` | full `--self-test` output (77 lines) | — |
| `.ufo/waves/round-79/build/base-c2-abs.txt`, `base-c2-dot.txt` | base measurement, both `--repo` forms | — |
| `.ufo/waves/round-79/build/home-from-verifiers.txt`, `home-from-verifiers-base.txt` | the counter run from its eventual `verifiers/` home in a scratch clone | — |

`SELF_SHA` is filled with the blanked sha of the delivered bytes
(`1f9744c84cce7fe9978074f6379a547f4d7affae8905fde0fd811e493693ccf9`); the drift guard therefore
passes on the build copy and on a straight copy into `verifiers/` (verified, see evidence 5). The L1
refills it after any edit at freeze.

## Behaviour (what the L1 freezes)

Frozen predicate implemented verbatim: `python3 -B verifiers/check_allowed_tools.py --rev <rev>`
prints `allowed-tools surfaces backed N of 6` and exits 0 iff N ≥ 5 **and** the script-only world is
below the target (conjunct (i)) **and** SKILL.md carries the rule line and a conformant gate row
((g)) **and** PROVINCE.md `## Core` has exactly one bullet naming the entry ((h)). Printed lines:
`measured-rev`, `allowed-tools surfaces backed N of 6`, `script-only world: M of 6`,
`opened this round R of 6`, `held at base: K`, `province surfaces named P of 6`,
`skill rule line ok|MISSING`, `registry home ok|MISSING`, then one finding per unbacked surface.
Exit 1 = content verdict; exit 2 = could not evaluate (unknown rev, unreadable registry/manifest,
tampered/ambiguous pinned snapshot, counter drift).

Conjuncts: (a) provenance trio + frozen five-cell surface table (exactly one per surface, exact
frozen first cell) + ≥3 backticked tokens with a key/`value`/`grant` role each occurring
ASCII-word-bounded in the cited snapshot; (b) 11-cell `mined` tier A/B registry row, `used-by` names
the entry, URL host + whole-segment path prefix equals the frozen host; (c) snapshot sha = manifest
pin = anchor fetch record; (d) 5–25-word located quote, whitespace-collapsed substring of the
declared text view, containing `allowed-tools`, Q70-clean; (e) `opened` = entry `verified-at:` =
2026-10-27; (f) plain grant cell with exactly the surface's frozen label and the quote carrying the
frozen page token; (g)(h)(i) as above.

### Amendments folded in (all pre-data, lane commits)

* `d9d01c2` + `60ba11f` — Markdown text view deletes every backtick byte and removes an
  unordered-list marker `(?m)^[ \t]{0,3}[*+\-][ \t]+`; `.html` keeps script/style→space, tags→space,
  entities decoded; then whitespace collapse. Fences are **not** stripped from snapshots (vibe
  documents the field only inside a fenced example), and the entry must name the shaping on one line
  (`.html`, `script`, entity/decoded, `whitespace`, backtick/inline).
* `18dacb3` — page tokens now claude `without prompting you for approval`, factory `metadata`
  (spec/msaf/pi `Experimental`, vibe `allowed-tools:` unchanged).
* `91a2fce` — factory binds to canonical `docs.factory.com/harness/skills`; the same page's
  `.md` route is accepted as the same page for both the registry pin and the entry binding, and
  `docs.factory.ai/cli/configuration/skills` (the 308 source) is **not** accepted.
* A markdown table cell is split escape-aware, so a `|` written `\|` is cell content (the pi row's
  quote shape) and the backslash is dropped before judging.

## Evidence (exact commands and exit statuses; full text in the receipts file)

1. `sha256sum check_allowed_tools.py` → `74e067cc…` ; `wc -l` → `2288` ;
   `python3 -B check_allowed_tools.py --print-self-sha` → `1f9744c8…`.
2. `python3 -B check_allowed_tools.py --self-test --work $TMPDIR` → **rc=0**,
   `self-test: 0 failure(s) over 231 assertions in 80 world(s)`.
3. Base, absolute form: `python3 -B <counter> --repo /home/vgpnk/Projects/shokunin/kotoba-shokunin
   --rev b10bcbc6b00f8f56b202ccbadca311007b5b463c` → **rc=1**, prints
   `allowed-tools surfaces backed 0 of 6` and
   `entry corpus/knowledge/allowed-tools-surfaces-round79.md absent at b10bcbc6…`.
4. Base, relative form: `cd <lane> && python3 -B <counter> --repo . --rev b10bcbc6…` → **rc=1**,
   identical verdict lines (Q66).
5. Eventual home: in a scratch clone of the lane at `HEAD`, with the counter copied to
   `verifiers/check_allowed_tools.py`, `python3 -B verifiers/check_allowed_tools.py --rev HEAD` →
   **rc=1**, `allowed-tools surfaces backed 0 of 6` (drift guard passes at the new path), and
   `--repo . --rev b10bcbc6…` → **rc=1**, same verdict.
6. Held-at-base probe (`git show b10bcbc6:corpus/SOURCES.md | grep -c -- <host>`): agentskills.io 13,
   code.claude.com 15, docs.factory.com/harness/skills 1, learn.microsoft.com 2,
   raw.githubusercontent.com/badlogic/pi-mono 1, raw.githubusercontent.com/mistralai/mistral-vibe 1 —
   i.e. `held at base: 5` (all but factory, which the amendment moved).
7. Temp-dir discipline: `mktemp()` returns under `$TMPDIR` (probe printed
   `/fast/scratch/hyaku/kotoba-r79/Kb79X01CounterBuild/tmp/probe-…`), `--work` is honoured, no
   literal `/tmp` in the file (`grep -c '"/tmp"'` → 0), no network imports (`grep -c
   'urllib.request|socket|urlopen'` → 0), and the counter runs no instrument of the measured tree
   (only `git show`/`git rev-parse` against committed bytes).

### Self-test coverage (80 worlds, 231 assertions)

* Honest worlds: 6 of 6 with `script-only world: 1 of 6`, `province surfaces named 6 of 6`,
  `registry home ok`, `skill rule line ok`; the same under a relative `--repo .`.
* Q47-style equivalents generated at measurement time: a quote spanning a raw line break; a cue
  wrapped in inline code (only a counter that deletes backticks finds it); the `.md` route of the
  canonical page; a fixture `.html` page with `<script>`/`<style>` decoys and an `&#45;` entity.
* One broken world per conjunct (a)–(i), plus a two-surface arm per (a)/(b)/(d)/(f) that flips the
  verdict to `4 of 6`, exit 1; plan controls C0 (base), C1 (token dump), C2 (wrong-page quote),
  C3 (shared banner), C4 (script-only), C5 (label-only), C6 (sibling host `pi-mono-evil`), C7
  (stale/wrong pin incl. tamper), C8 (first-answer baseline, no files) each have an arm.
* Exit-2 arms: unknown rev, absent registry, absent/malformed/escaping manifest, ambiguous pin,
  tampered snapshot, counter drift. The (i) arm proves the defect path: a rebound frozen table under
  which a mechanical scrape reaches `script-only world: 6 of 6` makes the counter exit 1 and print
  `script-only world reached the target (6 of 6): a counter defect, reported and never repaired by
  narrowing`.
* A real row shape is a permanent arm: `S231 row shape: quote spans an indented list inside a fenced
  example` reproduces the vibe row (`user-invocable: true allowed-tools: read grep ask_user_question`,
  four page tokens, fenced YAML block) and scores 6 of 6, so the freeze cannot reject that row on the
  counter side. `S230 row shape: a pipe-bearing table-row quote with a bare word as the value form`
  does the same for the pi row (`allowed-tools | Experimental pre-approved tool list`, written `\|`,
  tokens `allowed-tools`/`pre-approved`/`Experimental`) and scores 6 of 6: a bare word is a value form
  under the frozen token rule, so the pi page needs no syntactic value token and no relaxation. Two
  further arms fix the quote-cell formatting rule: a backticked-but-exact quote is found (one retry
  with backticks deleted), a backticked-but-absent quote still fails.

## Calibration notes / attack surface (for w2 reviewers)

1. **Margin one.** The claim is N ≥ 5 of a population of 6, so one broken surface still exits 0 at
   `5 of 6`; the self-test asserts the *finding* for single-surface breaks and the *verdict* for
   two-surface breaks. A reviewer who expects a single break to fail the verdict is testing the
   plan's margin, not the counter.
2. **Hosts are nearly free at base.** Five of six frozen hosts already appear in the base registry
   (evidence 6), so the counter's discriminating work is (c) pins, (d) quotes and (f) labels. C8
   (assert N=6 from the census) is excluded by the entry-level and (c) conjuncts: at base the
   verdict is `0 of 6` because the entry does not exist.
3. **Token roles.** `row_tokens` counts every backticked span after the surface cell, including
   inside the located-quote cell — backticking a phrase there adds tokens that must also occur in
   the snapshot. A value form may be a bare tool name, a bracketed/comma list or a YAML list item;
   the grant role is "the token contains the surface's frozen page token", so for pi/spec/msaf the
   cue word itself is the grant token and a separate value form is required.
4. **`metadata` is a short cue.** The frozen factory cue is `metadata`, so a quote saying
   `metadata-only` would also satisfy the cue test — the frozen cue, not an invention; the grant
   *label* still has to be exactly `metadata-only` in the plain cell.
5. **Byte-identical snapshots are the same page.** The banner test (Q70) fires only when the same
   quote line occurs in a snapshot whose raw bytes differ, so two ids pinned to the same page do not
   disqualify each other.
6. **The `.md` tolerance is narrow**: same host and the same path plus or minus a bare `.md` suffix,
   nothing else — `…/harness/skills-old` and `docs.factory.ai/…` are rejected (both armed).
7. **Factory's anchor does not have to show the redirect chain.** The plan states the chain is
   retained in the fetch record; requiring it would add a conjunct, so the counter only requires the
   `fetched <ISO8601>Z, HTTP 200, <bytes> B, sha256 <hex>` record to be present and to agree with
   the pin. Flagging rather than narrowing.
8. **`province surfaces named P of 6` is informational**; conjunct (h) requires exactly one `## Core`
   bullet naming the entry path (0 or 2 fails). Data seats should not read P as the gate.

## Freeze dependency found in coordination (not mine to fix)

The row seats committed per-seat manifest fragments
`.ufo/waves/round-79/snapshots/S2{26..31}.manifest`, each already in the
`<hex>  <basename>` form, but **the merged `snapshots/MANIFEST.sha256` the plan's
conjunct (c) pins does not exist yet**, so a measurement today would exit 2
(`no manifest at .ufo/waves/round-79/snapshots/MANIFEST.sha256`). That file is the
L1's freeze step; my counter reads only `MANIFEST.sha256` and ignores the fragments
(no second source of truth). Format check I ran, read-only, without scoring any row
(`python3 -B` over the fragments with the counter's own regex):

```
OK 9a67de891329… S226-spec.md      OK 34016233a42a… S229-msaf.html
OK 31623035b25a… S227-claude.md    OK 5b9805525b19… S230-pi.md
OK 81409d890cb1… S228-factory.md   OK fc48a5dbafe5… S231-vibe.md
fragments=6 lines=6 sha-verified=6 malformed=0
```

Every line parses and every digest equals the committed bytes (factory's matches
the plan's frozen `81409d89…`), so the merge is mechanical:

```
cat .ufo/waves/round-79/snapshots/S*.manifest | sort -k2 \
  > .ufo/waves/round-79/snapshots/MANIFEST.sha256
```

## Risks

* **(i) can stop C2 at data time.** M is measured on the real snapshots. If a mechanical scrape plus
  the single no-judgement label `unstated` reaches ≥ 5 of 6, the counter exits 1 and reports a
  counter defect — that is the plan's rule ("a control reaching the target is a counter defect,
  never repaired by narrowing"), so the L1 must be ready to take the honest stop rather than have a
  seat widen the predicate. In the honest fixture M = 1 (vibe is the only surface whose frozen label
  is `unstated`).
* **Amended contracts are still moving.** The text view and the factory/claude cues changed three
  times inside w1 (commits `d9d01c2`, `60ba11f`, `18dacb3`, `91a2fce`). The counter now matches the
  plan at `91a2fce`; any further pre-freeze plan edit needs a re-read of § C2 and a re-seal.
* **Two row drafts are stale against the amended text view** (I messaged the seats): the vibe draft's
  quote is in pre-amendment form (list markers still present, which the transform deletes), and any
  pi draft quote using backticks must be written in transformed form. Pipes are already handled; I
  see the L1 pinned pipe-free anchors in `18dacb3`, so that path is exercised only by the self-test.
* **Not a blocker:** the counter is not in `verifiers/` and no claim data is scored; that is the L1's
  freeze step.

## Tooling

No install or upgrade was needed or performed (stdlib `python3` 3.14, `git`). `pacman` untouched
(host-wide pause respected); no host service touched; no fleet-root or `~/.local/bin` write.

## Scratch

`/fast/scratch/hyaku/kotoba-r79/Kb79X01CounterBuild` (clone, fixtures, `$TMPDIR`) is removed at
yield; all receipts were copied into `build/` first. Nothing outside
`.ufo/waves/round-79/{build,w1}/` was written in the lane (`git status --porcelain
--untracked-files=no` → 0 tracked modifications).

VERDICT: C2 counter delivered to the frozen predicate (2,288 lines, sha256 74e067cc…, self-test 0 failures / 231 assertions / 80 worlds incl. permanent S230 and S231 row-shape arms, base prints `allowed-tools surfaces backed 0 of 6` exit 1 in both `--repo` forms and from `verifiers/`); the L1 may freeze its bytes, with (i)'s script-only world the one conjunct that can still stop C2 at data time.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/check_allowed_tools.py, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/X01-conjunct-map.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/X01CounterBuild-receipts.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/X01-counterbuild-receipts.sh, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/selftest.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/w1/Kb79X01CounterBuild.md
