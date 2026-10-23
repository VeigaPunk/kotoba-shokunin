# C2 redesign input — independent ground truth on real opencode files

Result: DONE — an independent, hand-labeled ground-truth set for the five generated agentdef boxes
now exists on real opencode files (8 agent files + roster config, 47 label rows in the TSV with line
evidence); the assigned source `~/.config/opencode/agents/*.md` does not exist on this host
(`ls`: `No such file or directory`), so the host's only real opencode agent set
(`opencodeufo/.opencode/agents/`) was substituted, and both the substitution and the assigned global
config are recorded below.

Scope note: C2 is withdrawn this round (erratum 1, `e02f5f5`). This file is a redesign input for a
later round only. No counter was run, no delegate exists or was written, and no lane file was edited.
Labels are hand readings of the frozen counter's docstring — "by READING (no instrument)" — with grep
used only to locate lines and to prove absence (whole-file absence is a superset of the box's scan
surface, so those absences are sound for the frontmatter/body scans).

## F0 — the assigned source path is absent (substitution, disclosed)

- `ls -la ~/.config/opencode/ ~/.config/opencode/agents/` (2026-10-23T02:46:39Z): `~/.config/opencode/`
  holds only `cli.json` (163 B), `opencode.json` (95 B), `service.json` (64 B);
  `ls -la ~/.config/opencode/agents/` → `No such file or directory`, exit 2 (re-verified);
  `ls ~/.config/opencode/agent/` (singular) → exit 2 as well.
- Host scan for real opencode agent sets (`find /home/vgpnk -maxdepth 6` over `.opencode`/`opencode`/
  `agent`/`agents` dirs, pruning `.cache`/`.git`/`node_modules`/…; plus `find /fast -maxdepth 4`, plus a
  deeper re-scan of `/home/vgpnk/Projects` at maxdepth 8): the re-scan returned only the four
  already-examined opencode dirs (`opencodeufo/.opencode`, `ufo-fsd-alpha/packages/opencode`,
  `ufo-fsd-alpha/substrates/opencode`, `xsnapshot/…/applied/opencode`), and exactly one of them holds
  agent definition files — `/home/vgpnk/Projects/opencodeufo/.opencode/agents/` (8 `.md` files) with
  `/home/vgpnk/Projects/opencodeufo/.opencode/opencode.jsonc` as its config.
- Substitution: that set is the ground-truth source. The assigned global `opencode.json` was also
  copied and is labeled as a vacuous roster artifact (F2). Out of scope but present on the host:
  `~/.config/devin/agents/*.md` (a different client, not opencode-shaped).

## F1 — the ground-truth set (provenance)

Local files, read-only; copied with `cp -p` into
`/fast/scratch/hyaku/kotoba-r56/C2RedesignTruth/`; copied sha256s equal the originals (same
`sha256sum` values run in both trees). Access time: `Fri 23 Oct 2026 02:49:34 AM UTC`.

| File (source) | Bytes | mtime | sha256 |
|---|---|---|---|
| `opencodeufo/.opencode/agents/architect.md` | 699 | 2026-10-11 13:43 | `79b831206e7ed38743365c6834f6f197f0332f6b05457a040fe352d215644494` |
| `…/agents/executor.md` | 886 | 2026-10-11 13:49 | `69f75825ae4dda00022ceb7f8b30a0014fa54acd469c6820dd38dde762767a85` |
| `…/agents/fallback.md` | 867 | 2026-10-11 14:32 | `0e79894b39bc2d3905a8a1c1d38941cf51770ded299624caf191b38a94257fa3` |
| `…/agents/porter.md` | 3313 | 2026-10-11 14:04 | `5363def488e2375466447d21f23d0fbe61d16333aaf7e7036009658edea81810` |
| `…/agents/reader.md` | 857 | 2026-10-11 13:43 | `791b1dbff4c2ddea8978ee4ea1d1bb3f6ec2c59a7fe236bcbef6e35e147d59d7` |
| `…/agents/reviewer.md` | 755 | 2026-10-11 13:43 | `cdbb043c7376e86034430bb3c689b0e0a3ab4b18ad559f78e92a400a56c54ff2` |
| `…/agents/scout-go.md` | 708 | 2026-10-11 14:32 | `37ec6fe5ebe0a3cc452c34c71c39705ee3c23b7c0b09aa2c81b587d7de5fd91b` |
| `…/agents/scout.md` | 653 | 2026-10-11 14:32 | `94137f7f1592caa16707bf7def9dded6609737d2f90be6f9b65617e64e5cd2e5` |
| `opencodeufo/.opencode/opencode.jsonc` | 141 | 2026-10-11 13:49 | `d21945bab279a0746de18ee278f23d7e9ff67dbfa9eb6359f46da734fd3b7876` |
| `~/.config/opencode/opencode.json` | 95 | 2026-10-12 08:39 | `fb067af039252d48ef5b5c573a5e12c17357af4324b218aca5efa36f882846dd` |

