ROW | souji | master (detached HEAD at the same commit) | 4edb25dfe262515d0da63224bbba71e02e36cba5 | SKILL.md | none | no | yes (generic integrator clause, no sibling named in it; kagi-shokunin appears only as an anti-trigger) | PROVINCE.md:3-4 | "**Domain:** fleet repository & workspace hygiene (掃除) — receipt-gated removal of stale, duplicate, and already-preserved artifacts."

# souji-shokunin — C1 adjacency finding

Classification: `none`. Souji cleans repositories; it never writes or audits another
lane's SKILL.md, prompt or AGENTS.md craft. Its only SKILL.md reader parses registry
citations in its own lane, and it refuses live lane work outright.

## 1. Pin

- `git -C /home/vgpnk/Projects/shokunin/souji-shokunin rev-parse master` -> exit 0,
  `4edb25dfe262515d0da63224bbba71e02e36cba5` (2026-10-21 18:56:48 -0300,
  "round-22 verifier spot-check: strict proof unproven, forward policy boundary held").
- `git -C ... symbolic-ref -q HEAD` -> exit 1, no output: HEAD is detached.
  `git -C ... rev-parse --abbrev-ref HEAD` -> `HEAD`.
  `git -C ... rev-parse HEAD` -> the same 4edb25d commit, so the checked-out state and
  `master` agree; all reads below use the explicit 40-hex, never `HEAD`.
- Top level at that commit: 17 entries
  (`git -C ... ls-tree --name-only 4edb25d | wc -l` = 17): `AGENTS.md LOG.md MINT.md
  PROVINCE.md SCORECARD.md SHONEN.md SKILL.md census corpus results tests tools .ufo
  .scratch .ufo-reports-placeholder err4.nl2 err4.z2`.
- Skill file: `git -C ... ls-tree -r --name-only 4edb25d | grep -E '^(skills?/[^/]+/)?SKILL\.md$'`
  -> exit 0, one line: `SKILL.md` (top level; no `skills/<name>/SKILL.md` tree).
- Sizes at the commit: SKILL.md 390 lines / 54881 B, PROVINCE.md 172 / 10088,
  AGENTS.md 20 / 1211, MINT.md 64 / 3540 (646 lines, 69720 B total).

## 2. Frontmatter and PROVINCE content

- SKILL.md frontmatter is `name`-less; only a `description:` key on line 2. Domain
  sentence: "Fleet repo & workspace hygiene (掃除)." Triggers are deletion words
  (`clean`, `prune`, `sweep`, `stale artifacts`, `dead worktrees`, `duplicate config`,
  `scratch bloat`, `quarantine`, `hygiene census`, `obsidian ledger`, `can I delete
  this`). Anti-triggers: git history rewrite, credentials, operator config, live or
  unpushed lane work, publishing.
- Arbitration sentence, verbatim from SKILL.md:2: "Sibling arbitration: contested
  artifact ownership is reported to the integrator, never silently absorbed." It names
  no sibling; the only sibling named anywhere in the description is `kagi-shokunin`,
  and only as an anti-trigger ("kagi-shokunin owns credential hygiene").
- PROVINCE.md `## Owns`: fleet-root hygiene surfaces, per-lane `.scratch/`, dead
  worktree metadata, duplicate configs, stale generated output, the Obsidian ledger,
  dry-run censuses. `## Refuses` includes `- Live lane work products (current-round
  drafts, uncommitted reports).` (PROVINCE.md:42). `## Adjacency` names mori,
  tsukuroi, kagi; `## Core / Frontier / Adjacent` adds kumitate, chousa.
- PROVINCE.md does not name kotoba: `git -C ... show 4edb25d:PROVINCE.md | grep -ci
  kotoba` -> 0, exit 1.

## 3. Sweep (Q14) — the classification evidence

Pinned province-bearing files = the lane's four province documents at 4edb25d
(SKILL.md, PROVINCE.md, AGENTS.md, MINT.md; 646 lines / 69720 B):

```
for f in SKILL.md PROVINCE.md AGENTS.md MINT.md; do
  git -C /home/vgpnk/Projects/shokunin/souji-shokunin show 4edb25d:$f; done \
| grep -cE 'SKILL\.md|prompt|AGENTS\.md|frontmatter|trigger|description|kotoba'
```
-> 2 (exit 0). Both hits are self-referential, neither is a claim on kotoba's ground:

