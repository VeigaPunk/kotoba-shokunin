author: KotobaR49.CriticC1Sizing (critic seat, read-only; design attack, build not awaited)

# Round 49 C1 (adjacency) claim-sizing critique

Lane base `a5adc146a2995dcc5a95a6d8db6e5674f75191ac` (`git rev-parse HEAD master` in the lane, both equal).
Run 2026-10-22, about 09:30–09:41Z. Scratch: `/fast/scratch/hyaku/kotoba-r49/seats/CriticC1Sizing/clone`.
Inputs read: `plans/round-49.md` C1, `AXES.md` adjacency row, `.ufo/prompts/kotoba-round-49.md` §6 item 9
(claim sizing), `corpus/lessons/round-48-verifier-spotcheck.md` R2.

## Rating: holds-bounded (a fixable defect, not a tradeoff)

As sized, the after-value repeats R2. The count 10 → 20 is a name count: a bare list prints 20, a list
labelling every sibling `none` prints 20, and so do names placed in an unrelated later section. The
content guard sits on a different file from the counted one, and it accepts quotes with no scope content.
The plan mines M29 ("content-blind counter") and then declares another content-blind counter. The claim
can still land a real adjacency move, but only if the counted value is tied to sibling-owned evidence.
The correction below does that with one command.

## Findings

1. **Name count, not an adjacency move (counterexamples CE1–CE4).** The plan's command, run in a private
   clone with `PROVINCE.md` mutated:
   - CE1: § Adjacent replaced by one line of the 20 bare names, with no classification and no quote: **20**.
   - CE2: 20 lines `- <name> — none`: **20**.
   - CE3: base file, plus a later `## Notes` section listing 10 unnamed siblings: **20**. The cause is
     that `awk '/^## Adjacent/,0'` runs to end of file.
   - CE4: base file, plus "prompts that carry audio cues or world lore": **12**. The words `audio` and
     `lore` are plain English words.
   Base reads **10** (exit 0). That matches the plan's Q19 before-value.
2. **The content guard does not close the gap.** (a) The guard reads the census entry, but the counter
   reads `PROVINCE.md`. Nothing joins the two, so CE1 or CE2 in `PROVINCE.md` next to a good entry
   passes both. (b) "The quote exists at the pinned commit" proves the quote was copied correctly, not
   that it describes scope. I took each sibling's `PROVINCE.md` H1 line as its quote (for example
   `# audio province`). A recheck at each sibling's HEAD passes **20/20**, and a mutated quote fails
   (exit 1). So a census of scope-free headings, every row `none`, passes both the counter and the guard.
   (c) The plan does not say the guard fails when the census has fewer than 20 rows. With 0 quotes, a
   loop over the quotes passes vacuously.
3. **`none` is absorption-free, but at base it is not honest for named siblings.** Classifying is
   reporting, not absorbing. But sibling-owned and lane-owned bytes contradict `none` for three lanes:
   - kotodama `SKILL.md` description at `35f0d49f`: "NOT prompt/skill craft (kotoba-shokunin)". Base
     `PROVINCE.md` files kotodama under "no overlap observed". That is a published boundary against
     kotoba, recorded as no overlap.
   - kagi and kake are named in kotoba's own `SKILL.md` description at `a5adc146` ("the five
     `*-shokunin` domain skills (kagi, kake, kasegi, kengaku, kumitate)"). Neither is in § Adjacent at base.
   - Boundary statements naming kotoba, from a sweep of the 20 siblings' `SKILL.md` and `PROVINCE.md`
     at HEAD: kengaku `SKILL.md` ("Sibling arbitration: kotoba owns prompt and skill craft"), kotodama
     (above), and kumitate `PROVINCE.md:27` ("Prompt and skill craft → kotoba"). The other mentions are
     incidental (kagi `SKILL.md:297`; tabi `SKILL.md:1313,1450` list kotoba in a `LANES=` string).
   Any sibling with a `SKILL.md` is also a surface kotoba's Domain line governs ("scopes SKILL.md/AGENTS.md
   quality"), so `none` has to mean "no domain overlap", stated separately from "kotoba audits their skill
   file". A `none` row needs its Q14 sweep.