Case layout for a counter check (built at
`/fast/scratch/hyaku/kotoba-r56/C2RedesignTruth/case-opencodeufo/`):

    case-opencodeufo/agents/{architect,executor,fallback,porter,reader,reviewer,scout-go,scout}.md
    case-opencodeufo/opencode.jsonc          (the real config, byte-identical)

Harness mapping note: the counter's case shape expects `opencode.json`; the real artifact is
`opencode.jsonc`. Renaming it does not change any label (F2, .02): the enrolled set is empty either
way. JSONC trailing commas (lines 5-6) make strict `json.loads` fail, so a delegate that parses the
file must not crash.

## F2 — labels (hand readings of the frozen counter docstring)

Reading source: `verifiers/check_agentdef_boxes.py`, blob last changed at the freeze commit
`0f58a469`, sha256 `8aeb9bcf611decdba9e1027c435c3f268e5c51112706f43d76f284ae05aeb8fe` (matches the
plan's stated counter hash), worktree unmodified (`git status --porcelain -- <file>` and
`git diff --stat -- <file>` both empty). Box readings cited: docstring lines 68 (.01), 79 (.02), 93
(.05), 107 (.06), 117 (.07). Full per-file rows: `C2RedesignTruth.tsv` (48 lines, every row exactly
4 tab-separated fields; 40 file×box rows, 5 directory rows, 2 roster rows).

Directory verdicts for `case-opencodeufo/` (case dir = `opencodeufo/.opencode`):

| Box | Verdict | Basis (with line evidence) |
|---|---|---|
| agentdef.01 | **PASS** | No file declares `name:` (`grep -nE '^name:'` over all 8 files: no match, exit 1). Clause (i) n/a; clause (ii) needs *every* sibling to declare a name — none does. Frontmatter key lines: `architect/fallback/porter/reader/reviewer/scout-go/scout` = 2 `description`, 3 `mode`, 4 `model`, 5 `color`, 6 `steps`, 7 `permissions`; `executor` = 2-5 then 6 `permissions` (no `steps`). |
| agentdef.02 | **FAIL** | Enrolled set = keys of the top-level `agent` map; `opencode.jsonc:3` is `"agents": {` (plural) → enrolled `{}` → all 8 files are orphans. No `subagents:` roster anywhere (`grep -nE '^subagents:'`: no match, exit 1) → no reachability edge. FAIL is robust: under a lenient plural-key reading, enrolled `{explore, general}` (lines 4-5) intersects no file stem and still reaches none. |
| agentdef.05 | **PASS** | Frontmatter scan; whole-file greps over all 8 files for ISO date (`[0-9]{4}-[0-9]{2}-[0-9]{2}`), month-name date, `round` (case-insensitive), `PROPOSE round`: no match, exit 1 each. Model version numbers (`4.7`, `1.3`, `6.1`, `5.3`, `4.1` at line 4) are not dates. |
| agentdef.06 | **PASS** | Body scan; whole-file greps for `your current task`, round index, one-shot phrases: no match, exit 1 each. Bare `task` occurs in bodies at `executor.md:21` (twice), `fallback.md:21`, `porter.md:66` (inside a code span) — explicitly not a defect. `porter.md:60` contains the literal `<YYYY-MM-DD>`, not a digit date. |
| agentdef.07 | **PASS** | Paragraphs (from the blank-line map), all distinct within each body: architect 19,21; executor 12, 14-17, 19 (heading), 21; fallback 19,21; porter 37(h), 39, 41, 43-46, 48, 50-52, 54, 56(h), 58, 60, 62(h), 64, 66, 68; reader 25,27; reviewer 19,21; scout-go 19,21; scout 19,21. Heading lines: `executor.md:19`, `porter.md:37/56/62` — titles all distinct, so no same-name section conflict. |

The single FAIL line evidence (agentdef.02), identical for all 8 files: the file's stem is not a key
of the top-level `agent` map (`opencode.jsonc` has no `agent` key; line 3 is `"agents": {`), and no
reachable agent names it, because no file carries a `subagents:` roster.

