# Round 81 freeze receipt — FINAL INPUTS, before declared after-value
# Assembled by seat Kb81S15FreezeShas (scribe, leaf, w1). Format: .ufo/waves/round-80/receipts/freeze-shas.txt.
# Receipt of record: .ufo/waves/round-81/receipts/freeze-shas.txt — the L1 KotobaR81 copies this body there and
#   commits it; THIS file (build/Kb81S15FreezeShas.md) is the assembly draft and is not the record.
# Base: b284223105f4d106f7e8f56ed4fd296c643cda0e
# Lane HEAD at assembly: b284223105f4d106f7e8f56ed4fd296c643cda0e (detached; 0 tracked modifications)
# Status: NOT FROZEN — every {{...}} below is an unfilled field whose producer had not landed when this was
#   assembled. A receipt that still carries a marker is not a freeze and must not be cited as one.
# This seat measured NO claim after-value. Every number below is (i) a base-revision measurement, (ii) a committed
#   receipt, or (iii) an input fact this seat re-derived from primary bytes — each with its command.

## §0 Base state (measured by this seat, 2026-10-27/28)

    git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD
    -> b284223105f4d106f7e8f56ed4fd296c643cda0e            (git rev-parse --abbrev-ref HEAD -> HEAD, detached)
    git -C … status --porcelain --untracked-files=no       -> empty (count 0)
    git -C … status --porcelain                            -> "?? .ufo/wapes", "?? .ufo/waves/round-81/", "?? plans/round-81.md"

    sha256  a3fe77454cf1190860ba5dd4ee2a9dcabf90ef383e42d5512fc6415a719c11f2  plans/round-81.md (untracked at base; the authoritative plan text)
    sha256  6512f94177ecea02a3c7f2aaba20c8a2037537d22c031ea24014cc547b43f7fd  .ufo/waves/round-81/receipts/census-before.txt
    sha256  28ab6cb4ec9fdd707f73a07d626f18288e0bc71d23d28168eff2b347b243d941  .ufo/waves/round-81/receipts/tipbattery-base-dot.txt
    sha256  930e2bd6b306b973a81144572f0b93a333379e501bffae1a8f8c50ec84dd6020  .ufo/wapes  (594 B, 5 lines; R80-D2 disowned probe output; R3 moves it to .ufo/waves/round-81/dispositions/wapes.txt, sha256 must survive the move)

## §1 C1 — consistency (calibration sub-axis), frozen counter

predicate (plans/round-81.md § C1, verbatim scope): `python3 -B verifiers/check_tip_battery.py --rev <rev>` on the
round-81 bytes (round-72/73 lineage counter amended by erratum E6) prints `guards 5 of 5` and
`tip battery exit 0: 6 of 6` and exits 0, both `--repo .` from the lane root and absolute `--repo <lane>`; at base
b2842231 it prints `tip battery exit 0: 4 of 6` and exits 1.

base receipt: .ufo/waves/round-81/receipts/tipbattery-base-dot.txt (sha256 above); last line
  `fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 4 of 6`
  guard lines (verbatim): `guard no-deletions PASS`, `guard floors PASS`, `guard instrument-size PASS`,
  `guard instrument-pin PASS`, `guard spotcheck-identity PASS`
  summary line (verbatim): `guarded paths 586, deleted 0; floors 15 rows; instruments added 22 / deleted 3 lines
  (cap 40); spotcheck base files 27`
  gate exits (verbatim shape `gate <script> exit N wall N s`): check_gate_registry 0, check_assertion_floors 0,
  verify_skill_checklist 0, verify_corpus_integrity 1, verify_corpus_independent 1, check_correction_sweep 0.
base exit 1 is code-entailed, not asserted: verifiers/check_tip_battery.py:399
  `return 0 if n == TOTAL and not failures else 1`, with `TOTAL = 6` (line 109) and n = 4 at base.

