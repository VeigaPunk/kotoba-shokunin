Result: MIXED — The two attributed quotations and the province boundary hold, but the intro generalizes command-hook semantics to hooks that can themselves ask a model to evaluate a prompt.

# CriticIntro — round 59 falsify

Seat: `KotobaR59.CriticIntro`. Axes: **depth, adjacency**. Reviewed lane data commit `c63ccc6823e1f6a8577acbb43d19551eadbbee9a`, not an evolving working copy. Read-only review checkout: `/fast/scratch/hyaku/kotoba-r59/CriticIntro`. No sandbox commits, lane-code execution, counter runs, mutations, or runtime judgments were performed. This is the assigned intro/scope review, not verification of the whole falsify milestone.

## 1. BREAKS — the universal hook/code contrast (depth)

**Attacked text:** `SKILL.md:123`, first sentence, especially “a hook is code the client runs at an event,” used to contrast a hook with text a model reads. The following two client-attributed quotations are accurate, but they do not support that contrast for every client and every hook type in the section.

**Concrete counterexample already present in the admitted evidence:** Claude Code supports a `type: "prompt"` hook at `PreToolUse`. The committed S096 snapshot lists prompt and agent handlers at `.ufo/waves/round-59/snapshots/S096.page:390-396`; `:3851-3857` expressly includes `PreToolUse` among events supporting those types. At `:395`, the prompt-hook definition says:

> send a prompt to a Claude model for single-turn evaluation.

At `:3893-3897`, the documented sequence is a model evaluation and a JSON decision, rather than execution of a Bash command. At `:3901`, the configuration uses a prompt string instead of a command. The freshly reopened S096 bytes have the same sha256 as the committed snapshot and SOURCES row; see the receipts below.

This is not a claim that the client fails to schedule a prompt hook. It is the narrower, directly supported distinction: **client-triggered execution does not imply that the check is non-model-based**. A reader can follow the generic “route a must-run check” instruction into a supported Claude prompt hook and still have the substantive decision depend on a model. S098 `:6` and S099 `:15` cannot establish otherwise for Claude Code.

**Smallest safe correction:** qualify the contrasting category as **command hooks**, not all hooks. For example, replace the first sentence with:

> Prompt rules are text the model reads; a command hook runs a configured command at a supported lifecycle event.

Keep the two existing attributed quotations. Add a short distinction, citing S096 `:395-396`: other hook types can invoke models. No hook-file token, event cell, frozen rule, target, or counter needs changing for this correction.

The entry opener at `corpus/knowledge/hook-files-round59.md:9-11` already says “command (or other handler)” and distinguishes who invokes the handler; that broader definition survives this counterexample. Do not incorrectly replace it with a claim that every hook is a shell command.

## 2. HOLDS / MIXED — sentence-by-sentence support and guarantees (depth)

| Attacked unit | Ruling | Evidence and limit |
|---|---|---|
| `SKILL.md:123`, sentence 1, prompt rule versus hook | MIXED | S099 `:15` supports the prompt-rule/code distinction for Copilot; S098 `:6` supports client-triggered actions. The universal hook category breaks on the Claude prompt-hook counterexample above. |
| `SKILL.md:123`, sentence 2, the two attributed quotations | HOLDS | S098 `:6` contains “without relying on the model to request the action” verbatim. S099 `:15` contains “Unlike custom instructions, hooks run code rather than asking the model to follow a rule.” verbatim. No Markdown bytes were stripped from either quoted substring. Both fresh fetches match the committed snapshots. |
| `SKILL.md:123`, sentence 3, routing plus scope exclusions | MIXED | Routing a lifecycle check to a hook is supported as a craft recommendation, not an unconditional enforcement guarantee. The exclusions hold under section 3 below. S098 `:154` supplies a concrete failure-policy limit. |
| `SKILL.md:123`, final Basis parenthetical | HOLDS | The referenced entry and SOURCES rows exist at the reviewed revision. The entry explicitly disclaims runtime observation at `:12` and `:68`. This reviewer did not treat its recheck command as evidence that any hook ran. |
| Entry `:16-19`, first scope sentence | HOLDS | Restricts the lane to locations/events and excludes writing, running, or debugging hook code. The census exclusion is correctly attributed; it is not supported by S098 `:6` or S099 `:15`, nor does it need to be. |
| Entry `:19`, host-hook ownership sentence | HOLDS, as an analysis boundary | Its named W0 evidence distinguishes client hook files from host package/initramfs hooks. Tsukuroi's pinned province independently names package state and mkinitcpio hook inspection; this is not permission to implement or run host hooks. |

