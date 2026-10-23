Result: MIXED — All six rejects have real opened or built candidates and C2's withdrawal is supported, but the rejection heading and plugin-path wording overstate what was refused.

# Scope and axes

Seat: KotobaR58.CriticGateReject. Target: content commit `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe`, `corpus/lessons/round-58.md:17-34`, against its named W0/build/control receipts and plan erratum 1. This is a scoped critic review, not round admission or a canonical trend judgment.

Axes: **calibration**, especially accurate rejection scope and chronology; supporting concerns are source/provenance fidelity and discernment. A syntactic exclusion from the frozen C1 counter is not, by itself, a finding that the documented feature is false or unusable.

I read existing receipts and selected captured source bytes, and used read-only Git to inspect chronology and the C2 shortcut. I did not rerun a counter, self-test, client, or judge. Reported counter results below are explicitly the named seats' recorded observations.

# Verdict per reject

## 1. C2 counter as a claim gate — REAL; withdrawal supported

Target: `corpus/lessons/round-58.md:19-22`.

- The rejected object was actually built: `verifiers/check_sweep_mutants.py` and its predicate are specified in `plans/round-58.md:75-84` and first committed at the frozen-counter revision.
- The shortcut was actually built and scored: `.ufo/waves/round-58/controls/CtlC2SourceGrep.md:7-15,75-105` identifies **sandbox c6b6f306bb21e64be05a530bf3c01fd78577a9c0 (/fast/scratch/hyaku/kotoba-r58/CtlC2SourceGrep)**. The recorded command at `:80` exited 0 and printed `sweep mutants killed 11 of 11; equivalents survived 5 of 5`. Pristine and restored runs printed 4 of 11 and 5 of 5, exit 1 (`:45-73,107-137`).
- I independently read that sandbox commit's diff with Git. It inserts source-text membership checks, two spelling canonicalizations, and `return int(bool(missing))` before the original behavioral body. This directly supports the lesson's description; it is not merely a claimed shortcut or an unbuilt idea.
- The lesson refuses the counter **as a claim gate**, not the existence of the counter or the subsequent R3 repair. Plan erratum 1 says exactly that (`plans/round-58.md:86-95`); `SKILL.md:465` explicitly says `claim withdrawn r58 before data` and `not a claim gate until redesigned and re-controlled`.

**Verdict:** a substantive validity refusal, not a non-event. A successful shortcut score is the reason for withdrawing the claim, not evidence that the claimed behavioral discrimination was achieved.

## 2. Copilot CLI `.claude/commands/` as row token — REAL; frozen-rule exclusion only

Target: `corpus/lessons/round-58.md:23-24`.

- `.ufo/waves/round-58/w0/CensusCopilotCLI.md:9-43` records the actual opened command-reference page, its metadata, exact path, and the foreign-marker/E5 failures. `build/SrcCopilotCLI.md:7-9,20` explicitly leaves the path in prose while omitting a counted token.
- I read the captured command reference at `/tmp/round58-srccopilotcli/cli-command-reference.md:1334`. Its unshaped 13-word sentence is: `Commands are an alternative to skills stored as individual `.md` files in `.claude/commands/`.`
- Fetch provenance is in the census at `:13-16`: `https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md`, `Fri 23 Oct 2026 07:39:09 AM UTC`, HTTP 200, 461944 bytes, sha256 `c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9`.
- The fixed row rule expressly rejects another client's marker and shared tokens (`plans/round-58.md:39-44`).

**Verdict:** real candidate and real refusal **as a C1 row token**. The same evidence affirmatively documents Copilot CLI support for this shared path; it does not establish a lack of command-file support. The lesson's explicit “as its row token” qualifier is important and should remain.

## 3. Copilot CLI `com.github.copilot/commands/` — REAL; reason needs narrower wording

Target: `corpus/lessons/round-58.md:25-26`.

- The actual captured S028 page prints the path in its Slash commands row at `/tmp/round58-srccopilotcli/cli-plugin-reference.md:159`; `:152-164` establishes the client-specific Agent Plugins 1.0 namespace and format restriction.
- The same source was opened in W0 and reopened during build: `w0/CensusCopilotCLI.md:49-52,56-81`; `build/SrcCopilotCLI.md:13,38`. Build provenance: `https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference.md`, `Fri Oct 23 08:08:39 AM UTC 2026`, HTTP 200, 47200 bytes, sha256 `d0d362cc5aa2ef84775145e499596c7e6529531c7b29972ae29f547b5da220d0`.
- Its first segment is not dot-led and contains interior dots, so the frozen grammar excludes it. This is enough to sustain the refusal without a semantic claim about who can author it.
- **Counterexample to the broad reason:** `w0/CensusCopilotCLI.md:69` marks “Folder where a user writes slash-command files” **YES, inside an Agent Plugins 1.0 plugin**. The captured authoring page also instructs the reader to create a plugin directory (`/fast/scratch/hyaku/kotoba-r58/ScoutCopilotPrompts/plugins-creating.body:23-27`) and locates commands inside that plugin (`:21`). Calling the path simply “not a user folder” can be read as denying user-authored command files there, which these receipts do not support.

