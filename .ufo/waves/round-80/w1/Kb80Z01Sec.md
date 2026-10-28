# Kb80Z01Sec — security review of round-80 tooling (w1, 2026-10-27)

Reviewer seat (leaf, no subagents). Scope per dispatch: unsafe writes, shell injection,
credential handling in fetch records, network exfiltration paths, seat-prompt write-scope
bounds. Pure read-only review + one fact-pipeline sweep; no scratch dir created, nothing to
clean. No tools installed (operator 2026-10-19 authorization unused).

## Reviewed bytes

- `.ufo/waves/round-80/build/run-battery.sh` (260 lines, read whole: 1-260) — Kb80E10Battery.
- `.ufo/waves/round-80/build/Kb80E04DeadPointer.patch` and the r79 original
  `.ufo/waves/round-79/build/Kb79E04DeadPointer/Kb79E04DeadPointer.patch` — byte-identical
  hunks (index e470eaa..051b8c5 both); the port did not alter reviewed bytes.
- `.ufo/waves/round-80/build/Kb80E02Symlink.patch` (mode 120000, target
  `../../../../.ufo/reports/round-76/kotoba.md`).
- E5 target as committed at the r80 base: `verifiers/check_tip_battery.py` (LINE_CAP :111,
  INSTRUMENT_PINS :125-, self-test :464-673).