| hit | text | what it is |
|---|---|---|
| SKILL.md:2 | `Triggers: 'clean', 'prune', ...` inside its own `description:` | matched by `trigger`/`description`; its own frontmatter |
| MINT.md:16 | "`launch-*.json` checkpoint files, round prompts, `prior-owners.json`," | matched by `prompt`; a demand instance counting fleet-root bloat that souji removed |

Per-pattern counts over the same four files (same pipeline, `grep -cE` per pattern):
`SKILL\.md` = 0, `AGENTS\.md` = 0, `frontmatter` = 0, `prompt` = 1, `trigger` = 1,
`description` = 1, `kotoba` = 0. So souji states no rule about SKILL.md anatomy,
frontmatter shape, AGENTS.md class, or prompt wording.

Case-insensitive `kotoba` per file at 4edb25d, each `grep -ci`, exit 1 on zero:
SKILL.md 0, PROVINCE.md 0, AGENTS.md 0, MINT.md 0.
Whole tree: `git -C ... grep -l -I -i kotoba 4edb25d | wc -l` = 139 files, 354
occurrences (`grep -o ... | wc -l`); all are hygiene census rows, seat transcripts,
wave reports and `tests/vault/fixture-src-*` path listings. Province-bearing files
among those hits: 0 (`... | grep -cE ':(SKILL|PROVINCE|AGENTS|MINT)\.md$'` = 0).

## 4. The two near-boundaries, and why neither is overlap

1. `tools/souji-landing-gate.py` reads a lane's SKILL.md at a revision and reports
   `LG-MISSING-REG` when a registry-cited path is absent (source line 1033-1043). It
   is pointer integrity, not craft — its own header at lines 16-19: "Scope:
   landing-claim consistency, failure-channel carry, and cited-path integrity. It is
   NOT a disclosure-enforcement or behavioral-regression suite". Every recorded
   invocation passes `--root /home/vgpnk/Projects/shokunin/souji-shokunin`
   (`git grep -n 'souji-landing-gate\.py --root'`, 16 hits, all own lane); PROVINCE.md
   (round 13, lines 95-97) limits evidence-integrity checking to "souji's own
   receipt/certification fragments".
2. Fleet-root round-prompt deletion (MINT demand 1) is artifact lifecycle after push,
   receipt-gated, and `## Refuses` bars live lane work and operator-owned surfaces. It
   does not reach kotoba's workbook: prompt wording and skill anatomy stay untouched.

Kotoba's own dispatch boundary is already recorded against kumitate ("kotoba owns the
prompt wording, not the runtime", PROVINCE.md Adjacent). Souji is neither the runtime
nor a wording surface.

## 5. Row guidance for the census entry / PROVINCE Adjacent

Suggested PROVINCE § Adjacent wording: "souji — fleet/workspace hygiene and
receipt-gated deletion; no craft overlap, it audits no sibling's SKILL.md, prompt or
AGENTS.md wording and refuses live lane work (its landing gate parses SKILL.md
registry citations in its own lane only)." The row carries description-names-kotoba=no
and an arbitration clause that is generic, so no arbitration target to add.

## 6. Evidence and limits

- Read-only: `rev-parse`, `ls-tree`, `show`, `log`, `grep` only. No `git status` (it can
  refresh the index), no jj, no writes in the lane, no tool installs, no web sources.
- Blob digests at 4edb25d: SKILL.md `dc79dad96df9f680dbb0f07f85a8cd07d3e5de5207e42c812621f720849bd780`;
  PROVINCE.md `3a2364d7cbea724485f64d3ff97ce9eb723f013559b969c491343320d582bda8`
  (`git show 4edb25d:<path> | sha256sum`).
- Unknown: working-tree bytes may differ from the commit blobs; HEAD equals master but
  cleanliness was not measured by design (no `git status`). Everything above is
  commit-blob truth at 4edb25d.
- Unknown: whether any other lane repo records a souji-delivered SKILL/prompt edit for
  a third lane; out of this row's surface (souji's own pinned files) and not needed for
  the classification, since the claim surface here is souji's skill and province docs.
