Result: MIXED — both `claim withdrawn` annotations land, read correctly and pass the frozen registry counter, but the same-class round-56 withdrawn counter (`check_agentdef_boxes.py`) carries no annotation, and nothing in the lane enforces the annotations' presence.

Scope: routed repair R1 at `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe` — the two in-cell `claim withdrawn`
annotations in `SKILL.md` § Gate registry (rows for `verifiers/check_infoless_fences.py`,
`verifiers/check_sweep_mutants.py`). Sandbox: `git clone` of the lane, `checkout 46b4a70…`, at
`/fast/scratch/hyaku/kotoba-r58/ReviewR1Annotations` (lane untouched; `git diff 46b4a70 8e52f064 -- SKILL.md`
is empty, so tip equals the state under attack for every line cited).

## Commands run (all under `timeout 300`, sandbox cwd)

1. `python3 -B verifiers/check_gate_registry.py --rev 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe`
   → `gate registry rows conformant 32 of 32 lane verifiers; phantom 0`, **exit 0**. (M77's "32 of 32"
   holds: the annotations are inert under the counter, the rows conform.)
2. `python3 -B verifiers/check_gate_registry.py --self-test` → `self-test: 0 failure(s) over 28
   assertions`, **exit 0**. No assertion mentions a withdrawn/annotated row.
3. `python3 -B verifiers/check_infoless_fences.py --rev 46b4a70…` → **exit 1** (a failing `gate`
   that the annotation correctly marks withdrawn).
4. `python3 -B verifiers/check_sweep_mutants.py --rev 46b4a70…` → `sweep mutants killed 11 of 11;
   equivalents survived 5 of 5`, **exit 0** (the instrument still passes; the annotation keeps its
   `1=failed`/`0=clean` verdict map legible while marking it non-claim).
5. `python3 -B verifiers/check_agentdef_boxes.py --rev 46b4a70…` → `agent-definition boxes executed
   and discriminating 0 of 9`, **exit 1** — every box `unexecuted`, because `verifiers/verify_agentdef.py`
   never shipped (`git ls-tree 46b4a70:verifiers/` shows only `check_agentdef_boxes.py`). This gate fails
   on every revision a reader runs it at, and its registry row gives no reason.
6. Annotation-drop mutant: stripped both ` — claim withdrawn …` cells, committed as sandbox
   `c83b195840eeee6a3036735fd1058cd715d52092` (/fast/scratch/hyaku/kotoba-r58/ReviewR1Annotations);
   `check_gate_registry.py --rev c83b1958…` → `32 of 32`, **exit 0**.

## Findings

### F1 (highest) — same-class withdrawn counter left unannotated: `check_agentdef_boxes.py`
`SKILL.md:446` registers `verifiers/check_agentdef_boxes.py` as `gate` with a bare verdict map — no
`claim withdrawn` cell — although round 56's C2 was **withdrawn before data** and the plan says the
counter "stays committed as the broken v1" (`plans/round-56.md:113-122`, `corpus/lessons/round-56.md:31`;
spot-check `corpus/lessons/round-56-verifier-spotcheck.md:127-141`). This is the identical defect class
R1 exists to cure (M70 `withdrawn-counter-kept-as-gate`, `corpus/lessons/round-58.md:49`): r57 and r58
counters got the annotation (rows 457, 465), the r56 counter did not. Worse, this row is the only one of
the three that **permanently fails** (exit 1 at `46b4a70`, command 5): a reader sees a `gate` that fails
every revision with no withdrawal note — the annotation was most needed here. The round-56 spot-check
§ 7 never routed it (its R-items cover other defects), so R1's sweep inherited the omission rather than
creating it; the repair is still incomplete. A consistent fix: same in-cell form, e.g.
`— claim withdrawn r56 before data; not a claim gate until redesigned and re-controlled`.

### F2 — the annotation is uncontrolled; silent reversion survives every gate
The frozen counter's grammar (`verifiers/check_gate_registry.py:74-76,178-224`) reads only `code=class`
pairs via `PAIR_RE`; the `— claim withdrawn …` tail is free prose it never inspects, and none of the 28
self-test assertions (`:245-336`) covers an annotated row. Demonstrated: sandbox mutant
`c83b195840eeee6a3036735fd1058cd715d52092` dropping both annotations scores `32 of 32`, exit 0 (command
6). R1's fix is therefore prose-only — a future edit deleting the annotation regresses M70 undetected.
[INFERENCE] This is the same "check a routed fix against the gate that judges it" class the lesson itself
names at M77 (`corpus/lessons/round-58.md:70-73`). A minimal control: a self-test arm asserting a
withdrawn row still conforms, or a registry rule that a `gate` row's trailing note match a whitelist.

### F3 — the round's own record contradicts itself on what the R1 fix was
`corpus/lessons/round-58.md` M70 row (:49) says "fix: round 58 **relabels the SKILL.md gate-registry row
as `probe`** and records the withdrawal reason (`plans/round-58.md:13`)" — citing the plan line that still
reads "registry row re-labelled `probe`" (`plans/round-58.md:13`). The committed fix is the in-cell
annotation, and the *same file* records that the `probe` relabel was rejected by
`check_gate_registry.py` (M77, `corpus/lessons/round-58.md:70-73`, `ExecR1Registry` 30-of-32). M70's fix
sentence was never updated to the landed repair. In-file contradiction on exactly this repair's record.

### F4 (minor) — annotation asymmetry: r57 row omits "before data"
Row 457: `claim withdrawn r57;` vs row 465: `claim withdrawn r58 before data (plan erratum 1);`
(`SKILL.md:457,465`). Both claims were withdrawn before data (r57 spot-check
`corpus/lessons/round-57-verifier-spotcheck.md:92-95`), and the before-data timing is the load-bearing
fact (it is why the withdrawal is a gate reject, not a claim miss — round-56 spot-check
`corpus/lessons/round-56-verifier-spotcheck.md:127-130`). The r57 cell is shorter and still readable, but
the pair is inconsistent in the one detail that matters. Cheap harmonisation while touching F1.

## What holds

- Both named annotations exist at `46b4a70`, are byte-plausible, sit in the verdict-map cell without
  breaking the frozen parser (no `code` digits collide; `32 of 32`, exit 0), and say the right thing:
  "not a claim gate until redesigned and re-controlled" accurately tells the reader the `gate` kind is a
  registry-mechanics artifact, not a live claim gate.
- Kind `gate` retained for both rows is the correct choice under the counter's own rules (probe + `1=failed`
  + `--self-test` handler is rejected; M77's 30-of-32 evidence). The repair is consistent with the gate
  that judges it.
- Cell placement (a trailing em-dash clause) is reasonable: the table has no claim-status column, and the
  counter tolerates the tail. No readability break.
- Exit-1 behaviour of `check_infoless_fences.py` (command 3) is honest: the row maps `1=failed`, and the
  annotation is the thing that tells a reader the failure is expected. On row 457 the convention works;
  row 446 is where the convention's absence hurts.

## Verification gaps / residual risk

- I did not run the full `--fetch` or contention paths; none bear on these annotations.
- Whether `check_agentdef_boxes.py` *should* remain a registered gate at all (vs. probe/deregistration in
  a redesign round) is L1's call; the finding is only that its current presentation contradicts the
  registry's own withdrawal convention.
- The `--json` route of `check_gate_registry.py` was not exercised; the row loop is shared, so risk is low.

Tools installed/updated: none (pacman transactions paused host-wide; all commands used preinstalled
python3/git).
