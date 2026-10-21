verdict: The governance gate extracts 817 repo-rooted occurrences across LOG.md and SCORECARD.md (805 checked, 9 quoted + 3 schematic excluded) and exactly one is dead — LOG.md:2111 `.ufo/round-45/drafts/v10/post-r44-hunt.py`, a runner that no commit ever contained; but a line-keyed erratum pin is already off by one (round-46 receipts say 2112), and 24 of the 805 are `../` fleet-relative subjects that die in any clone, so a fail-closed registry must key on (file, token, occurrence ordinal, sha256 of the exact line text) and must decide the parent-relative scope explicitly.

# C3 governance citation census — BASE c61a973b2e02e1ded169703ddcb06466f4edd8bd

All paths below are lane-relative at BASE. Measurement was read-only; worktree `git status --porcelain -- LOG.md SCORECARD.md` was empty and `git rev-parse HEAD` = `c61a973b2e02e1ded169703ddcb06466f4edd8bd`.

## 1. Reproducing the extraction

Command (lane, read-only):

```
python3 -B verifiers/verify_skill_checklist.py --json      # exit 1
```

Result: `pass: 9`, `fail: 1`, `na: 0`. The failing check:

```
governance.citation_resolves  FAIL  evaluated=805
detail: LOG.md:2111: '.ufo/round-45/drafts/v10/post-r44-hunt.py' does not resolve from
        /home/vgpnk/Projects/shokunin/kotoba-shokunin;
        9 quoted meta-finding(s), 3 schematic token(s) excluded
```

The extraction is `citation_subjects(..., exclude_quoted=True, exclude_schematic=True)` (`verifiers/verify_skill_checklist.py:1378-1428`) over `GOVERNANCE_FILES = ("LOG.md", "SCORECARD.md")` (`:348`) called from `check_governance_citations` (`:1454-1495`). A token counts when it is a single-backtick inline span on one line, starts with one of `CITATION_ROOTS` (`:347` — `corpus/ verifiers/ opencode/ .ufo/ ../`), carries no `< > * ? $`, does not start with `http`/`~`/`-`, and has a `/` after rstrip (`:1400-1414`). Resolution is `citation_resolve` (`:1295-1319`): `safe_resolve` in-repo, or up to 3 leading `..` hops resolved from the repo's ancestors — existence-only, no line-anchor check (`strip_token_dressing`, `:890-895`, strips `file.md:42` to `file.md`).

## 2. Totals (reproduced by importing the same module read-only)

| file | lines | inline spans | span words | routed | live | quoted | schematic |
|---|---|---|---|---|---|---|---|
| LOG.md | 2315 | 3763 | 4879 | 599 | 589 | 8 | 2 |
| SCORECARD.md | 283 | 833 | 2816 | 218 | 216 | 1 | 1 |
| **total** | | | | **817** | **805** | **9** | **3** |

- **Total occurrences: 817** (805 live + 12 excluded). The gate's `evaluated=805` is the live count only.
- 432 distinct live tokens; 150 repeat (top: `verifiers/compare_harness_independent.py` ×35, `verifiers/check_assertion_floors.py` ×33).
- Live root histogram: `verifiers/` 176, `.ufo/` 504, `corpus/` 101, `../` 24 (13 distinct).
- 62 live subjects resolve to a **directory**, not a file; 0 live subjects retain a `:N` anchor (the dressing stripper removes it), so the gate never checks that a cited line exists.

## 3. The 9 quoted meta-findings (each with line and current resolution)

Exclusion is purely syntactic — a token inside `"…"` on its own line (`:1397-1409`, `advance_quote_state` `:1321-1335`). "resolves" is `citation_resolve` at BASE:

