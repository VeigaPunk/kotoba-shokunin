# ExecDescControls — round-73 C2 (replacement) shortcut worlds

Seven overlay worlds for `check_own_description.py` (frozen predicate in
`plans/round-73-addendum-1.md`). Each directory holds one full `SKILL.md`
overlay (base `072048fa8e8a52c707d25f7079772fa317244eb7` with only the frontmatter
`description` value replaced; the body is byte-identical to base) plus a README
with the folded description, its length, replay commands and the observed gate
results.

**Headline: none of the six shortcut worlds (1–6) reads 3 of 3; the honest
world (7) reads 3 of 3, exit 0.** Worlds 1–6 read 2, 2, 2, 1, 2, 2.

## Matrix (observed, this wave)

| world | description | first sentence | R1 | R2 | R3 | counter | census | checklist |
|---|---|---|---|---|---|---|---|---|
| `w1-no-quoted-trigger` | 967 | 98 (99 with `.`) | pass | **fail** | pass | exit 1, 2 of 3 | exit 0, `names 9 of 9`, `length 967 of 1024` | exit 0 |
| `w2-first-sentence-under-40` | 891 | 22 (23 with `.`) | **fail** | pass | pass | exit 1, 2 of 3 | exit 0, `names 9 of 9`, `length 891 of 1024` | exit 0 |
| `w3-quote-not-in-triggers` | 958 | 89 (90 with `.`) | pass | **fail** | pass | exit 1, 2 of 3 | exit 0, `names 9 of 9`, `length 958 of 1024` | exit 0 |
| `w4-cut-to-99-drop-triggers-siblings` | 76 | 76 | pass | **fail** | **fail** | exit 1, 1 of 3 | exit 1, `names 0 of 9`, `length 76 of 1024` | exit 1, first FAIL `trigger.literal_trigger_string` |
| `w5-over-1024` | 1130 | 87 (88 with `.`) | pass | pass | **fail** | exit 1, 2 of 3 | exit 1, `length 1130 of 1024` | exit 0 |
| `w6-midphrase-period` | 1018 | 60 (61 with `.`) | pass | **fail** | pass | exit 1, 2 of 3 | exit 0, `names 9 of 9`, `length 1018 of 1024` | exit 0 |
| `w7-honest-rewrite` | 956 | 87 (88 with `.`) | pass | pass | pass | **exit 0, 3 of 3** | exit 0, `names 9 of 9`, `length 956 of 1024` | exit 0 |

`census` = `python3 -B verifiers/check_sibling_census.py
corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md
--skill SKILL.md`; `checklist` = `python3 -B verifiers/verify_skill_checklist.py`.
Base do-nothing control, same counter version: `own-description rules held 1 of 3`,
exit 1 (R1 150 chars, R2 no quoted trigger, R3 pass) — matches the addendum's
committed control. Raw gate output for every row (and for the base) is kept in
`logs/` (`<world>.census`, `<world>.checklist`, `<world>.counter.txt`,
`base.*`).

## Measured counter version

`check_own_description.py` from `.ufo/waves/round-73/w1/build/ExecDescCounter/`,
sha256 `58f65a3713925b164e56f2e54896331bac623197e957191a161240fd715627e9`
(hash verified identical before the base run, before the seven-world pass and
after it). The file was under active rewrite during this wave: four distinct
hashes were observed — `67ce5b8b…` (failed at import,
`NameError: name 'SKILL' is not defined`, caught mid-edit), `8f6963…`,
`4f565e2c…`, `d063168e…`, then the measured `58f65a37…`. The two versions
actually exercised — `d063168e…` and `58f65a37…` — produced **byte-identical
rule lines for all seven worlds** (diff excluding the `own-description rev`
line: empty), and the base control reads `1 of 3` on both. (An earlier,
unpinned build at ~21:03 gave the same N values for all seven worlds but was
not compared byte-wise.) Every number above belongs to `58f65a37…`; re-run
after integration.

## Replay (one world)

```sh
P=$(mktemp -d /tmp/k73-replay.XXXX)
for e in /home/vgpnk/Projects/shokunin/* /home/vgpnk/Projects/shokunin/.[!.]*; do
  b=$(basename "$e"); [ "$b" = kotoba-shokunin ] && continue
  ln -s "$e" "$P/$b"
done
git clone --shared -q --no-checkout /home/vgpnk/Projects/shokunin/kotoba-shokunin "$P/kotoba-shokunin"
git -C "$P/kotoba-shokunin" checkout -q 072048fa8e8a52c707d25f7079772fa317244eb7
cp w7-honest-rewrite/SKILL.md "$P/kotoba-shokunin/SKILL.md"
G="git -C $P/kotoba-shokunin -c user.name=replay -c user.email=replay@local.invalid"
$G add SKILL.md && $G commit -q -m 'overlay w7-honest-rewrite'
cd "$P/kotoba-shokunin"
python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md \
        --province PROVINCE.md --skill SKILL.md; echo "census exit $?"
python3 -B verifiers/verify_skill_checklist.py; echo "checklist exit $?"
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-73/w1/build/ExecDescCounter/check_own_description.py \
        --repo "$P/kotoba-shokunin" --rev "$(git rev-parse HEAD)"; echo "counter exit $?"
```

The sandbox **must** symlink hidden fleet entries (`.[!.]*`): a loop over
`/home/vgpnk/Projects/shokunin/*` alone leaves `../.ufo/...` citations dangling and
makes `verify_skill_checklist.py` exit 1 on `trigger.citation_resolves` /
`governance.citation_resolves` for reasons unrelated to the world. That is the
same class of hand-run/sandbox divergence as M127. `verifiers/check_tip_battery.py`'s
`build_sandbox` uses `fleet.iterdir()`, which includes hidden entries.

## Notes for the reviewer

- **World 6 is the pre-registered hollow pass on R1**: the first sentence is a
  fragment (`Prompt & skill craft — audits, writes, and rewrites SKILL.md`)
  and the rest of the old 151-character sentence continues after it
  (`AGENTS.md / dispatch prompts / system prompts for …`). R1 reads only the
  first sentence, so it passes at 60 characters; R2 still refuses it. The
  addendum assigns the hollowness judgement to the non-author reviewer.
- **R1's off-by-one**: the addendum's base figure is 151 characters; the
  counter measures the text *before* the separating `.`, printing 150 for the
  base. Both conventions leave every world on the same side of the 40–99
  bounds except world 1, where 98 vs 99 are both inside.
- **R2 is double-quote-only** (the counter's `QUOTED` regex), matching the
  predicate's wording; single-quoted or backticked triggers would not count.
- Worlds were committed only inside a throwaway `--shared` clone under `/tmp`;
  the commit shas in the per-world READMEs are sandbox-local, not lane objects.
