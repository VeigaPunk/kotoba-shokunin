Result: HOLDS — the lesson's Gate rows, rejections, mistake records and routed-defect
dispositions all verify at the judged revision; the only defects found are two record-level
gaps (a dangling `LOG.md § Round 52` citation and a fleet-root-relative watchdog citation
written as a lane-relative path), plus one partial class fit on M37.

Target: `corpus/lessons/round-52.md` @ `c8407a453788df964df5a7b835dd0ce1360de882` (HEAD).
Read in full; lines cited below are the file's.

## Findings (severity-ordered)

### LOW — `corpus/lessons/round-52.md:4` cites `LOG.md § Round 52`; no such entry exists

Lesson line 4: "Plan: `plans/round-52.md` at `4c003a4b` (counters frozen there). LOG.md § Round 52."
Evidence: `git show c8407a45:LOG.md | grep -c 'Round 52\|round-52'` → `0`; LOG.md's last two
entries are the round-51 landing pair (lines 2412, 2423 of the working file). The new README
index row (`corpus/README.md:79`, "LOG.md round-52 entry") repeats the same dangling pointer.
`verify_skill_checklist.py` does not catch it (both `*.citation_resolves` checks PASS — they
resolve file paths, not section refs). The lane's own round-50 record shows a sibling gate
(`unindexed`) does flag this class when a separate instrument runs; none was wired for LOG.md
entries this round. The LOG entry is still owed as a record.

### LOW — `corpus/lessons/round-52.md:3` cites `.ufo/watchdog.log` unqualified; it resolves only at the fleet root

`cd kotoba-shokunin && ls .ufo/watchdog.log` → No such file. The line exists at
`/home/vgpnk/Projects/shokunin/.ufo/watchdog.log:717` verbatim:
`2026-10-22T12:48:39-03:00 launch kotoba round=52 pgid=3875350 driver=hyaku-inline attempt=1`
(attempt=2 at :725, 14:30:04-03:00). Cited content is correct; the path is fleet-relative
while the file convention (PROTOCOL.md:140, SOURCES `used-by`, the lesson's own `corpus/...`
citations) is lane-relative. Prior lessons disambiguated fleet paths explicitly
(round-51 lesson M34 cites `/home/vgpnk/Projects/shokunin/.ufo/reports/...` with the full path).

### LOW — M37 `class` is `provider` (`corpus/lessons/round-52.md:11`); the class fits only the second failure

The row's evidence joins two events: seat-gate starvation (`wave-slot.sh acquire kotoba build 34`
timed out at 3,600 s, `live_estimate` 52→84 vs cap 85 — a fleet capacity event) and the 17:02Z
route outage (a provider event). `provider` covers the route outage but not the gate starvation,
which is orchestration capacity, not a provider. No class vocabulary is defined in PROTOCOL.md
(:140 fixes only the column shape `class · evidence · captured-by · fix`), and prior rounds used
free-form class text, so this is a fit gap, not a vocabulary violation. The row's own fix cell is
honest about it: "a capacity event, not a judgment error." Alternative accurate classes would be
`capacity`/`infrastructure`. Not a BREAK: the class is arguable and the evidence is complete.

### INFO — rejected bullets verified byte-exact

All four rejected-URL records reproduce on re-fetch (curl, UA `kotoba-review/52`,
2026-10-22T18:01Z): opencode `mcp-servers.md` 200/13,941 B, sha256 `12ed2af6c5f4…` (prefix
matches lesson :47), `grep -ci instructions` → 0; Copilot `add-mcp-servers.md` 200/14,240 B,
sha256 `640035aa0936…` (matches :52), one `instructions` hit at line 22 (registry-installation
sense, as recorded); `copilot/concepts/context/mcp.md` → HTTP 404, 502 B (:53); VS Code
`v1_104.md` → 404 page, 19,510 B (:55). Reason+flip present for the two client rejections
(:49-50, :53-54); the flip for Copilot is by-reference ("as for opencode") — compressed but
present. The third rejection is a URL variant, not a client; its disposition (:55-56) is a
404 record, not a client judgment — acceptable.

## Verified holds

