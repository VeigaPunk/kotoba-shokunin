# ScribeBoxesB — round 72 wave 1 (build): boxes A3 + A4 for SKILL.md § Trigger-fidelity checklist

**Verdict.** Both boxes are drafted and shape-verified against the lane's own extractor: each is one
live box in `## Trigger-fidelity checklist`, four lines, ≤96 chars per line, carrying its frozen
token set as whole words and ending with the frozen tail. Neither can land as-is, for three
measured reasons, all the L1's to close: (1) A4's id slot is the instructed placeholder `S2XX`, which
the predicate's `S###` shape rejects; (2) the two boxes add 8 lines to a 600-of-600-line file, so
`trigger.line_budget` fails at 608 until lines are freed; (3) two new map entries make 43 while
`box_total` is 41, which `load_map` rejects with `MapError` (exit 3). One sourcing gap rides on A4:
its `index` clause is grounded by the staged Vercel row, which the staged entry does not name in a
`source:` line. Deliverable: `.ufo/waves/round-72/w1/build/ScribeBoxesB/boxes.md`.

## Draft (verbatim)

```markdown
- [ ] The install path is declared and its trust level stated: the same body
      is untrusted data in one client and a gated capability in another, and
      a project or remote path runs no embedded command in at least one client.
      (sourced: S198, S199, S200, S202; entry: corpus/knowledge/client-trust-gates-round68.md)
- [ ] Content sits on the right rung: a skill holds what is too specific
      for an always-on file and too shaped for a one-off prompt, and the
      always-resident surface is an index, not a payload.
      (sourced: S2XX; entry: corpus/knowledge/resident-index-and-rungs-round72.md)
```

Per-box observable test and baseline classification text:

| box | observable test (reading only, no runtime) | classification text |
|---|---|---|
| A3 | For each fenced or inline command the body carries, the file names the install path the skill is discovered from (project root, remote URL, user directory) and the gate that path gets; FAIL when a command has no path statement, or the path is named and its trust left implicit. | `unexecuted:the install path is discovery-time state, not file text; partially covered by trigger.command_binary_resolves` |
| A4 | For each block, name its rung — prompt (one task), skill (too specific for an always-on file, too shaped for a one-off prompt), always-on (every session); FAIL when a skill body carries content that would sit unchanged in an always-on file, or the resident surface carries the payload instead of an index. | `unexecuted:rung placement is a content judgement (too specific, too shaped); no length or token proxy separates the rungs` |

## Findings

**F1 — the section's base shape (measured, not read from the plan).**
`python3 -B -c "…importlib load verifiers/verify_skill_checklist.py; extract_boxes(SKILL.md)"` →
`lines 600 boxes 41 section_boxes 15 executed_in_section 8 near 0` / `first_sec_line 266 last_sec_line 323`.
`wc -l SKILL.md` → `600`. So the plan's "600 of 600 lines" holds, the section holds 15 boxes, and 8
of them are executed.

**F2 — both drafts carry their frozen token set in exactly one box, case-sensitively.**
Same extractor on a `/tmp` copy with the two boxes appended after base line 327 →
`boxes 43 near 0 lines 608`; token-set hits `A3 [328]` `A4 [332]` (whole-word regex
`[A-Za-z0-9][A-Za-z0-9'\-]*`, no case folding; identical hits with folding). Text tails verified:
`A3 ends tail: True` / `A4 ends tail: True`. Line lengths `A3 [76, 76, 79, 94]`,
`A4 [72, 72, 57, 82]`. Both texts are live (not fenced, not commented) and carry no
`(executed: …)` annotation, which the map check would otherwise have to agree with.
A first draft failed this check: `A3 cs hits: []` — the sentence-initial capital `Install` does not
match the lowercase frozen token, so the landed text must keep `install` lowercase.

**F3 — the prose that states the box count goes stale on landing.**
`grep -n "fifteen boxes" SKILL.md` → `259:Eight of the fifteen boxes are **executed, not read** — marked`.
With A1–A4 landed the section holds 19 boxes and the executed count stays 8 (all four new rules are
`unexecuted:`), so the line must read "Eight of the nineteen boxes". Nothing machine-checks that
number (`check_box_map` reads `checklist-baseline.json`, not the prose), so it is a consistency
defect only a reader catches.

**F4 — the line budget blocks the landing.**
`sed -n '320,322p' SKILL.md` → `- [ ] File ≤ 600 lines; overflow already moved to referenced depth
files.` / `      (executed: \`trigger.line_budget\` — the number in this box is the threshold;` /
`      \`--max-lines\` applies only when the box states none)`, and `box_line_budget()` reads that
number as the threshold. Measured: base 600 lines, with my two boxes 608. `trigger.line_budget`
therefore FAILs until ≥8 lines are freed in the same commit (plus whatever A1/A2 add). My two boxes
are 8 of the round's ~16 new lines. Insertion index verified: after base line 326, before the blank
line 327 — `lines 608 boxes 43 near 0`, both boxes in section `Trigger-fidelity checklist`
(lines 327 and 331).

**F5 — `box_total` must rise with the entries or the gate exits 3.**
`sed -n '535,547p' verifiers/verify_skill_checklist.py` →
`if bt < len(boxes): raise MapError("box map %s: box_total %d is below the declared entry count %d" …)`
where `boxes = data["boxes"]` is the entry list. `grep -n box_total verifiers/checklist-baseline.json`
→ `253:  "box_total": 41`. Two new entries → 43 entries → `box_total` 41 is below the entry count, so
`load_map` raises before any box is compared. The floor in `check_box_map` is the weaker check
(`len(live boxes) < floor`); the loader's is the binding one.

