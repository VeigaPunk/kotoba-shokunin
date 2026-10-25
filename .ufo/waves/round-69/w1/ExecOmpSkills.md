# ExecOmpSkills — round 69, wave 1 (build+attack)

**Seat scope:** verify the omp and opencode skill surfaces this round touches; confirm the five
client URLs; verify `SKILL.md` line count at the tip and that the frontmatter parses.
**Verdict:** the five URLs are up and all five quotes are live; the tip's `SKILL.md` is exactly
**600 lines** with a **parsing** frontmatter; the in-flight draft is **603** and is **both
required and over budget** — it closes a real tip defect and simultaneously breaks the file's own
executed ≤600-line box. A verified 3-line remedy exists (below). Separate pre-existing blocker:
`verify_skill_checklist.py` cannot reach exit 0 at the tip for a reason no `SKILL.md` edit can fix.

**Lane:** tip at measurement `a238989a96cb0d2b939679126b832d75b861ca6e` (plan base `a5f7459f`,
plus the r69 plan commit). No lane file was written by this seat except this report; no `git write`
or index touch in the lane. Every check that executes code ran in `/tmp` shared clones
(`/tmp/k69-omp`, `/tmp/sb69`, `/tmp/fleet69`). No installs (nothing needed); pacman untouched.

---

## 1. The numbers asked for

| Measurement | Value |
|---|---|
| `ls /home/vgpnk/.agents/skills/ \| wc -l` (skill dirs) | **74** |
| …of which directories carrying a top-level `SKILL.md` | **74** |
| …of which symlinks into other trees | **5** (`omarchy`, `shokunin`, `swarm`, `tower`, `ufo`) |
| `find .agents/skills -name SKILL.md \| wc -l` (real files) | **69** — reconciles: 69 real + 5 symlinked = 74 |
| Duplicate skill basenames inside `~/.agents/skills` | **0** |
| `SKILL.md` at branch tip (`git show HEAD:SKILL.md \| wc -l`) | **600** |
| `SKILL.md` working tree (`wc -l`) — L1 content draft | **603** |
| Frontmatter | **parses** (PyYAML `safe_load`), keys `name`, `description` only |
| `name` | `kotoba-shokunin` (== directory name → `trigger.name_directory` PASS) |
| `description` | folded scalar `>`, **1 019 chars** (≤1 024 spec, ≤1 536 Claude Code) |

The 74/69 split is a read trap, not a defect: `find` does not follow the five symlinks while `ls`
counts them. Both numbers are correct.

Symlink targets, for the record:
`omarchy → ~/.local/share/omarchy/default/omarchy-skill`;
`shokunin → ~/Projects/ompskills/.omp/skills/shokunin`;
`tower → ~/Projects/ompskills/.omp/skills/tower`;
`swarm → ~/Projects/ompskills/.omp/skills/tower/swarm`;
`ufo → ~/Projects/ompskills/.omp/skills/ufo`.

## 2. The five client URLs (2026-10-25, `curl -I -s -o /dev/null -w '%{http_code}'`)

| Client | Code | Note |
|---|---|---|
| Roo Code | **301** → 2 redirects → **200** | final URL `https://roocodeinc.github.io/Roo-Code/features/skills/` |
| Amp | **200** | |
| Deep Code | **200** | |
| Junie | **200** | |
| opencode | **200** | |

All five reachable. Roo Code is reachable only after the redirect: `docs.roocode.com` now 301s to
the GitHub Pages host. **Actionable for C1:** the entry draft's `source:` line for S203 records the
pre-redirect host `https://docs.roocode.com/features/skills`; the quoted text lives on the redirect
target. A `--fetch` that does not follow 301 reads a redirect body, not the quote. Record the
effective URL (or the redirect) alongside the old one.

