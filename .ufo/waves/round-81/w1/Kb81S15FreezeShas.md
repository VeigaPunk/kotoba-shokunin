# Kb81S15FreezeShas — freeze receipt assembler (round 81, w1, scribe, leaf)

Seat: `Kb81S15FreezeShas`. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Round base and lane HEAD at
assembly: `b284223105f4d106f7e8f56ed4fd296c643cda0e`. Deliverable:
`.ufo/waves/round-81/build/Kb81S15FreezeShas.md` — the round-81 `freeze-shas.txt` body in the r80 format, with
**43 flat `{{…}}` markers** (41 real fields; two are the prose token in the header and in §13 step 1) wherever a
producer's output had not landed. sha256 of the deliverable: `2cf45b5dd7d7c08f17196bff8f48c8b9e62c8bf255d4d58d9fbf1a76021ae2d1`
(304 lines, 25196 B).

The receipt is **NOT FROZEN** and the deliverable says so in its own header: a marker left in place is an unfrozen
input, and §13 tells the L1 to stop rather than measure on unfrozen bytes. This seat measured **no claim after-value**
and scored nothing.

## 1. Measurements this seat performed (each with its command and result)

| command | result |
|---|---|
| `git -C <lane> rev-parse HEAD` | `b284223105f4d106f7e8f56ed4fd296c643cda0e` |
| `git -C <lane> rev-parse --abbrev-ref HEAD` | `HEAD` (detached) |
| `git -C <lane> status --porcelain --untracked-files=no` | empty, count 0 |
| `git -C <lane> status --porcelain` | `?? .ufo/wapes`, `?? .ufo/waves/round-81/`, `?? plans/round-81.md` |
| `sha256sum plans/round-81.md` | `a3fe77454cf1190860ba5dd4ee2a9dcabf90ef383e42d5512fc6415a719c11f2` |
| `wc -lc .ufo/wapes`; `sha256sum .ufo/wapes` | 5 lines / 594 B; `930e2bd6b306b973a81144572f0b93a333379e501bffae1a8f8c50ec84dd6020` |
| `git show b2842231:verifiers/check_tip_battery.py \| sha256sum` | `e33b17d74f5935a43b04272baf2d88d1d4cf4f879ee9cfa48bb25f89e744bc4a` (743 lines; blob `a356e9d1…`) |
| `git diff --numstat --no-renames 072048fa… b2842231… -- <six battery scripts>` | `22 3 verifiers/check_assertion_floors.py` only → **added 22 / deleted 3**, cap 40 |
| `git rev-parse` + `git show \| sha256sum` for the six battery scripts | all six base blobs are already last-members of their `INSTRUMENT_PINS` tuples (listed in the deliverable §9) |
| `git cat-file -e b2842231:<path>` for `verifiers/check_sdk_allowed_tools.py`, `verifiers/external-commits.json`, `corpus/knowledge/allowed-tools-sdk-round81.md` | all three ABSENT at base (nonzero exit each) |
| `git show b2842231:corpus/SOURCES.md \| sha256sum` | `4a4442a034173948726d98ff3b8841f4ef338e9d5cf49be8cde6b9a13c0694f4` |
| `… \| grep -cE '^\| S[0-9]{3} \|'` | **174 rows** at base, max id `S248` |
| `grep -c W04 .ufo/waves/round-81/receipts/census-before.txt` | 31 findings, all duplicate-url; final line `kotoba ok <path>` |
| `curl -sS -L --max-time 40 -w 'http=%{http_code} bytes=%{size_download}' https://code.claude.com/docs/en/agent-sdk/skills.md` | `http=200 bytes=28395`, curl exit 0 |
| `sha256sum` of that body | `ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2` |
| `grep -c "In SDK sessions, you can pre-approve tools for a project"` on the body | **1** occurrence, body line 348; the quoted span is 23 words |
| `git ls-tree b2842231 verifiers/ \| grep -c '\.py$\|\.sh$'` | 63 registry-universe entries |
| recount of the deliverable's markers | 43 (flat; no nesting) |

No heavy gate was re-run by this seat: the base battery receipt is a committed input
(`.ufo/waves/round-81/receipts/tipbattery-base-dot.txt`, sha256 `28ab6cb4…`), and Kb81E10Battery/Kb81E11Receipts
own the re-derivation. `/home/vgpnk/Projects/shokunin/scripts/hyaku/disk-guard.sh status` was checked before any
work; nothing heavy followed.

## 2. Findings

1. **The C2 snapshot pin is already double-confirmed before any seat fetches it again.** The base `SOURCES.md` row
   S248 (line 189) carries `28395 B, sha256 ac62c2df…` for
   `https://code.claude.com/docs/en/agent-sdk/skills.md`, and this seat's independent fetch today reproduced both
   numbers byte-for-byte. So the freeze can pin the snapshot to a value checked from two independent readings — but
   only if `snapshots/S249.md` stores the fetched body **verbatim**: a prepended header line changes the digest and
   fails conjunct (c). The deliverable states that invariant explicitly.
2. **S249 will duplicate S248's canonical URL, and the census will say so.** Measured precedent: S215 and S230 share
   a URL at base and the census emits `W04 S230 duplicate url …` for the later row. Expect
   `W04 S249 duplicate url code.claude.com/docs/en/agent-sdk/skills.md across scopes` at the tip: advisory,
   non-fatal (base prints 31 such lines and still ends `ok`). Flagged, **not repaired** — narrowing or editing
   S249's URL to silence it would break C2 conjunct (b). Routed to the L1/Kb81C02C2 as an expected output, not a defect.