base counter bytes: verifiers/check_tip_battery.py
  sha256  e33b17d74f5935a43b04272baf2d88d1d4cf4f879ee9cfa48bb25f89e744bc4a
  blob    a356e9d101f3021687a80e73fca284e7436976d2        (`git rev-parse b2842231:verifiers/check_tip_battery.py`)
  size    743 lines; `LINE_CAP = 40` (line 111); guard `BASE = 072048fa8e8a52c707d25f7079772fa317244eb7` (line 108)
  lineage cross-check: byte-identical to the r79 freeze entry
  (`.ufo/waves/round-79/receipts/freeze-shas.txt`: `e33b17d74f…  verifiers/check_tip_battery.py`); last commit
  touching it `ec7f853` (round 76). r80's E5 amendment never landed (r80 C1 was killed by W8–W10), so E6 amends the
  r76/r79-lineage counter, not an r80-amended one.

amended counter bytes (the round-81 claim bytes): {{verifiers/check_tip_battery.py at the landed tip}}
  sha256: {{…}}      <- Kb81E05Erratum counter-bytes receipt; recompute `git show <tip>:verifiers/check_tip_battery.py | sha256sum`
  patch:  .ufo/waves/round-81/build/Kb81E05Erratum.patch
  patch sha256: {{…}}   (E05 also writes build/Kb81E05Erratum.sha256; the two must agree)
  patch applies to base: {{apply-check exit | numstat added/deleted}}
  amended `--self-test`: {{failures/assertions/exit | receipt path}}
  amended counter print at tip, both forms: {{…}}  <- the AFTER-value; only the L1 measures it, after this receipt is committed

## §2 Erratum E6 — exact amended line set (measured on the base bytes, with line numbers)

E6 is allowed to change ONLY these lines of verifiers/check_tip_battery.py:

| base line(s) | base content (measured) | E6 change |
|---|---|---|
| 42–43 | docstring: `gain at most 40 lines in` / `total over the base AND lose at most 40` | cap mention → 140/140 |
| 106 | comment: `stays 40)` | cap mention updated |
| 111 | `LINE_CAP = 40` | `LINE_CAP = 140` |
| 120 | comment: `weakened inside 40 lines` | cap mention updated |
| 134–136 | `INSTRUMENT_PINS["verifiers/verify_corpus_integrity.py"]` = (71cb2730bfe89064567ad429bfd7c2da62aceb45, e470eaaea5ef11c582b8353c9344ddf730c1a57a) | + exactly one reviewed blob → 3 entries |
| 137–139 | `INSTRUMENT_PINS["verifiers/verify_corpus_independent.py"]` = (176abae3b66930d644482f95e1363932e4d143b4, edac0df79324ba62ee25ff10a6a4d422ef59da61) | + exactly one reviewed blob → 3 entries |
| 517 | `range(41)` (size-world padding) | derive from LINE_CAP (`LINE_CAP + 1`) |
| 522 | `"FAIL guard instrument-size: instruments gain 41 lines > 40"` | derive from LINE_CAP (`141 > 140`) |
| 553 | `_make_world(stub_root, padding=60)` | derive from LINE_CAP (`LINE_CAP + 20` = 160) |
| 559 | `"FAIL guard instrument-size: instruments lose 60 lines > 40"` | derive from LINE_CAP (`160 > 140`) |

Nothing else. The five guards' checks stay semantically identical: `no-deletions`, `floors`, `instrument-size`
(bound only), `instrument-pin` (pin-table membership only), `spotcheck-identity`.

