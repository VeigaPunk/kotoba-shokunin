# C1 per-rule witness — opencode OC-6 vs `opencode-1.19.3.strings`

verdict: OC-6's dotted id anchor `session.instructions.entry.put` is gone (0 hits in dump *and* binary), the surviving `/instructions/entries` hit is a generated **client-SDK stub only** — no server route identifier carries an instructions member — so the behaviour it claims (API-managed durable instruction entries) is ABSENT in 1.19.3; re-pin structurally and re-verdict the class to `excluded`, do not re-anchor it as governed.

BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`. Substrate: `/fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings`
(sha256 `f4d8f34a…`, binary `179ca421…`, self-reported `var n="1.19.3"` at dump line 447186).

## 1. What OC-6 witnesses at BASE (path:line)

- `verifiers/verify_surfaces.py:389-395` — comment + anchors:
  `OC_API_ROUTE = "/instructions/entries"` (:393), `OC_API_ID = "session.instructions.entry.put"` (:394).
  Comment claims: `session.instructions.entry.{list,put,remove}` over
  `/api/experimental/session/:sessionID/instructions/entries`, "durable entries announced to the model at the next step boundary".
- `verifiers/verify_surfaces.py:440-443` — `api = OC_API_ROUTE in dump and OC_API_ID in dump`; owns `opencode:api-entries/instructions`.
- Class declarations: `verifiers/surfaces-baseline.json:266-271` (`verdict: governed`);
  `corpus/knowledge/instruction-surface-census-round13.md:194-195` (prose) and `:209` (row).
- Self-test drop fixture: `verifiers/fixtures/surfaces/strings-opencode-drop-oc6.txt:1-3`; expectation at `verifiers/verify_surfaces.py:970`.

## 2. Anchor-by-anchor, measured

| anchor | dump lines | binary `grep -a` | where |
|---|---|---|---|
| `/instructions/entries` | **1** (line 606940) | **1** | generated client SDK only |
| `session.instructions.entry.put` | **0** (exit 1) | **0** | — |

The only hit is one 25,928-byte generated-client module line (`606940`), whose instruction block is:

```
instructions:{entry:{list:(a,l)=>s({method:"GET",path:`/api/session/${encodeURIComponent(a.sessionID)}/instructions/entries`,
  successStatus:200,declaredStatuses:[404,400,401],empty:!1},l).then(c=>c.data),
  put: ... method:"PUT", path:`.../instructions/entries/${encodeURIComponent(a.key)}`, body:{value:a.value}, successStatus:204 ...
  remove: ... method:"DELETE", path:`.../instructions/entries/${encodeURIComponent(a.key)}`, successStatus:204 ... }}