3. **The plan's cap arithmetic reads differently from the measured bytes, and the measured bytes are what the guard
   does.** The plan's kill rule says "40 base-spent + measured added ≤ 140"; the guard actually diffs the six battery
   scripts against the counter's own pinned `BASE = 072048fa…`, where the spend at `b2842231` is **22 added / 3
   deleted** (recomputed here; matches the base receipt's own summary line `instruments added 22 / deleted 3 lines
   (cap 40)`). Operative form frozen in §2 of the deliverable: `22 + added(E01) + added(E02) ≤ 140`, i.e. **≤ 118
   added lines** available to R1+R2; deleted headroom 137. No narrowing, no reinterpretation favourable to the claim.
4. **`exit 1` at base is code-entailed, not merely asserted.** `verifiers/check_tip_battery.py:399` returns
   `0 if n == TOTAL and not failures else 1` with `TOTAL = 6` (line 109). The committed base receipt's printed
   `4 of 6` therefore *is* exit 1. The freeze records the entailment instead of asking a reader to trust the plan's
   sentence, and the base receipt file itself does not carry an `rc=` header.
5. **r80's E5 counter amendment is dead provenance and no r81 pin may cite it.** The base counter is byte-identical
   to the r79 freeze entry (`e33b17d7…`), i.e. r80's `LINE_CAP` 60 amendment never landed (r80's C1 was killed). The
   deliverable marks r80's counter sha `20e49601…` uncitable, and ports r80's E04 as a *weaker ancestor* (marker file
   at a resolved report path would still pass it — the W8 class) and r80's E05 as *superseded* (marker-based external
   exemption). "Ported what is still correct" is recorded per artifact in §14 of the deliverable.
6. **E6's self-test re-anchoring has a concrete, checkable line inventory.** Base lines 42–43, 106, 111, 120,
   134–136, 137–139, 517, 522, 553, 559 are the only lines E6 may touch; in particular a bare `LINE_CAP` bump without
   moving lines 517/522/553/559 leaves the size arms unable to fire (a 41-line stub no longer exceeds 140), so the
   self-test would fail rather than silently weaken. That inventory is in §2 of the deliverable, with the
   pin-guard-vs-cap justification sentence pair the seat spec asked for.
7. **R6 is load-bearing for C1, not C2 housekeeping.** `check_gate_registry` fails a verifier file with
   `registry rows naming it: 0` over `git ls-tree <rev> verifiers/` (63 entries at base). A new
   `verifiers/check_sdk_allowed_tools.py` without its `SKILL.md` row turns gate 1 nonzero, so C1's `6 of 6` fails for
   a C2 reason. Recorded as a frozen input requirement (§8).

## 3. Pending markers, by producer (who fills what)

- **Kb81E05Erratum** — amended counter sha256, counter-bytes receipt, patch sha256 + apply-check/numstat, self-test
  result (§1, §4).
- **Kb81E01Integrity / Kb81E02Independent** (and Kb81E14PinAudit as second witness) — the two r81 instrument blobs,
  their patch sha256s and numstats (§2, §3, §4).
- **Kb81E04Baseline** — its patch sha256/numstat and the ported `refresh-corpus-baseline.py` sha256 (§4).
- **Kb81E03ExtManifest** — `verifiers/external-commits.json` sha256, the candidate build JSON sha256, the
  `bb65e3e4…` decision for pi-mono, the fetch transcript sha256 (§5).
- **Kb81E08C2Entry** — committed `snapshots/S249.md` + `S249.fetch.json` sha256 and the entry file sha256 (§4, §6).
- **Kb81E09C2Counter** — counter sha256/lines/bytes, base-output receipt sha256, self-test receipt sha256 (§7).
- **Kb81S09SkillRule** — the `## Gate registry` row text for the new counter (§8).
- **Kb81E06Controls / Kb81C01C1** — control-world receipts and the counter sha they ran (§12).
- **L1** — the at-tip battery print in both forms (§1, after the freeze), and the freeze commit sha line (§13 step 6).

## 4. Out of scope / not done (deliberate)

- No after-value measured, no control world run, no SCORECARD/report/lesson text written, no census re-run.
- No edits to `plans/`, `corpus/`, `verifiers/`, `SKILL.md`, `PROVINCE.md`, `MANIFEST.json`, `scripts/`,
  `.ufo/state/`; the receipt itself is a build-dir draft, not an edit to `receipts/`.
- No lane git mutation (no add/commit/checkout/stash); the only git calls were read-only `rev-parse`, `show`,
  `cat-file`, `status`, `diff --numstat`, `ls-tree`, `log`.
- No tool installed or upgraded (no pacman anywhere; nothing needed). Scratch lived only under
  `/fast/scratch/hyaku/kotoba-r81/Kb81S15FreezeShas/` and was removed before yielding; the fetched page bytes were
  used only for the digest and the quote-locality count.

## 5. Known limits of this deliverable

- Its §6 quote-locality facts are occurrence facts only; conjunct (d)'s "after the first heading in the text view" is
  Kb81C02C2/E08's measurement, and the deliverable says so rather than implying the condition is satisfied.
- The `174 → N` census delta is marked as Kb81E12Census's number; the `validate` invocation recorded in
  `census-before.txt` prints findings and an `ok` line but no row count.
- 41 unfilled fields mean nothing in the deliverable can be cited as a froze input yet; the header says NOT FROZEN
  in the first six lines so a reader cannot miss it.

VERDICT: Assembled the round-81 freeze receipt body with 41 exact `{{…}}` fields for unlanded seat outputs, plus measured base pins (counter `e33b17d7…`, six instrument blobs, 22/3 cap spend, S249 snapshot `ac62c2df…` re-derived and matching S248's committed pin), the E6 line inventory and justification pair, and seven findings incl. the S249/S248 duplicate-URL census consequence and r80's dead E5 provenance — NOT FROZEN, no after-value scored.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S15FreezeShas.md ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81S15FreezeShas.md