**Verdict:** real syntactic row exclusion, not a fake reject; the categorical “not a user folder” gloss is unnecessary and overbroad. See correction F2.

## 4. `.github/prompts/` attributed to Copilot CLI — REAL; product-scope refusal supported

Target: `corpus/lessons/round-58.md:27-29`.

- `build/ScoutCopilotPrompts.md:110-134` records opened prompt-file concepts/tutorial pages, their actual paths and IDE availability statements, rather than inventing an unobserved candidate.
- I read `/fast/scratch/hyaku/kotoba-r58/ScoutCopilotPrompts/concepts-prompt-files.body:5,11`: it prints the repository prompt path and says `Prompt files are available in Visual Studio Code, Visual Studio, JetBrains IDEs, and Xcode.` No Markdown bytes were stripped from that substring.
- Provenance: `https://docs.github.com/en/copilot/concepts/prompting-and-context/prompt-files.md`, `Fri 23 Oct 2026 08:10:29 AM UTC`, HTTP 200, 2316 bytes, sha256 `73b58a8dd61fd374eeaa508cbb5a8dbe1b63f590686adbcbef1fc6d750cfbd20` (`build/ScoutCopilotPrompts.md:114`). The bounded CLI docs-source/README/changelog search and lane-corpus grep are recorded at `:9-26`; this is not evidence about undocumented binary behavior.
- The separate attribution control was built and measured: `controls/CtlC1SharedLabel.md:256-284`, **sandbox 9093047e690c030d1d85228799afae0fbe8fbe6e (/fast/scratch/hyaku/kotoba-r58/CtlC1SharedLabel)**. Its recorded fetch run printed `custom command files found on the live page 1 of 1; new ground 0`, marked Copilot CLI BACKED, and exited 1. The lesson correctly reports F=1, not a predicate success.

**Verdict:** real scope rejection, and the lesson honestly distinguishes human scope review from the counter's row-level false attribution. “Printed only” should be read as the opened/swept surfaces, not an exhaustive claim about all possible documentation.

## 5. opencode served URL as S095 — REAL; quote-transport/source-URL refusal only

Target: `corpus/lessons/round-58.md:30-32`.

- `build/Srcopencode.md:17-29` records a real plain GET of `https://opencode.ai/v2/docs/commands/`: `Fri Oct 23 08:08:16 AM UTC 2026`, HTTP 200, 32304 bytes, sha256 `32591ac3db0056fdbf3b5e20b78e70514da0d7306707cbf7c412ca19276640e0`.
- The same seat records direct frozen-function calls: served URL `found_on_page` output `False`, command exit 0 (`:50-54`); pinned raw source output `True`, command exit 0 (`:45-48`). Its diagnosis is HTML tag-induced whitespace before the final period, not an absent command-file fact.
- I read the selected source capture `/fast/scratch/hyaku/kotoba-r58/Srcopencode/commands.mdx:21`; it contains the same locations and the exact selected sentence. Pinned URL/fetch/hash provenance is fully recorded at `build/Srcopencode.md:31-43`.

**Verdict:** an observed rejected scored URL, not a hypothetical failure. It must not be inflated into rejection of opencode's documented command-file behavior. The lesson already says “as the S095 URL,” correctly narrowing the decision.

## 6. Cursor `.cursor/commands/[command].md` — REAL; counted-token/source exclusion, not blanket fact rejection

Target: `corpus/lessons/round-58.md:33-34`.

- `w0/CensusCursor.md:62-72` records the actual opened changelog HTML, the printed filename pattern, and refusal under the no-changelog rule. It also notes that the bracketed pattern fails the frozen path regex.
- `build/SrcCursor.md:17` records the build reopen: `https://cursor.com/changelog/1-6`, `Fri Oct 23 08:10:18 AM UTC 2026`, HTTP 200, 145839 bytes, sha256 `8d2a8bcfbbd6f0d6a7e76cc4535106d5384a471564ba98e6cbe166be6a8f5152`, HTML line 2. The report explicitly calls this supplemental, not the scored source.
- **Strongest counterexample to the heading “not admitted”:** `corpus/SOURCES.md:106` has S094 at `mined` and explicitly retains that same changelog URL as supplemental filename/invocation evidence; its teaches cell retains a `[command].md` form. Thus this is not an entirely unadmitted source/fact. It is a rejected scored token/source choice with supplemental evidence retained.

**Verdict:** a real selection refusal, not a non-event. Narrow the heading/label rather than claiming the filename fact was wholly rejected. See F1.

# C2 chronology: what “before data” actually establishes

Read-only Git observations, exit 0:

