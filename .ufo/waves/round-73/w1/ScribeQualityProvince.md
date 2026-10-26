# Round 73 wave 1 — ScribeQualityProvince

**Verdict: drafted, not closed.** Five append-only blocks are written to
`.ufo/waves/round-73/w1/build/ScribeQualityProvince/blocks.md` (129 lines, 13,175 B) with insertion
anchors, landing order and per-row landing conditions. Q67 and Q68 are content-complete once the round's
lesson ids are substituted; Q66 also needs a gate that does not exist at the measured tip. C1's
registry ids and every claim value are `<<…>>` placeholders because neither counter nor
`corpus/lessons/round-73.md` exists at `ac8fc59` — nothing here asserts a post-data number. I confirm
the M127 cause at source and by `Path` semantics and did **not** re-run the battery (other seats own
that); the C2 base premise and Q66/Q67's "not caught" claims are re-derived here.

Measured at `ac8fc59` (wave-1 spec v3; base `072048fa8e8a52c707d25f7079772fa317244eb7`). No lane file
was modified: `git status --porcelain` shows only untracked `.ufo/waves/round-73/` entries. Scratch file
`/tmp/k73w1-ScribeQualityProvince-census.txt` removed (`ls /tmp | grep -c k73w1-ScribeQualityProvince`
→ `0`).

## Deliverable

`.ufo/waves/round-73/w1/build/ScribeQualityProvince/blocks.md`

| block | target | anchor (observed line at `ac8fc59`) |
|---|---|---|
| 1 | `PROVINCE.md` § Core bullet, round 73 | after the round-72 bullet (line 30), before `## Frontier` (line 31) |
| 2a | `corpus/README.md` Coverage-map row for `knowledge/chinese-vendor-skill-surfaces-round73.md` | after the `Round-72 lessons` row (line 140) |
| 2b | `corpus/README.md` `Round-73 lessons` index row | immediately after 2a |
| 2c | `corpus/README.md` § Frontier note, new area *Chinese-vendor skill surfaces* | after the Round-60 note (line 219), before `## Knowledge gaps` (line 221) |
| 3 | `corpus/QUALITY.md` rows Q66–Q68 | after Q65 (line 81, last line of the file) |

The PROVINCE bullet carries the three claims in the style of `PROVINCE.md:28-30` (title, `(round 73)`,
surface, entry path, counter with `--rev <rev>`, printed line, base figure) with values as `<<N>>`, ids as
`<<S-ids>>`.

## Findings

### F1 — M127's cause is real at the base, confirmed independently of the receipt

```
$ git show 072048fa8e8a52c707d25f7079772fa317244eb7:verifiers/check_tip_battery.py | sed -n '610p'
    fleet = Path(args.fleet) if args.fleet else repo.parent
$ python3 -c "from pathlib import Path; print('Path(\".\").parent ->', repr(Path('.').parent)); print('is lane?', Path('.').parent.resolve()==Path('.').resolve())"
Path(".").parent -> PosixPath('.')
is lane? True
```

With the documented `--repo .`, `fleet` is the lane itself, so `build_sandbox` symlinks the lane's own
entries beside the clone instead of the fleet root, and every `../` citation in the sandbox is
unresolvable. The receipt's own first failing line agrees (11 words as pasted, leading indentation the only
shaping):

```
$ sed -n '17,18p' .ufo/waves/round-73/receipts/m127-l1-repro.txt
  verify_skill_checklist.py: FAIL trigger.citation_resolves: line 558: '../.ufo/reports/round-7/kotoba.md' does not resolve from /tmp/k72-tip-4uezkznu/kotoba-shokunin
  check_assertion_floors.py: FAIL checklist observed=1863 floor=1863 self_test_failures=2
```

Its run B (`--repo <absolute lane path>`) reads `4 of 6`, i.e. the same two remaining reds minus the two
environment reds — consistent with the selection path being the whole difference. **Not observed:** I did
not run `check_tip_battery.py` myself; the base receipt records `wall 153.5s`, and re-running it would
decorate, not verify, a cause already fixed at file:line. The cause is now named at the plan's C3 surface
and entered in the QUALITY row Q68's grounding.

