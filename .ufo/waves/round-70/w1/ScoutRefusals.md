# ScoutRefusals — round 70, wave 1 (kotoba)

Seat: `L1Kotoba70.ScoutRefusals` (read-only scout). Run 2026-10-25 ~11:56–12:05 UTC against lane tip
`16b212a390c7ce68b6bce49b2c3766b154fbcbae`. Scratch: `/tmp/k70w1-ScoutRefusals.XXXX`, deleted on
return. Tools installed or updated: none (curl, git, python3, sha256sum, diff are already on the host).

## Verdict

All four refusals in `corpus/lessons/round-70.md` § Gate (lines 72–90) **hold as outcomes**: nothing
should be admitted. Two of them have a reason or flip that is not an observed fact:

| Refusal | Reason an observed fact (Q62)? | Flip real? | Verdict |
|---|---|---|---|
| S285/S286 (raw `.mdx`) | **Yes** — re-observed: the prose is identical, and all 4 entry quotes are present in the `.mdx` | **Yes**, checkable, currently not met | **Agree** |
| S301 (claude.com post) | **Mostly** — the comparator quote is verbatim, and S209 covers the baselines and blind comparison | **No** — the flip's premise "S209 does not describe [blind comparators]" is **false** (S209 line 214) | **Agree** with the refusal; **disagree** with the flip |
| S303 (`improve_description.py`) | **Yes** — lines 64 and 68, the pass rule in `run_eval.py` 231–234, and no citing entry are all confirmed | **Yes** — the script rewrites descriptions through `claude -p` | **Agree** |
| `english-leads-relocated-round9.md` | **Yes** — the entry's negatives are unbounded, and round 70 has no OpenAI sweep receipt | It can be run (I ran it), but it **refutes** the entry rather than flipping it | **Agree**, but **understated**: the entry is false, not merely unswept |

The heaviest finding: the OpenAI page the registry lead names **exists**. It is at
`https://developers.openai.com/blog/eval-skills.md`, is listed in OpenAI's blog `llms.txt`, carries
the `id,should_trigger,prompt` CSV protocol, and has Wayback 200 captures from 2026-01-24, nine months
before the staged entry said "That page does not exist."

---

## 1. S285/S286 — raw `.mdx` duplicates of S210/S209 — AGREE

Refusal (lesson lines 74–77): "the same documents S209/S210 already cite, observed by fetching both
forms; a second row per document adds no fact (CORPUS.md rule 4). Flip: the rendered `.md` and the
repository source diverge on a quoted sentence."

Staged rows (`/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md:89-90`): S285 is
`optimizing-descriptions.mdx` (13151 B) and S286 is `evaluating-skills.mdx` (16755 B).

**Fetch** (`curl -sSL -o S285.mdx -w '%{http_code} %{size_download}' …/docs/skill-creation/optimizing-descriptions.mdx`, and the same for evaluating-skills):
```
S285 200 13151
S286 200 16755
```
These byte sizes equal the staged rows. `git ls-remote https://github.com/agentskills/agentskills refs/heads/main` →
`69ef37e9424c0a7ea9dd2293b559e43ec8176379`.

**Prose diff after normalising markup.** I diffed the lane snapshots against the `.mdx` after
normalising `* `→`- `, dropping ` theme={null}`, folding absolute `agentskills.io/…​.md` links to `/…`,
and dropping `[!TIP]`/`<Tip>` wrappers and blank lines:
- S209 vs S286: the only remaining hunk is lines 1–5 (the rendered "Documentation Index" banner and
  H1 versus the `.mdx` YAML front matter).
- S210 vs S285: the front-matter hunk, plus `\~60%`/`\~40%` versus `~60%`/`~40%` and nested `*`/`-`
  bullets. No sentence differs.

**Quotes the admitted entry relies on, counted in the `.mdx`** (`grep -cF`):
```
The main file you author by hand is `evals/evals.json`. :: S286=1
recording **PASS** or **FAIL** with specific evidence :: S286=1
Not everything needs an assertion. :: S286=1
S210 quote :: S285=1   ("A should-trigger query passes if its trigger rate is above a threshold (0.5 is a reasonable default).")
```

**CORPUS.md rule 4** (`/home/vgpnk/Projects/shokunin/CORPUS.md` line 123): "Expansion is knowledge,
not rows … There is no row quota; a short registry of opened, honestly tiered rows beats a long one."
It supports the refusal, though it is a general principle rather than a no-duplicate-document rule.

**Flip:** real and mechanically checkable; I ran it above, and today it is not met.

**Gap (provenance, not falsity):** "observed by fetching both forms" has no committed receipt. The
`.ufo/waves/round-70/snapshots/` directory holds only S209–S211, and
`rg -l -i 'S285|S286|\.mdx' .ufo/waves/round-70` (excluding `w1/`) hits no fetch log. The
observation is true, but it is re-derived here, not pinned.

## 2. S301 — claude.com "Improving skill-creator…" — AGREE with refusal, DISAGREE with flip

