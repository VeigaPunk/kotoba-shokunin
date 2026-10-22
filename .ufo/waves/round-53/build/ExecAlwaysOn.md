Result: DONE — C2 implementation and patch are packaged for L1 integration; post-integration gates remain unrun.

## Files changed

Patch: `.ufo/waves/round-53/build/ExecAlwaysOn.patch` (generated from base `3bb0a7a33e6eb585a83a1a55dee30b26079b1e36`).

Implementation files:
- `verifiers/verify_alwayson.py`
- `verifiers/checklist-baseline.json` — only `alwayson.04` and `alwayson.07` now delegate to `verifiers/verify_alwayson.py`; their pinned text hashes are unchanged.
- `verifiers/verify_skill_checklist.py` — rejects absolute delegate paths as outside the map repository, documents that rule, and adds one self-test arm.

Fixture files under `verifiers/fixtures/alwayson/`:
- `manifest.json`
- `a04-plain-rules/AGENTS.md`
- `a04-version-number/AGENTS.md`
- `a04-iso-date/AGENTS.md`
- `a04-iso-timestamp/AGENTS.md`
- `a04-month-day/AGENTS.md`
- `a04-dated-claude-md/CLAUDE.md`
- `a04-fenced-date/AGENTS.md`
- `a04-dotted-version/AGENTS.md`
- `a04-abbreviated-month-day/AGENTS.md`
- `a04-gemini-out-of-scope/AGENTS.md`, `a04-gemini-out-of-scope/GEMINI.md`
- `a04-size-control/AGENTS.md`
- `a04-outside-link/outside.md`, `a04-outside-link/target/AGENTS.md` (symlink to `../outside.md`)
- `a04-date-free-transient/AGENTS.md`
- `a07-agents-only/AGENTS.md`
- `a07-claude-only/CLAUDE.md`
- `a07-import-redirect/AGENTS.md`, `a07-import-redirect/CLAUDE.md`
- `a07-symlink-redirect/AGENTS.md`, `a07-symlink-redirect/CLAUDE.md` (symlink to `AGENTS.md`)
- `a07-two-rule-files/AGENTS.md`, `a07-two-rule-files/CLAUDE.md`
- `a07-prose-mention/AGENTS.md`, `a07-prose-mention/CLAUDE.md`
- `a07-nested-claude-only/.claude/CLAUDE.md`
- `a07-nested-pair/.claude/AGENTS.md`, `a07-nested-pair/.claude/CLAUDE.md`
- `a07-gemini-ignored/AGENTS.md`, `a07-gemini-ignored/GEMINI.md`
- `a07-local-conflict/AGENTS.md`, `a07-local-conflict/CLAUDE.local.md`
- `a07-nested-claude-conflict/AGENTS.md`, `a07-nested-claude-conflict/.claude/CLAUDE.md`
- `a07-wrong-symlink-target/AGENTS.md`, `a07-wrong-symlink-target/OTHER.md`, `a07-wrong-symlink-target/CLAUDE.md` (symlink to `OTHER.md`)
- `a07-fenced-import-mention/AGENTS.md`, `a07-fenced-import-mention/CLAUDE.md`
- `a07-inline-import-mention/AGENTS.md`, `a07-inline-import-mention/CLAUDE.md`
- `a07-claude-local-companion/CLAUDE.md`, `a07-claude-local-companion/CLAUDE.local.md`

No counter, `verifiers/floors-registry.json`, or `verifiers/check_assertion_floors.py` was changed. No local commit was made; this seat only delivers the patch.

## Behavior and evidence