```sh
timeout 30 git --no-optional-locks log --format='%H %cI %s' f56f6e191762c27c1aa2af11a204db9e2ca4edec..8e52f064f21580dff368b50a2a2d304ecccaaea9
```

Observed revision/time order (UTC converted from the printed `-03:00` offset):

| Event | Revision | UTC |
|---|---|---|
| Plan draft | `8db2070270147510e4729f04d657168c265229e4` | 07:34:43Z |
| Frozen counters/targets | `3de87aad29e960c95ed35840442f424c48c29729` | 07:51:33Z |
| Erratum 1 + control receipts | `a39942c94027cd3875144284112422d1aa642260` | 08:07:32Z |
| Submitted content | `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe` | 08:20:32Z |
| Measurement/index receipts | `8e52f064f21580dff368b50a2a2d304ecccaaea9` | 08:24:50Z |

I also ran, exit 0:

```sh
timeout 30 git --no-optional-locks show --format=fuller --stat a39942c94027cd3875144284112422d1aa642260
timeout 30 git --no-optional-locks show --format=short a39942c94027cd3875144284112422d1aa642260 -- plans/round-58.md
```

Observed: the erratum commit includes `controls/CtlC2SourceGrep.md` and adds the withdrawal paragraphs to the plan. It does not replace the C2 predicate. The plan's `~08:05Z` is an approximate in-text decision time; Git independently establishes commitment at 08:07:32Z, not the exact decision time.

The first R3 executor baseline is stamped 08:09:40Z; its patched-work evidence is stamped 08:12:25Z (`build/ExecC2Arms.md:60-115`). That receipt expressly calls the frozen-counter result record-only, not a revived claim (`:3-6,154-157`). This supports withdrawal **before repaired-content measurements**. It does not mean no measurements of any kind existed: baseline/control results were necessarily already observed to motivate withdrawal.

One naming inconsistency should not be laundered into chronology: erratum `plans/round-58.md:86-87` calls this a “pre-freeze control,” but the control explicitly started from and scored the already frozen `3de87aad` (`controls/CtlC2SourceGrep.md:9,24,48`). The accurate order is counter freeze → control → withdrawal → build measurements. This does not overturn the withdrawal.

# Findings and smallest safe corrections

## F1 — “Not admitted” conflates role exclusion with rejected knowledge

**Counterexample:** the Cursor changelog/pattern is retained as supporting evidence in mined S094 (`corpus/SOURCES.md:106`) while the Gate header calls all listed items not admitted (`corpus/lessons/round-58.md:17`). Several bullets are clearly choices of counted token or scored URL, not refusals of their documented facts.

**Impacted axes:** calibration and provenance; potentially discernment if these mechanical exclusions are later described as independent quality rejections. No such downstream trend verdict is asserted here.

**Smallest correction:** replace the heading with:

> Rejected for the stated use (opened or built this round; not used as a claim gate, counted token, or scored URL)

Add “as the scored token/source” to the Cursor label. Preserve the supporting fact and all frozen rules/counts.

## F2 — “Not a user folder” exceeds the plugin-path evidence

**Counterexample:** the census itself recognizes user-authored slash-command files inside the plugin (`w0/CensusCopilotCLI.md:69`), and the source prints their directory. What fails is the declared path grammar, not existence or authorability.

**Impacted axes:** calibration and technical source fidelity.

**Smallest correction:** replace the end of the Copilot plugin bullet with:

> a client-specific path inside Agent Plugins 1.0; excluded by C1's frozen leading-dot and non-final-dot rules.

For chronology precision, use “post-counter-freeze, pre-build control” and “before claim-content data” when restating erratum 1. No counter, predicate, target, or admission authority needs to change.

# Verification and custody

The additional read-only source inspection command was:

```sh
timeout 30 git --no-optional-locks -C /fast/scratch/hyaku/kotoba-r58/CtlC2SourceGrep show --format= --unified=4 c6b6f306bb21e64be05a530bf3c01fd78577a9c0 -- verifiers/check_correction_sweep.py
```

Exit 0. Observed diff: 20 inserted lines at the start of `self_test()`, including `source = Path(__file__).read_text(encoding="utf-8")`, the two canonicalizations, required-text membership checks, and the early return before the existing body. The commit is **sandbox c6b6f306bb21e64be05a530bf3c01fd78577a9c0 (/fast/scratch/hyaku/kotoba-r58/CtlC2SourceGrep)**, not a lane commit.

An initial metadata command used a mistyped `-C /home/vgpn/Projects/shokunin/kotoba-shokunin` and exited 128 with `No such file or directory`; the corrected lane command above succeeded. That failed command supplies no evidence.

Only this report was written. No lane product edits, Git writes, jj changes, source fetches, sandbox mutations, executable probes, tests, builds, client calls, paid calls, tool installs/updates, agent dispatches, or other runtime invocations were performed. Existing source-fetch provenance is attributed to the original receipts, not presented as a fresh fetch by this seat. The canonical Rust judge remains responsible for round/axis/trend decisions.
