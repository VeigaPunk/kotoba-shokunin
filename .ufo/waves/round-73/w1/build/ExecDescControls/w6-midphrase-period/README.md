# w6-midphrase-period — round-73 C2 (replacement) shortcut world

**Purpose.** A period inserted mid-phrase (after "SKILL.md") so R1 reads a 60-character first sentence while the old 151-character sentence continues after it: a hollow pass on R1, R2 must fail.

**Expected under the frozen predicate (`plans/round-73-addendum-1.md`):** below 3 of 3 — a world that reads 3 is a counter defect.

## Overlay

- File: `SKILL.md` (this directory) — the lane's SKILL.md at base `072048fa8e8a52c707d25f7079772fa317244eb7` with only the frontmatter `description` value replaced; the body is byte-identical to base.
- Overlay sha256: `900931ef8f4b85ee1c80408c6643a7296ce05c6331b136bd38dd47bfb85431d1`
- Description (folded) sha256: `b5f665133b32ba60c85b5b9c0c27b2567acfddc321181872ecb9bdd7c20417ef`, fold length **1018** characters.
- First sentence: 60 characters (text before the first `. ` followed by an uppercase letter; 61 including the terminal period).
- Frontmatter block: 19 lines including both `---` delimiters (`name:` through closing `---` = 18 lines); base is 19.

**Description (folded, verbatim from this overlay's frontmatter):**

```
Prompt & skill craft — audits, writes, and rewrites SKILL.md. AGENTS.md / dispatch prompts / system prompts for trigger fidelity and decision density. Triggers: "skill file", "SKILL.md", "frontmatter description", "trigger words", "prompt craft", "write a skill", "audit this skill", "skill quality". Anti-triggers: general prompt engineering for model outputs (not skill files), runtime code changes, and domain content inside a skill's reference/ tree. Sibling boundary: kagi, kake, kasegi, kengaku and kumitate own their own SKILL.md content — this skill audits and reports; fixes route to the owning lane. chousa owns the research method; kama owns endpoint verification; kengaku owns measured capability effects of prompt format; tameshi owns the fixture and mutation method. NOT kotodama-shokunin: kotodama owns naming and language for fictional worlds despite the similar name. Note: shokunin files sit outside the omp skill discovery roots, so this text never reaches the omp router — craft here is audit-side.
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
$G add SKILL.md && $G commit -q -m 'overlay w6-midphrase-period'
cd "$P/kotoba-shokunin"
python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md \
        --province PROVINCE.md --skill SKILL.md; echo "census exit $?"
python3 -B verifiers/verify_skill_checklist.py; echo "checklist exit $?"
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-73/w1/build/ExecDescCounter/check_own_description.py \
        --repo "$P/kotoba-shokunin" --rev "$(git rev-parse HEAD)"; echo "counter exit $?"
```

The counter draft lives under `build/ExecDescCounter/` during wave 1, so it needs an explicit `--repo` (its default lane root is derived from `parent.parent`, which is correct only once it lands in `verifiers/`).

## Observed (this wave)

Sandbox-local overlay commit `62f14c7dbf5a19fa93e14560fcdd59d660bf97ee` (throwaway `--shared` clone; the sha is not in the lane and is not part of the deliverable — the overlay file sha256 above is the stable identity).

- `check_sibling_census.py …` — **exit 0**; last line: `skill description length 1018 of 1024`
  - first FAIL line: none (all rows verified, all 9 adjacent lanes named)
- `verify_skill_checklist.py` — **exit 0**; first FAIL line: none
- `check_own_description.py` (draft sha256 `58f65a371392…`) — **exit 1**, `own-description rules held 2 of 3`
- The earlier draft `d063168e5d4e…` produced byte-identical rule lines for this world (diff of the two outputs, excluding the `own-description rev` line: empty).

      description 1018 characters (R3 ceiling 1024)
      first sentence 60 characters: Prompt & skill craft — audits, writes, and rewrites SKILL.md
      R1 pass: first sentence 60 characters is inside 40-99
      R2 fail: whole words skill+prompt yes; no quoted trigger in the first 99 characters
      R3 pass: description 1018 <= 1024; verifiers/check_sibling_census.py exit 0
      frontmatter lines 19->19 (inserted 15, deleted 15 inside the frontmatter)
      own-description rules held 2 of 3