| # | location | token | resolves | what the line is |
|---|---|---|---|---|
| 1 | LOG.md:462 | `.ufo/reports` | yes | quoted example of a pointer shape that "dies off-layout" |
| 2 | LOG.md:722 | `.ufo/prompts/` | **no** | quoted count of three citations renamed to host-absolute form |
| 3 | LOG.md:757 | `.ufo/prompts/` | **no** | same three sites re-cited in the R16 review note |
| 4 | LOG.md:769 | `corpus/nope.md` | **no** | decoy shell argument (`cat corpus/nope.md`) |
| 5 | LOG.md:834 | `corpus/absent-round17.md` | **no** | decoy fixture path in the citation fixture note |
| 6 | LOG.md:843 | `../shared/live.md` | **no** | hermetic child/parent self-test fixture path |
| 7 | LOG.md:1130 | `corpus/QUALITY.md` | yes | "The absence of `corpus/QUALITY.md` … was observed" (historical, true when written) |
| 8 | LOG.md:1282 | `verifiers/fixtures/pins/` | yes | quoted inside an integrator-proof sentence |
| 9 | SCORECARD.md:118 | `corpus/QUALITY.md` | yes | "`corpus/QUALITY.md`" **is absent in this checkout"** — present tense, in the live `## planned` section (ends at `## retired`, SCORECARD.md:121) |

`.ufo/prompts/` has never existed as a tracked object (`git rev-list --all --objects | grep '\.ufo/prompts/'` → empty) and is absent on disk; it is a host-absolute path quoted as prose.

**Counterexample (quoted exclusion masks a false claim):** `corpus/QUALITY.md` exists at HEAD — it was added by `f2f9ee1d88bc42d80fb96075db0fc3b43fb8a321` (2026-10-19 19:29:36 -0300), 4783 bytes on disk, `git cat-file -e HEAD:corpus/QUALITY.md` succeeds. SCORECARD.md:118 remains a present-tense absence claim but the gate cannot see it because of the quote. LOG.md:1130 is a historical record (append-only), so only SCORECARD:118 is actually stale — but a registry that merely *counts* quoted exclusions would keep both green forever.

## 4. The 3 schematic exclusions

| # | location | token | resolves |
|---|---|---|---|
| 1 | LOG.md:280 | `../.ufo/…` | **no** (ellipsis) |
| 2 | LOG.md:370 | `.ufo/reports/round-N/` | **no** (`round-N` grammar, `SCHEMATIC_CITATION_RE` `:349`) |
| 3 | SCORECARD.md:129 | `.ufo/reports/round-N/kotoba.md` | **no** |

All three are grammar illustrations, correctly excluded.

## 5. Dead citations

**Under the gate's own contract there is exactly one dead live subject** (805 checked, 1 bad; the detail string names no second):

```
LOG.md:2111  `.ufo/round-45/drafts/v10/post-r44-hunt.py`
```

The full line (873 chars, reproduced verbatim; sha256 of the line = `7dcbf123313d46c469cab9f5dac2daa7567e54ac1ddf7cffdd1fd38c74200135`):

> - At `2026-10-19T19:38:15Z`, the census replay command `python3 .ufo/round-45/drafts/v10/post-r44-hunt.py` and its two documented R41 draft replay commands each exited 2 because the referenced runners are absent. The prefixed V10 evidence scripts and R45 result JSON exist; the R41/R45 draft paths listed in U1.md do not. The V10 documented gate set was rerun `2026-10-19T19:36:35Z–19:36:53Z` at the frozen comparator blob `git show HEAD:verifiers/compare_harness_independent.py` SHA-256 `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`: join exited 0 at protocol 24/24 (output SHA `60da2f224759ecdc6c7232941a3d5ee20f59b1097c6624eac5d063768ed3bbec`), self-test passed 255 assertions, floors passed exact `10/150/91/87/1597/62/104/255/150`, and both corpus gates exited 0. Evidence and command output SHAs are in U1.md; temporary HEAD snapshot was removed.

The line itself records the absence ("each exited 2 because the referenced runners are absent"), matching round-47 plan C3's premise. It is an **erratum candidate, not a fixable citation**: LOG.md is append-only, so the only honest closure is a pinned registry entry that asserts *absent at BASE* and fails if the path reappears.

