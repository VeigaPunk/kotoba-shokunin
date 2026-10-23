Result: HOLDS — all three named statements verified verbatim on the re-opened pages at `46b4a706`; two low-severity findings (citation placement for the same-name rule, rejection-mechanism brittleness) and one imprecision note, no content defect.

Seat: ReopenS028Copilot. Attacked `SKILL.md:116` (Copilot CLI row) and `corpus/knowledge/command-files-round58.md:18-21` (entry sentence) at `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe`. Text at the revision is byte-identical to the worktree for both files (`git show 46b4a706:<file>` grep, 2026-10-23T08:30Z). Fetched bytes in `/fast/scratch/hyaku/kotoba-r58/ReopenS028Copilot/`; read-only in lane.

## Fetch receipts

| URL | `date -u` batch | HTTP | bytes | sha256 |
|---|---|---:|---:|---|
| `https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference.md` (S028) | `Fri 23 Oct 2026 08:27:03 AM UTC` | 200 | 47,200 | `d0d362cc5aa2ef84775145e499596c7e6529531c7b29972ae29f547b5da220d0` |
| `https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md` (S031 page) | same | 200 | 461,944 | `c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9` |
| `https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference.md` | same | 200 | 166,811 | `8be36090c19a7e284d4137f03db150927f3f215fb3b21ddfc9d87c614bec21b0` |
| `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills.md` | `Fri 23 Oct 2026 08:29:32 AM UTC` | 200 | 10,057 | `989af4981773349a74feaebfe98cdac9895b394707d201545ba55c8f9f4131a0` |
| `https://raw.githubusercontent.com/github/copilot-cli/main/changelog.md` (corroboration only) | same | 200 | 289,859 | `c4b793bd6555bf699c1f6ef61fb9052e6400df8f475c97fdae25ba5084531dfb` |

Every hash matches the recorded build/census receipt byte-for-byte (SrcCopilotCLI, CensusCopilotCLI).

## Verdict per named statement

**1. The quote at `:456` — HOLDS, byte-exact.**
`cli-plugin-reference.md:456` (line 456 of the fetched 47,200-byte body) is a diagram divider inside the
"Loading order and precedence" code fence:

```
456:  │  --- then commands (.claude/commands/), skills override commands ---│
```

`then commands (.claude/commands/), skills override commands` is a contiguous substring; no bytes stripped,
10 whitespace-separated words. The diagram's `AGENT SKILLS` box (`:447-455`) lists skill locations; the divider
then routes to commands. The SKILL.md cell's `(S028 `:456`)` citation is accurate.

**2. "no own folder: it loads Claude Code's .claude/commands/" — HOLDS, qualified.**
The only user-facing command-file location on either reference page is `.claude/commands/` — Claude Code's
folder, named as a "Claude-compatible" pattern in the skills table's idiom:
- `cli-command-reference.md:1334`: "Commands are an alternative to skills stored as individual `.md` files in `.claude/commands/`." (Only `.claude/commands` hit in the 461,944-byte file; grep for `copilot/commands|copilot/prompts|github/prompts|github/commands`: none.)
- `cli-plugin-reference.md`: the same path appears only inside the diagram `:456`.
- `cli-config-dir-reference.md:13-35`: the `~/.copilot` top-level table lists `agents/`, `skills/`, `instructions/`, `hooks/`, `extensions/` etc.; zero `commands/` or `prompts/` substring in the whole 166,811-byte file.
- `cli-plugin-reference.md:159` does name `com.github.copilot/commands/` — but `:152` ("Agent Plugins 1.0 does not define portable … commands"), `:154` and `:164` scope it to plugin packages only. Legacy plugins name arbitrary command paths via the `commands` manifest field (`:213`). The entry discloses this honestly: "a CLI plugin's `com.github.copilot/commands/` namespace is a plugin path, not a user folder" (entry `:20-21`).
- Changelog `:2932` (0.0.399): "Support `.claude/commands/` single-file commands as simpler alternative to skills" — same single folder.
- Web search (2026-10-23): no documented Copilot-named command folder; a machine-level `~/.copilot/commands/` exists only as open feature request `github/copilot-cli#3343`. `.github/prompts/` is VS Code IDE prompt files, never CLI commands.

So "no own folder" is a true negative *as qualified by the row's next clause*: the CLI reads only a
foreign-marked folder plus plugin-internal paths, not a Copilot-named user folder.