```

Note the route is **`/api/session/...`**, not the census comment's `/api/experimental/session/...` — the `experimental` prefix is drift even for the client stub.

Zero-hit sweep (each `grep -c -F`, exit 1): `session.instructions.entry`, `session.instructions`, `instructions.entry`,
`instructionsEntry`, `instructions.entries`, `entry.list`, `entry.put`, `entry.remove`, `instructions.entry.`,
`instruction_entries`, `instruction-entries`, `instructions-entries`, `instructionEntries`, `instruction-entry`,
`InstructionsEntry`, `entry:"`, `entries:"`, `"/instructions`, `"/entries`. All 0.

## 3. The behaviour is absent on the server, not merely renamed

The binary bundles three SDK generations (client lines `443093`, `445282`, `606940`); only `606940` has the
instructions namespace. The *server* side is enumerated by route identifiers (`identifier:"…"` annotations,
`S.make(<group>).add(T.make(<group>).add(C.<verb>(<name>, <path>, …)))`):

- **534** unique route identifiers; **0** contain `instruct` (61 are `v2.*`, 26 are legacy `session.*`; neither has an instructions member).
- 19 route groups (`session`, `experimental`, `sync`, `tui`, …) — none registers an instructions route.
- No path fragment exists outside the client stub: `"/instructions` 0, `"/entries` 0, `entries:"` 0, `"/api/session/:sessionID/instructions` 0.
- No caller: `instructions.entry.` 0, `entry.put(` 0, `entry.remove(` 0.
- No schema/DB trace: `"instruction"` 0; the three `instruction:` hits are non-route (`Unrecognized endpoint parameter instruction:` error text at 444827, two `system_instruction:` fields at 449545/449560).
- The client bundle is *ahead* of the bundled server: 47 of its 91 paths have no server-registry counterpart (`/move`, `/rename`, `/pending`, `/form`, `/shell`, `/skill`, `/synthetic`, …), so client presence cannot evidence a local server surface.

The **old** (round-14) second instruction subsystem *is* fully live: `instruction-context` (line 445482),
`InstructionContext.observe` (445482), `Instruction.systemPaths` (443993), `core/instructions` (445481),
`targets:["AGENTS.md"]` (445482), `Previously loaded instructions no longer apply.` (445482). That is a different
class (`opencode:instruction-context/AGENTS.md`, retired in round 18), not evidence for OC-6.

Classification, per anchor:
- `"/instructions/entries"` — **anchor-still-present**, client stub only (route prefix drifted).
- `"session.instructions.entry.put"` — **renamed-to-structural-X**: `instructions:{entry:{list:` + the keyed entries tail; no dotted id family survives (0 of 534 route ids).
- described behaviour (API-managed durable entries, server-side, announced at next step boundary) — **behaviour-absent** in 1.19.3. `step boundary`/`stepBoundary` are 0-hit too.

## 4. Verifier result at BASE (freshest measurement)

```
python3 -B verifiers/verify_surfaces.py --omp-strings <18.12.5 strings> \
  --opencode-strings <1.19.3 strings> --check surfaces.opencode_extract --json
→ exit 1
→ "OC-6 (owns opencode:api-entries/instructions; missing /instructions/entries + session.instructions.entry.put)"
```

Operability hazard worth fixing during C1: this message lists **both** anchors although `/instructions/entries` is present.
`rule()` (`verifiers/verify_surfaces.py:405-407`) sets `missing = list(anchors)` whenever the conjunction fails, so a
re-pinner reading only the FAIL text would conclude the whole surface vanished. I did not change `rule()` (all six rules
and the self-test strings depend on it); recommend per-anchor presence reporting or an explicit note.

## 5. Minimum discriminating anchor set for 1.19.3

- For the **behaviour as described** (server-managed entries): **empty set** — no anchor set can witness a route the
  server does not expose. Any rule anchored on `/instructions/entries` alone passes on a dead client stub (false witness).
- For the **client-SDK surface only** (acceptable only with the class carried `excluded`):

| # | anchor | dump | drop-oc6 fixture | dump minus line 606940 | omp 18.12.5 dump |
|---|---|---|---|---|---|
| 1 | `instructions:{entry:{list:` | 1 | 0 | 0 | 0 |
| 2 | `instructions/entries/${encodeURIComponent(` | 1 | 0 | 0 | 0 |

Each anchor is necessary (remove either → no match), jointly sufficient, minifier-free (`encodeURIComponent` is a
platform global; the rest are API property names), and cross-harness clean. The pair covers list + keyed put/remove;
no third anchor adds discrimination.

## 6. Recommendation + draft patch

`opencode:api-entries/instructions` moves `governed → excluded` (the corpus already uses this verdict for
declared-with-no-consumer surfaces, cf. `opencode:config/instructions`), with the sweep in the reason; OC-6 keeps the
class id (so two-way extraction parity still holds) but anchors on the two structural shapes.

Draft: `.ufo/waves/round-47/build/C1WitnessOC6.patch` (11 files, +40/−31), machine evidence in `C1WitnessOC6.sweep.json`.

- `verifiers/verify_surfaces.py` — OC-6 comment rewritten with the sweep; `OC_API_ROUTE`/`OC_API_ID` → `OC_API_NS`/`OC_API_KEYED`; predicate updated.
- `verifiers/surfaces-baseline.json:266-271` — `verdict: excluded` + reason (534 ids / 0 instruct / no caller / 0-hit old id).
- Census — prose item 4 rewritten to "(excluded in 1.19.3)" with route-prefix correction; row moved § B (:209) → § C with reason (:227 after patch).
- Fixtures — `strings-opencode-clean.txt:19-21`, `-extra.txt:16-17`, `-drop-oc1..5` OC-6 blocks replaced with the structural pair;
  `-drop-oc6.txt` comment reworded **without** embedding the anchor literals (a comment containing them would defeat the drop fixture).

Validation (in scratch clone `/fast/scratch/kotoba-r47/C1WitnessOC6/lane`, BASE + patch):
- `python3 -B verifiers/verify_surfaces.py --self-test` → **0 failures over 87 assertions, exit 0**.
- Full run on the frozen snapshots → exit 1, **4 PASS / 3 FAIL**; OC-6 is no longer among the failures. Remaining:
  `surfaces.literal_present`, `surfaces.no_uncovered_class` (omp vacuity 0/8) and OC-1/OC-4 (sibling lanes).
- `table_parity` 38 ids PASS, `literal_parity` 38 rows PASS, `kind_parity` 38 rows PASS, `excluded_reason`
  10 excluded all reasoned PASS.
- `git apply --check` of the saved patch against a fresh BASE clone → exit 0.
- Patched extractor on the real dump: `OC-1 False, OC-2 True, OC-3 True, OC-4 False, OC-5 True, OC-6 True`;
  extracted ids include `opencode:api-entries/instructions`.

If L1 prefers to keep the class governed, the structural anchors still apply, but the class would then claim a live
instruction surface the 1.19.3 bundle does not implement — I advise against it.

## 7. Commands (all read-only except the scratch clone)

| command | exit | key output |
|---|---|---|
| `grep -c -F '/instructions/entries' opencode-1.19.3.strings` | 0 | 1 (line 606940) |
| `grep -c -F 'session.instructions.entry.put' opencode-1.19.3.strings` | 1 | 0 |
| `grep -a -c -F 'session.instructions.entry.put' bin/opencode-1.19.3` | 1 | 0 |
| `grep -a -c -F '/instructions/entries' bin/opencode-1.19.3` | 0 | 1 |
| `grep -o -E 'identifier:"[^"]+"' … \| sort -u \| wc -l` | 0 | 534 |
| same, `\| grep -c -i instruct` | 1 | 0 |
| `grep -o -E '[CTS]\.[a-z]+\("[^"]+","[^"]*instructions[^"]*"' … \| wc -l` | 0 | 0 |
| `python3 -B verifiers/verify_surfaces.py --opencode-strings … --check surfaces.opencode_extract --json` (BASE, scratch) | 1 | OC-6 unmatched |
| `python3 -B verifiers/verify_surfaces.py --self-test` (patched, scratch) | 0 | 87/87 |
| `git apply --check C1WitnessOC6.patch` (fresh BASE clone) | 0 | clean |

No tools installed or upgraded. No production file in the lane root was written; all edits live in
`/fast/scratch/kotoba-r47/C1WitnessOC6/lane`.

## 8. What I did NOT check

- No runtime probe: I did not launch `opencode serve`/the 1.19.3 binary to enumerate live HTTP routes; every claim is static (dump + `grep -a` on the binary). A runtime 404/200 on `PUT /api/session/:id/instructions/entries` would convert the "server absent" inference into a direct observation.
- No diff against the round-18 `v2.0.26` binary/dump (not on this host). `LOG.md:950` records "6/6 rules" PASS there, which implies the dotted id existed in that substrate; the loss is therefore read as substrate drift `[INFERENCE]`, not as a prior false pin. The 1.19.3 < 2.0.26 version order is unexplained from local artifacts.
- Did not establish which package/version the `606940` client module came from, nor whether a newer server (remote/desktop) implements the route.
- Did not check UTF-16/compressed copies of the bundle; the ELF carries plain UTF-8 JS and dump vs binary agree on both anchors.
- Did not run lane-wide gates in the fleet root; all verifier runs used the scratch clone and the frozen snapshot.
- Did not verify semantic intent of the 534-id registry beyond name matching (e.g. an instructions route registered without an `identifier` and built from pieces that themselves contain no `instruct`/`entries` fragment — excluded by the fragment sweep).