**Second class, not counted by the gate:** 24 of the 805 live subjects are `../`-rooted and resolve only because the lane sits inside the fleet root. They are dead in any other location (see §7). 13 distinct tokens: `../AXES.md`, `../MISSION.md`, `../PROTOCOL.md`, `../SCORECARD.md`, `../.ufo`, `../.ufo/l0-questions.md`, `../.ufo/reports/round-9|11|16/kotoba.md`, `../.ufo/waves/shokunin12h-20261014-p1-repair/members/`, `../kasegi-shokunin/corpus/instruments/` (+`resolve.py`, `anchorcheck.py`). `../SCORECARD.md` is the **fleet** scorecard, not the lane's — a resolution the gate cannot distinguish.

**Third, outside the gate's file set:** the same dead runner is cited at `corpus/knowledge/harness-independent-round41-census.md:3` as a `recheck:` command. `GOVERNANCE_FILES` covers only LOG.md/SCORECARD.md, and `verifiers/verify_corpus_integrity.py:141-143` (`UFO_POINTER_RE`) matches only `.ufo/reports/round-\d+/*.md`, so this duplicate is ungated. `grep -ln 'recheck' verifiers/*.py` → exit 1 (no instrument reads `recheck:` lines), matching round-46 lesson M4 (`corpus/lessons/round-46.md:22`). That same corpus file already records the history at line 115: "the `recheck:` runner … was never committed (`git log … | wc -l` → 0)".

## 6. Did `.ufo/round-45/drafts/v10/post-r44-hunt.py` ever exist?

- `git log --all --format='%H' -- '.ufo/round-45/drafts/v10/post-r44-hunt.py' | wc -l` → **0**.
- `git rev-list --all --objects | grep 'post-r44-hunt'` → exactly one object, and it is not the script: `e06e3fd863baae47d6fe6c272aa3966500cf7d8b .ufo/round-45/evidence/v10-post-r44-hunt.json`.
- `.ufo` is **tracked and not ignored** — `git check-ignore -v` on the path → exit 1; `git ls-files .ufo | wc -l` → 9647; `git log --all -- .ufo | wc -l` → 53. So the zero is authoritative, not an ignore artifact.
- The only tracked entry under `.ufo/round-45/drafts*` is `bda9eed0044baab4df4986d1303b41dae2bf6e90 .ufo/round-45/drafts-report-skeleton.md`; there is no `drafts/v10/` in any tree.
- The script nonetheless ran once: LOG.md:1979 (in `50507ca5`) records runner SHA-256 `3a70d405eb147d7029abb3f76668da60f65ec99002c37eda383d11ad458add86` for an untracked draft, and `.ufo/round-45/scouts/V10.md` repeats it. Its output survives — `.ufo/round-45/evidence/v10-post-r44-hunt.json`, 256850 B, sha256 `b7cd1fbd4e0b94e578a5f7efa43690ee272bb535a0032b3561d8b66bc647a9be`. No `PRUNE.log` names the path.

History of the gate-visible form (calibration-critical):

- `50507ca5` and `36ab0d3`: citation is the **relative** `drafts/v10/post-r44-hunt.py` at line 1979 (not gate-visible; no `CITATION_ROOTS` prefix).
- `36ab0d3` (round-46 WIP) adds the `.ufo/`-rooted form in the U1 bullet: `git show 36ab0d3:LOG.md` line **2112**.
- `78ee57e5` (merge `origin/master`): same text, now line **2111**; `git diff --stat 36ab0d3 78ee57e -- LOG.md` = 8 insertions, 1 deletion (net −1 above the bullet). Every revision from `78ee57e` through BASE reports 2111 (checked `04192c2`, `f2f9ee1`, `78ee57e`).
- Eight committed round-46 receipts still say **2112** — e.g. `.ufo/round-46/evidence/g1/final5/checklist.json:58` — so the receipts and BASE disagree by one line.

