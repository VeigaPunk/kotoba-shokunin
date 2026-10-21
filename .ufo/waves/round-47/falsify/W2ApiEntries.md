verdict: HOLDS — the retirement of `opencode:api-entries/instructions` survives a full server-route/handler/operation-id sweep of the frozen opencode 1.19.3 dump; the durable census under-records the client stub and the plan's required Q14 sweep, and no gate witnesses the retirement.

# W2ApiEntries — retirement of `opencode:api-entries/instructions`

Tree `7ad7fadfc09354b74fb66605dfb0c1182c115a2f` (BASE `c61a973`). Substrate: `/fast/scratch/kotoba-r47/shared/{opencode-1.19.3.strings,bin/opencode-1.19.3}`; `sha256sum -c SHA256SUMS` 4/4 OK exit 0; live `~/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe` and `~/.local/bin/omp` are byte-identical to the frozen copies (179ca421… / fdbc8136…); `omp --version` → `omp/18.12.5`. The npm package contains only `bin/opencode.exe`, `package.json`, `postinstall.mjs`, `LICENSE`, so the dump is the whole shipped surface.

Scope: only the retirement claim (`corpus/knowledge/instruction-surface-census-round13.md:242-245`, ledger `:313`, baseline note `verifiers/surfaces-baseline.json:3`). C2/C3, the omp half of C1 and the pins gate were not attacked here.

## F1 — no server route, handler or operation id exists (retirement holds)

The census asserts “no server route or `session.instructions.entry.put` id exists” (`corpus/knowledge/instruction-surface-census-round13.md:243-244`) and retires the class (`:313`); the baseline records the same in its assembled note (`verifiers/surfaces-baseline.json:3`). I could not falsify it:

- `instructions/entries` occurs **3×** in the dump and **3×** in the raw ELF (offsets 149,434,931 / 149,435,112 / 149,435,337), all inside one generated client object in the web-SPA chunk `/$bunfs/root/index-B5F0ExSs-vg79mw52.js` (48,587,202–51,323,508). UTF-16LE/BE: 0.
- The server route table is Effect HttpApi (`C.<method>(identifier, "/api/…", …)`), **58 registrations**; the `/api/session/:sessionID/*` subset is **20 paths**; the embedded brace-form spec table has the same 20. No instruction path: `"/api/session/:sessionID/instructions"` **0**, `:sessionID/instructions` **0**, `"/instructions"` **0**.
- The server's own generated client chunk `/$bunfs/root/chunk-0eyvn34x.js` (10,278,438–10,338,219) has **51** `url:"/api/…"` literals and **0** `instructions`. Normalizing `:param`/`{param}` to one placeholder, the 58-registration server path set and this client's 51-path set are **exactly equal** (51 == 51, server-only ∅, client-only ∅) — the server's own client is a faithful mirror of its route table, and that table has no instructions path.
- Operation ids: `session.instructions` **0**, `v2.session.instructions` **0**, `InstructionEntry` / `instructionEntry` / `instructionsEntries` / `instructions_entries` **0**, `entry.put` **0**. Of the 58 route identifiers, none contains `instruct`.
- Legacy surface: the `Dn` route-name table (24 entries, base `yn="/session"`) and the brace-form `/session/{sessionID}/…` table also contain no instruction path.
- No Hono app: `app.get(` **0**; the `Hono` tokens are Honolulu timezone names, an Apache regex and Bun feature flags. The route surface is the Effect HttpApi table above.
- `python3 verifiers/verify_surfaces.py` (frozen dumps **and** default resolution) → 7/7 PASS, exit 0; `surfaces.opencode_extract` prints “9/9 declared class(es) from 7/7 rules”.

Base→after is a clean cutover, not a silent drop: at `c61a973` the baseline had 5 opencode ids including `opencode:api-entries/instructions` governed, and `git show c61a973:verifiers/verify_surfaces.py:442` has `rule("OC-6", ["opencode:api-entries/instructions"], api, …)`; at 7ad7fad the baseline has 9 opencode ids, none matching `api-entries`, and OC-6 owns `opencode:instruction-context/AGENTS.md` (`verifiers/verify_surfaces.py:497`).

Counts (all exit 0):
```
python3 -c 'd=open(sys.argv[1],errors="replace").read();print(d.count(sys.argv[2]))' /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings '<anchor>'
session.instructions.entry.put            0
instructions:{entry:{list:                1
instructions/entries                      3
"/api/session/:sessionID/instructions"    0
InstructionEntry                          0
entry.put                                 0
```

## F2 — the client stub is full CRUD, not `list`-only; the census row under-cites it

`corpus/knowledge/instruction-surface-census-round13.md:313` cites only `` client stub `instructions:{entry:{list:` 1 ``. That count is literally correct, but the same object (dump offset 49,628,338) also defines:

- `list`: GET `/api/session/${sessionID}/instructions/entries`, 200, statuses `[404,400,401]`;
- `put`: **PUT** `/api/session/${sessionID}/instructions/entries/${key}`, body `{value}`, **204**, statuses `[404,413,400,401]`;
- `remove`: **DELETE** `/api/session/${sessionID}/instructions/entries/${key}`, **204**, statuses `[404,400,401]`.

