# RevKamaRow — reviewer report (C3 adjacency: S117 audit)

Scope: independently opened `/home/vgpnk/Projects/shokunin/kama-shokunin/corpus/knowledge/self-assessment-at-writing.md`
(read-only sibling repo), chose my own located quote, audited the planned/drafted S117 row's `teaches`
cell against the file, verified the tier-B honesty, and wrote a final Gate line (below — it differs
from ScribeC3's on two substantive points). This seat wrote only this report; no lane, fleet, sibling,
`.ufo/state`, or jj/git-index writes; no dispatch.

Subject under review: ScribeC3's draft row and Gate line (received via peer message; its report at
`.ufo/waves/round-61/wave/ScribeC3.md:38` carries the same text):

```markdown
| S117 | kama-shokunin — `../kama-shokunin/corpus/knowledge/self-assessment-at-writing.md` | own-work | B | writing-revision calibration for prompt-craft self-assessment | the entry head, “Checking self-assessment statements at writing” | Checking a self-assessment against its writing revision can distinguish a calibration error present then from later drift | queued | 2026-10-23 | 180d | corpus/knowledge/writing-revision-calibration-round61.md |
```

## Independent open — evidence measured by this seat

```sh
cd /home/vgpnk/Projects/shokunin/kama-shokunin && date -u && sha256sum corpus/knowledge/self-assessment-at-writing.md && wc -c -l corpus/knowledge/self-assessment-at-writing.md && git log -1 --format='%H %cI' -- corpus/knowledge/self-assessment-at-writing.md
```

```text
Fri 23 Oct 2026 07:10:28 PM UTC
cd6e3730085ed08ca583604390e84c352ea122e4a6386e383d261a0a0b4cf959  corpus/knowledge/self-assessment-at-writing.md
  33 5831 corpus/knowledge/self-assessment-at-writing.md
6de225c289b7682bf280cffb4a07de3fb7d1275c 2026-10-23T16:09:39-03:00
```

Re-verified after a later HEAD move (`HEAD` is now `7f595a3b…`, an unrelated commit; the file's last
commit is still `6de225c…` and its sha256 re-checked identical at ~19:12Z). So the cited bytes are
stable inside kama commit `6de225c289b7682bf280cffb4a07de3fb7d1275c` and remain so at the time of
this report.

## My own located quote (chosen independently; different from ScribeC3's)

`self-assessment-at-writing.md:7` — “a calibration check, not a freshness-only check”

```sh
cd /home/vgpnk/Projects/shokunin/kama-shokunin && date -u; grep -c 'a calibration check, not a freshness-only check' corpus/knowledge/self-assessment-at-writing.md; printf '%s\n' 'a calibration check, not a freshness-only check' | wc -w
```

```text
Fri 23 Oct 2026 07:12:09 PM UTC
1
7
```

Occurs exactly once (line 7, end of the mechanism paragraph), 7 words, exit 0. It is the file's own
name for the property the `teaches` cell borrows — the most compact self-evidencing phrase for the
row's scoped benefit.

## Audit of the `teaches` cell — PASS

Draft: *"Checking a self-assessment against its writing revision can distinguish a calibration error
present then from later drift."*

- Grounded in the file's actual demonstration, not its verdict: `self-assessment-at-writing.md:7`
  states the mechanism — the counter evaluates each statement "against the committed tree/history at
  `W`, not just against the current tip" — and :7 then concludes "A mismatch therefore records a
  calibration error present when the statement was written … rather than later drift." The draft's
  hedge "can distinguish" honestly preserves the file's own limits (:22 bounded extractor; :24–33
  "a correction row reads 'the stated evidence did not resolve at writing', not 'the claim was
  false'").
- It claims a design capability of the documented practice, which is what tier B underwrites here —
  it does not claim the kama counter is correct or was re-run. Correct, because the file itself
  states "no fresh counter run performed" (:2) and its baseline receipt is `met` false (:20). A
  teaches cell claiming a verified result would have been a defect.
- Single grounded benefit, one sentence, matches the contract's `teaches` spec and stays inside the
  frozen scope. PASS.

## Tier-B honesty — PASS (B is the honest tier)

Contract (`/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:26-30`):

- **Not A**: tier A means "primary or authoritative for that scope … the lane's own re-runnable gate
  output". This artifact is neither: it is not this lane's gate output, and no re-runnable instrument
  of *kotoba's* stands behind it (the described counter is kama's; the file even records that its
  author did not re-run it). A would overclaim.