Refusal (lesson lines 78–81): "its evaluation claims ("comparator agents for A/B comparisons: two
skill versions, or skill vs. no skill") restate what S209 states as the specification with tier-A
authority. Flip: an entry about blind comparators, which S209 does not describe."

**Fetch:** `curl -sSL -A 'Mozilla/5.0' … improving-skill-creator-test-measure-and-refine-agent-skills`
→ `S301 200 585760`. I extracted the text with a regex strip (`S301.txt`, 1638 words).
- Date "March 3, 2026" is at text line 110.
- Text lines 161–162: "comparator agents / for A/B comparisons: two skill versions, or skill vs. no
  skill. They judge outputs without knowing which is which, so you can tell whether a change
  actually helped." The lesson's quote is verbatim.

**What S209 covers** (`grep -n -i 'blind\|comparator\|baseline\|without the skill\|no skill\|previous version' snapshots/S209-evaluating-skills.md`):
- L52: "run each test case twice: once **with the skill** and once **without it** (or with a previous version)"
- L110–112: the without-skill baseline, and the previous version as the baseline
- **L212–214** (a `[!TIP]` under § Grading outputs, line 168, before § Aggregating results, line 216):
  "For comparing two skill versions, try **blind comparison**: present both outputs to an LLM judge
  without revealing which came from which version."
- L90: "Each eval run should start with a clean context". This also covers S301's "clean context" /
  no cross-contamination point.