4. **Is it a learning claim? Partly; most of it is inventory.** The ground is already partly covered:
   - `.ufo/round-46/scouts/w2-connector.md` already scanned every sibling, including audio, revenger,
     game-dev-2d, game-dev-3d, kumitate and souji, and named three contested items.
   - `corpus/knowledge/fleet-skill-audit-round5.md` measured 0/5 arbitration clauses.
   - `corpus/README.md:106-108` records the arbitration gap as "measured and persisted".
   - `corpus/knowledge/sibling-citation-routing-round16/21` hold the routing replay.
   What would be new is the classification of the 10 unnamed siblings and the harness-selection sources.
   The plan also has to address a premise problem: kotoba's own description says "the shokunin files are
   not in an omp skill discovery root, so their descriptions never reach the omp skills router". My sweep
   of 10 discovery roots (evidence below) finds no lane `SKILL.md` offered; only the generic `shokunin`
   skill is installed. So the "arbitration clause" column measures an audit-side property with no router
   effect on this host. The entry must say so. Otherwise it implies selection behaviour the host does not
   exhibit.
   - Three siblings have no `SKILL.md` (audio, game-dev-2d, revenger), so their scope quote must come from
     `PROVINCE.md`, and the arbitration column is n/a for them, not `no`.
   - `S002`, `S013`/`S021` and `S014` already cover client-side skill loading and implicit invocation.
     New rows on the same URLs add to the existing W04 duplicate-URL warnings.
5. **Pins are required, and the closure must never use sibling HEAD.** Sibling HEADs moved during this
   session: kake `8ecbefe` → `5a83d13b`, tameshi `3b20f07` → `f4e8f7d8`, tsukuroi `44e9542` → `f923750d`
   (two `rev-parse` runs minutes apart). A value re-derived at sibling HEAD will drift.
6. **No-harm risk (consistency and calibration).** The drift guard forbids editing the `SKILL.md`
   frontmatter, and the frontmatter still says "the five `*-shokunin` domain skills". After C1,
   `PROVINCE.md` would name 20 siblings while the description names five. The L1 should record this as a
   carried defect in the lesson or the report, not leave it silent. Do not edit the frontmatter this round.
7. **Arbitration belongs to the integrator.** AXES.md says "Lane reports name contested scope; integrator
   arbitrates". A `contested` row must name the scope and route it (report § or L0 line). It must not
   state which lane wins. Kumitate's and kengaku's published splits can be quoted as their position, not
   adopted as the ruling.

## Proposed after-value (stronger than the plan's; one command over committed bytes)

Count the siblings that have a published boundary with kotoba but no `contested` or `adjacent` row in
`PROVINCE.md` § Adjacent. The set comes from the sweep above: siblings named in kotoba's own description
(kagi, kake, kasegi, kengaku, kumitate), plus siblings whose own scope files name kotoba as a boundary
(kengaku, kotodama, kumitate). Together that is 6 siblings. The section is bounded at the next `## `
heading.

```sh
for n in kagi kake kasegi kengaku kotodama kumitate; do awk '/^## Adjacent/{f=1;next} /^## /{f=0} f' PROVINCE.md | grep -E "\b$n\b" | grep -qE "\b(contested|adjacent)\b" || echo $n; done | wc -l
```

| PROVINCE.md state (scratch clone) | plan counter | proposed counter |
|---|---|---|
| base `a5adc146` | 10 | **6** |
| CE1 bare 20-name list | 20 | 6 |
| CE2 all 20 `none` | 20 | 6 |
| CE3 names in a later section | 20 | 6 |
| six rows labelled `contested`/`adjacent` | — | 0 |

