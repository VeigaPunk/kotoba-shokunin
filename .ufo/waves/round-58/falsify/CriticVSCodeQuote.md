Result: MIXED — The current VS Code excerpt supports the Local workspace location, but its Q42 note falsely denies whitespace changes; the earlier user-level-tail criticism does not apply to this replacement excerpt.

## Scope and axes

Read-only criticism of the VS Code quote in `corpus/knowledge/command-files-round58.md:28-37` and `corpus/lessons/round-58.md:12` at lane content commit `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe`. Axis under attack: **calibration**, specifically accurate quotation/provenance and the boundary between source support and counter normalization. Depth is relevant only to whether the location is actually supported. This is not a claim-admission or round verdict.

## 1. BREAKS: the transport note is incomplete and its byte assurance is false

Evidence:

- Entry `:28-30` discloses pipes represented as `&#124;`, then says “no other byte is changed.” Gate `:12` likewise mentions pipes only.
- Reopened S091 has the identical 13,729-byte body and full SHA-256 recorded by the source seat and registry. Its selected span at fetched `S091.prompt-files.md:21-25` is below. Backticks, pipes, the blank line and line breaks are retained; no bytes inside this displayed source span are intentionally stripped. The selection starts at `that` within line 21 and ends at the final pipe on line 25; the earlier sentence prefix and following newline are outside the selection.

```text
that the Local harness uses for prompt files.

| Scope | Default file location |
|-------|-----------------------|
| Workspace | `.github/prompts` folder |
```

The entry/Gate do **two** transformations: encode nine U+007C pipe bytes, and fold four LF bytes in three runs (two after line 21, one after line 23, one after line 24) into three U+0020 spaces. The blank line disappears. The pipe-only transformation does not produce the landed quotation. Q42 (`corpus/QUALITY.md:53`) explicitly covers folded lines and requires the note to identify removed bytes.

A bounded, in-memory calculation on this displayed span and the landed quote, without importing/executing lane code, completed successfully with this observed output:

```text
Source pipe bytes: 9
Source LF bytes: 4
LF runs: [2, 1, 1]
Encoded quote matches pipe-only replacement: False
Encoded quote matches pipe replacement plus whitespace folding: True
HTML-decoded and whitespace-folded quote matches folded source: True
Whitespace words after backtick removal: 22
Outside-token command/prompt words: ['prompt']
User-profile / user-level tail included: False
Calculation exit: 0
```

The comparison was `entry_quote == source_span.replace('|', '&#124;')`, followed by comparison with `re.sub(r'\s+', ' ', source_span.replace('|', '&#124;'))`; the first returned False and the second True. This demonstrates a false byte-fidelity assurance, not invented source wording. The source seat already disclosed both transformations in `.ufo/waves/round-58/build/SrcVSCode.md:6`; the integrated note lost the whitespace disclosure.

## 2. HOLDS: the outside-token word is appropriately scoped, not the old user-level borrowing

The current outside-token `prompt` comes from line 21's introduction to **this very table**, not from its Workspace row. Thus it is in adjacent prose rather than the same table row; that distinction should not be hidden. But the prose expressly introduces the Local harness's default prompt-file locations, and the selected table row retains the `Workspace` label. This is a contiguous span, not a splice joining unrelated assertions.

`CriticCensus.md:44-55` attacked the different W0 selection at source `:25-28`, which ran through the User profile row and ended in the later user-level creation paragraph. The integrated quote ends at `:25` and contains neither that row nor that paragraph. `build/SrcVSCode.md:6` explicitly records replacing the W0 excerpt. Repeating the old user-level-tail accusation against the content commit would misdescribe the evidence.

The entry also expressly limits prompt files to Local harness sessions (`:17-18`); the current quotation itself retains `Local`. There is no evidence here of a false `.github/prompts` attribution or loss of workspace/Local scope.

## Reader impact and smallest safe correction

A reader is misled about **verbatim byte provenance**, not about which folder the Local workspace uses. Encoding pipes is reasonable table transport; whitespace folding is also understandable but must not be denied. The quoted material is a table-introduction fragment plus table rows, not a complete prose sentence naming the path.

Keep the token, source, excerpt and frozen rules/targets. Replace the VS Code part of the entry's quote note with:

> The VS Code quote is a contiguous source span (`prompt-files.md:21-25`), transported into one table cell: its nine `|` bytes are represented as `&#124;`, and four LF bytes in three runs (two after line 21, one after line 23, one after line 24) are folded to three ASCII spaces. No wording or other bytes within the selected span are changed. The outside-token `prompt` comes from the table's introduction on line 21.

Amend Gate `:12`'s parenthesis to disclose the same pipe encoding **and** the four-LF/three-space folding, with a pointer to that note. Preserve the other clients' existing notes.

The full-page target search for `\.github/prompts` returned only fetched line 25. That row contains no outside-token command/prompt word. [INFERENCE] This fetched page therefore offers no single-line unshaped alternative that contains both the token and the required outside-token word; inventing a prose sentence is not a safe Q42 repair. The displayed raw span above provides the exact source presentation for reopening.

This is a fixable calibration defect, not an unavoidable depth/calibration trade: honest disclosure preserves the actual evidence. Leaving the false assurance unresolved would retain calibration harm. No change to the counter, predicate, rule or target is proposed, and this review does not establish or overturn F/G or C1 admission.

## Reopening and command evidence

Sandbox setup, exit 0, no output:

```sh
env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE timeout 120 git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r58/CriticVSCodeQuote && env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE timeout 30 git -C /fast/scratch/hyaku/kotoba-r58/CriticVSCodeQuote checkout -q 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe
```

Primary source: https://code.visualstudio.com/docs/agent-customization/prompt-files.md

```sh
timeout 5 date -u '+%Y-%m-%dT%H:%M:%SZ' && timeout 75 curl --location --fail --silent --show-error --output /fast/scratch/hyaku/kotoba-r58/CriticVSCodeQuote/S091.prompt-files.md --write-out 'HTTP %{http_code}; bytes %{size_download}; URL %{url_effective}\n' https://code.visualstudio.com/docs/agent-customization/prompt-files.md && timeout 5 wc -c /fast/scratch/hyaku/kotoba-r58/CriticVSCodeQuote/S091.prompt-files.md && timeout 5 sha256sum /fast/scratch/hyaku/kotoba-r58/CriticVSCodeQuote/S091.prompt-files.md && printf 'Exit: 0\n'
```

Observed output; exit 0:

```text
2026-10-23T08:26:22Z
HTTP 200; bytes 13729; URL https://code.visualstudio.com/docs/agent-customization/prompt-files.md
13729 /fast/scratch/hyaku/kotoba-r58/CriticVSCodeQuote/S091.prompt-files.md
4ad1b2bcaf78c9166b1609610f354d9cb8b1ff9c9e7cf643c443fad04dac6685  /fast/scratch/hyaku/kotoba-r58/CriticVSCodeQuote/S091.prompt-files.md
Exit: 0
```

The diagnostic used Python Eval with a 15-second deadline on already displayed strings. No lane code, self-test, full counter, client CLI, browser, paid model call, or alternate judging runtime was run. No tools were installed/updated, no sandbox commits were made, and no client-silence claim is asserted. Only this report was written in the lane.
