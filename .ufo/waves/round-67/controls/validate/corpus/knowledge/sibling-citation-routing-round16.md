source: `verifiers/verify_skill_checklist.py:1117-1232`; five sibling `SKILL.md` inputs identified in the companion JSON; fleet `../MISSION.md:84-88` and `../AXES.md:16`.
verified-at: 2026-10-15; lane baseline `581e2932850db9cb917844662651f533bfd98519`; observed source digests and contextual revisions are persisted in the companion JSON.
recheck: run the counting command below with the measured lane revision and `frozen`; use `live` only for a new source observation, never as a historical replay.

# Round 16 redispatch — classify before routing citation misses

## Claim and boundary

One adjacency move: replace an unclassified raw miss list with an exhaustive,
source-backed, owner-addressed disposition packet. The input population is
**226 raw subjects, 222 after four schematic exclusions, 14 raw unresolved
occurrences**. Before the ledger: **0 classified / 14 unclassified**. After:
**14 classified / 0 unclassified**, with exact occurrence-key equality.
The raw existence result remains fourteen; no files were invented to lower it.

The older scorecard's “225 checked” is not this run's denominator. Its older
“10 dead” row is not a semantic defect census. The aggregate historical counts
alone cannot establish which four individual occurrences were added. This
record supersedes those units for the current observation, not the filed
historical bytes. See `LOG.md:1005` for inherited-evidence qualification.

**Adjacency score: 8.0 → 8.0, hold.** Planner `R16AdjPlanNow` and critic
`R16AdjCriticNow` recommended hold; neither is an external verifier. A complete
author-side classification packet is useful but does not establish the rubric's
outside-lane measurement or an acknowledged integrator handoff. No other score
is raised. No sibling, domain, runtime, routing or verifier implementation changed.

## Preserved evidence

`corpus/knowledge/sibling-citation-routing-round16.json` contains:

- Original normalized token observations, including the recorded existence
  result for every subject. Their canonical SHA-256 is
  `61e3fd60afd6477caabcea49321b4ac082c54fe878ef2046e8a47042fc74e627`.
- Token-only projections preserving each raw token's source line. Re-extraction
  from every projection was compared with the full observed input before the
  projections were saved: **5/5 identical subject lists**. Targeted original
  context excerpts preserve the role-classification evidence.
- Original full-source digests, contextual source revisions, fourteen distinct
  occurrence keys, explicit owners/actions, and three prepared routing packets.

Four input hashes match their contextual revision's `SKILL.md`. Kake's hash
`bae7b1d05de4010f95f37e5ce2fbd76beae5875105784fcf1407655d9b6011f7`
identifies **working-tree bytes**, not its contextual HEAD
`20d13115323fba21bb3d63204cce13425feaf399`. No sibling work was committed or
rewritten to manufacture a revision pin.

A projection is **not** a full-source byte snapshot and cannot reconstruct its
full-source hash. Frozen mode replays extraction over the token projection and
counts the retained resolution observations; it does not re-probe the old
filesystem. Live mode executes the unchanged resolver against current sibling
files and rejects changed source digests/populations. Neither mode verifies
anchors, historical source contents, runtime producers or domain truth.

## Occurrence dispositions

| ID | Source occurrence | Role | Consumer disposition |
|---|---|---|---|
| r16adj-01 | `../kagi-shokunin/SKILL.md:285` | schematic | no missing-file repair |
| r16adj-02 | `../kagi-shokunin/SKILL.md:287` | schematic | no missing-file repair |
| r16adj-03 | `../kake-shokunin/SKILL.md:78` | foreign-base | optional-clarity |
| r16adj-04 | `../kasegi-shokunin/SKILL.md:33` | foreign-base | optional-clarity |
| r16adj-05 | `../kasegi-shokunin/SKILL.md:130` | historical-unavailable | no missing-file repair |
| r16adj-06 | `../kasegi-shokunin/SKILL.md:304` | schematic | no missing-file repair |
| r16adj-07 | `../kasegi-shokunin/SKILL.md:695` | historical-unavailable | no missing-file repair |
| r16adj-08 | `../kasegi-shokunin/SKILL.md:720` | historical-unavailable | wording-defect |
| r16adj-09 | `../kengaku-shokunin/SKILL.md:578` | brace-set | no missing-file repair |
| r16adj-10 | `../kumitate-shokunin/SKILL.md:84` | runtime-artifact | no missing-file repair |
| r16adj-11 | `../kumitate-shokunin/SKILL.md:107` | runtime-artifact | no missing-file repair |
| r16adj-12 | `../kumitate-shokunin/SKILL.md:183` | runtime-artifact | unresolved-defect: current producer claim |
| r16adj-13 | `../kumitate-shokunin/SKILL.md:448` | runtime-artifact | no missing-file repair |
| r16adj-14 | `../kumitate-shokunin/SKILL.md:671` | schematic | no missing-file repair |

Partition: **4 schematic + 1 brace-set + 2 foreign-base + 3 historical-unavailable
+ 4 runtime-artifact = 14**. This follows the counting command, not a count of
confirmed broken current files. The repeated kasegi final-audit token at lines
695 and 720 remains two occurrences with different local wording.