- `verifiers/verify_alwayson.py:4-8` documents the CLI/output/exit contract. The date check scans the selected files as text, including fenced examples; recognizes ISO dates/timestamps, month-day strings, and the documented date-free cues; and does not classify dotted version strings as dates (`:76-98`). It bounds each selected file to 1 MiB and safely opens in-target paths without following escaping symlinks (`:113-261`).
- For canonicality, the selected names are `AGENTS.md`, `CLAUDE.md`, `CLAUDE.local.md`, `.claude/AGENTS.md`, and `.claude/CLAUDE.md` (`verify_alwayson.py:10-22,65-74`). `CLAUDE.local.md` counts as a CLAUDE-class source when AGENTS.md coexists, but is not an accepted redirect. Only a sibling `CLAUDE.md` symlink to `AGENTS.md`, or an exact import line outside inline/fenced code, redirects (`:292-377`). The fixtures include prose, inline-code, and fenced-code false redirects; a symlink to a different file; and both `.claude/CLAUDE.md` and `CLAUDE.local.md` conflicts.
- Source basis was reopened from `https://code.claude.com/docs/en/memory.md`: fetched 2026-10-22T20:16:31Z, HTTP 200, 51,971 bytes, SHA-256 `971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff`. At line 112 it says, “Import parsing skips Markdown code spans and fenced code blocks.” At line 442 it describes putting an `@AGENTS.md` import in a `CLAUDE.md` next to it; lines 452-455 show the sibling symlink form. Lines 61-64 name `./CLAUDE.md`, `./.claude/CLAUDE.md`, and `./CLAUDE.local.md`; lines 370-375 name the CLAUDE-class files and both `AGENTS.md` and `.claude/AGENTS.md`. These source quotes are each under 25 words.
- The documented exclusions are explicit in the instrument docstring (`verify_alwayson.py:24-35`): it does not recurse beyond those fixed paths, inspect `.claude/rules/`, `.agents/`, `AGENTS.local.md`, `AGENTS.override.md`, `GEMINI.md`, other clients, ancestor/global/managed instructions, or settings. It does not infer semantic transience unless one of its lexical cues is present. No network is used.
- `verifiers/fixtures/alwayson/manifest.json:1-31` and the constant expectations at `verify_alwayson.py:402-431` cover all 12 frozen counter cases plus 16 additional cases. The additions include a date in a fenced example, dotted version control, abbreviated month-day, a date-free transient cue, an over-limit read arm, an escaping symlink, and import/source-selection boundaries. The self-test has 28 cases and 89 assertion calls by static count (4 corpus/direction checks, 3 per case, and 1 size-bound arm); it was not run, so no after-tally or green result is claimed. There was no `verify_alwayson.py` self-test at base, so no before-tally exists.
- `checklist-baseline.json:223-244` delegates only the two requested boxes. `verify_skill_checklist.py:1244-1248` rejects absolute paths and `..` escapes; `:2464-2469` adds the absolute-path failure arm. `floors-registry.json:5-7` still records the prior checklist floor of 1851. The added `rec` call makes the expected checklist self-test count 1852 [INFERENCE]; the self-test was not run and the floor file was intentionally left for L1. The existing generic delegate-proof path is retained.

### Live host observation only

Final observation command ran the new instrument against these discovered target directories; this is not a claim or a test result:

| target | box | observed status | exit | detail |
|---|---|---:|---:|---|
| `/home/vgpnk/.agents` | alwayson.04 | FAIL | 1 | `AGENTS.md:1` matched ISO date `2026-10-19` |
| `/home/vgpnk/.agents` | alwayson.07 | PASS | 0 | 1 selected file; no independent AGENTS/CLAUDE pair |
| `/home/vgpnk/Projects/shokunin` | alwayson.04 | PASS | 0 | no recognized date/transient cue in 1 selected file |
| `/home/vgpnk/Projects/shokunin` | alwayson.07 | PASS | 0 | 1 selected file; no independent pair |
| `/home/vgpnk/Projects/ufo-fsd-alpha` | alwayson.04 | FAIL | 1 | dates at lines 87, 139 (`2026-09-20`) and 268 (`2026-09-21`) |
| `/home/vgpnk/Projects/ufo-fsd-alpha` | alwayson.07 | PASS | 0 | 1 selected file; no independent pair |
| `/home/vgpnk/Projects/kimi-code` | alwayson.04 | PASS | 0 | no recognized date/transient cue in 2 selected files |
| `/home/vgpnk/Projects/kimi-code` | alwayson.07 | PASS | 0 | 2 selected files; no independent pair |
| `/home/vgpnk/Projects/opencodeufo` | alwayson.04 | PASS | 0 | no recognized date/transient cue in 1 selected file |
| `/home/vgpnk/Projects/opencodeufo` | alwayson.07 | PASS | 0 | 1 selected file; no independent pair |

The requested `/home/vgpnk/.claude/CLAUDE.md` was not found. The observation loop's shell exit was 0; each per-box exit is shown above. It was run twice, with the same results.

## Checks, risks, and blockers