Measured cap arithmetic (recomputed by this seat, not copied):

    git -C <lane> diff --numstat --no-renames 072048fa8e8a52c707d25f7079772fa317244eb7 b2842231… -- <six battery scripts>
    22   3   verifiers/check_assertion_floors.py
    TOTAL added=22 deleted=3

  at base: 22 of 40 added lines spent (18 headroom), 3 of 40 deleted (37 headroom).
  after E6 (cap 140): added headroom for R1+R2 = 140 − 22 = 118; deleted headroom = 137.
  the plan's `40 base-spent + measured added ≤ 140` is used here in its operative form, because the guard diffs
  against 072048fa (not against the round base): at the tip, `22 + added(E01) + added(E02) ≤ 140`.
  measured numstat of the reviewed instrument blobs, recorded before data: {{A}} added / {{D}} deleted
  (`git apply --numstat` of Kb81E01Integrity.patch + Kb81E02Independent.patch against base, or
  `git diff --numstat base <tip> -- <six scripts>`), i.e. {{22+A}} spent of 140 → {{118−A}} lines left.
  sanity bound from the r80 stack over the same two gates (predecessor design, measured in
  .ufo/waves/round-80/build/Kb80E15BaselineOrder.md §1): 22/3 floors + 27/4 integrity + 10/3 independent =
  59 added / 10 deleted — i.e. this repair class has historically fit a 60-line cap with one line of headroom
  (the r80 runbook says so explicitly), so 140 is slack, not cover.

Erratum-E6 justification (declared before data, once; one sentence per load-bearing question):

(Cap bound.) The cap is secondary: raising `LINE_CAP` 40 → 140 changes only how much drift the size guard tolerates
above a reviewed rewrite of two 1470-/1153-line gates, which the base budget of 18 added lines cannot accommodate
against an estimated 60–120 added lines, and any gain past 140 still trips `instrument-size`.

(Pin guard.) The pin guard is load-bearing: `instrument-pin` requires each of the six battery scripts at the measured
rev to be byte-identical to its base blob or to one reviewed blob, so a weakened instrument cannot pass at any cap —
a 2-line stub fails the pin (self-test `guard-pin` arm, base lines 525–538) exactly as a 60-line deletion fails the
size arm (base lines 552–562) — which is why E6 may add pin-table members and a numeric bound but must never edit a
guard's logic.

## §3 Instrument pins — the two reviewed r81 blobs (E6 item b)

base blobs (measured; both already members of their tuples, so the base itself is pinned):

    verifiers/verify_corpus_integrity.py    blob e470eaaea5ef11c582b8353c9344ddf730c1a57a  sha256 3e600f4b70e4664048c0c09b06bf6a28cb00ff37fbb8c78f597a1f1452c03748
    verifiers/verify_corpus_independent.py  blob edac0df79324ba62ee25ff10a6a4d422ef59da61  sha256 c9cef5b3ecca5e9cfdac26b77702ac39186049ed782ce4a250776939a06e7ff2

r81 reviewed blobs (exactly one new member per tuple):

    integrity  : {{…}}   source: build/Kb81E01Integrity.blob, or `git -C <clone> hash-object verifiers/verify_corpus_integrity.py` after applying Kb81E01Integrity.patch to base
    independent: {{…}}   source: {{build/Kb81E02Independent.blob or the same hash-object recipe with Kb81E02Independent.patch}}

independent recomputation recipe (for Kb81E14PinAudit / Kb81V01C1): fresh `git clone --shared` at base → `git apply`
E01 (then E05 for the counter) → `git hash-object verifiers/verify_corpus_integrity.py`.
freeze invariant: E05's tuple member == blob of the patched file == `git rev-parse <tip>:verifiers/verify_corpus_integrity.py`.
A mismatch is an `instrument-pin` failure at the tip, i.e. C1 red for a bookkeeping reason.

## §4 Patches and copied files (each with sha256)

patches (must each pass `git apply --check` against base):

    .ufo/waves/round-81/build/Kb81E01Integrity.patch        sha256 {{…}}   numstat {{A/D}}   (R1: report-pointer <rev>:<path> object resolution + report content identity)
    .ufo/waves/round-81/build/Kb81E02Independent.patch      sha256 {{…}}   numstat {{A/D}}   (R2b: same binding, independent implementation)
    .ufo/waves/round-81/build/Kb81E04Baseline.patch         sha256 {{…}}   numstat {{A/D}}   (R3 disposition + R4 coverage-map row; no instruments)
    .ufo/waves/round-81/build/Kb81E05Erratum.patch          sha256 {{…}}   numstat {{A/D}}   (E6 counter amendment, §2)

