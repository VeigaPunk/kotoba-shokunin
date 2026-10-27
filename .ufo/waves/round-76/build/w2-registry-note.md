# Round-75 wave-2 registry note — repair R3 (round-76 plan § C2)

Landing path of this note: `.ufo/waves/round-76/w2-registry-note.md` (round-76 plan § C2, repair R3).
This copy is the draft filed at `.ufo/waves/round-76/build/w2-registry-note.md`; the round-76 integrator
lands it at the path above before the C2 counter (`verifiers/check_r75_routed_repairs.py`) runs.

Subject: `.ufo/waves/round-75/w2-results.json` (round 75, wave 2, `kotoba-r75-w2`; 64 seats; tracked
at commit `d118a3b`; sha256
`e4ce0f6d3be78fa6db5da230ca6ec5e388c08e5f0196ebe66600e39da17bcf5c`).

## The defect

The results file names a report file for seat `R75Attack28` that does not exist. The named path appears
only inside the seat's embedded verdict prose; the results entry itself carries **no** top-level
`report` field (unlike sibling seats `R75Attack08`, `R75Attack13`, `R75Attack51`, …, which do).

### Machine-checkable excerpt of the results entry

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
```

Named report path, verbatim from the verdict string:
`kotoba-shokunin/.ufo/waves/round-75/w2/R75Attack28.md` (fleet-root-relative form).

### Existence checks (both forms of the named path)

```
$ cd /home/vgpnk/Projects/shokunin
$ test -e kotoba-shokunin/.ufo/waves/round-75/w2/R75Attack28.md; echo $?
1
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
$ test -e .ufo/waves/round-75/w2/R75Attack28.md; echo $?
1
```

The file was never committed and no untracked leftover remains, so it is a phantom (never written),
not a lost or deleted file:

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
$ git log --all --oneline --diff-filter=A -- '.ufo/waves/round-75/w2/R75Attack28.md'
(no output — no commit ever added the path)
$ git status --porcelain -- .ufo/waves/round-75/w2
(no output — clean; the absent report is not an untracked working-tree file)
```

## The file count: 63 of 64 report files

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
```

The wave directory holds 64 entries: 63 `.md` report files plus `swarm-registry.json` (the wave
registry, which lists all 64 seats as members and carries no report paths). The results file lists
64 seats and 64 result entries with 64 unique names and 0 empty outputs — i.e. **0 dead seats**.

```
$ jq -r '.seats, (.results|length), ([.results[]|select((.output//"")=="")]|length), ([.results[].name]|unique|length)' .ufo/waves/round-75/w2-results.json
64
64
0
64
```

## Reconciliation

Round-75 wave 2 settled **64 of 64 results with 0 dead seats**; the wave directory holds **63 of 64
report files**. The single gap is seat `R75Attack28`: its results entry names
`kotoba-shokunin/.ufo/waves/round-75/w2/R75Attack28.md`, and that path does not exist — it was never
committed and no untracked copy remains. The seat's substantive verdict (above) stands as recorded in
the results file; only the report artifact is missing and cannot be recovered, because it was never
written. This note is that record: the results file and the wave directory now reconcile — one
phantom report reference, attributed, counted, and explained.

This note closes routed defect **R3** of `corpus/lessons/round-75-verifier-spotcheck.md` § 6
("wave hygiene"): "`w2-results.json` seat `R75Attack28` names `w2/R75Attack28.md`, which does not
exist (63/64 report files). Recover the report bytes or append a registry note recording the phantom,
so the results file reconciles with the wave dir." Recovery of the bytes was attempted and is
impossible — the path never entered the tree (no add-commit in any ref, no working-tree copy), so the
registry-note branch of the routed defect is the operative one.

Measured at lane `HEAD` `4de12b61f75c73e3675ef0e422cc2be0f7da8960` (round-76 plan and wave-spec
commits on top of the r75 closure tip `b7f13f4b39cbd43076a85568adca763a6f674e7a`). The r75 wave-2
artefacts themselves were committed at `d118a3b` and are unmodified since; the counts above are
re-measured from committed bytes in the current working tree, which `git status` reports clean for
`.ufo/waves/round-75/w2`.