- **Gate shape (assignment item 1).** Every new row S032–S038 (:17-40) carries URL, access
  timestamp, byte count, sha256 and a located quote ≤25 words: S032 9 w (:19), S033 21 w (:22),
  S034 12 w (:25), S035 21 w (:28), S036 7 w (:31), S037 18 w (:34), S038 15 w (:38-39).
  Locations given by page line or section name; S037's §-name location is weaker than a line
  number but locatable. Counter corroboration: `check_mcp_instructions.py --rev c8407a45`
  → `mcp instructions backed 5 of 7 clients`, exit 0 — the counter requires the lesson to hold
  each client row's S-id and quote verbatim, so S032–S036's lesson cells are machine-verified;
  `--rev c8579a4c` → `0 of 7`, exit 1. `--fetch` was not re-run by this seat (live-page check
  is the Reopen seats' scope).
- **Rejections (item 2).** opencode and Copilot CLI carry evidence (grep counts), reason and
  flip (:47-54); the VS Code `.md` variant carries its 404 disposition. "No row was written"
  (:58) confirmed: `git diff c8579a4c..c8407a45 -- corpus/SOURCES.md` is pure `+` rows
  S032–S038, no reject rows.
- **Rows touched old→new (item 3).** `:62` claims "None of S001–S031 changed in place"; the
  SOURCES diff contains zero `-` lines — confirmed. `contract rule 2` = append-only
  (`.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`, Rules §2: only `status`/`recheck`/`used-by`
  change in place, logged old→new; a correction is a new row opening `supersedes S0NN —`):
  S038's `teaches` opens "supersedes S031 —" (diff line 15, S038 row at SOURCES.md:51 @ head)
  and no S001–S031 cell changed — both rule 2 clauses satisfied, citation accurate.
- **Mistakes (item 4).** Both rows carry the PROTOCOL.md:140 shape class · evidence ·
  captured-by · fix (:10-11). M36 `captured-by` cites PROTOCOL § Evidence standard "Corrections
  sweep every mention" — exists verbatim at `/home/vgpnk/Projects/shokunin/PROTOCOL.md:363`
  (section :343). **M36 fix shown able to fail**, executed this session:
  `python3 -B verifiers/check_correction_sweep.py --rev c8579a4c` → exit 1 with
  `FAIL r51-c2-readme corpus/README.md:119`, `FAIL r51-c2-scorecard-lead SCORECARD.md:28`,
  `FAIL r51-c2-province PROVINCE.md:17` (every claimed FAIL line matches); `--rev c8407a45`
  → `correction sweep: 0 stale block(s)`, exit 0; `--self-test` → `0 failure(s) over 5
  assertions`, exit 0. Registry (`check_correction_sweep.py:30-37`) holds exactly the three
  stale blocks M36's evidence names; Q29 exists at `corpus/QUALITY.md:40` @ head with the
  M36 back-reference. **M37 classed right**: see LOW finding above — partial fit, evidence and
  disposition honest; `build-dispatch.json` counts confirm 34 spawns, and
  `.ufo/waves/round-52/build/` and `falsify/` hold only `swarm-registry.json` with empty
  gate files — "not run, not replaced" is accurate (falsify was dispatched then cut off by the
  restart, leaving no seat reports; the lesson's "not run" omits the dispatch nuance but does
  not overstate). `captured-by: none` correct — no gate captures seat starvation.
- **Routed-defect dispositions (item 5).** (1) README correction at `:158-161` inside the same
  bullet and index-row correction at `:75` naming `removed in a scope` — verified at head.
  (2) `SCORECARD.md:28` depth lead now opens with the declared `4 of 7` on the plan-commit
  counter `7c81a787` — `git cat-file -t 7c81a787` → commit, subject "round-51: plan … C2
  counter check_overlap_levers.py"; the widened `7 of 7` is labelled a second measurement and
  "six rows are new" is corrected to four. (3) non-credit of round-51 C2 is correctly a
  non-defect per plan :70-73. (4) carried items named with reasons (:75-77): fixture lines
  9/15/33 of `strings-omp-18.12.6.txt` are `}` / `}` / bare `//` comment at both `c8579a4c`
  and `c8407a45` — unlabelled, "carried" accurate; no S024 superseding row at `c8407a45`
  (`git show c8407a45:corpus/SOURCES.md | grep -c S039` → 0) — "carried" accurate; the reason
  (gate starvation + route outage) matches M37's evidence.
- **Repair blocks.** PROVINCE `:17` stale line + `:18` appended round-52 correction verified at
  head; M36's evidence that the closure did not route PROVINCE is consistent with
  `corpus/lessons/round-51-verifier-spotcheck.md:158-167` (defects 1-2 = README + SCORECARD
  only; defect 3 = C2 non-credit; PROVINCE absent).
- **Fetch-log disclaimer** (:42-43) correctly marks `/fast/scratch/...` copies as non-evidence.

## Judged-revision vs working tree

`git status` at review time shows attempt-2 wave edits in flight in the working tree
(`SCORECARD.md`, `SKILL.md`, `corpus/SOURCES.md` — S039 superseding S024 added —,
`corpus/knowledge/mcp-server-instructions-round52.md`). All holds above were checked at
`c8407a45` via `git show`/`--rev`. The carried items' absence was confirmed at the judged
revision, not the moving tree. The attempt-1 uncommitted `SCORECARD.md` diff leaves the
repaired depth row at :28 untouched (its hunks cover the coverage and freshness rows plus
the history table); it asserts round-52 coverage `5 of 7` / `--fetch` 5 of 5 and freshness
`4 of 4`, consistent with this session's counter runs (5-of-7 observed directly; the fetch
and freshness figures were not re-executed by this seat).

## Verification gaps (owned elsewhere or unreachable)

- Quote-on-page fidelity for S032–S038 and the Copilot-CLI source-tree claim are assigned to
  the Reopen/Sweep seats; this seat verified record-internal evidence only (hashes, byte
  counts, grep counts, and the four rejected URLs live).
- M37's clock-level details (`live_estimate` 52 then 84, the 17:10Z second acquire) are not
  recorded in `.ufo` artifacts (gate files are 0 B); only the 34-seat dispatch and the empty
  wave directories corroborate. [INFERENCE]: plausible from the watchdog's 12:48→14:30 attempt
  gap, not independently confirmed.
- `validate` status of `build-dispatch.json` ("validated") is taken from the dispatch file's
  own schema field; the validator run was not replayed.