files copied into the lane at integration (not patches; sha256 of the published build artifact is the freeze pin):

    build/Kb81E03ExtManifest.json          sha256 {{…}}  →  verifiers/external-commits.json        (§5)
    build/check_sdk_allowed_tools.py       sha256 {{…}}  →  verifiers/check_sdk_allowed_tools.py   (§7)
    build/allowed-tools-sdk-round81.md     sha256 {{…}}  →  corpus/knowledge/allowed-tools-sdk-round81.md (§6/§7)
    snapshots/S249.md                      sha256 ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2 (re-derived, §6)
    snapshots/S249.fetch.json              sha256 {{…}}  (must carry that same sha256 in its `sha256` field)
    build/refresh-corpus-baseline.py       sha256 {{…}}  (r80 port; integration tool, not a lane file)

## §5 Manifest — verifiers/external-commits.json (R2, the reviewed external-commit evidence manifest)

The term "manifest" in this receipt's scope is this file: it is the only manifest either claim binds. Explicitly NOT
frozen here: the fleet-root MANIFEST.json (not an input to C1 or C2), and the wave dispatch manifest
(w1-spec.json sha256 6521642a663defa7f30fd353537f3fa213764242920b4e1fcb4929cb6def92cd;
 w1-dispatch.json sha256 02344bc58603f90edb24c7ec934c2b45802491bb2cbe4c3bef9941adba290912 — recorded for
 reproducibility of the seat set only).

    verifiers/external-commits.json sha256 {{…}}      bytes: build/Kb81E03ExtManifest.json sha256 {{…}}
      (committed file MUST be byte-identical to that build artifact; absent at base — `git cat-file -e b2842231:verifiers/external-commits.json` nonzero, measured)
    expected entries (E03 verifies each from primary bytes; count must equal the number of exempted hex tokens):
      1. 7bb48f213ac677f943d5c791199ed3dddf302f00 -> mistralai/mistral-vibe
         evidence .ufo/waves/round-79/snapshots/S231.fetch.json  sha256 e75f057a8e8f8319df227a254a42526ed096c7d0dc5364307365729a08ae738f
           (its note records: `main` resolved to 7bb48f21… by `git ls-remote` 2026-10-27T21:43:03Z; the
            commit-pinned raw URL served the same 77634 B / sha256 fc48a5dbafe572fedd1457cffba8442aacd296dddaf50833ac3104252cb016b0)
      2. pi-mono head bb65e3e4…  {{E03 decides: required only if an exempted token needs it; the S230 row's token is one hash}}
         evidence .ufo/waves/round-79/snapshots/S230.fetch.json  sha256 b4fc56e3a874f3a1d9c83bd0cb281a4ecf24350ff5a672d1c662a7ad943ba34c
           (body pin: 4793 B, sha256 5b9805525b194474ef1fe5455a0917ef15ed7f710aa9bec2eee11879556469e5)
    fetch transcript: build/Kb81E03ExtManifest-fetch.txt sha256 {{…}}
    fail-closed rule (frozen): a hex token is `commit_external` iff absent from lane AND fleet AND present in this
    manifest with a committed receipt that proves the repo→hash association; a line marker (`owner/repo@`, a repo URL
    in the same row) NEVER exempts. Missing from the manifest → `commit_unresolvable` stays red (W6/world-9 classes).

## §6 Snapshot — .ufo/waves/round-81/snapshots/S249.md (C2 conjunct c)

independently re-derived by this seat from primary bytes (input fact, not an after-value):

    curl -sS -L --max-time 40 -o s249.html -w 'http=%{http_code} bytes=%{size_download}' https://code.claude.com/docs/en/agent-sdk/skills.md
    -> http=200 bytes=28395   (curl exit 0)
    sha256   ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2

second confirmation of the same bytes: corpus/SOURCES.md row S248 (base line 189) already records
`fetched 2026-10-27, HTTP 200, 28395 B, sha256 ac62c2df…` for this exact URL. Two independent readings agree.

    committed snapshot .ufo/waves/round-81/snapshots/S249.md sha256 {{…}}   <- MUST equal ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2
      (a snapshot that prepends a header line changes the digest and fails conjunct (c); pin the fetched body verbatim)
    fetch record .ufo/waves/round-81/snapshots/S249.fetch.json sha256 {{…}}  (its `sha256` field must carry the same value, and the counter's pin must equal both)

quote locality (measured on the fetched body): the sentence
  "In SDK sessions, you can pre-approve tools for a project or personal skill with the skill's allowed-tools frontmatter or with the allowedTools option"
occurs exactly once (`grep -c` = 1) at body line 348 and is 23 words (≤25); the same text block carries
`allowManagedPermissionRulesOnly`. Conjunct (d)'s "after the first heading in the text view" is E08/Kb81C02C2's
measurement, not this seat's; only the occurrence facts above are frozen here.
caveat (frozen): the page is live; a later re-fetch may differ. The counter reads committed bytes, so the pin is the
committed file, never the URL.

## §7 C2 counter — verifiers/check_sdk_allowed_tools.py (new)

    .ufo/waves/round-81/build/check_sdk_allowed_tools.py  sha256 {{…}}  {{N}} lines / {{B}} bytes
    base absence proven: `git cat-file -e b2842231:verifiers/check_sdk_allowed_tools.py` -> nonzero (measured ABSENT)
    base output (must be `sdk allowed-tools surface documented 0 of 1`, exit 1): {{base receipt sha256 of build/Kb81E09C2Counter-base.txt}}
    `--self-test` (fixture worlds: satisfying / pin-mismatch / S248-usedby-missing / quote-outside-text-view):
      {{failures/assertions/worlds | selftest receipt sha256 of build/Kb81E09C2Counter-selftest.txt}}
    at-tip output (the AFTER value; L1 only): {{…}}
    coupling: the counter must not land without its registry row (§8) — R6.

## §8 Registry / tree coupling (R6) — a frozen input requirement, not documentation polish

The registry gate's universe is `git ls-tree <rev> verifiers/` (top level, `.py`/`.sh`): measured 63 entries at base.
It fails a verifier file with `registry rows naming it: 0` (verifiers/check_gate_registry.py:228-234). Therefore:
a new `verifiers/check_sdk_allowed_tools.py` without a SKILL.md `## Gate registry` row makes gate 1 exit nonzero, and
C1's `6 of 6` fails for a C2 reason. Row shape: the r80 `verifiers/check_allowed_tools.py` row (SKILL.md:518) —
name, `gate`, entry command `python3 -B verifiers/check_sdk_allowed_tools.py --rev <rev>`, verdict map
0/1/2, `--self-test`, pinned values, write scope, owner `kotoba`. Row text: {{Kb81S09SkillRule draft}}.
Also frozen: adding files under `verifiers/` is an addition, not a deletion (`no-deletions` unaffected), and
`instrument-size`/`instrument-pin` are scoped to the six BATTERY scripts, so the new file changes neither.

## §9 Verified-binding surface that must NOT move at the tip

The six battery scripts at base, each already pinned (blob = the last tuple member for the pinned ones):

    check_gate_registry.py       blob 95ffed389f483c3d6f93db3c08dcfdb9a2240576  sha256 01b8ad1b1a2d9f7568dc6b970cd5c9ec621bf58af411973f001fa3ad0c35ddce
    check_assertion_floors.py    blob 9cb860bda21ef8d24fcb0603aa85372b96f3ac41  sha256 84458c057eef2bff8d7c76e4fdc029428688e3920deb0b69f948387433061f21
    verify_skill_checklist.py    blob 6aab16849bd6d71ded8f3bcb3f95668f14f6a78f  sha256 b7d7b0fca8be17cfa18e75fe4d130a0d429e34f5f4e1a30fdc5fb22a70539615
    verify_corpus_integrity.py   blob e470eaaea5ef11c582b8353c9344ddf730c1a57a  sha256 3e600f4b70e4664048c0c09b06bf6a28cb00ff37fbb8c78f597a1f1452c03748  (E6 adds one member)
    verify_corpus_independent.py blob edac0df79324ba62ee25ff10a6a4d422ef59da61  sha256 c9cef5b3ecca5e9cfdac26b77702ac39186049ed782ce4a250776939a06e7ff2  (E6 adds one member)
    check_correction_sweep.py    blob c94b771fa7d798ef45fc3bb640422ee7910f81a6  sha256 df66b485cc00a5058643b387882abe648d6e83b66d68a5865596e88515309c2f

Also unmoved: `corpus/lessons/*-verifier-spotcheck.md` base files (base receipt `spotcheck base files 27`; new
spotcheck files are INFO only); every `verifiers/floors-registry.json` row (base receipt `floors 15 rows`, no floor
lowered, no row dropped); SKILL.md as a `no-deletions`-guarded path.
`verifiers/corpus-baseline.json` IS expected to move (R4 re-record) — it is not a pinned input; its movement is the
integration's proof that the zero classes are clean.

## §10 Cross-check against the r79/r80 freezes

r79 recorded (`.ufo/waves/round-79/receipts/freeze-shas.txt`) sha256 of check_tip_battery.py e33b17d7…,
verify_corpus_integrity.py 3e600f4b…, verify_corpus_independent.py c9cef5b3…, baseline.json 945eb49e… — all four are
identical at the r81 base today (measured, §1/§9). Consequence: nothing drifted into this round unnoticed; the only
intended byte movement in the measured surface is the E6 line set plus the two pinned blobs. r80's freeze (E5,
`LINE_CAP` 60) is dead provenance — its C1 was killed and its bytes never landed; the r81 counter base is the same
bytes r79 froze.

## §11 SOURCES pre-state (the R5 / S249 / S250 surface), measured at base

    corpus/SOURCES.md sha256 4a4442a034173948726d98ff3b8841f4ef338e9d5cf49be8cde6b9a13c0694f4
    rows matching `^\| S[0-9]{3} \|`  = 174   (`git show b2842231:corpus/SOURCES.md | grep -cE …`); max id S248
    census-before.txt: 31 findings, all `W04 duplicate url … across scopes`, final line `kotoba ok <path>`;
      that invocation prints no row count → the 174 → N delta is Kb81E12Census's measurement, not this seat's

    S248 (base line 189) old side — frozen, so the lesson's old→new is checkable:
      tier B, status `queued`, used-by `—` (em dash), evidence cell already carries this page's pin
      28395 B / sha256 ac62c2df… plus two located quotes.
      C2 conjunct (e) moves only used-by: `—` → the new entry name.

    observation (flagged, NOT repaired): S249 duplicates S248's canonical URL. Measured precedent: S215 and S230
    share a URL at base (both rows present) and the census emits `W04 S230 duplicate url …` for the LATER row.
    Expect the analogous `W04 S249 duplicate url code.claude.com/docs/en/agent-sdk/skills.md across scopes` at the
    tip: advisory, non-fatal (base carries 31 such lines and still ends `ok`). Narrowing or editing S249's URL to
    silence it would break conjunct (b) — the census finding is the correct state, not a defect.
    S230/S231 stay append-only (audit trail); S250 is the supersede row (plan § C1 repair 5).

## §12 Controls bind to these bytes

Every control world must name the counter sha256 it ran; a world receipt naming a different counter is not evidence
about this claim. Worlds (plans/round-81.md kill rule): W0 base `4 of 6`; W1 index+baseline only; W2 R1 only;
W3 R2 only; W4 stub inside a battery instrument → `instrument-pin`/`instrument-size`; W5 spot-check edited →
`spotcheck-identity`; W6 real lane commit masked by an `owner/repo@` marker absent from the manifest →
`commit_unresolvable`; W7 dead lane hash in a lane-URL row → `commit_unresolvable`; W8 seven-byte marker file at the
fleet report path → `report_dead`; W9 manifest entry without a committed receipt → red.
receipts: {{build/Kb81E06Controls/…, build/Kb81C01C1-*.txt — pending}}
counter sha under test: {{…}}   (must equal §1's amended sha)

## §13 Freeze checklist for the L1 (ordered; each step is a gate on the next)

1. Fill every `{{…}}` above; each field names the command or artifact that fills it.
2. `git apply --check` each of the four patches against base → exit 0 each; record numstat.
3. Amended counter `--self-test` → exit 0; record failures/assertions and the counter-bytes sha256.
4. Assert each E6 pin equals `git rev-parse <tip>:<instrument>` and that no other battery blob moved (§9).
5. Assert the snapshot digest equals ac62c2df… (§6) and the manifest evidence paths exist in the committed tree.
6. Copy this body to `.ufo/waves/round-81/receipts/freeze-shas.txt`, add `# freeze commit <sha>` after committing.
7. Only then run the control worlds and the after-value (both `--repo .` and absolute forms); every after receipt
   names the freeze commit and the counter sha.
8. If any marker cannot be filled because its producer never landed: say so and stop. A marker left in place is an
   unfrozen input; C1/C2 stop rather than measure on unfrozen bytes, and the receipt is never retro-fitted.

## §14 Provenance — what the r80 artifacts contribute, and what changed

    .ufo/waves/round-80/build/Kb80E04DeadPointer.patch   sha256 d7169dd8f9db17a908f00c1e62a668d73c7ca96cca75626807fb81889f4a5d78
      PORTED but STRENGTHENED: it resolves a `<rev>:<path>` report pointer as a git object and stops there; a
      seven-byte marker file at the resolved path still passes it (that is exactly W8/W10, which killed r80's C1).
      r81 R1 keeps the object resolution and adds report content identity — resolved bytes must carry `## SHONEN`
      and be >= 400 bytes — so a marker file stays `report_dead`. The r80 patch alone is insufficient; it is the
      design ancestor, not an input.
    .ufo/waves/round-80/build/Kb80E05GrammarFix.patch     sha256 a4345d34d3a8e35d7697b5abc05d077c2bb43e49e636edd6937590b1b223a2d3
      SUPERSEDED: its external-commit class is marker-grammar based (an `owner/repo@` or a repo URL in the row
      exempts). r81 R2 replaces the exemption source with verifiers/external-commits.json backed by a committed
      repo->hash receipt (§5); a marker alone never exempts. Kept as provenance only; must NOT be applied.
    .ufo/waves/round-80/build/refresh-corpus-baseline.py  sha256 8481be46ab6b74656fe7fa68c53300a5e490ee23265e69768d4dfeed770b470a
      PORTED unchanged (unless E04 found a defect): refuses a dirty tree (measured r80: exit 2 naming the offending
      paths), `--repo .`, `--carry none`. Run only after the tracked tree is clean.
    .ufo/waves/round-80/build/run-battery.sh              sha256 cddf2dd8852801206a152dec62a62d64409453a280cef82cb3a002d7636d7601
      PORTED to .ufo/waves/round-81/build/run-battery.sh  sha256 19b878a12d07a5dc5a0e05b548a0be23910deaef72360be07f40b40f921fc76a
      (landed by Kb81E10Battery; `set -u`, TMPDIR-honouring, own-exit capture, per-receipt header `# rev=… cmd=… utc=…`).
    .ufo/waves/round-80/build/Kb80E15BaselineOrder.md
      PORTED as ordering logic only: its arithmetic sentence ("22 already spent + patch lines == the amended cap")
      is reused in §2 with 140 in place of r80's 60, and its dirty-tree pre-flight (measured r80: exit 2 naming
      the offending paths) is the precondition for the baseline re-record in §13 steps 2-6.
    r80's freeze receipt (`.ufo/waves/round-80/receipts/freeze-shas.txt`, E5: `LINE_CAP` 40 -> 60) is DEAD
    PROVENANCE: that amendment never landed, so no r81 pin may cite its counter sha 20e49601…; the r81 base counter
    is the r79-frozen bytes (§1).