So the durable census describes a weaker counter-signal than the round's own evidence: `.ufo/waves/round-47/build/C1CriticRepin.md:21` already records ``{list,put,remove}`` and the two 204 paths (its “1 hit” counts the client object, not the string; the dump has 3 path templates). This does not make the retirement wrong — the client is the **SPA's** generated client, not the server's. The web-SPA client carries 12 session-resource families with no v2 server route (`form`×5, `generate`, `instructions/entries`×2, `move`, `pending`, `rename`, `synthetic`, `background`, `command`, `fork`, `shell`, `skill`), i.e. it is version-skewed against this server; the server's own client has none of them. The web chunk contains exactly 6 `instructions` tokens (4 in the client object, 2 in integration-OAuth data `o.data.instructions`) and no call site. [INFERENCE] the CRUD methods are unused generated code; minified property access could in principle hide a call site, but no `instructions` token exists outside those 6 positions.

Repro: `python3 -c 'd=open("/fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings",errors="replace").read();i=d.find("instructions:{entry");print(repr(d[i-60:i+900]))'`.

## F3 — the required Q14 sweep is not in the durable record

`plans/round-47.md:26` requires “every class that no longer exists re-verdicted with its sweep” (Q09, Q14); `corpus/QUALITY.md:25` defines Q14 as “a negative claim carries its sweep: the search that produced the absence”. The census's negative claim at `:243-244` records only the old operation-id count (`session.instructions.entry.put` 0) and the client-stub count; it does not record the route search. The sweep exists only in wave evidence, `.ufo/waves/round-47/build/C1CriticRepin.md:21` (`:sessionID/instructions` 0, `experimental/session/…instructions` 0). My wider sweep (58 registrations / 20 v2 paths / 20 brace paths / 51 client URLs / 103 `/api/` literals / 3 total `instructions/entries` occurrences) reproduces the absence, but a reader of the census alone cannot. This is a calibration defect in the record, not a falsification of the retirement.

## F4 — no gate witnesses the retirement (mutation test)

`check_opencode_extract` (`verifiers/verify_surfaces.py:727`) enforces declared↔produced parity only; `grep -n "retired" verifiers/verify_surfaces.py` returns comments at `:363` and `:1056`, no check. I appended two plausible registrations to a copy of the frozen dump:

```
C.put("session.instructions.entry.put","/api/session/:sessionID/instructions/entries/:key",...)
C.get("session.instructions.entry.list","/api/session/:sessionID/instructions/entries",...)
```
(`/fast/scratch/kotoba-r47/w2/KotobaR47-2.W2ApiEntries-2/mut/oc-with-instructions-route.strings`), then ran `python3 verifiers/verify_surfaces.py --opencode-strings <mutated> --omp-strings <frozen omp>` → **7/7 PASS, exit 0**. A future 1.19.x that re-adds the route would keep the gate green; the landed mitigation is the prose ledger (`census:305-321`), not a machine witness. This is exactly the gap the round's own critic predicted at `.ufo/waves/round-47/build/C1CriticRepin.md:38` (“removing a dead class from baseline+census together keeps 7/7, so ‘never silently dropped’ has no machine witness”).

## F5 — stale class-count in the census's Honest ceiling

`corpus/knowledge/instruction-surface-census-round13.md:371` still says `surfaces.opencode_extract` “must reproduce all **5** declared opencode class ids” (and `:370` “six code-shape rules”). At 7ad7fad the baseline declares **9** opencode ids and the check runs **7** rules (OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6) — the verifier prints “9/9 declared class(es) from 7/7 rules”. The sentence was true at BASE (`git show c61a973:corpus/knowledge/instruction-surface-census-round13.md:287-288`, when the baseline had 5 opencode ids and 6 rules) and was not updated by the round-47 edit that added § B′ and the ledger. Q13 (`corpus/QUALITY.md:24`) requires a count to carry its command; this one is contradicted by the gate output. It does not affect the retirement verdict, but it is a concrete calibration defect in the same class-set record.

## Counterexamples / negative results

- **No server route found** under any enumeration: 58 `C.*` registrations, 20 `:sessionID` paths, 20 brace paths, 24 `Dn` names, 51 client URLs, 103 unique `/api/` literals, 3 total `instructions/entries` occurrences (all SPA client). Raw binary and UTF-16 agree.
- **No operation id/type/handler**: `session.instructions` 0, `v2.session.instructions` 0, `InstructionEntry` 0, `entry.put` 0, no instruction-bearing route identifier.
- **The only “hit”** is the SPA's generated CRUD client (F2), which also carries endpoints this server does not implement; it cannot carry the server route.
- **The mutation** (F4) shows the opposite direction is also true: planting the route does not redden any gate.

## What I did NOT check

- I did not run the server or issue an HTTP request; the absence is static (dump, raw bytes, embedded route tables), not a runtime 404 observation. I did not execute the frozen ELF or the `~/.local/bin/opencode` wrapper.
- I did not decode the SPA source map (`index-B5F0ExSs.js.map` is referenced but I did not verify whether it is embedded) or run the SPA; the “unused generated client” is `[INFERENCE]` from the 6-token scan.
- I did not check other opencode builds/versions (1.19.x range or 2.x) or the live npm registry; only the pinned `179ca421…` ELF.
- I did not attack C2, C3, the omp half of C1, the `check_substrate_pins.py` 3/3 claim, or the `oc-*` mutation fixtures/`--self-test`; another lane owns those. (`verify_harness_claims.py` exits 1 on omp catalogue drift and `oc.roots.names_plus_builtin` 11≠7; it never mentions `api-entries`.)
- I did not verify that the server actually serves the SPA bundle `index-B5F0ExSs.js` (it is embedded and referenced by the embedded `index.html`); that is irrelevant to server-route absence.
- No tools were installed or upgraded for this lane.

Artifacts: `W2ApiEntries.sweep.json` (substrate hashes, counts, route/client enumeration, mutation result). No production files were modified; all mutation work is in `/fast/scratch/kotoba-r47/w2/KotobaR47-2.W2ApiEntries-2/`.