**F6 — A3's cited rows and entry pass predicate (b) and (c) as they stand.**
`awk -F'|' 'NR>=1 && ($2 ~ /S19[89]|S20[0-28]/)' corpus/SOURCES.md` → S198, S199, S200, S201, S202 all
`mined`, tier `B`, `used-by` `corpus/knowledge/client-trust-gates-round68.md`; S208 `mined`, tier `A`,
same `used-by`. `grep -n "^source:\|^verified-at:\|^recheck:" corpus/knowledge/client-trust-gates-round68.md`
→ `source:` lines 1-6, `verified-at: 2026-10-24` line 7, `recheck: 90d …` line 8. The claims in the box
map onto the rows: S198 "Skill content is untrusted resource data; host tool and sandbox policy remains
authoritative." (13 words); S200 "Project skills (.kilo/skills/ in a repository) and skills fetched from
remote URLs never execute commands" (16 words); S202's teaches cell "a project skill is discovered only
inside a trusted folder, so the install path is part of what the skill can do" (21 words).
Rows dropped for the line bound: S201 and S208 — five ids make the tail 99 chars with the 6-space
indent (bound 96); S208 is the approval shape, not an install-path gate, and S201's anchor is
superseded by S208.

**F7 — A4's entry does not exist, and its `index` clause is not grounded by the four staged rows.**
`test -e corpus/knowledge/resident-index-and-rungs-round72.md` → `ABSENT`. The staged entry
(`/home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/skill-vs-always-on-boundary.md`)
names four rows in its `source:` lines (S261-S264: Letta, Factory, pi, Hermes). `sed -n '17p;20,21p'`
of it → `- Factory: "Use skills when instructions are too specific for always-on AGENTS.md" —` (10 words)
and `- pi: "Use a skill when a workflow needs more context than a prompt template but does` /
`  not need a new executable integration point."` (22 words) — these ground `always-on`, `prompt`,
`skill`, but no staged row's quote carries `index`. The `index` claim is grounded by the Vercel eval,
staged as `S248`: `grep -n "^| S248 " SOURCES.append.md` → anchor cell carries "A compressed 8KB docs
index embedded directly in `AGENTS.md` achieved a 100% pass rate, while skills maxed out at 79%" (20
words). The staged entry cites it only as prose ("Round 5's Vercel eval", line 28) and cites a second
unrowed id ("round 6's S268", line 23), so the landed entry needs `source:` lines for both — else the
box asserts an unsourced clause and predicate (d) has no quote cell to snapshot.

**F8 — id space: staged rows collide on S203-S213 and shift.**
`wc -l .ufo/waves/round-72/assimilation/{reg-ids,staged-ids,collisions}` → `139 / 188 / 11`;
`tail -3 reg-ids` → `S211 S212 S213`; `grep -o "^| S[0-9]\{3\}" corpus/SOURCES.md | sort | tail -3` →
`S211 S212 S213`; `grep -c "^| S214 " corpus/SOURCES.md` → `0`. So S214 is the first free id and the
11-id collision window is S203-S213, i.e. staged ids shift by +11 (staged S248 → S259, staged
S261-S264 → S272-S275). [INFERENCE: the shift is arithmetic from the two id lists; no seat has yet
recorded the mapping decision, and the guard-proof mirror holds only the 139 base rows
(`grep -c "^| S" guard-proof/SOURCES-with-indented-S234.md` → `139`; `grep -c "^| S273 "` → `0`).]
The placeholder `S2XX` in my A4 tail is therefore a placeholder in fact as well as in form.

**F9 — no § Sources bullets are needed for the four new entry citations.**
`grep -n "skill-eval-artefacts-round70\|independent-verification-round12" SKILL.md` → only `241:` and
`317:` (body citations, no § Sources bullet). `grep -n "client-trust-gates-round68" SKILL.md` → no
match at base. Precedent says a body-cited entry needs no § Sources bullet, so the four boxes add no
lines there — which matters given F4.

**F10 — style deviations I chose deliberately.**
The tail path is not backticked, unlike the surrounding prose, because the frozen tail is
`(sourced: S###[, S###…]; entry: <repo-relative path>)` and a backticked path would change the literal
the counter matches; no gate reads a bare path in box text (`citation_subjects` reads backticked
tokens only). A3's tail line is 94 chars — the longest of the four — because the entry path is 46
chars; a five-id tail does not fit.

## Not observed (stated, not claimed)

- No lane gate was run against the live tree: my two boxes exist only in a `/tmp` copy, and I may not
  edit `SKILL.md`. `verify_skill_checklist.py` end-to-end with the boxes landed (box_map + line budget
  + self-test) is unrun; the numbers in F1/F2 come from the module's own `extract_boxes`, imported
  from `verifiers/verify_skill_checklist.py`, applied to that copy.
- No C1 counter exists yet, so the frozen predicate's own run on any world is unobserved by me.
- The A4 entry's text, snapshots and id numbering are other seats' work; F7 states what the landed
  entry must contain, not that it exists.

## Hygiene

- Scratch `/tmp/k72w1-ScribeBoxesB.TQIH` (copies `SKILL.md`, `SKILL2.md`, `SKILL3.md`, `SKILL4.md`)
  created and deleted before return.
- Wrote only `.ufo/waves/round-72/w1/build/ScribeBoxesB/boxes.md` and this report. No committed lane
  file, no git/jj write, no fleet-repo or shokuknow write.
- No tool installed or upgraded; no pacman transaction attempted.
- No credential material, session URL or `op://` reference in this report.