No self-tests, checklist gate, frozen counter, assertion-floor check, build, lint, or formatter was run during this build wave. In particular, `python3 -B verifiers/check_alwayson_boxes.py --rev HEAD`, `python3 -B verifiers/verify_skill_checklist.py --json`, `python3 -B verifiers/verify_alwayson.py --self-test`, `python3 -B verifiers/verify_alwayson.py --box-proof`, and `python3 -B verifiers/verify_skill_checklist.py --self-test` remain unrun for the parent post-integration gate. No local commit was made, so the `--rev HEAD` acceptance measurement is pending L1 integration. LSP was unavailable in the supplied tool inventory. No tools were installed.

Risks are limited to the declared lexical approximation and the selected Claude Code file scope; other transient phrasing and other clients' files are deliberately not checked. The host results above are observations only.

A few fixture writes were initially directed to alternate scratch paths by mistake; those files were removed. The cleanup command that used `rmdir -p` exited 1 only at the nonempty `/fast/scratch/hyaku` ancestor, after removing the empty descendant path. A separate unused fixture scaffold in the clone was removed before packaging. These temporary artifacts are not in the patch.

## Shell commands and exit codes

- Sandbox setup: `unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r53/ExecAlwaysOn && git -C /fast/scratch/hyaku/kotoba-r53/ExecAlwaysOn checkout -q 3bb0a7a33e6eb585a83a1a55dee30b26079b1e36` — exit 0.
- First source-fetch attempt to a not-yet-created fixture directory — exit 23; curl reported HTTP 200 and 0 bytes written.
- `mkdir -p /fast/scratch/hyaku/kotoba-r53/ExecAlwaysOn/.scratch && curl -L -sS https://code.claude.com/docs/en/memory.md -o /fast/scratch/hyaku/kotoba-r53/ExecAlwaysOn/.scratch/claude-memory.md -w 'HTTP %{http_code}\nbytes %{size_download}\n' && sha256sum /fast/scratch/hyaku/kotoba-r53/ExecAlwaysOn/.scratch/claude-memory.md` — exit 0; HTTP 200, 51,971 bytes, hash above.
- Fixture-directory `mkdir -p` setup (two calls) — exit 0 each.
- Removal of the first misplaced file and the two alternate-scratch fixture batches — exit 0 for the direct `rm`, and exit 0 for the batch cleanup.
- Creation of the three symlinks under the clone — exit 0.
- `rmdir -p /fast/scratch/hyaku/Projects/shokunin/kotoba-shokunin/verifiers/fixtures/alwayson/a07-prose-mention && rm -f /fast/scratch/hyaku/kotoba-r53/ExecAlwaysOn/verifiers/fixtures/alwayson/a07-outside-link/outside.md && rmdir /fast/scratch/hyaku/kotoba-r53/ExecAlwaysOn/verifiers/fixtures/alwayson/a07-outside-link/target /fast/scratch/hyaku/kotoba-r53/ExecAlwaysOn/verifiers/fixtures/alwayson/a07-outside-link` — exit 1 at the nonempty `/fast/scratch/hyaku` ancestor; the `&&` cleanup after it did not run.
- `rm -f /fast/scratch/hyaku/kotoba-r53/ExecAlwaysOn/verifiers/fixtures/alwayson/a07-outside-link/outside.md && rmdir /fast/scratch/hyaku/kotoba-r53/ExecAlwaysOn/verifiers/fixtures/alwayson/a07-outside-link/target /fast/scratch/hyaku/kotoba-r53/ExecAlwaysOn/verifiers/fixtures/alwayson/a07-outside-link` — exit 0.
- Final source metadata fetch: `printf 'fetched_at='; date -u +%Y-%m-%dT%H:%M:%SZ; curl -L -sS https://code.claude.com/docs/en/memory.md -o /fast/scratch/hyaku/kotoba-r53/ExecAlwaysOn/.scratch/claude-memory.md -w 'HTTP %{http_code}\nbytes %{size_download}\n' && sha256sum /fast/scratch/hyaku/kotoba-r53/ExecAlwaysOn/.scratch/claude-memory.md` — exit 0, fetched at `2026-10-22T20:16:31Z`.
- Removal of fetched source scratch file/directory — exit 0.
- Live observation loop (`python3 -B ... --check ... --target ... --json`) — run twice; shell exit 0 each time; per-box results above.
- Required packaging command, `git -C /fast/scratch/hyaku/kotoba-r53/ExecAlwaysOn add -A && git -C /fast/scratch/hyaku/kotoba-r53/ExecAlwaysOn diff --cached --binary 3bb0a7a33e6eb585a83a1a55dee30b26079b1e36 > /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-53/build/ExecAlwaysOn.patch` — exit 0.