- C2 counter draft `.ufo/waves/round-79/build/check_allowed_tools.py` (2288 lines, ranges as
  cited) — the round-80 port `.ufo/waves/round-80/build/c2_controls.py`/counter was NOT in
  build/ at review close (glob Kb80E01*/E03*/E05*/E06*/*c2_controls* → no files, this session);
  r79 drafts reviewed in their place, per the dispatch fallback rule. Said fallback used.
- `.ufo/waves/round-79/build/refresh-corpus-baseline.py` (419 lines, ranges as cited).
- `.ufo/waves/round-79/build/c2_controls.py` (1144 lines, ranges as cited).
- `.ufo/waves/round-80/build/Kb80S15FreezeShas-receipts.txt` (pin/blob provenance).

## Findings

### MEDIUM-1 — E5 as declared breaks the counter's own size-mutant self-test (C1-blocking if ported literally)

`verifiers/check_tip_battery.py:514-522` (current base bytes): the size world is built with
`_make_world(size_root)` whose default is `padding: int = 0` (:427), so the base instrument is
`STUB_OK` (2 lines, :404); the mutant writes `STUB_OK + range(41)` pad lines → numstat
added=41, deleted=0. Assertions hardcode both numbers:
`check("size world exits 1", rc == 1, ...)` (:520) and
`"FAIL guard instrument-size: instruments gain 41 lines > 40" in out` (:521-522).

Under the declared E5 delta (`LINE_CAP` 40→60 at :111, `INSTRUMENT_PINS` +2 at :125, nothing
else), 41 ≤ 60 → instrument-size does not fire; INSTRUMENT_PINS is `{}` in self-test (:464-466)
and that world sets no pin, so no other guard fires → world exits 0 and both assertions fail →
`--self-test` reds → the floors gate (which runs instrument self-tests) reds → C1 cannot reach
`guards 5 of 5`. The plan's kill-rule sentence ("E5 changes only the LINE_CAP bound and
pin-table membership") does not name this line, but the `> 40` in the expected string is the
rendered cap constant — the mutant bound is derivative of the same declared change, not new
guard logic.

Minimal fix (fold into the E5 hunk before freeze): size world mutates with `range(61)` (or
`LINE_CAP+1`) and expects `... gain 61 lines > 60` — or derives the string from `LINE_CAP`.
Note the adjacent pin world (:531, +2 lines) stays inside either cap and still fails via
instrument-pin: unaffected. The stub world (:553-557, padding=60, file replaced by STUB_OK)
still reds post-E5 on the deleted side (~1000 > 60): unaffected.

### LOW-1 — E04 pointer branch: `and/or` precedence consults the fleet with no citing repo

Both patch generations, `verifiers/verify_corpus_integrity.py` new code (~:275-279 post-patch):

```python
return bool(lane) and git_ok(lane, "cat-file", "-e", token) or git_ok(
    fleet_root, "cat-file", "-e", token)
```

`and` binds tighter than `or`: when `lane` is None (citing file under no `.git` anywhere up the
parent chain) the first conjunct is False and the fleet `cat-file -e` runs anyway, although the
guard comment says "the citing repository first, then the fleet root". Read-only (`cat-file -e`),
list-form argv (no shell), fails closed in practice (both probes return False for a dead token);
token cannot start with `-` in the armed branch? It can (`-x:.ufo/...` → head=`-x`), but git then
errors the unknown object and git_ok returns False — no injection, no resolution. Severity LOW
(semantic fidelity/defense-in-depth). Minimal fix:

```python
if lane is None:
    return False
return git_ok(lane, "cat-file", "-e", token) or git_ok(fleet_root, "cat-file", "-e", token)
```

Verified NOT a finding: the new self-test arm's `git init/add/commit` runs on
`fleet_root = root / "fleet"` inside `tempfile.TemporaryDirectory()` (verify_corpus_integrity.py
:1010-1014), never on the real fleet; `FLEET_ROOT` (:127) is measurement-time read-only.
`subprocess` is imported (:114).

### LOW-2 — refresh-corpus-baseline.py guards the leaf, not the path components

`.ufo/waves/round-79/build/refresh-corpus-baseline.py:258-260` refuses only
`<root>/verifiers/corpus-baseline.json` being a symlink; a committed `verifiers/` symlink would
silently redirect both the baseline write (:356-358) and the gate executions
(`sys.executable str(root / script)` at :141, REQUIRED `is_file()` checks at :133-134 all follow
symlinks) — foreign gate bytes would run with cwd=root and could write the baseline themselves.
Operator-run on a clean tree, so LOW; the write-scope contract ("writes exactly one path", :47)
is the invariant being defended. Minimal fix: refuse `(root / "verifiers").is_symlink()` and
require `Path(root / rel).resolve().is_relative_to(root)` for REQUIRED + BASELINE.
Clean otherwise: `open_tree` requires `--repo` to be its own toplevel (:120-131), refuses dirty
trees, gate JSON under `$TMPDIR` with unlink-on-exit (:408-411), all subprocess list-form.

### LOW-3 — fleet-shaped sandboxes are write-through (inherited, two implementations)

`check_tip_battery.py:186-201` (`build_sandbox`) and `run-battery.sh:115-121` both symlink every
real fleet entry beside the sandbox clone, so a gate under measurement writing `../<entry>`
would mutate the REAL fleet tree. This is deliberate (fleet hops must resolve), the measured
gates are themselves pin/pattern-guarded, and no reviewed gate writes outside its root — noted
as hardening only. Two runner-specific nits: `ln -s ... 2>/dev/null || true` (:121) silently
tolerates a failed fleet symlink (a world silently less fleet-shaped; gate receipts would still
capture the consequence, so detectable, but not flagged); and `run-battery.sh` receipt 09 runs
the census against the LIVE fleet tree by design (`CENSUS_NOTE`, :189-191) — a verdict source
that is not pinned to `<rev>`, correctly labeled as such in the receipt header.

### INFO — recorded, not defects

- CLI-trust writes: `check_allowed_tools.py:2237-2238` (`--work` mkdir, parents=True),
  `c2_controls.py:1040-1042` (`--work`) and `:1138-1139` (`--out` write_text) write wherever the
  operator points them. Operator trust boundary; no elevation path.
- `c2_controls.py` alternates write (`:781`) lands inside the world's own
  `.git/objects/info/alternates`, pointing at the base clone's object store read-only; world
  toplevel assertion `:782-784` and the `rm -rf` traps stay inside `--work`/TMPDIR.
- `check_allowed_tools.py` manifest traversal is closed: absolute/`..`/leading-`/` pin names
  rejected (:718-720) with a red-before self-test arm (:1913-1916); snapshots are read as
  committed blobs via `git show` (Repo class :672-695, read-only); SELF_SHA drift guard exits 2
  (:2252-2256); every unevaluatable state is EnvError exit 2 (fails closed).
- Self-test `os.chdir(d)` (:2181-2188) restores in `finally`; `d` is a `mktemp` dir.
- E02 symlink arithmetic verified: from `.ufo/reports/round-76/`, four `..` reach the fleet root
  (lane is one level down), target is the fleet's own report; fails closed (dangling) when the
  fleet tree is absent. No traversal: target bytes are fixed in the patch.
- Freeze provenance: r80 freeze receipt records the E04-only instrument blob
  `051b8c5f8676cba5c8d6047c8c9f7fcb56cd8f9f` (git blob id, matching INSTRUMENT_PINS 40-hex
  format) before after-values; the second (grammar) blob is not yet published — must appear in
  `.ufo/waves/round-80/receipts/freeze-shas.txt` before any C1 after-value (plan § C1).

### Clean verdicts (each with its sweep)

- Shell injection — NONE FOUND. run-battery.sh read whole (1-260): every variable expansion
  inside a `bash -c` string goes through `q()` = `printf '%q'` (:69-71, receipts 01-02, 15);
  all other expansions double-quoted; direct exit capture `( cd ... exec timeout ... bash -c )
  >>"$f" 2>&1; rc=$?` (:157-159) — M80-1 compliant; `figure_of`'s `grep|tail` formats
  figures only, never a verdict; `rm -rf -- "$S"` bounded to the per-run scratch dir with
  EXIT/HUP/INT/TERM traps; unmatched globs filtered by `[ -e ]`.
- Credential handling in fetch records — NONE FOUND. Counter grammar `FETCHED_RE` captures
  date/HTTP/bytes/sha only; `grep -i 'token=|api[_-]?key|sig=|op://|Authorization|password|
  secret|Bearer'` over `corpus/SOURCES.md` → 0 hits; over `.ufo/waves/round-79/snapshots/*` →
  only third-party doc prose with placeholders (`S231-vibe.md:814` `your_mistral_api_key`,
  env-var NAMES). No live secrets, no `op://`, no basic-auth URLs.
- Network exfiltration — NONE FOUND. No network client in any reviewed artifact:
  check_allowed_tools.py imports `urllib.parse` (parsing only, `page_key` :789-791);
  c2_controls.py docstring claim "No network" matches its imports (:109-120);
  refresh-corpus-baseline.py has no network imports; run-battery.sh uses git/python3/coreutils
  only (:51-52). The six C2 pages are re-opened by seats, not by counters.
- Dispatch write-scope sweep (fact pipeline over `.ufo/waves/round-80/w1-dispatch.json`):
  absolute-path followers = lane 201, fleet `.ufo` 3, fleet `scripts` 2, `CORPUS.md` 1; no
  sibling lane, no `shokuknow` write, no fleet-root write target; exactly one `rm -rf --`
  (the scratch trap). No seat is instructed to write outside lane + sanctioned scratch.

### LOW-4 (wording) — seat-prompt write-scope self-contradiction

The dispatch's "Write scope" section says "You may write ONLY inside
/home/vgpnk/Projects/shokunin/kotoba-shokunin", while the scratch recipe, scratch discipline and
TMPDIR export direct every heavy operation to `/fast/scratch/hyaku/kotoba-r80/<SeatName>/` —
outside the lane. The host guard ("plus your own scratch") resolves it, but a seat applying the
Write-scope sentence literally must either refuse the recipe or mis-scope itself. Fix: amend the
Write-scope paragraph to name both sanctioned roots (the wave tree under the lane; the seat's
own scratch dir) instead of "ONLY inside <lane>". No observed seat harm this round; bounded
wording defect.

## Residual risk and verification gaps

1. E5 patch (Kb80E06CounterErratum), the two grammar-class patches (Kb80E05GrammarFix), the
   E01/E03 ports and a round-80 c2_controls.py were absent from build/ at review close.
   MEDIUM-1 must be checked against the ACTUAL E5 hunk when it lands; if the port is literal
   (two lines only), C1's own battery reds. Main-agent/L1: verify the E5 hunk touches
   :111, :125-area, AND :517/:521-522 coherently (or derives the string from LINE_CAP).
2. The second INSTRUMENT_PINS blob and the amended-counter sha are unpublished; freeze-shas
   completeness is Kb80S15FreezeShas's gate — my review confirms only the E04 blob so far.
3. run-battery.sh un-exercised here (no run performed — this is a static review; the ~104 s
   battery runs belong to the battery seat). Its exit-capture shape was verified by reading,
   not by execution.
4. The governance gate's 3-hop prose rule vs the symlink blob's 4-hop content: the plan asserts
   prose-only scanning; the r79 receipts (`Kb79E02-sym-*`, `Kb80E02-sym-tipbattery.txt`,
   `Kb80E02-sym-floors.txt` in r80 build) indicate the symlink world was measured, but I did not
   re-run those gates.

## Addendum (post-publish cross-check, same session)

Two peer audits (Kb80V03Instruments, Kb80E10Battery) contradict the plan's §Trigger/repair-5
token attribution and tighten the cap arithmetic. (a) verified by me on primary base bytes
(read-only `git show 398cbe1:…` + gate grammar read); (b)/(c) attributed to Kb80E10Battery's
measured stack world (exit-captured numstat), not independently re-measured here.

(a) The two base `commit_unresolvable` tokens are `corpus/SOURCES.md:171` (S230: "…resolved to
`badlogic/pi-mono` commit `7bb48f213ac677f943d5c791199ed3dddf302f00`") and
`corpus/SOURCES.md:172` (S231: "served commit `7bb48f213ac677f943d5c791199ed3dddf302f00`") —
backticked full-40-hex tokens in the counted `commit `<hex>`` grammar
(verify_corpus_integrity.py:25-26, :537-538), third-repo objects by construction. The
plan-named `google-gemini/gemini-cli@451a02ff` (SKILL.md:174, SOURCES.md:59/70) and
`zed-industries/zed@cfb894a5` (SOURCES.md:63) exist but sit outside the counted grammar
(URL-pinned, `owner/repo@`-prefixed — the exact spelling introduced by the r53 M45 rewrite,
corpus/lessons/round-53.md:44 — or fully-quoted context per :60-63). The plan's §Trigger
misidentifies the tokens it must clear.

(b) Cap arithmetic (attributed, Kb80E10Battery): the instrument-size guard diffs the six
BATTERY scripts against the pinned r72 base 072048fa (not 398cbe1); at 398cbe1 the spend is
22 added / 3 deleted (all 22 in check_assertion_floors.py), so after E04 (+17) the grammar
class has ≤ 21 added lines across BOTH corpus gates under the amended cap of 60. The published
S07 grammar candidate (96+75 added) cannot fit; arms in the gates' self-test bytes cannot fit
either — E05 must re-derive the cap arithmetic or move the arms out of the gates' bytes.
Note this does NOT interact with MEDIUM-1: check_tip_battery.py is the battery's counter, not
one of the six numstat-diffed instruments, so the size-mutant fix costs nothing against the cap.

(c) New grammar hazard (attributed, Kb80E10Battery): the C2 entry
corpus/knowledge/allowed-tools-surfaces-round80.md:125 carries a full-hex commit citation on a
line whose only repo hint is the bare name "mistral-vibe" (no owner/repo token or URL on that
line); under an unmarked-token-stays-red arm shape, landing the entry ADDS a third
unresolvable — the class must treat a bare repo name as a marker, or the entry's citation must
carry one.

Consequence (same C1-blocking class as MEDIUM-1, owner Kb80E05GrammarFix): a repair-5 grammar
class keyed only on in-token `owner/repo@<hex>` classifies ZERO of the two real blockers →
`commit_unresolvable` stays 2 → integrity stays red → C1 cannot reach `guards 5 of 5` /
`tip battery exit 0: 6 of 6`. The class must use the plan's parenthetical "(or otherwise an
explicit third-repository citation)" at LINE scope: repo name anywhere on the line (URL cell or
prose span) plus a counted-grammar hex token. Classification-only, per plan; pinning
`7bb48f21…` by hash would be the forbidden narrowing move. Do NOT rewrite SOURCES.md:171-172 in
place (M45, corpus/lessons/round-54.md:13). Ordering for the L1 (E10, matches the refresh
script's zero-mode refusal at :280-285): rows → E04 → E05 → refresh → commit → measure.

Corroborating oddity for the corpus owners: S231's token is byte-identical to S230's pi-mono
commit on a mistral-vibe row — likely a r79 wave recording error (and the same hex reappears in
the C2 entry per (c)); the lesson note belongs to the round-80 lesson's `## Gate`, not an
in-place row edit.

## Addendum 2 (C2-side counter defect, verified in draft bytes; S230 root cause)

Kb80E08C2Entry reports two items; both check out against the bytes I hold.

1. Q70 heading heuristic vs HTML views (counter defect, owner: the round-80 counter port /
   freeze seat). `check_allowed_tools.py` r79 draft: `quote_location` (:885-897) rejects a quote
   on any line starting with `#` and anything at or before `first_head + 1`, where `first_head`
   is the FIRST `#`-prefixed line of the text view; `text_view` (:328+) for `.html` snapshots
   strips script/style and replaces tags but keeps `#`-prefixed code-comment lines as ordinary
   text. S229-msaf.html names `allowed-tools` exactly once (raw :818, view line 95), and the
   view's first `#` line is a Python comment in a code sample (view :168) → every admissible
   msaf quote is structurally "in the first-heading block". No honest quote exists under the
   draft counter; only a quote dodge could satisfy it, which is exactly the
   counter-defect-not-repair-by-narrowing class (Q71/Q74). The same `first_head` logic in the
   mechanical generator (:1169-1175) inherits the flaw. Verified by me in draft bytes; the
   page-side measurements (1 occurrence; view line numbers) are E08's, consistent with the
   snapshot I read at :253-256 for other checks. Fix shape for the counter seat: heading
   detection must be view-syntax-aware (Markdown ATX only for `.md`, or tag-derived headings
   for `.html`), or the first-heading block must start at the first real heading.

2. S230/S231 token mix-up root cause confirmed (corpus erratum, lesson `## Gate`, not an
   in-place row edit): `S230.fetch.json` records pi-mono main at fetch time =
   `bb65e3e49710fbd14f10c7792d0eaa6e2b2c5923` (path commit `25cc5c7bf4cbc76b2e134c729eb8d57d521ed749`);
   `7bb48f213ac677f943d5c791199ed3dddf302f00` is the MISTRAL-VIBE commit (`S231.fetch.json`).
   So base `corpus/SOURCES.md:171` (S230) cites the wrong repository's commit — this upgrades
   Addendum 1's "likely recording error" to a confirmed wrong-repo citation, AND it means both
   base `commit_unresolvable` tokens resolve to ONE third-repo object (vibe) recorded twice:
   repair 5's grammar class must still classify BOTH line shapes (S230's has a correct
   `badlogic/pi-mono` name on the line with a wrong hex; S231's is self-consistent). E08's entry
   fixes are re-measured on their side (entry carries 0 commit-shaped citations per the gates'
   own COMMIT_RE; one pinned basename per line).

VERDICT: three C1-blocking pre-freeze defects (MED: E5 size-mutant self-test breaks the amended counter; grammar class must key line-scope third-repo citations or commit_unresolvable stays 2 — confirmed on base bytes, plan token attribution wrong; grammar budget ≤ 21 added lines across both gates makes self-test-resident arms unshippable per E10's numstat), one C2-blocking counter defect (Q70 '#'-heading heuristic structurally bars the honest msaf quote — verified in draft bytes per E08's page measurements), plus the earlier LOW/hardening set; injection/credential/exfiltration/traversal surfaces clean with named sweeps.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80Z01Sec.md