**3. "a same-named skill wins" — HOLDS in content; citation imprecise (see F1).**
`cli-command-reference.md:1334` ends: "Commands have lower priority than skills with the same name." The
same-name keying is stated by the command reference, i.e. the S031 page already in SOURCES. The S028 diagram
line says only "skills override commands" with no same-name key — the unconditional phrasing is consistent
(`:1302` notes commands use tier-based dedup internally, but commands live in one folder, so the skill-vs-command
rule is effectively name-keyed). A same-named skill wins on both pages.

## Findings

**F1 (low): the same-name rule is cited to the unkeyed line.**
`SKILL.md:116` attaches the same-name claim to `(S028 `:456`)`, whose words carry no key ("skills override
commands"). The entry's Limits line does the same: "precedence between a command and a same-named skill is
recorded only where a page states it (Copilot CLI, S028 `:456`)" — the keyed statement is
`cli-command-reference.md:1334`, on the S031 page. The claim is true and corpus-backed, so this is a
citation-precision defect, not a content error. L1 correction: cite `S031 :1334` (or "S028 `:456`, keyed
at S031 `:1334`") for the same-name clause; S028 `:456` stays correct for "skills override commands" and for
the folder path in the diagram.

**F2 (low): the row's counter-rejection runs on a citation token, not on "no folder".**
`judge` takes the first backticked span of the Command files cell as the token
(`check_command_files.py:764-765`). The integrated cell's first backticked span is `:456` — the citation —
which fails `TOKEN_RE` (colon), so the row is rejected with "command token ':456' is not well-formed"
(C1-measure.txt:9). The outcome is correct and the counter is frozen and unattackable, but the mechanism
diverges from the build draft's stated intent ("deliberately contains no backticked span",
SrcCopilotCLI.md:9): the cell is excluded because a *citation* happens to be backticked. Any future edit
that moved the citation out of backticks and backticked `.claude/commands/` would flip the row into the
shared-token/foreign-marker path (rejecting both this row and Claude Code's via E5, F→5, predicate still
0) — worth recording only as adjacency knowledge for later rounds; no change needed at `46b4a706`.

**F3 (note): "What a file sets — as Claude Code" overstates format parity.**
Copilot CLI documents a *simplified* subset: "`argument-hint`, `description`, `allowed-tools`,
`disable-model-invocation`", no `name` field (`cli-command-reference.md:1334`). Claude Code's fuller
surface (named `arguments` for `$name`, etc., S089) is not documented for the CLI. "as Claude Code" is a
fair pointer for a table cell but drops the documented subset boundary; the README's "argument-substitution
behaviour … still not held" (`corpus/README.md:171`) already discloses the unverified residue. Optional
tightening: "Claude Code's format, simplified subset (four fields documented)".

## Adjacency checked, clean

- Entry line 18-20 phrasing "its plugin reference loads Claude Code's folder" — metonymy, accurate: the
  path is printed on the plugin reference (`:456`) and the store is documented on the command reference
  (`:1334`).
- `corpus/README.md:170` index sentence ("loads Claude Code's `.claude/commands/` and lets skills override
  commands") — matches both pages.
- Lesson Gate re-open row (`corpus/lessons/round-58.md:38-40`) — hash, size and quote all match this seat's
  fetch.
- S028 row's other anchors verified in the same fetch: `:195` ("Brief description. Max 1024 chars."),
  `:349` ("Plugin description. Max 1024 chars."), `:411-421` (loading order and precedence prose —
  agents/skills first-found-wins, MCP last-wins).
- Row-rule scope: the row records the folder the client's own page names for user-written command files;
  the plugin namespace and legacy manifest field are plugin-package surfaces, correctly excluded and
  disclosed, not silently dropped.

## Residual risk

- No client run (declared in the entry, `:13`); runtime precedence between a command and a same-named
  skill is doc-attested only. Feature request `github/copilot-cli#3343` indicates user-level command
  folders are absent today but desired — recheck on the S028 `90d` cadence stands.
- "Not silent" sweep for this item covers the two reference pages, config-dir reference, add-skills page,
  changelog, web search, and lane corpus. The full `github/docs` repository source tree was not cloned;
  a docs-repo file that never ships to the site could in principle exist [INFERENCE — considered low-risk:
  the served site is the surface the row cites].
- `:456` is inside a fenced ASCII diagram, so the quote's meaning depends on diagram position (it sits
  under the AGENT SKILLS box); the plain-text line alone does not name the same-name key (F1).

No tools installed or upgraded; nothing needed beyond curl/sha256sum/grep. No lane code executed; no git
writes. Report file only: `.ufo/waves/round-58/falsify/ReopenS028Copilot.md`.