## 7. Counterexamples a pinned erratum registry must survive

**(a) Line-key binding is already broken.** sha256 of the exact line text: BASE:2111 = `7dcbf123…0135`, 36ab0d3:2112 = `7dcbf123…0135` (equal), while 36ab0d3:2111 = `5e63e21478b59c197de68f5dfcb9746ffd3532884c5cea8e41e5f0778ebe47a0` (a different bullet). A registry transcribed from the round-46 receipts with `LOG.md:2112` binds to the R37 null-echo bullet at BASE (LOG.md:2112), not the dead citation.

**(b) The gate is location-dependent.** Cloned BASE to `/fast/scratch/kotoba-r47/C3GovCensus-9/lane` and ran the same read-only command: `governance.citation_resolves FAIL evaluated=805`, now with **25** dead subjects — the 1 true dead citation plus all 24 `../` subjects (`LOG.md:177,255,311,779,824×2,974,1203,1221`; `SCORECARD.md:3,5×2,15,31,34×4,100,123,133×2,144,240`). A registry listing only LOG.md:2111 would leave a red gate in every clone/CI. The integrator must either drop `../` from the governance scan (it is the only root that escapes the repo) or pin each with an explicit out-of-repo disposition.

**(c) Fail-closed needs an "absence still holds" assertion.** Prototype `C3GovCensus.registry-probe.py` (artifact) imports the production extractor and pins `(file, token, ordinal, line_sha256)`:
- lane, BASE: `live=805 dead=1 problems=0`, exit 0;
- relocated clone: exit 1 with 24 `UNREGISTERED` (the `../` class);
- created the cited path in the clone (a real file with the cited name): probe emits `STALE ERRATUM (path resolves again): LOG.md:2111 …` — a suppression-only registry would have stayed green;
- inserted one blank line above the bullet: the dead subject reports at line 2112, `pin/orphan problems: []`, same line hash — the pin survives drift;
- deleting the path again returns the clone to the 24-`../` baseline only.

**(d) The oracle cannot see line anchors or directories.** 0 live subjects carry `:N` (stripped), 62 resolve to directories. So "resolves" means "some path exists", not "the cited artifact/line exists".

**(e) Duplicate ungated claim.** See §5 third class: the corpus `recheck:` line is a second copy of the same dead path and no verifier reads it.

## 8. Artifacts written

- `.ufo/waves/round-47/build/C3GovCensus.md` (this report)
- `.ufo/waves/round-47/build/C3GovCensus.json` (100776 B: counts, all 805 live subjects with line/token/resolves, the 12 exclusions with resolution, dead list, 13 distinct parent-relative tokens)
- `.ufo/waves/round-47/build/C3GovCensus.registry-probe.py` (advice prototype; imports the production verifier from `--repo`, exits 0 iff every dead subject is pinned and no pin is stale)

No production file was modified; no lane gate other than the named read-only verifier was run; no tool was installed or upgraded.

## 9. What I did NOT check

- Did not run `verify_corpus_integrity.py`, `verify_corpus_independent.py`, `verify_harness_claims.py`, `verify_surfaces.py`, or `check_substrate_pins.py` (not this item; C3's corpus-index half belongs to another seat).
- Did not run the checklist `--self-test`; the extraction claims here come from the live run and a read-only import of the same module.
- Did not run any `jj` command (auto-snapshot would write `.jj` state in the lane); git history is the sole record used.
- Did not verify whether `3a70d405…` matches any surviving bytes — only that the hash is recorded in LOG.md:1979 and `.ufo/round-45/scouts/V10.md`.
- Did not audit the 805 live subjects semantically; the oracle is existence-only and was used as-is.
- Did not judge whether SCORECARD.md:118's absence sentence is meant as historical narrative; I report only that it is present-tense in the live `## planned` section and false at HEAD.
- Did not inspect fleet-level files behind the `../` tokens beyond their existence.