**Reason assessment:** largely an observed fact. S301's comparison and isolation claims are present
in S209. It slightly overreaches, because S301 states facts S209 does not:
- blind judging of **skill vs. no skill** (S209's blind tip names only "two skill versions");
- "improved triggering on 5 out of 6 public skills" (text line 165);
- availability in Claude.ai, Cowork and the Claude Code plugin.

No admitted entry needs any of these, so the outcome stands.

**Flip assessment: not real as worded.** Its premise, "S209 does not describe [blind comparators]",
is an assertion about what a source lacks, which is the failure mode Q62 names (`corpus/QUALITY.md`
line 78), and it is **false**: S209 L214 describes blind comparison by name. An entry about blind
comparators would be grounded on S209 at tier A, so the flip would never move S301. The only narrower
flip that would work is an entry on blind judging of skill vs. no-skill runs, or on the 5-of-6
triggering result.

Per Q62, the correction is an appended notice, not a rewrite of the refusal.

**Side gap:** `corpus/SOURCES.md` § Leads (lines 232–233 and 274–275) still lists "Claude blog —
Improving skill-creator: Test, measure, and refine Agent Skills" as unopened. Round 70 opened that
page (S301) but the lesson does not say the lead stays open or is resolved. The staged S301 row's
`teaches` cell (the post exists, on claude.com) is the one fact S301 adds that the refusal does not
address.

## 3. S303 — `improve_description.py` — AGREE

Refusal (lesson lines 82–84): "classifies results by `should_trigger` (lines 64, 68) but the pass
rule the entry states lives in `run_eval.py`; no admitted entry cites it. Flip: an entry about
automated description rewriting."

**Commands and output:**
- `curl -sSL … anthropics/skills/main/skills/skill-creator/scripts/improve_description.py` →
  `S303 200 11116`.
- `git ls-remote https://github.com/anthropics/skills refs/heads/main` →
  `dbd4588f9e1033efb41dad4bef2f7947c8993d44`.
- sha256 of the main bytes equals the pinned `dbd4588` bytes: both are `87d86457…accf80`.
- `grep -n should_trigger S303.py` →
  ```
  64:        if r["should_trigger"] and not r["pass"]
  68:        if not r["should_trigger"] and not r["pass"]
  ```
  The line numbers match the lesson.
- `grep -n 'threshold\|trigger_rate\|>=' S303.py` → no output, so the improver states no pass rule.
- The pass rule is in `snapshots/S211-run_eval.py.txt`:
  ```
  231: if should_trigger:
  232:     did_pass = trigger_rate >= trigger_threshold
  234:     did_pass = trigger_rate < trigger_threshold
  ```
- `rg -n 'S301|S303|improve_description|claude.com/resources' corpus SKILL.md` → hits only in the
  refusal text (`skill-eval-artefacts-round70.md:64`, and `lessons/round-70.md` lines 78, 82, 108).
  No entry cites S303.

**Flip:** real. The script's lines 20–48 define `_call_claude` (a `claude -p` subprocess), lines
50–175 build a prompt and parse `<new_description>…</new_description>` (lines 142, 146, 175), and
line 220 `new_description = improve_description(…)`. That is automated description rewriting.

**Extra, strengthening the refusal:** the staged S303 `teaches` cell (`SOURCES.append.md:107`) says
the label is implemented "by Anthropic's skill-creator and not by OpenAI". The "not by OpenAI" half is
refuted by finding 4.

## 4. `english-leads-relocated-round9.md` — AGREE with refusal; the reason is a fact but understated, and the flip is mis-specified

Refusal (lesson lines 85–90): the central claim is a negative over a whole vendor's documentation;
"this round ran no bounded sweep of that documentation (Q62 …). Flip: a logged, bounded sweep of
OpenAI's docs index. The registry lead naming an OpenAI 'Testing Agent Skills Systematically with
Evals' page … stays a lead, unopened."

**Is the reason an observed fact?** Yes, on both halves.
- The staged entry's title is "…OpenAI publishes skills but never that protocol". Its body says
  "That page does not exist", "OpenAI's own documentation index names no skills page at all", and
  "has no referent in OpenAI's documentation at all". Those are unbounded negatives, even though its
  counted sweep covered only three pages.
- `rg -l -i 'openai' .ufo/waves/round-70` (excluding `w1/`) hits only W04 S086 duplicate-URL census
  lines (`receipts/census-before.txt:8`, `assimilation/census-validate-append.txt:10`). Round 70 has
  no OpenAI sweep receipt.

**Running the flip's bounded sweep.** Here is what it shows, all fetched 2026-10-25:
1. Top-level index: `curl https://developers.openai.com/llms.txt` → `200 6201`, 47 lines,
   `grep -i skill` = 0. The entry's "index names no skills page" is true **only at the top level**.
   The index routes to 12 sub-indexes.
2. The 12 sub-indexes, all 200. `grep -c -i skill`: blog 5, codex 8, cookbook 2, plugins 5,
   showcase 2, learn.chatgpt.com 8 (byte-identical to codex), and 0 for the other six. Skill-titled
   links: 10 pages, including
   `[Testing Agent Skills Systematically with Evals](https://developers.openai.com/blog/eval-skills.md)`
   (`blog/llms.txt` line 37).
3. Pages fetched, all 200, with `should_trigger` counts:
   ```
   blog/eval-skills.md                 should_trigger=2
   api/docs/guides/tools-skills.md     0   (S310 — staged claim holds)
   cookbook/examples/skills_in_api.md  0
   plugins/concepts/skills.md          0
   plugins/build/skills.md             0
   blog/skills-shell-tips.md           0
   blog/skills-agents-sdk.md           0
   blog/rethinking-skills-and-prompts-for-gpt-6-astra.md 0
   learn.chatgpt.com build-skills / skills-and-plugins / enterprise/skills  0 each
   ```
4. `blog/eval-skills.md`: sha256 `6cf414bb…94d3a2`, 19356 B, H1 "Testing Agent Skills Systematically
   with Evals". Line 162 is `id,should_trigger,prompt`; line 181 is "Including at least one
   `should_trigger=false` case helps catch **false positives**". That is the "should_trigger CSV
   protocol" exactly as the registry lead describes it.
5. Existence before the staged entry was written:
   - `web.archive.org/cdx … url=developers.openai.com/blog/eval-skills` → captures with status 200
     at `20260124012727`, `20260124012932`, `20260124013002`, `20260130…`, and `20261016083449`.
   - The `id_` capture from 20260124012727 (130655 B) contains the title and 2 occurrences of
     `should_trigger`.
   - The page's live `last-modified: Sat, 24 Oct 2026 23:13:53 GMT` is the site-build time, not
     publication: `api/docs/guides/tools-skills` shows 23:16:29 the same night.

**Assessment.** The refusal is correct and correctly invokes Q62, but it is **understated**. The
staged entry is not merely unswept: its central claim ("That page does not exist", "OpenAI … never
that protocol") is **false**, and it was already false when it was written on 2026-10-24. Its three
per-page zero counts are true, but they are not the claim.

The flip is runnable (1 + 12 + 11 fetches, under 2 s). As worded, though, "a logged, bounded sweep"
turns the refusal into an admit just by being run. Run, it refutes the entry. A correct flip would be
"a bounded sweep returning zero `should_trigger` across OpenAI's skill pages", and that condition is
now known to fail.

The lesson's "The registry lead … stays a lead, unopened" leaves a **correct** lead unopened. It is
openable at `https://developers.openai.com/blog/eval-skills.md` (tier-B vendor blog), and the
should_trigger protocol has three homes, not two: the specification (S210, 7 occurrences of
`should_trigger`), Anthropic's skill-creator (S124, S211, S303), and OpenAI's blog.

Per Q62, the correction is an appended notice (and a new row if the lead is opened), never a rewrite
of the refusal text.

## Confidence and remaining unknowns

- High confidence on all four verdicts. Every finding was re-fetched by this seat today, and the
  hashes and line numbers are above.
- The S301 text was extracted with a regex HTML strip, not a renderer. Line numbers refer to the
  derived `S301.txt`, and the quoted sentences were checked by eye against that text.
- Not checked: whether `blog/eval-skills.md` existed under that exact `.md` URL on 2026-10-24.
  Wayback captured the HTML route. Its presence in `blog/llms.txt` was observed only today.
- Not run: the lane's verifiers (`check_skill_evals.py`, `check_r69_routed_repairs.py`), which are
  outside this question.
- Side note, outside scope: § Leads also lists "anthropics/skills — skill-creator/SKILL.md" as
  unopened, although S124 (`corpus/SOURCES.md:135`) opened it.