**Strongest guarantee counterexample:** `.ufo/waves/round-59/snapshots/S098.page:154` documents command `preToolUse` timeouts falling through to normal permissions, including policy hooks. The same fetched line contains:

> instead of assuming that every failure blocks work.

Thus putting a required policy check in the right hook file does not, by itself, establish fail-closed enforcement. S098 `:14` also describes organizational restrictions; S099 `:23-26` limits events by execution surface. These are documentary counterexamples, not reproduced runtime behavior.

Importantly, **“every time” in the current first sentence modifies the requirement imposed on the rule; it is not an explicit claim that a hook has been observed to succeed every time.** I do not report that phrase alone as a false guarantee. The useful correction is to prevent the routing recommendation from being read as a sufficient enforcement guarantee:

> Route a lifecycle-bound check to a supported command hook; verify the client's scope, enablement, and timeout/failure policy before relying on enforcement.

The entry's `:13` “must-run check” is likewise a requirement, not measured reliability. A short pointer to the same limitation would keep its routing summary aligned; no promise of universal execution or deterministic outcomes should be added. Testing/implementing the handler remains outside this lane.

## 3. HOLDS — scope does not absorb executable-surface ownership (adjacency)

`corpus/knowledge/instruction-surface-census-round13.md:259-266` identifies the excluded objects as classes outside its craft-governed rule-text inventory:

- `:264`: settings discovery is behavior configuration, not durable rule text.
- `:265`: extension/hook/tool module roots are “executable surfaces, out of prompt-craft province”. This is an exact contiguous substring; no Markdown was stripped.
- `:266`: plugin module roots are code, not text.

The new entry does not reclassify those executable roots as prompt-rule classes. It names configuration locations and event identifiers to explain **when prompt text is the wrong mechanism**, then explicitly refuses implementation/execution/debugging. Merely naming the destination is not authoring the executable surface. That reading agrees with `PROVINCE.md:3-6` (prompt and skill craft; refuse other domains) and `:24` (the exact documentary routing scope, runtime behavior unheld). It also preserves the runtime boundary at `PROVINCE.md:57`: kotoba owns prompt wording, not the runtime.

The scope paragraph's citation shorthand “§ excluded surfaces” points to the actual census heading “C. Excluded loader-derived classes”; the quoted exclusion itself is present at `:265`. This is a resolvable descriptive pointer, not false provenance. No census rewrite or broader executable ownership is warranted.

For host hooks, `.ufo/waves/round-59/w0/ConnSiblingHooks.md:32-36` distinguishes package/initramfs hooks from client-AI hook configuration. I independently read tsukuroi's `PROVINCE.md` at its cited lane commit `15c9ac0e1b02917f43c0bc016d6060f888cb603a` using:

```sh
timeout 20s env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git --no-optional-locks -C /home/vgpnk/Projects/shokunin/tsukuroi-shokunin show 15c9ac0e1b02917f43c0bc016d6060f888cb603a:PROVINCE.md
```

Exit 0. Observed Core text names pacman state and the “Initramfs v42 and boot recovery” row, whose boundary is:

> Inspect effective mkinitcpio drop-ins, hooks and recovery stages; never rebuild or boot.

Its adjacent section also says recipients are analysis/report owners, not permission to repair. Therefore the host sentence survives as a domain/analysis handoff. It must not be expanded into an authorization for tsukuroi or kotoba to run or repair hooks.

**Smallest safe scope correction:** none required. Preserve the existing exclusions while fixing the technical generalization. This is a fixable prose defect, not an unavoidable depth-versus-adjacency tradeoff. Expanding kotoba into handler implementation/runtime guarantees would instead cross the documented boundary; this review neither admits such a trade nor invokes a judge.

