# w5-over-1024 — round-73 C2 (replacement) shortcut world

**Purpose.** The honest rewrite plus padding to 1130 characters: R1 and R2 hold, R3's ceiling must fail.

**Expected under the frozen predicate (`plans/round-73-addendum-1.md`):** below 3 of 3 — a world that reads 3 is a counter defect.

## Overlay

- File: `SKILL.md` (this directory) — the lane's SKILL.md at base `072048fa8e8a52c707d25f7079772fa317244eb7` with only the frontmatter `description` value replaced; the body is byte-identical to base.
- Overlay sha256: `a0cf83984da8aa1d0da8aff63815dcaaba90c7a38e0bdec2b3d0f514db870795`
- Description (folded) sha256: `e7956ce1828ef253f2d9752c695d00eb2f4f372a299d2c08a62dfc00dd24f288`, fold length **1130** characters.
- First sentence: 87 characters (text before the first `. ` followed by an uppercase letter; 88 including the terminal period).
- Frontmatter block: 19 lines including both `---` delimiters (`name:` through closing `---` = 18 lines); base is 19.

**Description (folded, verbatim from this overlay's frontmatter):**

```
Prompt & skill craft — audits a "skill file" for prompt triggering and decision density. Triggers: "skill file", "SKILL.md", "frontmatter description", "trigger words", "prompt craft", "write a skill", "audit this skill", "skill quality". Anti-triggers: general prompt engineering for model outputs (not skill files), runtime code changes, and domain content inside a skill's reference/ tree. Sibling boundary: kagi, kake, kasegi, kengaku and kumitate own their own SKILL.md content — this skill audits and reports; fixes route to the owning lane. chousa owns the research method; kama owns endpoint verification; kengaku owns measured capability effects of prompt format; tameshi owns the fixture and mutation method. NOT kotodama-shokunin: kotodama owns naming and language for fictional worlds despite the similar name. Note: shokunin files sit outside the omp skill discovery roots, so this text never reaches the omp router — craft here is audit-side. Padding for the length control: trigger fidelity, decision density, audit-side craft, sibling routing, exclusion vocabulary, quoted triggers, and frontmatter line stability.
```

## Replay

Every gate below was run from a fleet-shaped sandbox of the base. The sandbox must symlink **hidden** fleet entries too (`.ufo`, `.omp`, ...): a loop over `/home/vgpnk/Projects/shokunin/*` alone leaves `../.ufo/...` citations dangling and makes `verify_skill_checklist.py` exit 1 for reasons unrelated to this world.

```sh
P=$(mktemp -d /tmp/k73-replay.XXXX)
for e in /home/vgpnk/Projects/shokunin/* /home/vgpnk/Projects/shokunin/.[!.]*; do
  b=$(basename "$e"); [ "$b" = kotoba-shokunin ] && continue
  ln -s "$e" "$P/$b"
done
git clone --shared -q --no-checkout /home/vgpnk/Projects/shokunin/kotoba-shokunin "$P/kotoba-shokunin"
git -C "$P/kotoba-shokunin" checkout -q 072048fa8e8a52c707d25f7079772fa317244eb7
cp SKILL.md "$P/kotoba-shokunin/SKILL.md"   # this directory's overlay
G="git -C $P/kotoba-shokunin -c user.name=replay -c user.email=replay@local.invalid"
$G add SKILL.md && $G commit -q -m 'overlay w5-over-1024'
cd "$P/kotoba-shokunin"
python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md \
        --province PROVINCE.md --skill SKILL.md; echo "census exit $?"
python3 -B verifiers/verify_skill_checklist.py; echo "checklist exit $?"
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-73/w1/build/ExecDescCounter/check_own_description.py \
        --repo "$P/kotoba-shokunin" --rev "$(git rev-parse HEAD)"; echo "counter exit $?"
```

The counter draft lives under `build/ExecDescCounter/` during wave 1, so it needs an explicit `--repo` (its default lane root is derived from `parent.parent`, which is correct only once it lands in `verifiers/`).

## Observed (this wave)

Sandbox-local overlay commit `0f731434d13999d26cac92bd04328c591524343d` (throwaway `--shared` clone; the sha is not in the lane and is not part of the deliverable — the overlay file sha256 above is the stable identity).

- `check_sibling_census.py …` — **exit 1**; last line: `skill description length 1130 of 1024`
  - first FAIL line: `FAIL skill description length 1130 is outside 1-1024 characters (S018: the description field must be 1-1024 characters)`
- `verify_skill_checklist.py` — **exit 0**; first FAIL line: none
- `check_own_description.py` (draft sha256 `58f65a371392…`) — **exit 1**, `own-description rules held 2 of 3`
- The earlier draft `d063168e5d4e…` produced byte-identical rule lines for this world (diff of the two outputs, excluding the `own-description rev` line: empty).

      description 1130 characters (R3 ceiling 1024)
      first sentence 87 characters: Prompt & skill craft — audits a "skill file" for prompt triggering and decision density
      R1 pass: first sentence 87 characters is inside 40-99
      R2 pass: whole words skill+prompt yes; quoted trigger "skill file" (in the Triggers list)
      R3 fail: description 1130 > 1024; verifiers/check_sibling_census.py exit 1: FAIL skill description length 1130 is outside 1-1024 characters (S018: the description field must be 1-1024 characters)
      frontmatter lines 19->19 (inserted 15, deleted 15 inside the frontmatter)
      own-description rules held 2 of 3

