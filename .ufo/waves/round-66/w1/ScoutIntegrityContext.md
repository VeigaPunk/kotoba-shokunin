# ScoutIntegrityContext — trace: COMMIT_RE → citation_findings → corpus_observations

Seat: UFO-FSD scout (read-only; no edits to lane source, claims, counters, plans, or receipts).
Scope: `verifiers/verify_corpus_integrity.py` in the kotoba lane.
Pinned base: `11385e04e368c1e94ab1a5a89d7439033eb1f855` (ancestor of tip; controls frozen there).
Measured tip: `2a8eba56b3f9321b70c569fa2816d42237ca49a2` (working tree at review time).
All sandbox fixtures ran under `/tmp/r66-scout-ictx/`; one throwaway git repo (`/tmp/r66-scout-ictx/ambig2/repo`) was created and discarded there only.

## 1. Trace

`citation_findings(rel, text, pointer_exists, commit_resolves)` (`verifiers/verify_corpus_integrity.py:491`) scans every line of every tracked `corpus/**/*.md`, including fenced lines — there is no `fenced_lines` call in the POINTERS path (unlike INDEX, which marks a fence-opaque named class, `:434-436`).

Per line, second loop (`:520-531`):

1. `COMMIT_RE` (`:149`) — `(?<![A-Za-z0-9_-])commit[ \t]+`([^`\n]+)``. Lookbehind excludes `pre-commit `/`commits ` (verified: `commits` fails `[ \t]+` immediately after `commit`). The token is the backticked capture `group(1)`; `group(0)` covers `commit `token``.
2. **Context exclusion** (`:522-524`): `inside_quotes(line, m.start(1), m.end(1))` (double quotes enclosing the *token* on its line — odd quote count before AND a `"` after, `:313-319`) OR `inside_code_span(line, m.start(0), m.end(0))` (the *whole match* enclosed by one equal-width unescaped backtick run pair, `:321-341`). Either → `commit_quoted_excluded`, recorded as `<token> (quoted meta-finding)`; never `nonhash`, never `commit_total`.
3. **Non-hash** (`:526-528`): `is_hex_object_id` = `^[0-9a-fA-F]{7,40}$` (`:303-305`); failure → `commit_nonhash` (zero-mode check).
4. **Count then resolve** (`:529-531`): `commit_total += 1` *before* resolution, so the equal-mode census includes unresolvable citations; `commit_resolves(token.lower())` failure → `commit_unresolvable` (zero-mode check).

`corpus_observations(repo)` (`:614-679`) injects, per tracked md file: `report_pointer_exists(repo/base, token)` (citing dir first) and `commit_resolves(hex_id, repo)` (default `fleet_root=FLEET_ROOT`). Aggregation is additive counts plus sorted `*_detail` lists; `evaluate` (`:711-728`) adjudicates `equal` vs `zero`; `main` exits 1 on any DRIFT (`:1451`).

## 2. Lane-first / fleet-root fallback — CONFIRMED on live objects

**Commits** (`commit_resolves`, `:591-603`; r66 addition, absent at pinned base — base line 617 was a lane-only inline `cat-file -e` lambda):

- Lane first: `git -C <repo> cat-file -e <hex>^{commit}`; on success, returns True (fleet never queried).
- Fleet fallback: only when `fleet_root.is_dir()`; `cat-file -e` in `FLEET_ROOT=/home/vgpnk/Projects/shokunin`.
- Observed live at tip: `7b370d54…` (round-65 lesson:11), `1154d57a…` (round-66 lesson:11), `def4b9ff…` (round-62 lesson:13) are `lane=no, fleet=YES` — resolve *only* via the hop; `7b80ae80` (round-60 lesson:37) is `lane=YES, fleet=no` — lane-first short-circuit in vivo.
- Base-vs-tip difference verified against `git show 11385e04:...`: at base, `citation_findings` excluded only `inside_quotes` (no `inside_code_span`) and `corpus_observations` resolved lane-only — matching the control's `unresolvable=3` at pinned base vs `unresolvable=0` at tip (my live run).

**Report pointers** (`report_pointer_exists`, `:270-274`):

- Citing directory first: `(repo / Path(rel).parent / token).resolve().is_file()` for relative/bare; absolute/`~` resolved literally via `resolve_pointer` (`:261-267`).
- Fleet fallback is **bare-only**: `token.startswith(".ufo/reports/") and (FLEET_ROOT/token).is_file()`. A failing `../.ufo/…` relative pointer does NOT hop.
- Load-bearing, not a corner case: all 35 live bare `.ufo/reports/round-N/kotoba.md` tokens in the corpus resolve `citing=False laneroot=False fleet=True` — the fleet `.ufo` (with lane-named `<lane>.md` files) is their only home. The lane's own `.ufo/reports/` (rounds ≤29) is unreachable by bare pointers; `laneroot=False` for every live token. Caveat: a bare pointer intended lane-local is structurally dead; the shape is documented fleet-relative.

## 3. Code-span exclusion boundaries — mapped, one defect found

`inside_code_span` semantics (all probed, `probe.py`):

| line | result | correct? |
|---|---|---|
| ``The `` commit `451a02ff` `` grammar…`` | True (excluded) | yes — w2 span encloses whole match; the one live instance `round-54-verifier-spotcheck.md:147` |
| `` `commit `abc1234` `` | False | yes — match only partially enclosed |
| `` `x commit `abc1234` y` `` | False | yes — CM splits the w1 spans; citation survives |
| `` `a` commit `abc1234` `b` `` | False | yes — token's own w1 opener is the first width-matching close candidate → `break` shields it |
| ```` ``` commit `abc1234` ``` ```` | True | consistent — w3 span encloses |
| ``\` commit `abc1234` `` | False | yes — escaped opener skipped (`unescaped` counts preceding `\`, even count = unescaped) |
| **`` ``a`` commit `abc1234` `` ``** | **True — WRONG** | **defect F1** |

**F1 — closer-reuse false accept (silent drop).** `inside_code_span` never consumes a run that already closed an earlier span: with `` ``a`` commit `abc1234` `` `` the trailing ` `` ` opens a span (per the function), and since the token's `x` backticks are width 1, no width-2 run can close it — the candidate loop never hits `break`, and an unclosed "open" span still satisfies the range test. CommonMark parses the tail ` `` ` as literal text (no partner), so the citation is live. Measured:

```text
citation_findings('corpus/lessons/x.md', '``a`` commit `abc1234` ``\n', …, λh: h=='abc1234')
→ commit_total=0, commit_quoted_excluded=1, detail=['…: abc1234 (quoted meta-finding)']
control 'commit `abc1234`' → commit_total=1
```

A live citation is silently dropped from `commit_total` (equal-mode drift downward) and mislabeled `(quoted meta-finding)`. Trigger: a same-or-wider-width run *after* the match whose only plausible partner closed before the match. Zero instances in current corpus (scan: only round-54-sc:147 excluded, correctly). Severity: latent false accept.

**Quote boundary** (`inside_quotes`, token-only span): two citations inside one quoted span (`"commit `aaaa111` and commit `bbbb222`"`) both excluded correctly; the corpus's one odd-quote line (`round-8.md:3`, `commit `8c300ad` ("…`) is quoted-**after**-token with odd count *including* that quote → 1 quote before is even → correctly counted. Line-local heuristic is conservative both directions (unclosed quote before = counted; unmatched quote after + odd before = excluded — the documented meta-finding shape).

## 4. False reject — POINTERS family is fence-blind (defect F2)

INDEX (round 36, scout P3b) made fenced regions opaque — "a coverage row quoted inside a ``` block is an example, not an index promise" — with a *named* `index_tokens_fenced` counter. `citation_findings` has no fence stage and no `*_fenced` counter:

```text
citation_findings(rel, 'example:\n```text\ndead `.ufo/reports/round-99/kotoba.md` commit `deadbee`\n```\nlive commit `abc1234`\n', …)
→ report_total=1, report_dead=1 (line 3), commit_total=2, commit_unresolvable=1 (line 3: deadbee)
```

A fenced example's dead pointer → `report_dead` DRIFT (exit 1, baseline-independent); its commit → `commit_total` + possibly `commit_unresolvable` DRIFT. Live corpus impact today: 7 pointer tokens on fenced lines — 4 `<lane>` placeholders (`cold-run-round11.md:66,100,142,280`, self-excluded), 1 quoted (`round-57.md:86`), **2 counted in `report_total`** (`cold-run-round11.md:65`, `round-57.md:86`'s neighbors both resolve, so no visible failure yet). Zero commit citations on fenced lines today. Severity: latent false reject + silent equal-mode inflation; live counts currently clean only because every fenced pointer happens to resolve or be excluded/quoted.

## 5. Nonexistent objects remain unresolved — CONFIRMED

- `^{commit}` peel means blobs/trees/tags fail too; `git_ok` returns False on any nonzero (no exception path). 40-hex `f…f` in neither repo → False (self-test `commit-hop/neither`, plus my live probes).
- Live: `commit_unresolvable=0 []` at tip; base control showed `unresolvable=3` — the three fleet commits now resolve via the hop, so the zero-mode check is genuinely exercised.
- `git_ok` caveat: `FileNotFoundError` (no git binary) is not translated to `Inconclusive` — unreachable in `main` (`git rev-parse` runs first) but the exported helper isn't total.
- **Ambiguity caveat (demonstrated):** `cat-file -e <ambiguous-prefix>^{commit}` exits 128 → counted `commit_unresolvable` even though the object exists. Mined real collision `6ebf01e{0b65…,3925…}` (two blobs) → `commit_total=1, commit_unresolvable=1`. Defensible as "a citation a reader cannot resolve is a defect," but it is a false-reject class vs. "object exists."
- Portability caveat: `FLEET_ROOT` is hardcoded (`:125`); a missing/relocated fleet → `is_dir()` False → silent `False` for every fleet-resolving citation (35 bare pointers + 3 fleet commits in the current corpus = 38 false findings off-host). Documented as "reads False, never raises" — intended, but it couples the lane gate to this host's filesystem.

## 6. Consistency/calibration notes (C2 surface)

- Baseline `verifiers/corpus-baseline.json` expects `tracked 118, unindexed 0, report 79/0, commits 37/0/0`. **Tip live run: 5/9, exit 1** — DRIFT `tracked_files 119`, `report_total 82`, `commit_total 38` (equal-mode, need baseline re-record) and **`unindexed=1` — `corpus/lessons/round-66-verifier-spotcheck.md` (zero-mode, baseline-independent: the round-66 lesson is tracked but has no coverage-map row yet)**. Consistent with the plan's "re-record observed corpus counts only after all round corpus entries land"; the C2 exit-0 predicate is not yet reachable at this tip.
- `COMMIT_HOP_MARKER` literal (`:588`) is what `check_r66_routed_repairs.py:40` pins as the D2 "integrity-source hop" evidence.
- `quoted meta-finding` label now covers both quote and code-span exclusions — the r54-spotcheck grammar complaint that motivated D2's code-span clause.

## 7. Verdict

| # | Class | Site | Status |
|---|---|---|---|
| F1 | false accept (silent drop) | `inside_code_span` `:333-340` | latent; fixture above; 0 live instances |
| F2 | false reject + count inflation | `citation_findings` no fence stage | latent; 2 live fenced pointers counted; fixture above |
| — | ambiguity/environment | `commit_resolves`/`git_ok` | caveat, demonstrated; documented partial design |

Lane-first/fleet-root fallback: confirmed working and load-bearing on real objects (3 commit hops, 35 pointer hops). Nonexistent objects: confirmed unresolved, zero-mode enforced. No production edits made; no claim, counter, threshold, plan, or receipt touched.
