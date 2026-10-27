# Seat B09RepairR3R4 — round 76 w1 (build draft for C2 repairs R3 and R4)

Seat: `B09RepairR3R4` (leaf build seat, godspeed). Lane: `kotoba`
(`/home/vgpnk/Projects/shokunin/kotoba-shokunin`). Round 76, wave `w1`.
Measured lane `HEAD`: `4de12b61f75c73e3675ef0e422cc2be0f7da8960` (round-76 plan + wave-spec commits on
top of the r75 closure tip `b7f13f4b39cbd43076a85568adca763a6f674e7a`).

## Files written by this seat

| Path | What it is |
|---|---|
| `.ufo/waves/round-76/build/w2-registry-note.md` | Draft of the R3 registry note (round-76 plan § C2, repair R3). **Landing target: `.ufo/waves/round-76/w2-registry-note.md`** — the integrator copies it there before `verifiers/check_r75_routed_repairs.py` runs, because that counter reads the landing path. |
| `.ufo/waves/round-76/w1/B09RepairR3R4.md` | This seat report. |

No lane source, LOG, SCORECARD, MANIFEST, template, script, `.ufo/state/`, `.scratch/`,
`considerthese/`, jj state or git index was touched. No git/jj write of any kind (`git log/show/status/ls-files`
only). No installs were needed (tools used: `jq` already present at `/home/vgpnk/.local/bin/jq`,
`python3`, `git`, `ls`, `grep`); nothing was installed. No scratch directory was used beyond an empty
`/fast/scratch/hyaku/kotoba-r76/B09RepairR3R4/` (removed before this report was finalised).

## Task 1 — R75Attack28 phantom: confirmed, counted, explained

The seat's assignment was to confirm that the r75 w2 registry entry for `R75Attack28` names a report
path, to `test -e` that path, and to count the report files present (expect 63 of 64).

**Confirmed.** `R75Attack28` does name a report path, but only inside the seat's embedded verdict
prose — the results entry carries **no** top-level `report` field, unlike siblings such as
`R75Attack08`, `R75Attack13` and `R75Attack51` which do. The named path is
`kotoba-shokunin/.ufo/waves/round-75/w2/R75Attack28.md` (fleet-root-relative form).

### Exact commands and outputs (all run read-only, cwd stated)

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
$ jq -c '.results[] | select(.name=="R75Attack28") | {name, agent, has_report_field: has("report"), report_field: (.report // null), note}' .ufo/waves/round-75/w2-results.json
{"name":"R75Attack28","agent":"reviewer","has_report_field":false,"report_field":null,"note":null}

$ jq -r '.results[] | select(.name=="R75Attack28") | .output | fromjson | .verdict' .ufo/waves/round-75/w2-results.json
R75Facet28 survived with a material qualification: facts and boundary test are supported, but its preventative advice is misleading if read as odd runs OR deduplication; both are required to preclude equality at the default 0.5, or state the comparator. Written report: kotoba-shokunin/.ufo/waves/round-75/w2/R75Attack28.md

$ jq -r '.results[] | select(.name=="R75Attack28") | .output | fromjson | .evidence[]' .ufo/waves/round-75/w2-results.json
Verified measured revision 65a5c7a663249e0522cc49e4a148424200d9ddfe.
Entry lines 58–72; S211-run_eval.py.txt lines 213–234 and 260–268 establish strict-vs-inclusive threshold and duplicate pooling.
Read-only arithmetic check confirmed equality at 0.5 for two duplicate 3-run entries and for one unique 2-run entry.
Reopened S210 cited snapshot; no live fetch or production execution.

$ cd /home/vgpnk/Projects/shokunin
$ test -e kotoba-shokunin/.ufo/waves/round-75/w2/R75Attack28.md; echo $?
1
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
$ test -e .ufo/waves/round-75/w2/R75Attack28.md; echo $?
1
```

**The file count is 63 of 64 report files**, exactly as expected:

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
$ ls .ufo/waves/round-75/w2/*.md | wc -l
63
$ ls -1 .ufo/waves/round-75/w2/ | wc -l
64
$ ls -1 .ufo/waves/round-75/w2/ | grep -v '\.md$'
swarm-registry.json
$ for n in $(jq -r '.results[].name' .ufo/waves/round-75/w2-results.json); do [ -e ".ufo/waves/round-75/w2/$n.md" ] || echo "MISSING $n"; done
MISSING R75Attack28
$ jq -r '.seats, (.results|length), ([.results[]|select((.output//"")=="")]|length), ([.results[].name]|unique|length)' .ufo/waves/round-75/w2-results.json
64
64
0
64
```