Quote presence re-opened live (all five confirmed, matching the plan's wording):

- **Roo Code** — "Project skills override global skills, mode-specific override generic"; the
  native `.roo/skills/` root is labelled "Roo-specific (higher priority)" against the shared root.
- **Amp** — "Local skills mask repository skills with the same name." (plus "A personal skill masks
  a workspace skill with the same name, and both mask official Amp skills.")
- **Deep Code** — "If multiple skills resolve to the same name, only the highest-priority one is
  kept."
- **Junie** — "the project-level skill takes precedence and the user-level skill is ignored."
- **opencode** — "Ensure skill names are unique across all locations."

**opencode's rule is uniqueness, not precedence — confirmed by absence as well as presence.** The
page's only "override" hits are navigation items for *tool permissions* ("Override per agent"); it
states no order and no collision outcome. That is exactly the C1 characterization, and it is a
distinct kind from the other four.

## 3. The draft is required *and* over budget — measured both sides

Two executed contracts collide at exactly three lines.

- `check_skill_precedence.py` / `check_r68_routed_repairs.py` / `check_province_core.py` are
  committed at the tip as top-level blobs under `verifiers/`.
- `check_gate_registry.py`'s universe is **every non-recursive `verifiers/*.py|*.sh` blob** (49 at
  the tip) and each must have exactly one conformant row in `SKILL.md`'s `## Gate registry` — the
  registry home is *pinned to SKILL.md*, so rows cannot be relocated to a depth file.
- `trigger.line_budget` is `executed:` in `verifiers/checklist-baseline.json`, binds the box's own
  number ("File ≤ 600 lines", box at line 319), and the tip has **zero headroom**.

Differential measurement in `/tmp` at the same layout:

| Revision | lines | `check_gate_registry.py` | `trigger.line_budget` |
|---|---|---|---|
| tip `a238989` | 600 | **46 of 49**, exit 1 — missing exactly the three r69 counters | **PASS** 600 |
| L1 draft | 603 | **49 of 49**, exit 0 | **FAIL** 603 — "exceed budget 600 (from box at line 319)" |

Missing-row identity at the tip (`check_gate_registry.py --rev HEAD`):

```
verifiers/check_province_core.py             no registry rows naming it: 0 (need 1)
verifiers/check_r68_routed_repairs.py        no registry rows naming it: 0 (need 1)
verifiers/check_skill_precedence.py          no registry rows naming it: 0 (need 1)
gate registry rows conformant 46 of 49 lane verifiers; phantom 0
```

So the tip is already non-conformant by exactly the three rows the draft adds. The draft's rows are
otherwise clean: each carries 8 cells (9 pipes), identical arity to all 20 neighbouring rows, and
the rows' cited paths all resolve (`trigger.citation_resolves` 169 → **175** tokens, PASS). The
**only** new failure is the line count.

### Verified remedy (proved in `/tmp`; lane untouched)

The box map hashes a box *after joining its continuation lines*, so reflowing a continuation is
hash-preserving. Merging three continuation pairs reclaims exactly 3 lines:

1. `- [ ] Stale-risk facts (model names, versions, prices) are either pinned with a` + its
   `source or deferred to \`--help\` …` continuation → one line.
2. `(executed: \`trigger.line_budget\` — … the threshold;` + `\`--max-lines\` applies only when the
   box states none)` → one line.
3. `(executed: \`trigger.no_placeholder\` — … after a` + `negation, or quotes it in backticks, …`
   → one line.

Measured on draft + these three reflows:

```
PASS checklist.box_map_complete: evaluated 41 — 41 boxes mapped (8 executed, 4 delegated, 29 unexecuted)
PASS trigger.line_budget:        evaluated 600 — 600 lines within budget 600 (from box at line 318)
PASS trigger.citation_resolves:  evaluated 175
gate registry rows conformant 49 of 49 lane verifiers; phantom 0        (exit 0)
```

`box_map_complete` staying PASS with the 8/4/29 split unchanged proves the reflow preserved every
box text hash, so the byte-pinned baseline did not move. Both gates pass at 600 lines. This is the
shape the draft needs before it can land; **I did not apply it — `SKILL.md` is not mine to edit.**

## 4. Pre-existing blocker on the same surface: `governance.citation_resolves`

`verify_skill_checklist.py` cannot reach exit 0 at the tip, at either revision, and no `SKILL.md`
edit can change that. Two `LOG.md` tokens are counted as unresolved citations:

- `LOG.md:2676` — `.ufo/waves/round-67/w1/controls/census-validate-append.txt`
- `LOG.md:2678` — `.ufo/waves/round-67/w1/controls/junk-world/`

Both are *documented* corrections/removals, not live breakage:

- 2676 is the round-67 erratum (routed defect R67-2): "the file that exists is
  `.ufo/waves/round-67/controls/census-validate-append.txt`". That corrected path **exists and is
  tracked** (1 573 bytes).
- 2678 discloses the 254 MB `junk-world/` control mirror that round 68 removed; it is genuinely
  absent, by design.

The excuse mechanisms are exhausted, not wrong: `GOVERNANCE_ERRATA_HORIZON = 2315` (one pinned row,
line 2111) and `GOVERNANCE_CORRECTIONS_HORIZON = 2621` (three pinned rows). Both errata sit at 2676
and 2678, past both horizons, so they are pinned nowhere. The checker reported
"1 recorded absence(s) excused, 3 recorded correction(s) excused" — those are the older rows only.

Mechanism to fix, if the L1 wants it: add `(2676, <sha256 of that LOG line>, "LOG.md",
<r67 report line>, ".ufo/waves/round-67/w1/controls/census-validate-append.txt",
".ufo/waves/round-67/controls/census-validate-append.txt")` to `GOVERNANCE_CORRECTIONS` and raise
the horizon to 2676, with the same fail-closed self-test fixture the existing rows carry. The pin
hash measured today is `f0ddc4347ac0b83cf14ddedba70fca3af0f4045e8194e1d8c98e04e935b2a31e`. That is
a `verifiers/` edit — not this seat's — and it must not be done without its own broken-world test.

Consequence for round-69: **any claim that rests on `verify_skill_checklist.py` exiting 0 is
currently unreachable at the tip.** None of the three frozen predicates does, so this is a latent
constraint rather than a falsified claim — but it is the reason the "checklist 10/10" line cannot
be asserted this round.

Parent-relative tokens are a second-order effect and were separated out: with the fleet parent
materialised (`../PROTOCOL.md`, `../.ufo/...`, sibling lanes) every one of them resolved; the two
failures above survive that materialisation, so they are in situ real, not clone artifacts.

## 5. omp and opencode surface findings

- **opencode reads both compat roots.** Its documented global locations include
  `~/.agents/skills/<name>/SKILL.md` *and* `~/.claude/skills/<name>/SKILL.md` (plus its native
  `~/.config/opencode/skills/`). All three native roots are **absent on this host** (checked
  `~/.config/opencode/skills`, `~/.config/opencode/skill`, `.opencode/skills` in the fleet root and
  in the lane), so every opencode-visible skill arrives through a compat root.
- **14 live name collisions.** `~/.agents/skills` and `~/.claude/skills` share 14 basenames:
  `agents, dubbing, music, omarchy, onboarding, realtime, setup-api-key, sound-effects,
  speech-engine, speech-to-text, text-to-speech, update-skills-from-changelog, voice-changer,
  voice-isolator`. All 14 are **byte-identical** today (matching SHA-256 pairs), so nothing is
  broken now — but opencode's only stated rule is that names be unique across locations, so this
  is the live counter-example to the rule the C1 entry documents. It is also a latent divergence:
  updating one copy and not the other silently changes which skill answers, and the docs say
  nothing about which one wins. Useful as the concrete instance for C1's opencode row; do not
  present it as observed client behaviour (no client was run against a collision).
- **The lane's own skill is not mounted.** There is no `kotoba*` entry in `~/.agents/skills`, so
  this round's `SKILL.md` edits do not reach the omp/opencode surface until installed. No drift
  risk from the draft, and no live consumer breaks while the 600-line dispute is settled.

## 6. What this seat did not do

- Did not edit `SKILL.md`, `corpus/`, `verifiers/`, `PROVINCE.md`, `plans/` or any committed file;
  did not apply the 3-line remedy anywhere but a `/tmp` clone.
- Did not run any counter inside the lane; did not touch the lane's jj state or Git index.
- Did not run `--fetch` against the five pages with the C1 counter (that is the fetch arm's seat);
  the quote checks above are this seat's own re-opening, and the Roo redirect finding is theirs to
  reconcile with `--fetch` behaviour.
- Ran no build, lint, test or formatter run beyond the two counters named here.

## 7. Residual risks

1. **Draft lands at 603 → `trigger.line_budget` FAIL.** Guard: reclaim 3 lines with the verified
   reflow (§3) in the same edit that adds the rows. Landing the rows alone trades
   `gate_registry 46/49` for `line_budget FAIL` — no net gain, and it is the file's own box that
   breaks.
2. **`governance.citation_resolves` unresolvable from content** (§4). Pinned-row edit required;
   carries its own self-test obligation.
3. **Roo citation points at a redirecting host** — record the effective URL, or `--fetch` may read
   a redirect body.
4. **14 duplicated skill names across two live roots** — harmless today (byte-identical), silent
   wrong-answer risk the moment one side is edited alone.
