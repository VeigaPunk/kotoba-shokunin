# Round 73 — plan addendum 1 (erratum E1, before any claim data)

Committed before any wave seat scored any claim and before wave 1 spawned (the dispatcher reported
`cap-defer` for `w1.ready` at the time of writing; `ls .ufo/waves/round-73/` shows no `w1.ready.dispatched`).
Supersedes **C2 of `plans/round-73.md`** only; C1 and C3, their predicates, controls and kill rules are untouched.

## Why C2 changes

`PROTOCOL.md:398` (§ Gate standard, Registry): "a child lane's *registry home* is its own `SKILL.md`", and
`PROTOCOL.md:418-421` (Delivery): "closure grades no gate conformant until its registry row exists at the lane's
*registry home*". The planned C2 moved the 56 registry rows out of `SKILL.md` into `verifiers/REGISTRY.md`: that
would take every gate row out of its protocol home and make closure grade the lane's gates not conformant.
Observed: the rows already carry exactly the eight protocol fields (`sed -n 427,440p SKILL.md`), so there is no
in-place slimming that honours the protocol. `considerthese/2026-10-25.md` item 2 is therefore **not worked** and
an L0 question is appended (`kotoba | round-73 | …`, fleet `.ufo/l0-questions.md`) asking whether a pointer
registry would be acceptable. No code or file was changed for the dropped C2.

## C2 (replacement) — depth (owned, 9): SKILL.md's own description obeys the lane's own trigger rule

**Axis:** `depth` (owned, 9). **Surface:** the frontmatter `description` of this file — the lane's own trigger
surface — read against its own rule: `corpus/knowledge/frontmatter-trigger-surface.md:116-120` ("write for the
truncator … match-critical WHEN material in the first ≤99 chars") and `:68` (the deterministic truncator keeps at
most 99 characters, the first sentence wins if ≥ 40). **Source:** `considerthese/2026-10-25.md` § Self-improvement
suggestions item 5 ("Description self-audit still pending … 1,019/1,024 chars and the first sentence is 151 chars
against the skill's own 99-char render rule"), the one considerthese proposal worked this round; item 4 (the
`SKILL.md:21-23` "two harnesses here" frame) and items 1–3 stay open. The description's own `Note:` says the file
sits outside the omp discovery roots, so this is audit-side craft, not router behaviour — the claim is that the
lane practises the rule it teaches, and it says nothing about any router.

**Frozen predicate (the same sentence in this plan, in the counter's docstring and in the receipt):**

```
python3 -B verifiers/check_own_description.py --rev <rev>  ->  prints "own-description rules held N of 3", exit 0 when N == 3
```

At `--rev`, `D` is the frontmatter `description` of `<rev>:SKILL.md` folded (every whitespace run → one space;
the value ends at the first column-0 line, as `check_sibling_census.py` reads it). Rule `Ri` holds iff:

- **R1** the first sentence of `D` (the text before the first `. ` or `: ` followed by an uppercase letter, else
  the first 99 characters) is between 40 and 99 characters long;
- **R2** the first 99 characters of `D` contain the whole words `skill` and `prompt` and at least one
  double-quoted string that is also a member of the `Triggers:` list of `D`;
- **R3** `len(D) <= 1024` and the tree's own `python3 -B verifiers/check_sibling_census.py
  corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md` exits 0 (all 9
  `adjacent` lanes still named in an ownership clause), run by the counter from a fleet-shaped sandbox of `<rev>`.

Guard the counter prints but the predicate does not count: the frontmatter keeps its line count, so every
`SKILL.md:<line>` citation after it stays valid (`git diff --numstat <base> <rev> -- SKILL.md`, inserted − deleted
lines inside the frontmatter must be 0; the counter prints `frontmatter lines base→rev`).

**Do-nothing control:** the base `072048f` scores `own-description rules held 1 of 3` (R3 only; R1: the first
sentence is 151 characters; R2: no quoted trigger in the first 99), exit 1 — receipt committed before data.
**Shortcut controls (committed worlds, each must read below 3):** a 99-character first sentence with no quoted
trigger; a first sentence under 40 characters; a first sentence that holds a quoted string not in the Triggers
list; the description cut to ≤ 99 characters dropping the Triggers list and the sibling clauses (R3 fails); a
description over 1,024 characters; the first sentence made short by inserting a period mid-phrase while the old
151-character sentence continues after it (R1 reads the new first sentence only — judged by the non-author
reviewer for hollowness; the counter prints the first sentence). **Kill rule:** any shortcut world scoring 3 means
the counter is wrong; fixed before data; nothing changes after a seat has scored data (Q28). **Seat re-targets:**
the wave-1 seats whose items name the registry move (`ScoutRegistryConsumers`, `ExecWeightCounter`,
`ExecWeightControls`, `ExecRegistryMove`, `ScribeSkillPointer`, `ReviewerRegistryMovePlan`, `CriticC2Counter`,
`MutGateRegistry`) are re-pointed to this claim by message: consumers of the frontmatter text instead of the
registry; counter and worlds for `check_own_description.py`; description drafts; the sibling-census gate under
mutation. Their old-C2 reports are kept as evidence of the protocol conflict, not as claim data.
