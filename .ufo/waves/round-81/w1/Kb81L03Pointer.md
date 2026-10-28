# Kb81L03Pointer — report-pointer recon (R1 input)

Round 81 w1, scout seat. Scope: enumerate every `.ufo/reports/` citation shape in the
corpus; for each `<rev>:<path>` token, which repo holds the object; `HEAD:` ambiguity;
the round-76 fleet-report symlink's resolution and hash; and whether `## SHONEN`+≥400 B
is the right content-identity bound, with counterexamples. Read-only: no lane/git
mutation; all `git` calls were `cat-file -e`, `rev-parse`, `ls-files`, `ls-tree`,
`cat-file -p` (exits pasted below). Evidence files copied to
`.ufo/waves/round-81/build/Kb81L03Pointer.{integrity-observed.json,pointer-sites.json}`.

## 1. Citation census (base `b2842231`, working tree)

Grammar (frozen at `verifiers/verify_corpus_integrity.py:146-148`):

    UFO_POINTER_RE = (?<![\w.\-/])((?:/|~|(?:\.\.?/)*)[^\s`\"]*?\.ufo/reports/round-\d+/[^\s`\"]*\.md)

`python3 -B verifiers/verify_corpus_integrity.py --repo . --json` (exit 1, expected at
base) over the 155 tracked corpus files, 154 `.md`:

| class | count | detail |
|---|---|---|
| checked pointers (`report_total`) | 111 | 110 resolve, 1 dead |
| `report_dead` | 1 | `corpus/lessons/round-77-verifier-spotcheck.md:15: HEAD:.ufo/reports/round-77/kotoba.md` |
| excluded (placeholder `<>`/`…`/glob/space) | 8 | `.ufo/reports/round-1/<lane>.md` ×7 sites, `<repo>/.ufo/reports/round-11/kotoba.md` ×1 |
| quoted-context (inside `"…"`) | 2 | `README.md:68`, `lessons/round-57.md:86` |
| shapes of the 111 | bare 65 · absolute 44 · relative 1 · tilde 1 | `pointer_shape()` classes |

Full site list: `build/Kb81L03Pointer.pointer-sites.json` (rel, line, shape, token,
resolved target). Shape notes:

- **bare** (65): `.ufo/reports/round-N/kotoba.md` — resolves via
  `report_pointer_exists` fleet fallback: `(FLEET_ROOT / token).is_file()`,
  `FLEET_ROOT = /home/vgpnk/Projects/shokunin` (verifier line 127, 273-277). The citing
  dir lookup (`corpus/lessons/.ufo/...`) always misses; fleet is the de-facto resolver.
- **absolute** (44): 37 fleet-absolute `/home/vgpnk/Projects/shokunin/.ufo/reports/…`,
  7 lane-absolute `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/reports/…`
  (rounds 21, 23, 37, 45 — the lane-hosted era). Zero lowercase `/projects/` tokens
  (the r17 dead-pointer class is fully repaired in this population).
- **relative** (1): `README.md:58` `../.ufo/reports/round-23/kotoba.md` →
  `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/reports/round-23/kotoba.md`
  (resolves *into the lane worktree*: `corpus/../.ufo` = lane root).
- **tilde** (1): `lessons/round-1-aggregator-audit.md:9`
  `~/Projects/shokunin/.ufo/reports/round-1/kotoba.md` → `expanduser()`, HOST-DEPENDENT
  (`$HOME`); resolves only because this host's HOME is `/home/vgpnk`.
- **`<rev>:<path>`** (1): see §2.
- **placeholder**: the 8 excluded above — `<lane>.md`, `<repo>/` prefix.
- **directory / no-suffix**: tokens like `.ufo/reports/round-1/` never match the regex
  (needs `.md` tail) — not pointers, not counted (documented at
  `corpus-integrity-round11.md:115`).
- **`:line` suffixes** (`…/kotoba.md:193`) — regex ends the token at `.md`; the `:NNN`
  is context, not part of the promise.

Target-repo split of the 110 resolvable: **FLEET 102, LANE 8** (the 7 lane-absolute +
1 relative; all lane-hosted rounds {21, 23, 37, 45}). Rounds cited: 1–17 fleet era,
21/23/37/45 lane era, 46–80 fleet era (fleet `kotoba.md` is absent for rounds 20–45 —
verified `ls -e` on the fleet worktree; the lane repo alone carries those reports, mode
100644). Round-76 is the only lane report that is a **symlink** (`ls-files` mode
120000, blob `bf7c7e0c…`).

## 2. `<rev>:<path>` tokens — object presence, both repos

`git cat-file -e <token>` exits (lane / fleet):

| token | lane | fleet | notes |
|---|---|---|---|
| `HEAD:.ufo/reports/round-77/kotoba.md` | **128** (`fatal: path '.ufo/reports/round-77/kotoba.md' does not exist in 'HEAD'`) | **0** | the corpus's only such token; lane tree has no round-77 report |
| `4419fb9:.ufo/reports/round-15/kotoba.md` | 128 | 0 | `.ufo/round-26/scouts/S5.md:23` — tracked lane file, outside corpus (gate blind) |
| `e8a81ac:.ufo/reports/round-28/kotoba.md` | 0 | 128 | `.ufo/round-35/scouts/N08.md:30` |
| `ecb26c3:.ufo/reports/round-32/kotoba.md` | 0 | 128 | `.ufo/round-35/scouts/N12.md:7` |
| `HEAD:.ufo/reports/round-23/kotoba.md` | 0 | 128 | lane-only path (fleet never carried r23 `kotoba.md`) |
| `HEAD:.ufo/reports/round-15/kotoba.md` | 128 | 0 | fleet-only path (lane never carried r15) |
| `HEAD:.ufo/reports/round-76/kotoba.md` | 0 | 0 | **both exist — different objects** (below) |

Commits: `4419fb9` lane=128 fleet=0; `e8a81ac`/`ecb26c3` lane=0 fleet=128 — the era
boundary is real: round 20–45 kotoba reports and their commits are lane objects only;
early/late rounds are fleet objects only. Any single-repo probe gets the other era
wrong.

### `HEAD:` IS ambiguous — three independent mechanisms (observed, not inferred)

- HEAD itself differs: lane `b284223105f4d106f7e8f56ed4fd296c643cda0e`, fleet
  `8566072e04f235b23b48786cbb61589837017c97`.
- Asymmetric presence: `HEAD:.ufo/reports/round-77/kotoba.md` = fleet-only (lane 128);
  `HEAD:.ufo/reports/round-23/kotoba.md` = lane-only (fleet 128). So "the repo that
  resolves it" is not stable across rounds.
- **Same path, different object**: `HEAD:.ufo/reports/round-76/kotoba.md` is lane blob
  `bf7c7e0c0c39a57c49224c87348afc74dca14db4` (mode 120000 — the 43-byte symlink text
  `../../../../.ufo/reports/round-76/kotoba.md`) vs fleet blob
  `f83f2aae112b73325a5b1779921ef67b3f041cd9` (mode 100644, 8128 B, the real report).
  Citing-repo-first picks the lane symlink; a content-identity check on that object
  sees 43 bytes of link text, not a report.

R1 consequence: `<rev>:<path>` identity must (a) iterate candidates lane-then-fleet per
the plan, (b) apply the content screen to **each** candidate, not short-circuit on the
first `cat-file -e` hit — else the r76 lane symlink launders as "resolved" while being
link text, and (c) either dereference mode-120000 blobs (re-read the target path's
object — relative link resolves against the lane worktree → fleet file) or treat
link-text bytes as non-report and continue the ladder. Existence alone (r80 E04 patch:
partition on `:`, `cat-file -e` lane then fleet) resolves W10's `HEAD:` ancestor but
binds nothing about the resolved bytes.

## 3. The fleet-report symlink (`.ufo/reports/round-76/kotoba.md`)

- `readlink`: `../../../../.ufo/reports/round-76/kotoba.md` → resolves to
  **/home/vgpnk/Projects/shokunin/.ufo/reports/round-76/kotoba.md** (the FLEET repo's
  file; the lane worktree's own copy of its round-76 report is the fleet object via
  symlink — consistent with the r80 `Kb80E02Symlink` landing).
- link blob: 43 B; `git ls-files -s` mode `120000`.
- resolved target: 8128 B regular file (fleet `ls-tree` 100644), `## SHONEN` ×1.
- sha256 of resolved bytes: `a025051d389368ea3a1078b7a64d3847c1e6ff25328fc1645a7be34f30e3f78f`
  — **byte-identical to the r80 receipt** `Kb80C01C1-marker-shas.txt` line 1, and to
  `sha256sum -b` on the lane symlink (which follows the link). The W10 marker the r80
  critic substituted (7-byte `marker`, sha256 `d4169ac5…`) fails both conjuncts of the
  proposed bound.
- `ls -la`/`stat` quirk to record: `stat -c %s` on the symlink reports 43 (link
  length); `stat -Lc %s` reports 8128. Any `len(bytes)` bound MUST stat the resolved
  object, not lstat the pointer.

## 4. Is `## SHONEN`+≥400 B the right identity bound? NO — 12 counterexamples

I evaluated all 111 live pointers against "`resolved bytes contain `## SHONEN` AND
size ≥ 400`" (script reuses the verifier's own regex/resolution; method and full output
in `build/Kb81L03Pointer.pointer-sites.json` run log):

**11 currently-live, honest pointer sites flip to `report_dead` under the bound**
(report_dead 1 → 12; corpus gate stays red = C1 killed by its own repair):

| site | token target | size | `## SHONEN` | what it actually is |
|---|---|---|---|---|
| `README.md:24` | fleet r5 `kotoba.md` | 5080 | 0 | real report, pre-SHONEN era |
| `README.md:26` | fleet r1 `kotoba.md` | 3365 | 0 | real report (`# kotoba-shokunin — round-1 findings`) |
| `README.md:28` | fleet r4 `kotoba.md` | 3367 | 0 | real report |
| `README.md:49` | fleet r8 `kotoba.md` | **120** | 0 | the round-8 report IS a respawn marker — corpus knowingly cites it (`lessons/round-8.md:4-5`: "120 B, a respawn marker") |
| `knowledge/checklist-execution-round15.md:70` | fleet r14 `kotoba.md` | 9463 | 0 | real report (DRAFT-marked) |
| `lessons/round-1-aggregator-audit.md:9` | fleet r1 (tilde) | 3365 | 0 | as above |
| `lessons/round-1.md:4` | fleet r1 | 3365 | 0 | as above |
| `lessons/round-4.md:4` | fleet r4 | 3367 | 0 | as above |
| `lessons/round-5.md:4` | fleet r5 | 5080 | 0 | as above |
| `lessons/round-8.md:5` | fleet r8 | **120** | 0 | as above |
| `lessons/round-9-aggregator-corpus-verdict.md:24` | fleet r14 | 9463 | 0 | as above |

Clause attribution: `## SHONEN` alone breaks all 11; `≥400 B` alone breaks only the 2
round-8 sites (round-15's 273 B marker file — itself titled "closeout (marker)" — is
NOT cited anywhere as a pointer; verified by census, not by guess). Fleet era reports
with `SHONEN=0` that ARE cited: r1 (3 sites), r4 (2), r5 (2), r8 (2), r14 (2); uncited
SHONEN-less reports (r13, r16, r17) don't count against the bound today but the bound
penalizes them on first citation.

**Non-report files that PASS the bound** (lane-tracked; a W10 attacker can substitute
content of this class and still read alive — the bound is a screen, not identity):
`.ufo/round-38/drafts-report-skeleton.md` (20142 B, `## SHONEN` at line 76),
`.ufo/round-37/evidence/b2-shonen-section.md` (4066 B, `## SHONEN` at 15),
`.ufo/round-40/evidence/b2-shonen-section.md` (5375 B, `## SHONEN` at 17), plus 44
more draft/skeleton/scout/evidence files — `git grep -l '^## SHONEN' -- '*.md'` outside
`.ufo/reports/` returns **47 lane-tracked paths** total. A 500 B extract of any of
these at the report path satisfies both conjuncts while not being the round's report.

Interpretation for R1 (recon, not a design ruling): `## SHONEN` is a **round ≥~19**
convention (r3/r6/r7/r9–r12/r19+ have it; r1/r4/r5/r8/r13–r17 don't). A single conjunct
applied to every resolved target fails the corpus's own honest history: honest early
reports and honest marker-shaped reports (r8 120 B) exist and are cited. The W10 class
(substituted non-report bytes) needs *some* content screen, but a bound that accepts
this lane's legacy targets MUST be disjunctive or era-scoped — e.g. "contains `## SHONEN`
OR carries a `^# ` report title + ≥N structure lines" still fails r8's marker if it
demands ≥400 B; the only bound that passes r8 is one accepting a titled <400 B report,
which a 7-byte `marker` file also fails (r8 starts `# kotoba round-8 closeout\n\n…`
≈ 3 content lines — distinguishing a bare 7 B `marker` needs at minimum "starts with a
`# ` heading line", which a crafted fake trivially carries). The honest statement:
content-identity against *substituted* bytes is only soundly bound by expected-content
pins or per-era shape rules; `## SHONEN`+400 B alone both over-kills (11 sites) and
under-binds (draft files pass it).

## 5. Peripheral observations (for the R1 implementer)

- `report_pointer_exists` currently does **filesystem** checks only; `<rev>:<path>`
  is misclassified `bare` by `pointer_shape` and resolved as the literal path
  `corpus/…/HEAD:.ufo/…` → always dead. The single dead token is the r77 spot-check's
  `HEAD:` citation inside a *backticked command* `git show HEAD:…` — the pointer path
  has NO code-span exemption (`inside_code_span` is applied only to `COMMIT_RE`
  tokens, lines 526-529 vs 512-523). R1's object-expression arm is the correct repair;
  do not "fix" it by excluding code spans, or the quoted-context/class boundary moves
  under the kill-rule's "no dropped classification" clause.
- The S230/S231 `commit_unresolvable` pair (`SOURCES.md:171-172`,
  `7bb48f21…`) is the commit family (`commit `…`` grammar), NOT a `.ufo/reports`
  pointer — R2's `external-commits.json` manifest binds it; orthogonal to pointer
  resolution but shares the lane-then-fleet ladder (`commit_resolves`, lines 600-612).
- `check_report_pointers.py` (r73, `--report`) is a *different* pointer universe:
  backticked spans in a round report resolving to lane-tree paths; it drops `:NNN`
  locators and skips `<rev>:`-style absolute/tilde tokens per R6. It will also see
  `HEAD:.ufo/…` tokens in the r81 report if any are written there — flag for whoever
  writes the report, since bare `.ufo/reports/` isn't in its R7 prefix ladder either.
- Host-dependence note: the one tilde pointer resolves via `$HOME`; on any other
  operator host it dies. Not this round's problem (shape already counted green at
  base), but the fleet-fallback form is the portable spelling.
- Verifier JSON census for this exact run: `build/Kb81L03Pointer.integrity-observed.json`
  (`report_total 111, report_dead 1, report_pointers_excluded 8, quoted 2,
  shapes {bare 65, absolute 44, relative 1, tilde 1}`, `commit_total 46,
  commit_unresolvable 2, commit_truncated 4, commit_quoted_excluded 6,
  tracked_files 155, unindexed 1` — matches the plan's base-gate truths).

## 6. R1 design facts at a glance

- Resolution ladder for `<rev>:<path>`: lane `cat-file -e` first (r80 E04 ordering),
  fleet second — BUT apply the content screen per candidate and let a screen failure
  continue the ladder, or the r76 symlink blob becomes a false accept and honest
  markers become false rejects.
- For filesystem (non-rev) pointers, the resolved *file* can be a symlink whose target
  lives in the other repo — bind the resolved bytes (dereferenced), never lstat size.
- Content bound must accept: ≥400 B `## SHONEN` reports (modern), ≥3 KB `## `-structured
  reports without SHONEN (r1/r4/r5/r13–r17 era), <400 B titled marker-reports (r8, and
  r15 if ever cited) — or those citations must be reclassified, which moves the corpus
  under the kill rule if done by narrowing the gate rather than correcting the rows.
- `HEAD:` tokens resolve repo-locally; cite `<full-40-hex>:<path>` if a stable referent
  is wanted — `HEAD:` in this corpus resolves only via the fleet fallback today.

VERDICT: `## SHONEN`+≥400 B as stated fails 11 honest live pointer sites (incl. the 120 B round-8 marker-report) while passing 47 lane-tracked non-report draft/skeleton files — use it as a screen inside a lane-then-fleet, per-candidate, symlink-aware resolver, not as the identity bound itself.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81L03Pointer.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81L03Pointer.integrity-observed.json /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81L03Pointer.pointer-sites.json
