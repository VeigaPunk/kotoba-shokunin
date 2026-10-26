# w2-first-sentence-under-40 — round-73 C2 (replacement) shortcut world

**Purpose.** A 22-character first sentence (23 with the period): R1's lower bound must fail while R2 and R3 stay satisfiable.

**Expected under the frozen predicate (`plans/round-73-addendum-1.md`):** below 3 of 3 — a world that reads 3 is a counter defect.

## Overlay

- File: `SKILL.md` (this directory) — the lane's SKILL.md at base `072048fa8e8a52c707d25f7079772fa317244eb7` with only the frontmatter `description` value replaced; the body is byte-identical to base.
- Overlay sha256: `2777e75fbb0cbdb5b5a00da782f1df469719b3e1f0e61b8cdc1d54199215a964`
- Description (folded) sha256: `7c532a8964a0d1c4ed78138ed32789ca15cd425aec6f49f9ae1a6f26cec4f1f2`, fold length **891** characters.
- First sentence: 22 characters (text before the first `. ` followed by an uppercase letter; 23 including the terminal period).
- Frontmatter block: 19 lines including both `---` delimiters (`name:` through closing `---` = 18 lines); base is 19.

**Description (folded, verbatim from this overlay's frontmatter):**

```
Skill and prompt craft. Triggers: "skill file", "SKILL.md", "frontmatter description", "trigger words", "prompt craft", "write a skill", "audit this skill", "skill quality". Anti-triggers: general prompt engineering for model outputs (not skill files), runtime code changes, and domain content inside a skill's reference/ tree. Sibling boundary: kagi, kake, kasegi, kengaku and kumitate own their own SKILL.md content — this skill audits and reports; fixes route to the owning lane. chousa owns the research method; kama owns endpoint verification; kengaku owns measured capability effects of prompt format; tameshi owns the fixture and mutation method. NOT kotodama-shokunin: kotodama owns naming and language for fictional worlds despite the similar name. Note: shokunin files sit outside the omp skill discovery roots, so this text never reaches the omp router — craft here is audit-side.
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
$G add SKILL.md && $G commit -q -m 'overlay w2-first-sentence-under-40'
cd "$P/kotoba-shokunin"
python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md \
        --province PROVINCE.md --skill SKILL.md; echo "census exit $?"
python3 -B verifiers/verify_skill_checklist.py; echo "checklist exit $?"
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-73/w1/build/ExecDescCounter/check_own_description.py \
        --repo "$P/kotoba-shokunin" --rev "$(git rev-parse HEAD)"; echo "counter exit $?"
```

The counter draft lives under `build/ExecDescCounter/` during wave 1, so it needs an explicit `--repo` (its default lane root is derived from `parent.parent`, which is correct only once it lands in `verifiers/`).

## Observed (this wave)

Sandbox-local overlay commit `2afb3e846df0913e0394e3d5f3cfbb14c1c97860` (throwaway `--shared` clone; the sha is not in the lane and is not part of the deliverable — the overlay file sha256 above is the stable identity).

- `check_sibling_census.py …` — **exit 0**; last line: `skill description length 891 of 1024`
  - first FAIL line: none (all rows verified, all 9 adjacent lanes named)
- `verify_skill_checklist.py` — **exit 0**; first FAIL line: none
- `check_own_description.py` (draft sha256 `58f65a371392…`) — **exit 1**, `own-description rules held 2 of 3`
- The earlier draft `d063168e5d4e…` produced byte-identical rule lines for this world (diff of the two outputs, excluding the `own-description rev` line: empty).

      description 891 characters (R3 ceiling 1024)
      first sentence 22 characters: Skill and prompt craft
      R1 fail: first sentence 22 characters is outside 40-99
      R2 pass: whole words skill+prompt yes; quoted trigger "skill file", "SKILL.md", "frontmatter description" (in the Triggers list)
      R3 pass: description 891 <= 1024; verifiers/check_sibling_census.py exit 0
      frontmatter lines 19->19 (inserted 15, deleted 15 inside the frontmatter)
      own-description rules held 2 of 3