- **Not C**: C is "lead only — never sole support for an admitted entry." This is a primary artifact
  of a sibling lane for its documented scope — the frozen counter sha256 `fe11d599…`, preregistration
  and baseline receipt are pinned in its frontmatter (:1–3), i.e. reproducible detail — so it can
  legitimately support the scoped entry it is cited for, which is more than a lead. C would underclaim.
- **B**: "strong secondary (expert write-up with reproducible detail)" — exact fit: a curated
  knowledge entry documenting a checked practice with frozen SHAs and a stated recheck command. B
  honest. `kind: own-work (sibling repo path)` matches the plan's frozen wording; `queued` is honest
  (the used-by entry is not yet landed, and `queued` avoids the mined-used-by integrity check firing
  on a nonexistent path). `recheck: 180d` is defensible — a committed document, not a churning page.

## Defects / notes on the draft

1. **Anchor cell omits the revision the contract requires** (`anchor — exact section / heading /
   page / line plus revision (version, commit, or publication date)`). ScribeC3 itself records the
   gap: "did not … record a content hash or commit pin" (its report :14, :86). Fix for integration:
   append `; kama commit 6de225c289b7682bf280cffb4a07de3fb7d1275c, sha256
   cd6e3730085ed08ca583604390e84c352ea122e4a6386e383d261a0a0b4cf959` to the anchor cell. Sibling
   files are mutable — the pin makes the row self-evidencing (same standard the C1 A4 arm applies to
   web snapshots this round).
2. **Located-quote backtick drop**: line 7 literally contains `` `W` ``; ScribeC3's quote drops the
   backticks. Verbatim discipline (the same honesty the r60 S106/S107 Gate lines applied, noting
   dropped markers) wants either the backticks kept or a parenthetical noting the drop.
3. **Gate line lacks access evidence**: prior Gate lines (round-60 lesson `## Gate`) carry accessed
   timestamp, byte size and sha256. ScribeC3's line carries only path + word count + UTC. My final
   Gate line below carries the evidence.
4. Minor: source cell `kama-shokunin — `../kama-shokunin/…`` is self-redundant; and the `../`
   prefix only resolves if SOURCES-relative paths are interpreted from the lane root (consistent
   with prior corpus citations such as `../verifiers/…` in README index cells and round-16/21
   `../<lane>-shokunin/…` sibling citations — the convention holds, so this is a nit, not a defect).

## Final Gate line for S117 (differs from ScribeC3's — recommended text)

Target: `corpus/lessons/round-61.md` `## Gate` — append:

```markdown
- **S117 kama-shokunin — writing-revision calibration** — `../kama-shokunin/corpus/knowledge/self-assessment-at-writing.md` — opened read-only 2026-10-23 (33 lines, 5,831 B, sha256 `cd6e3730085ed08ca583604390e84c352ea122e4a6386e383d261a0a0b4cf959`; file last committed in kama `6de225c289b7682bf280cffb4a07de3fb7d1275c` 2026-10-23T16:09:39-03:00; seats `ScribeC3`, `RevKamaRow`) — `self-assessment-at-writing.md:7`: "a calibration check, not a freshness-only check"
```

Differences from ScribeC3's Gate line: (a) access evidence added (size + sha256 + introducing
commit), closing the pin gap its own report admits; (b) my independently chosen quote — the file's
own calibration-vs-freshness name — instead of the mechanism clause (and no backtick-drop issue);
(c) both seats named, since the row now rests on an independent second open.

## Residual risk / what I could not verify

- The row is a draft; whether the L1 integrates it verbatim (with or without the anchor pin fix) is
  not observable at wave time. Same for the entry and README row — I reviewed their text for the
  bleed boundary (practice-level borrowing, "no kama domain content imported", tier-B scope
  disclaimers all present and consistent with the plan) but cannot verify the landed bytes.
- Kama's repo is live; the pin (sha256 + commit `6de225c`) is the durable reference — if the file
  changes before the counting command runs, the row's sha256 would go stale, which is exactly why
  the pin belongs in the row.
- I did not re-run kama's counter (`count-c1.py`); per the honesty rule, nothing here asserts its
  behavior — only what the committed file documents.

Installs: no installs.
Blockers: none.
Attacked/produced: audited ScribeC3's S117 row (teaches grounded — PASS; tier B honest — PASS;
anchor missing revision pin + quote backtick drop flagged) and produced a final, evidence-carrying
Gate line for S117.