So: 64 seats, 64 result entries, 64 unique seat names, 0 empty outputs ⇒ **0 dead seats**; the wave
directory holds 64 entries, of which 63 are `.md` reports and the 64th is `swarm-registry.json`
(the wave registry — it lists all 64 seats as members and stores no report paths, so it is not a
report and must not be counted as one; the round-60 erratum already fixed this counting class).

### Phantom, not a lost file — recovery of the bytes is impossible

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
$ git log --all --oneline --diff-filter=A -- '.ufo/waves/round-75/w2/R75Attack28.md'
(no output — no commit in any ref ever added the path)
$ git status --porcelain -- .ufo/waves/round-75/w2
(no output — clean; no untracked working-tree copy either)
$ git ls-files .ufo/waves/round-75/w2 | wc -l
64
```

`R75Attack28.md` was never committed and never existed in the working tree, so it was never written
and cannot be recovered. That closes the first branch of routed defect R3
(`corpus/lessons/round-75-verifier-spotcheck.md` § 6: "Recover the report bytes **or** append a
registry note recording the phantom") in favour of the registry-note branch. The seat's substantive
verdict (quoted above) stands as recorded in the results file; only the artifact is missing.

Provenance of the measured bytes: `.ufo/waves/round-75/w2-results.json` and the wave directory are
tracked at commit `d118a3b` ("round-75: clarify sourced trigger threshold boundary"); the results
file sha256 is `e4ce0f6d3be78fa6db5da230ca6ec5e388c08e5f0196ebe66600e39da17bcf5c`.

### R3 draft content (`.ufo/waves/round-76/build/w2-registry-note.md`)

The drafted note carries: the subject file and its sha256; the machine-checkable jq excerpt of the
`R75Attack28` entry (the `has_report_field:false` object plus the verbatim verdict string naming the
report path plus the four evidence lines); both `test -e` arms with exit 1; the never-added /
clean-worktree commands that make the gap a phantom rather than a deletion; the 63/64 count with its
command and the `swarm-registry.json` disambiguation; the 64/64/0/64 seats-vs-results-vs-empty-vs-unique
figures; and the reconciliation paragraph stating 64/64 settled, 0 dead, 63/64 report files, the
attributed phantom, and the impossible-recovery finding.

## Task 2 — R4: the LOG § Round 75 closing line

The filed r75 entry ends with the `**Pointer:**` bullet whose text still reads
"`.ufo/waves/round-75/w2/` (64-seat wave-1 reports); w2 falsify results pending;
`corpus/lessons/round-75.md`." (`LOG.md:2810`, § Round 75). The repair is **append-only**: the filed
text stays; one closing line is appended after it.

**Drafted closing line (one appended sentence; land it verbatim):**

```
- **W2 settlement (closing line appended in round 76; R4):** wave `kotoba-r75-w2` settled 64 of 64 results with 0 dead seats and 63 of 64 report files present; the one absent report, seat `R75Attack28` (named `kotoba-shokunin/.ufo/waves/round-75/w2/R75Attack28.md`, which does not exist), is recorded as a phantom in `.ufo/waves/round-76/w2-registry-note.md` (R3).
```

It carries all four elements the plan's R4 requires (64 seats, 0 dead, 63/64 reports, the
`R75Attack28` phantom "per R3") and it cites the note's **landing** path
`.ufo/waves/round-76/w2-registry-note.md`, which is what R3 requires of LOG § Round 75 (not the
`build/` draft path).

Coordination: the LOG drafting seat `B19LogScribe` independently drafted the same block; I sent it
this exact sentence (`agent://B19LogScribe`) so the two drafts stay byte-identical on the R4 clause.
Their R2 receipt sentence (`noharm-at-tip.txt`) is theirs and is not duplicated here.

## Behaviour delivered

- R3 is draftable and its content is grounded in committed bytes: named path confirmed, existence
  denied at both path forms, 63/64 counted with commands, phantom attributed and explained, and the
  "recover the bytes" branch closed as impossible.
- R4 has one append-only closing sentence that satisfies the plan's R4 wording and cross-cites the
  R3 note at its landing path.
- Neither draft claims anything about a counter run: `verifiers/check_r75_routed_repairs.py` does not
  exist at the measured `HEAD` (it is a round-76 touch-list file), so **no counter was executed and no
  counter verdict is claimed**. The `r75 routed repairs closed 4 of 4` line remains to be measured by
  the integrator after the note and the LOG line land.

## Retained evidence (verbatim, re-runnable at `HEAD` `4de12b61`)