- Kagi's ellipses define citation classes. Kasegi's and kumitate's ellipses
  illustrate path families; none promises an ellipsis-named file.
- Both kengaku brace expansions exist, as rechecked by `R16AdjScoutNow` at the
  pinned source revision. One brace occurrence has two targets, not two findings.
- Kake and kasegi identify actual fleet L0 decision keys. A matching issue key
  and the fleet SSOT establish that base; existence somewhere else would not.
- Kasegi's sources at 130 and 695 are explicitly lost-tree. At 720, the same
  unavailable audit appears in present-tense prose without the local qualifier.
  Historical role and actionable wording are separate fields.
- Kumitate explicitly excludes workspace/run artifacts from source-file
  verification (`../kumitate-shokunin/SKILL.md:664-674`). A queue is runtime
  input, so the class is runtime-artifact, not universally runtime-output.
  Runtime role does not establish effective root, producer presence or freshness.

## Owner handoff packet — awaiting integrator mirroring

The route objects are **prepared-for-integrator**. Publication in this lane's
round report delivers the packet to protocol/aggregator review; no owner
acknowledgment, sibling correction or aggregator-ledger mirror is claimed.

| Route | Owner and occurrences | Requested action / acceptance | Status |
|---|---|---|---|
| r16adj-route-kake | kake, r16adj-03 | Optional clarity: name fleet-root L0 path, keyed by `kake` + `round-12`, not a drifting line number; no timer action or fresh systemd claim. | prepared; owner decision pending |
| r16adj-route-kasegi | kasegi, r16adj-04 and r16adj-08 | Optional fleet-root qualifier at line 33. Substantive: qualify line 720's unavailable historical source and date the present-tense block, preserving do-not-refile safety; do not restore missing bounty artifacts. | prepared; owner decision pending |
| r16adj-route-kumitate | kumitate, r16adj-12 | Correct or date-mark the unsupported present-tense durable-latch claim against the current Map plus console/ledger sinks; also re-anchor the stale origin-work source-base header. No runtime-file creation. | prepared; owner correction/re-census pending |

Kumitate's producer finding is substantive, not a clearance by runtime class.
`R16AdjKumitateNow` and `R16AdjCriticNow` found that the named current producer
does not establish the claimed dedicated latch-file persistence. The parent
read the current implementation at
`/home/vgpnk/Projects/ufo-fsd-alpha/scripts/fleet-dispatcher.mjs:7920-7948`,
source revision `964f443ee53df0ce06bd689af01f0dea031b01f9`: `telemetryLatches`
is a `Map`; `emitLatched` selects `log` or `logConsoleOnly`, then updates the
Map; `clearLatched` deletes its entry. The executor also reported no matches
for the named durable-latch symbols in the current source/history sweep.
The bounded finding does not reconstruct prior non-HEAD behavior or prescribe
an orchestration-code fix. Owner choices: correct current wording or date-mark
the historical description. The ledger retains primary role `runtime-artifact`
and explicit actionable issue `unresolved-defect`; it does not silently exclude
this occurrence as expected missing output.

## Counting command

Run from the kotoba repo root. The command is an evidence-counting probe, not a
fleet acceptance gate. An absent ledger at the valid before revision counts as
zero classifications; malformed evidence is rejected. Frozen mode is the
comparable before/after input population. Live mode is the actual-surface smoke
run and deliberately stops on source drift.

Before:

```sh
python3 -c 'from pathlib import Path; import sys; exec(Path("corpus/knowledge/sibling-citation-routing-round16.md").read_text().split("<!-- count-code -->\n```python\n",1)[1].split("\n```",1)[0])' 581e2932850db9cb917844662651f533bfd98519 frozen
```

After, use the exact measured lane revision recorded in `SCORECARD.md`; `HEAD`
is convenient only when checking the currently checked-out delivered revision:

```sh
python3 -c 'from pathlib import Path; import sys; exec(Path("corpus/knowledge/sibling-citation-routing-round16.md").read_text().split("<!-- count-code -->\n```python\n",1)[1].split("\n```",1)[0])' HEAD frozen
python3 -c 'from pathlib import Path; import sys; exec(Path("corpus/knowledge/sibling-citation-routing-round16.md").read_text().split("<!-- count-code -->\n```python\n",1)[1].split("\n```",1)[0])' HEAD live
```

The code below is the command's sole source; copying it into `python3 - REV MODE`
with a heredoc is equivalent. The committed JSON remains the evidence input.