Declare **6 → 0**. Keep 10 → 20 only as the expansion observable, as R2 advised for the round-48 entry
count. Known limit: a row reading `adjacent: x` passes. So the census quote guard still has to cover the
`PROVINCE.md` rows, by joining each row's sibling, pinned commit and classification to the entry, and it
must fail when there are fewer than 20 rows. The six-member set is a judgment over the sweep (incidental
mentions excluded, see Finding 3). The entry should print that sweep so the closure can re-derive the set.

## Smallest safe correction

1. Replace the declared after-value with the 6 → 0 count above, bound the awk range at the next
   heading, and keep 10 → 20 as a secondary observable.
2. Make the recheck guard cover the `PROVINCE.md` rows as well as the entry: each row's sibling,
   pinned commit and classification must equal the entry's. It must exit non-zero when there are fewer
   than 20 rows, and each quote must come from the sibling's `description:` or Owns/Refuses block, not a
   heading. Show it failing on CE1 and on an H1-only quote.
3. The entry states that lane `SKILL.md` descriptions are not router-visible on this host (kotoba
   `SKILL.md:12-14`), with the discovery-root sweep; arbitration columns are audit-side.
4. `contested` rows route to the integrator; carry the "five siblings" frontmatter line as a defect.

## Evidence (commands, exit codes)

- `git -C kotoba-shokunin rev-parse HEAD master` → both `a5adc146…`; exit 0.
- Before: `git show a5adc146:PROVINCE.md | awk '/^## Adjacent/,0' | grep -oE '<plan regex>' | sort -u | wc -l`
  → 10 (chousa kama kasegi kengaku kotodama kumitate mado mori revenger tameshi); exit 0.
- `ls -d /home/vgpnk/Projects/shokunin/*-shokunin | wc -l` → 21 (20 siblings plus kotoba).
- Sibling `SKILL.md` presence: `git -C <repo> ls-tree -r --name-only HEAD | grep -E '(^|/)SKILL\.md$'`.
  It is absent for audio, game-dev-2d and revenger; all 20 have `PROVINCE.md` (`git cat-file -e HEAD:PROVINCE.md`).
- Boundary sweep: for each sibling, `git -C $d show HEAD:{SKILL,PROVINCE}.md | grep -c kotoba`. Hits:
  kagi 1/0, kengaku 1/5, kotodama 1/1, kumitate 0/1, tabi 2/0; others 0. Loop exit 1 (last `[ ]` false).
  Lines were read with `grep -n kotoba`.
- Router visibility: I swept 10 roots (`~/.agents/skills`, `~/.claude/skills`, `~/.omp/agent/skills`,
  fleet `.omp/skills`, `.agents/skills`, `.claude/skills`, `skills`, `~/.config/opencode/skill{,s}`,
  `~/.codex/skills`) with `readlink -f`. The only `shokunin` hit is
  `~/.agents/skills/shokunin -> ~/Projects/ompskills/.omp/skills/shokunin`, which is not a lane `SKILL.md`.
  `grep -l shokunin ~/.omp/agent/config.yml ~/.config/opencode/opencode.json*` → exit 1. [INFERENCE]
  omp may have discovery roots outside this list; I did not read the omp loader source.
- CE1–CE4 and the proposed-counter table: run in the scratch clone and restored afterwards. `git status
  --porcelain | wc -l` → 0. `sha256sum` of the restored `PROVINCE.md` = `git show HEAD:PROVINCE.md` =
  `02740235b0f0d8dc437305d74ca540604a293d41c158c8d04503e8b410d4c993`.
- Degenerate-quote probe: for each of the 20 siblings, `q=$(git show $sha:PROVINCE.md | head -1)`, then
  `grep -cF "$q"` ≥ 1 → pass 20/20. The mutated quote `# audio provincX` → `grep -c` printed 0, exit 1.
- `git show a5adc146:corpus/QUALITY.md | grep -c Q25` → 0 (Q25 is still to be added, as the plan says).
- No web sources fetched; no tools installed or upgraded; no lane, fleet or sibling bytes written except
  this report.