| Claim | Command | Result |
|---|---|---|
| seat names a report path | `jq -r '.results[] \| select(.name=="R75Attack28") \| .output \| fromjson \| .verdict' .ufo/waves/round-75/w2-results.json` | names `kotoba-shokunin/.ufo/waves/round-75/w2/R75Attack28.md` |
| entry has no top-level `report` field | `jq -c '.results[] \| select(.name=="R75Attack28") \| {name, agent, has_report_field: has("report"), report_field: (.report // null), note}' .ufo/waves/round-75/w2-results.json` | `{"name":"R75Attack28","agent":"reviewer","has_report_field":false,"report_field":null,"note":null}` |
| named path absent | `test -e kotoba-shokunin/.ufo/waves/round-75/w2/R75Attack28.md; echo $?` | `1` |
| lane-relative path absent | `test -e .ufo/waves/round-75/w2/R75Attack28.md; echo $?` | `1` |
| 63 of 64 report files | `ls .ufo/waves/round-75/w2/*.md \| wc -l` | `63` |
| 64th dir entry is not a report | `ls -1 .ufo/waves/round-75/w2/ \| grep -v '\.md$'` | `swarm-registry.json` |
| only R75Attack28 missing | per-seat `[ -e … ]` loop over `jq -r '.results[].name'` | `MISSING R75Attack28` |
| 64 seats / 64 results / 0 dead | `jq -r '.seats, (.results\|length), ([.results[]\|select((.output//"")=="")]\|length), ([.results[].name]\|unique\|length)' …` | `64 64 0 64` |
| never committed | `git log --all --oneline --diff-filter=A -- '.ufo/waves/round-75/w2/R75Attack28.md'` | empty |
| no untracked leftover | `git status --porcelain -- .ufo/waves/round-75/w2` | empty |
| wave artefacts tracked | `git ls-files .ufo/waves/round-75/w2 \| wc -l` | `64` |
| results-file digest | `sha256sum .ufo/waves/round-75/w2-results.json` | `e4ce0f6d3be78fa6db5da230ca6ec5e388c08e5f0196ebe66600e39da17bcf5c` |
| r75 filed closing text (to append after) | `sed -n '2810p' LOG.md` | `- **Pointer:** … w2 falsify results pending; …` |

## Risks and blockers

- **Path risk (action required by the integrator, not by this seat):** the plan's C2 R3 conjunct names
  `.ufo/waves/round-76/w2-registry-note.md`, while this seat's write scope names the `build/` draft
  path. If the draft is left at `build/` only, the counter's R3 conjunct will fail. The integrator must
  land the note at `.ufo/waves/round-76/w2-registry-note.md` before running the counter; the draft's
  first two lines already declare the landing path so the copy is unambiguous.
- **The counter's R3 content check is not yet written**, so the note's exact phrasing may need to
  satisfy a token rule not yet fixed. The note deliberately carries both the natural-language
  reconciliation and the machine-checkable excerpt so either style of check can bind.
- **`R75Attack28`'s verdict remains only as recorded.** This seat did not re-adjudicate the seat's
  substantive finding (threshold-equality guidance) and makes no claim about it.
- **Counting-class caution (carried, not fixed here):** the directory's 64th entry,
  `swarm-registry.json`, is not a report. Any count that uses `ls -1 <dir> | wc -l` would read
  "64 report files" and be wrong; the note and this report both show the `.md`-filtered count and
  name the 64th entry.
- No blockers for the two assigned drafts.

## Bounds honored

Leaf seat: no task/subagent/agent dispatch, no background job, no spawn. Writes confined to the two
paths named in this seat spec, both inside the lane repo. No git or jj mutation anywhere (read-only
`git log`/`show`/`status`/`ls-files`/`diff` only; no `commit`, `push`, `add`, `stash`, `checkout`).
No fleet-root file written; no `~/.local/bin` or PATH-directory write; no `pacman`; no install; no
scratch left behind (the empty scratch dir was removed).

VERDICT: R3 and R4 drafts complete and grounded — R75Attack28 confirmed to name the absent report `kotoba-shokunin/.ufo/waves/round-75/w2/R75Attack28.md` (test -e exit 1 at both path forms, never committed, no untracked copy), 63 of 64 report files counted (`ls .ufo/waves/round-75/w2/*.md | wc -l` → 63; the 64th entry is `swarm-registry.json`), 64/64 results with 0 dead; note draft at `.ufo/waves/round-76/build/w2-registry-note.md` (landing target `.ufo/waves/round-76/w2-registry-note.md`) and the append-only R4 closing line drafted verbatim in this report; no counter executed, no counter verdict claimed.