## 4. Source reopening receipts

All three sources were opened through ordinary curl, without a browser, challenge bypass, or client/model calls. Each curl below exited 0, followed by `timeout 5s wc -c <output>`, `timeout 5s sha256sum <output>`, and `timeout 5s date -u`, also exit 0. Paths are within this seat's scratch checkout.

### S098

```sh
timeout 45s curl --connect-timeout 10 --max-time 40 --location --silent --show-error --user-agent 'Mozilla/5.0' --output /fast/scratch/hyaku/kotoba-r59/CriticIntro/S098.live.page --write-out 'url=%{url_effective}\nhttp=%{http_code}\nbytes=%{size_download}\n' https://code.visualstudio.com/docs/agent-customization/hooks.md
```

Observed output:

```text
url=https://code.visualstudio.com/docs/agent-customization/hooks.md
http=200
bytes=15152
15152 /fast/scratch/hyaku/kotoba-r59/CriticIntro/S098.live.page
98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08  /fast/scratch/hyaku/kotoba-r59/CriticIntro/S098.live.page
Fri 23 Oct 2026 09:53:22 AM UTC
```

Relevant fetched-byte lines: `S098.live.page:6,14,154`. Hash equals committed `snapshots/S098.page` and `corpus/SOURCES.md:110`.

### S099

```sh
timeout 45s curl --connect-timeout 10 --max-time 40 --location --silent --show-error --user-agent 'Mozilla/5.0' --output /fast/scratch/hyaku/kotoba-r59/CriticIntro/S099.live.page --write-out 'url=%{url_effective}\nhttp=%{http_code}\nbytes=%{size_download}\n' https://docs.github.com/en/copilot/concepts/customizations/hooks.md
```

Observed output:

```text
url=https://docs.github.com/en/copilot/concepts/customizations/hooks.md
http=200
bytes=8428
8428 /fast/scratch/hyaku/kotoba-r59/CriticIntro/S099.live.page
23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4  /fast/scratch/hyaku/kotoba-r59/CriticIntro/S099.live.page
Fri 23 Oct 2026 09:53:22 AM UTC
```

Relevant fetched-byte lines: `S099.live.page:15,23-28`. Hash equals committed `snapshots/S099.page` and `corpus/SOURCES.md:111`.

### S096 — strongest local counterexample reopened

```sh
timeout 45s curl --connect-timeout 10 --max-time 40 --location --silent --show-error --user-agent 'Mozilla/5.0' --output /fast/scratch/hyaku/kotoba-r59/CriticIntro/S096.live.page --write-out 'url=%{url_effective}\nhttp=%{http_code}\nbytes=%{size_download}\n' https://code.claude.com/docs/en/hooks.md
```

Observed output:

```text
url=https://code.claude.com/docs/en/hooks.md
http=200
bytes=274129
274129 /fast/scratch/hyaku/kotoba-r59/CriticIntro/S096.live.page
c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8  /fast/scratch/hyaku/kotoba-r59/CriticIntro/S096.live.page
Fri 23 Oct 2026 09:53:22 AM UTC
```

Relevant fetched-byte lines: `S096.live.page:390-396,3849-3857,3893-3901`. Hash equals committed `snapshots/S096.page` and `corpus/SOURCES.md:108`.

The committed-snapshot fingerprint command also exited 0:

```sh
timeout 5s sha256sum .ufo/waves/round-59/snapshots/S096.page .ufo/waves/round-59/snapshots/S098.page .ufo/waves/round-59/snapshots/S099.page
```

```text
c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8  .ufo/waves/round-59/snapshots/S096.page
98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08  .ufo/waves/round-59/snapshots/S098.page
23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4  .ufo/waves/round-59/snapshots/S099.page
```

No tools installed or updated. Only this report was written in the lane. Suggested prose is not integrated. No conclusion about the frozen C1 counter's acceptance, whole-round no-harm column, or runtime hook reliability is claimed.
