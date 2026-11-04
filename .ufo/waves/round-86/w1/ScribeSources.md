# ScribeSources — round 86 w1 report

## Behavior
- Opened S255: the omp 18.15.0 TypeScript embedded in `/home/vgpnk/.local/bin/omp` (sha256 `6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f`, 276785328 B, `omp --version` → `omp/18.15.0`). I read it with python mmap + re and copied nothing out of the binary.
  - Module headers found: `extensibility/skill-descriptions.ts` at 178767936; `extensibility/skills.ts` at 177495678; `discovery/helpers.ts` at 172784226; the minified directory loader `async function Ba(e, t) {` at 172790245. Further headers: `discovery/builtin.ts` at 173814223, `claude.ts` at 173837493, `agents.ts` at 173864077, `codex.ts` at 173878972, `extensibility/settings.ts` at 172759165.
  - Located quote (11 tokens) at 178770368: "const c = o >= E ? r.slice(0, o).trimEnd() : r;"
- Upstream repository: the ELF holds the string `github.com/can1357/oh-my-pi`. `curl -sI` returned 200 for the repo, for `releases/tag/v18.15.0`, and for the blob and raw URLs of `skill-descriptions.ts` and `discovery/builtin.ts` at v18.15.0.
  - The raw file is 16687 B, sha256 `7321adfc…`. It has `MAX_PREVIEW_CHARS = 100`, `MIN_PREVIEW_CUT = 40`, `MAX_COMPRESSED_CHARS = 160` and `MAX_COMPRESSED_WORDS = 12`, and the same sentence regex as the bundle. I do not claim byte identity.
- `corpus/SOURCES.md`: added one row, S255, at line 196 (11 cells, LF only). `git diff --numstat` shows `1 0`.
- `corpus/README.md`, § Coverage map: added rows for `knowledge/omp-catalogue-model-round86.md` and `lessons/round-86.md`.
- `corpus/README.md`, § Frontier: appended a Round-86 note on *Loader-rule freshness* below the Round-81 note. It names the counter command and does not rewrite any earlier note. `git diff --numstat` shows `4 0`.

## Gates
- `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`:
  - Final result: **exit 0, 33 W04, 0 E**. That is the same as the round-start count of 33 W04.
  - The first run, before ExecModel and ScribeEntry had written their files, failed with exit 1 and two `E11 S255 missing used-by` rows. Those rows cleared once the files existed.
- `verify_corpus_integrity.py --json` exits 1 both before and after my edits. The `corpus.index.*` values:

  | check | before | after |
  |---|---|---|
  | `tracked_files` | 167 vs 166, DRIFT (pre-existing) | 167 vs 166, DRIFT |
  | `unindexed` | 1, DRIFT: `corpus/lessons/round-85-verifier-spotcheck.md` (pre-existing, not in my item) | 1, DRIFT (unchanged) |
  | `stale_patterns` | 0 | 2, DRIFT: README lines 172 and 173 |
  | `missing_paths` | 0 | 0 |

  `stale_patterns` reads 2 because the two new files exist on disk but are not tracked yet. It should return to 0 once the L1 commits them (my inference; not run after a commit).
- ExecModel's `CANDIDATE_READY` file reports scratch commit 903bd78e, `omp catalogue lines reproduced 215 of 215`, G1–G4 PASS, exit 0. I quote this from its file; I did not rerun it.

## Touched surfaces
`corpus/SOURCES.md`, `corpus/README.md`, and `.ufo/waves/round-86/w1/ScribeSources/{fetch-record.txt,row.md,census.txt,integrity-index.txt}`, plus this report.

## Out of scope / findings
- F1: `corpus/lessons/round-85-verifier-spotcheck.md` has no index row. This red was there before the round; I left it for the L1.
- F2: S255 has `recheck` set to `on-release`. Every other row's recheck value is a duration such as `90d`. The census accepted it with no warning.
- F3: inside the ELF, `loadSkills` and `loadSkillsFromDir` appear only as strings, because the bundle is minified. The function bodies are minified symbols (`Ba` is the directory loader), so the row's anchor cites byte offsets, not function names.

## Tooling
No tools installed or upgraded. The scratch directory `/fast/scratch/hyaku/kotoba-r86/ScribeSources` has been deleted.