Roster rows: `(roster) opencode.jsonc` → .02 FAIL (lines 1-7 as above; trailing commas at 5-6);
`(roster) ~/.config/opencode/opencode.json` → .02 PASS **vacuous** — its directory has no agent files
at all (`ls ~/.config/opencode/agents/` → No such file or directory), so all five boxes pass with
zero files; it must not be used as a discriminating case.

## F3 — calibration findings for the redesign

1. **Discrimination is one-sided.** A delegate that always answers PASS scores 4 of 5 boxes on this
   real set (all but .02). Real-file ground truth alone cannot separate "always PASS" from a correct
   instrument: the redesigned counter must keep generated FAIL cases, or the ground truth must gain
   real FAIL carriers.
2. **The .02 FAIL is robust** to the `agent`/`agents` key ambiguity, which makes it a good anchor
   label; every other box's real verdict is PASS.
3. **Real traps in the bytes** (each is a plausible shortcut worth a hard negative):
   - JSONC: trailing commas `opencode.jsonc:5-6` → strict `json.loads` raises; a delegate must not
     crash (any exit other than 0/1 makes the box not count).
   - Plural key `agents` vs the reading's `agent`.
   - Date-heuristic bait for .05: dotted version numbers in `model:` (`xai/grok-4.7`, `muse-spark-1.3`,
     `gpt-6.1-sol`, `glm-5.3-flash`, `deepseek-v4.1-flash`); and a literal `<YYYY-MM-DD>` token in
     `porter.md:60` (body, so also a scan-surface bait).
   - Cross-file duplicate bait for .07: `scout.md` and `scout-go.md` bodies are byte-identical; the
     rule is intra-body, so a cross-file duplicate detector false-fails.
   - Heading-as-paragraph: `executor.md:19` is a long `##` heading line inside an otherwise
     paragraph-only body.
   - Bare-`task` hard negative for .06 at three real body sites.
4. **Vacuity trap.** A config-only case directory (like `~/.config/opencode/`) has zero agent files →
   all five boxes PASS vacuously. It carries no discrimination and must never count as evidence.
5. **Coverage gap the redesign must fill.** The host has no real agent file that declares `name:`, no
   `subagents:` roster, no dated frontmatter, no one-shot text, and no duplicated paragraph — so the
   real set exercises no FAIL case for .01/.05/.06/.07 and no roster-edge PASS case for .02. Its value
   is PASS-side calibration, the .02 FAIL, and the traps above.

## F4 — reproduce (commands as run; exit codes)

    ls -la ~/.config/opencode/ ~/.config/opencode/agents/          # agents/: No such file or directory (exit 2)
    find /home/vgpnk -maxdepth 6 … -type d -name '.opencode' …     # exit 0; only opencodeufo/.opencode
    cp -p <sources> /fast/scratch/hyaku/kotoba-r56/C2RedesignTruth/src/ ; sha256sum …   # exit 0
    grep -nE '[0-9]{4}-[0-9]{2}-[0-9]{2}' *.md                    # no match, exit 1
    grep -niE '<month names>[ -]+[0-9]|[0-9]+[ -]+<month names>' *.md   # no match, exit 1
    grep -niE 'round' *.md                                         # no match, exit 1
    grep -ni 'propose round' *.md                                  # no match, exit 1
    grep -ni 'your current task' *.md                              # no match, exit 1
    grep -niE 'one-shot|once only|only this once|for this task only|this time only|just this once' *.md  # no match, exit 1
    grep -nE '^name:|^subagents:' *.md                             # no match, exit 1
    grep -n -E '^---$' *.md ; grep -n -E '^#{1,6} ' *.md ; grep -n -E '^$' *.md   # fence, heading, blank-line maps
    awk -F'\t' '{print NF}' C2RedesignTruth.tsv | sort | uniq -c   # 48 lines, all NF=4

## F5 — unknowns and notes

- Whether opencode 1.19.4 actually consumes `opencode.jsonc`'s `agents` key was not checked (no client
  run; out of scope for the counter's reading).
- Host scan bounds: `/home/vgpnk` maxdepth 6 with heavy dirs pruned, `/fast` maxdepth 4; other mounts
  were not scanned, so a second real opencode set could exist elsewhere.
- The two control receipts (`CtlC2Heuristics`, `CtlC2GeneratorKeyed`) were not re-read or re-derived
  here; this file adds no evidence about them.
- No tool was installed or upgraded (nothing needed). No lane file was written or modified; outputs
  are this report, `C2RedesignTruth.tsv`, and scratch copies under
  `/fast/scratch/hyaku/kotoba-r56/C2RedesignTruth/`. No lane code was executed, so no sandbox clone
  was made and no sandbox commit exists.

Report: .ufo/waves/round-56/build/C2RedesignTruth.md