<!-- count-code -->
```python
import collections, hashlib, importlib.util, json, subprocess, sys
from pathlib import Path
repo = Path.cwd()
revision, mode = sys.argv[1], sys.argv[2]
relative = "corpus/knowledge/sibling-citation-routing-round16.json"
fixture = json.loads((repo / relative).read_text())
module = repo / "verifiers/verify_skill_checklist.py"
try:
    expected = fixture["instrument"]["sha256"]
except (KeyError, TypeError):
    raise SystemExit("instrument_pin_absent")
if hashlib.sha256(module.read_bytes()).hexdigest() != expected:
    raise SystemExit("instrument_drift")
canonical = json.dumps(fixture["observations"], ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
if hashlib.sha256(canonical).hexdigest() != "61e3fd60afd6477caabcea49321b4ac082c54fe878ef2046e8a47042fc74e627":
    raise SystemExit("observation_snapshot_drift")
spec = importlib.util.spec_from_file_location("citation_measurement", module)
verifier = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verifier)
if revision == "WORKTREE":
    ledger = fixture
else:
    subprocess.run(["git", "cat-file", "-e", revision + "^{commit}"], check=True)
    present = subprocess.check_output(["git", "ls-tree", "--name-only", revision, "--", relative], text=True).strip()
    ledger = json.loads(subprocess.check_output(["git", "show", revision + ":" + relative])) if present else None
population, source_pins, per_lane = [], {}, {}
for source in fixture["sources"]:
    lane = source["lane"]
    saved = [r for r in fixture["observations"] if r["lane"] == lane]
    if mode == "frozen":
        lines = [""] * max(r["line"] for r in source["projection"])
        for row in source["projection"]:
            lines[row["line"] - 1] = row["text"]
        subjects, _ = verifier.citation_subjects(lines)
        if subjects != [{k: r[k] for k in ("line", "token", "raw")} for r in saved]:
            raise SystemExit("projection_population_mismatch")
        missing = [(lane, r["line"], r["token"]) for r in saved if not r["resolved"]]
        source_pins[lane] = source["sha256"]
    elif mode == "live":
        base = repo.parent / (lane + "-shokunin")
        data = (base / "SKILL.md").read_bytes()
        source_pins[lane] = hashlib.sha256(data).hexdigest()
        subjects, _ = verifier.citation_subjects(data.decode().splitlines())
        missing = [(lane, r["line"], r["token"]) for r in subjects if not verifier.citation_resolve(r["token"], base)]
    else:
        raise SystemExit("mode must be frozen or live")
    population.extend(missing)
    per_lane[lane] = {"subjects": len(subjects), "unresolved": len(missing)}
rows = [] if ledger is None else ledger["findings"]
keys = [(r["lane"], r["line"], r["token"]) for r in rows]
if ledger is not None:
    if ledger["schema"] != "kotoba-sibling-citation-routing-v1":
        raise SystemExit("unknown_schema")
    if source_pins != {r["lane"]: r["sha256"] for r in ledger["sources"]}:
        raise SystemExit("source_drift: reclassify changed inputs before comparing")
    if len(keys) != len(set(keys)) or len({r["id"] for r in rows}) != len(rows):
        raise SystemExit("duplicate_classification")
    if collections.Counter(keys) != collections.Counter(population):
        raise SystemExit("classification_population_mismatch")
    routes = {r["id"]: r for r in ledger["routes"]}
    if len(routes) != len(ledger["routes"]):
        raise SystemExit("duplicate_route")
    for row in rows:
        if row["class"] not in {"schematic", "brace-set", "foreign-base", "historical-unavailable", "runtime-artifact", "unresolved-defect"}:
            raise SystemExit("unknown_class")
        if row["owner"] != row["lane"] or not all(row.get(k) for k in ("reason", "evidence", "action")):
            raise SystemExit("owner_or_evidence_missing")
        if row["actionable"]:
            route = routes.get(row["route"], {})
            if route.get("owner") != row["owner"] or row["id"] not in route.get("finding_ids", []):
                raise SystemExit("actionable_route_missing")
print(json.dumps({"revision": revision, "mode": mode, "per_lane": per_lane,
    "subjects": sum(r["subjects"] for r in per_lane.values()),
    "unresolved": len(population), "classified": len(rows),
    "unclassified": len(population) - len(rows),
    "actionable": sum(r["actionable"] for r in rows),
    "routes": 0 if ledger is None else len(ledger["routes"]),
    "classes": dict(sorted(collections.Counter(r["class"] for r in rows).items()))}, sort_keys=True))
```

## Executed checks

Before at `581e2932850db9cb917844662651f533bfd98519`: live extraction returned
226 subjects / 14 unresolved / 0 classified / 14 unclassified, exit 0. Frozen
replay of that revision returned the same counts. The implemented worktree's
frozen **and live** runs returned 226 / 14 / 14 / 0, four actionable
clarification/reverification occurrences and three prepared routes, exit 0.
Actual post-commit revision/output is recorded in `SCORECARD.md` and `LOG.md`.

Five in-memory negative controls exercised this exact counting code without
changing the evidence file: dropped occurrence → `classification_population_mismatch`;
duplicate replacing an occurrence → `duplicate_classification`; removed route
→ `actionable_route_missing`; changed retained resolution →
`observation_snapshot_drift`; altered projection → `projection_population_mismatch`.
Each exited 1 with the named finding. These are input-integrity probes, not
permanent tests or proof of semantic classification. No source mutation,
source-file repair or new standalone gate was required.