### F2 — the C2 premise (plan addendum 1, considerthese item 5) re-derived

```
$ python3 - <<'EOF'
lines = open('SKILL.md').read().split('\n')
i = next(k for k, l in enumerate(lines) if l.startswith('description: >'))
buf = []
for l in lines[i+1:]:
    if l.startswith('  '): buf.append(l.strip())
    elif l == '': continue
    else: break
import re
d = re.sub(r'\s+', ' ', ' '.join(buf)).strip()
print('folded len', len(d))
m = re.search(r'[.:]\s+[A-Z]', d)
print('first sentence len', len(d[:m.start()+1]))
EOF
folded len 1019
first sentence len 151
```

1,019 characters folded and a 151-character first sentence: the addendum's two numbers are the tree's
numbers, so the premise of the C2 do-nothing control (R1 must fail at the base) rests on observed bytes.
The `1 of 3` figure is the addendum's own and is **not** re-derived here — `check_own_description.py`
does not exist yet. The supporting line pointers in my PROVINCE bullet also re-read: `frontmatter-trigger-surface.md:68`
("at most 99 chars — first sentence wins if ≥40") and `:116-120` ("write for the truncator … match-critical
WHEN material in the first ≤99 chars").

### F3 — Q67's "not caught" half is measured, not assumed

The routed D3 damage is present in the tree at `072048f`:

```
$ awk 'NR>=207 && NR<=214 {printf "%d: %s\n", NR, substr($0,1,110)}' <(git show 072048fa8e8a52c707d25f7079772fa317244eb7:corpus/SOURCES.md)
207:   `
208: 
209: - **2026-10-24 — placement correction (appended by the L1 in wave 2):** the two round-64 notes
210:   originally landed at EOF under `
211: 
212: - **2026-10-25 — round-72 assimilation openings.** Question: where do vendors state which instruction surface 
213: 
214: ## Leads (unopened)` (the placement defect `CriticW2Frontier` F3 caught at the
```

(`substr($0,1,110)` trims the two long log-entry lines at 110 characters; nothing else is shaped. The
same 207–214 range at `HEAD` diffs empty against this: `diff <(git show 072048f:corpus/SOURCES.md | sed -n
'207,214p') <(git show HEAD:corpus/SOURCES.md | sed -n '207,214p')` → `IDENTICAL`.)

and the census gate is green on it:

```
$ timeout 120 ../scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba; echo "exit=$?"
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
exit=0
```

So neither the row grammar (`W04` warnings only) nor append-only (Q34) reads placement: an entry can be
inserted inside a prose note and split it with every gate green. That is Q67's criterion, and the row
cites those exact lines and this command.

### F4 — Q66's class exists: the r72 report named receipts that do not

```
$ grep -n "tip-check" ../.ufo/reports/round-72/kotoba.md | cut -c1-160
70:  (`tip-check_tip_battery.txt`, `tip-tip_battery-run2.txt`): the counter's sandbox reads `check_assertion_floors.py` and
103:  (`receipts/tip-check_substrate_repin_v2.txt`).
$ grep -c "tip-check" SHONEN.md
0
```

The report itself carries the two names (opened here, not taken from the spot-check); the lane `SHONEN.md`
does not, so my Q66 row credits the report only, while the spot-check's `report/SHONEN` wording is wider
than what this lane's bytes show. The receipts directory confirms neither name exists:

```
$ ls .ufo/waves/round-72/receipts | paste -sd' ' -
base-battery.txt base-outputs c-selftest-check_author_rules.txt c-selftest-check_substrate_repin_v2.txt c-selftest-check_tip_battery.txt c1-base.txt c2-base.txt c3-base.txt census-after.txt census-before.txt freeze2-counters.txt tip-author_rules.txt tip-noharm.txt tip-substrate_repin_v2.txt tip-tip_battery-run2.txt tip-tip_battery.txt
```

No `tip-check_*` file is in that directory at the base; the spot-check records the citation
(`corpus/lessons/round-72-verifier-spotcheck.md:31-34`). Q04 (source/recheck commands), Q49 (seat
`Report:` trailer) and Q60 (`git cat-file -e <rev>:<path>`, which needs a revision the bare pointer does
not carry) each miss this shape — that sentence is inside the row.

### F5 — the addendum's protocol premise re-opened, not inherited

```
$ grep -n "registry home" ../PROTOCOL.md
398:- **Registry.** The schema is this section's; a child lane's *registry home* is its own `SKILL.md`.
421:  lane's *registry home* defined under **Registry** above.
```

The addendum's reason for replacing C2 stands on the protocol's own words, so my PROVINCE bullet names no
registry move and my blocks never touch `SKILL.md`.

### F6 — `check_province_core.py` cannot certify the round-73 bullet

```
$ sed -n '44,50p' verifiers/check_province_core.py
AREAS = (
    ("round 67", "corpus/knowledge/instruction-authority-ladder-round67.md",
     "verifiers/check_instruction_authority.py"),
    ("round 68", "corpus/knowledge/client-trust-gates-round68.md",
     "verifiers/check_client_trust_gates.py"),
)
```

Its count is frozen to rounds 67/68; at the r73 tip it prints `province core rows 2 of 2` whether or not
Block 1 lands. What it does constrain is the no-harm conjunct (docstring `:23-25`): `## Frontier` and
`## Adjacent` must stay byte-identical to its base. My bullet is an inside-`## Core` append only, and the
blocks file says so. **Consequence for the L1:** do not cite this gate as evidence that the round-73
Core bullet exists; a row-existence check or a reviewer read is the evidence.

### F7 — insertion-point arithmetic against the live files

`corpus/QUALITY.md` is 81 lines with Q65 last, `corpus/README.md` line 140 is the `Round-72 lessons` row,
line 219 the Round-60 Frontier note, line 221 `## Known gaps`, `PROVINCE.md` line 30 the round-72 Core
bullet and line 31 `## Frontier`. All five anchors are text-identified in the blocks file as well, so a
landing ahead of them cannot silently misplace an append (the M129/D3 class the row Q67 records).

## Blocks I could not finish, and why (no fabrication)

1. **C1 registry ids and all values.** `verifiers/check_cn_vendor_surfaces.py` does not exist at
   `ac8fc59` (`ls` → no such file), and the lane ids exist only in the L1's renumber-by-document step.
   `<<S-ids>>` / `<<N>>` stay placeholders; the blocks file names the collision that makes this
   mandatory (staged `S214`, `S216`–`S219`, `S221` against lane rows `S214`–`S216`).
2. **Q66's `checked by` clause.** `verifiers/check_report_pointers.py` does not exist either; the row
   lands with the gate or with that clause deleted (stated in the blocks file as a landing condition).
3. **Mistake ids M128–M130.** `corpus/lessons/round-73.md` does not exist yet; the blocks file states the
   substitution rule and that a row grounded in an id the lesson does not carry is the M3 class.
4. **Block 2b's lesson rows.** Its `## Gate` / `## Mistakes` / `## Falsify corrections` cells are
   placeholders by construction: wave 1 has run no falsify wave, so no correction count can be written.

## Not in my scope (reported, not acted on)

- Q66's gate, C1's counter and C2/C3 fixes are other seats' deliverables; I read and cited their absence,
  nothing more.
- The C1 target decision (Q45 census) is the L1's; I only routed the consequence into Blocks 1/2a/2c.
- Tooling: nothing installed or upgraded. Network: nothing fetched — every fact here comes from committed
  bytes or the local `Path` implementation.

## For the L1

1. Land `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md` + snapshots + manifest → then 2a →
   `corpus/lessons/round-73.md` → 2b/Block 3 (ids) → Block 1 → 2c.
2. Replace `<<S-ids>>`, `<<M-id>>`, `<<N>>` with measured values; Q66 without its gate loses the check
   clause.
3. `check_province_core.py` is a no-harm byte-identity guard here, not a witness for the new bullet (F6).
