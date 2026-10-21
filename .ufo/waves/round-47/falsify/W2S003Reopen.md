verdict: PARTIAL — S003's "Cannot contain XML tags" is live for both `name` and `description` (byte-identical to the round-46 fetch), the C2 gate really scans both fields, and its provenance label is true; but the gate's YAML-escape arm reds tag-free descriptions (plain/single-quoted and `>` escapes) while the docstring claims "double-quoted … decodes to [markup]", and that scope, the label text and the "2 evaluated" figure are unpinned by any test.

Lane-authored review, not non-author closure. Tree: `7ad7fadfc09354b74fb66605dfb0c1182c115a2f` (BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`), read in a detached clone at `/fast/scratch/kotoba-r47/w2/W2S003Reopen-2/kotoba-shokunin`; no production file written, no install performed. Probe artifact: `.ufo/waves/round-47/falsify/W2S003Reopen.probes.json`.

## 1. Freshness — S003 still says it, for both fields (holds)

Fetched independently 2026-10-21T16:54Z (`curl -sSL`, both forms):

| surface | HTTP | bytes | sha256 |
|---|---|---|---|
| `…/agent-skills/best-practices.md` | 200 | 42,028 | `727f3fa1168eb1c33ce6a3cbfc94a02ef1dfd647388f6ca9daf7cb6294762f42` |
| `…/agent-skills/best-practices` (HTML) | 200 | 1,178,610 | `29ef57c99c63ac679152d1aa6fc9ebcde9fde9a3929fc67fb9a9977af5317786` |

- `.md` is **byte-identical** to the round-46 record (`.ufo/round-46/evidence/w2/sources/fetch-log.json` `/rows/2`, accessed 2026-10-19T18:40:54Z, same sha) and to this wave's `SrcS003.json`. Zero drift over two days — the strongest freshness signal available.
- The rule is present **twice, for both fields**: `name` "Cannot contain XML tags" at `best-practices.md:155` and `description` at `:162` (both inside the "YAML Frontmatter" note under `## Skill structure`, `:146`), restated at `:1133` (`name`) and `:1134` (`description`, "no XML tags"). The rendered HTML carries both bullets (byte offsets 149464 and 149682) and the hydration payload; the `.md` is not a divergent variant.
- Evidence-hygiene note: the HTML sha256 is **not** reproducible (`29ef57c9…` today vs the wave record `f7637bb4…`, 41 bytes difference — Next.js request-varying payload). Byte-identity claims should rest on the `.md` only; the wave already does.
- Open spec S001 is silent: `https://agentskills.io/specification.md` (HTTP 200, 7,608 B, sha `9a67de89…`) has **zero** "xml" matches; its `description` row (`:31`) and bullet list (`:101-103`) carry no tag rule, and its `name` charset (`:63-64`) already excludes `<`, so the only operative delta is `description`. S002 (`79489bd2…`, 20,349 B) mentions XML only as a serialization choice for the client's skill list (`:167`, `:169`, `:280`). **The label "absent from the open spec (S001)" is true.**
- S012 is verified from the pinned tree: `quick_validate.py` at `dbd4588…` (sha `67cf5703…`, matches `corpus/lessons/round-47.md:35`) rejects `description` if `'<' in description or '>' in description` (`:80-81`) and requires a kebab-case `name`; **"Anthropic's packager bans any '<'/'>' and is stricter" is true.**

## 2. C2 implementation — both fields, tags correctly caught (holds)

`verifiers/verify_skill_checklist.py` at 7ad7fad: id registered at `:310`, dispatched at `:2391-2392`, function at `:1294-1313`, regexes at `:404-406` and `:409`, docstring bullet at `:97-104`, fixtures wired at `:1806-1809`.

- `:1298` builds `present` from `("name", "description")`; `:1302-1306` scans each. Both are load-bearing: a name-only tag (`name: kotoba<x>`) is `FAIL … XML tag in name: '<x>'` (rc 1), and removing `"name"` from the tuple turns the self-test red (20 failures) in a clean full-tree copy — matching the design's M5 kill.
- Description-only tags fail: `</skills>`, `<skills/>`, `<skill name="a">`, `<!-- -->`, `<?php`, folded `</Skills` + `>`, and the DQ-escaped `\u003cskills\u003e` (fixture `xml-tag-dq-escape`) all FAIL; the control fixture (arrows, `a < b`, `<=`, `<500`, `cat <<EOF`, `&lt;`, `≤`, guillemets) PASSes. A body-only tag (`# clean <skills>`) PASSes (rc 0), consistent with "only name/description" — the scan is correctly scoped.
- Live: `python3 -B verifiers/verify_skill_checklist.py --json` → **exit 0, 11/11**, `trigger.no_xml_tag` **PASS, evaluated 2**. Before arm: the same check on `git show c61a973:SKILL.md` → **exit 1**, `XML tag in description: '<skills>'`.
- Frontmatter count: `sed -n '/^---$/,/^---$/p' SKILL.md | grep -c '<skills>'` → **1** at BASE, **0** at HEAD (grep exit 1); the token survives in body prose only (`SKILL.md:22, :91, :96, :99, :111, :430`) — claim wording accurate.
- Instrument arithmetic: BASE archive (`git archive c61a973`) self-test → **0 failures over 1597**; HEAD → **0 failures over 1845**; `verifiers/floors-registry.json:6` pins 1845. Matches LOG.md:2322 and SCORECARD.md:31.

## 3. What breaks — the escape arm is broader than the rule it cites

**F1 (main): a legal, tag-free description reds, and the message asserts a tag that does not exist.**

Repro (`--check trigger.no_xml_tag`; files under `/tmp`, not the lane):

| frontmatter | YAML value (PyYAML) | S012 packager | kotoba gate |
|---|---|---|---|
| `description: Use \u003c when documenting escapes.` | `Use \u003c when documenting escapes.` — no `<` | `Skill is valid!` rc **0** | **rc 1**, `XML tag in description: '\\u003c'` |
| `description: 'Use \u003c when documenting escapes.'` | same literal text | valid | **rc 1** |
| `description: "a \u003c b"` | `a < b` | invalid (any `<`) | **rc 1** — yet literal `a < b` **PASSes** (`:1978`) |
| `description: "a \u003e b"` | `a > b` | invalid (any `>`) | **rc 1** — yet literal `a > b` **PASSes** |
| `description: "a \x3e b"` | `a > b` | invalid | **rc 1** |

Two defects in one arm:
1. **Quote-style blindness.** `parse_frontmatter` strips outer quotes at `:590` and decodes nothing; `check_no_xml_tag` therefore sees only the backslash text. In a plain or single-quoted scalar YAML does **not** decode `\u003c`, so the value contains no `<` at all — S003 permits it and Anthropic's own packager accepts it, while the gate reports an "S003 Anthropic rule" violation. The docstring at `:100-101` says "a YAML **double-quoted** … escape that decodes to one"; the code cannot implement that qualifier.
2. **`>` escapes are matched too, though `>` is never a tag.** `YAML_ANGLE_ESCAPE_RE` (`:409`) is `\\(?:x3[cCeE]|u003[cCeE]|U0000003[cCeE])`; the character class `[cCeE]` includes the hex digits `e`/`E` (= 0x3E, `>`), so `\x3e`/`\u003e`/`\U0000003E` match as well as `3c`. `a \u003e b` decodes to `a > b` — no XML markup — yet the detail line prints `XML tag in description: '\u003e'`. S003 does not ban `>`; only S012 does, and the gate **passes** the literal `>`. The gate therefore enforces part of S012 for escapes while claiming S003, and fails to enforce it for literal text: it is neither rule, consistently.
3. The design report *did* name a narrow version of this: `.ufo/waves/round-47/build/C2CriticRule.md:50` — "fails closed, with a theoretical FP only for a plain scalar that spells the escape literally". It is reachable, not theoretical, and the class is wider than "plain scalar" (single-quoted; `>` escapes; double-quoted escapes whose decoded `<` starts no tag); the comment at `:407` ("decode to \"<\"/\">\"") and the class `[cCeE]` suggest the `>` half is accidental or at least undesigned.

**F2: the honest label is not test-pinned.** Clean full-tree baseline `0 failure(s) over 1845`; three surviving mutants (each rc **0**, 0 failures) in copies of the tree:
- M-esc-gt: add `x3e`/`u003e` to the escape class (already matched) → survives.
- M-label: replace the detail label with `"open spec S001 rule (S003 agrees)"` → survives; nothing asserts the provenance text.
- M-evaluated: return `evaluated=1` on PASS while still scanning 2 fields → survives; the `PASS 2 evaluated` fact in LOG.md:2322/SCORECARD.md:31 is not asserted anywhere.
The label is honest at this commit, but a later edit can falsify it silently — the same class Q19/M22 exist for.

**F3: the S003 row's own conditional update was not applied.** `.ufo/waves/round-47/build/SrcS003.md:52` recommended `used-by: SKILL.md → SKILL.md, verifiers/verify_skill_checklist.py`, **"conditional — apply only when C2's description XML-tag check actually lands in that file"**. It landed (`:97, :310, :1294`), yet `corpus/SOURCES.md:16` still ends `… | 90d | SKILL.md |` and `git diff c61a973 7ad7fad -- corpus/SOURCES.md` shows only new rows S012–S015 plus a provenance paragraph — the S003 row is untouched. `corpus/lessons/round-47.md:30` records "no existing row's `status`, `recheck` or `used-by` changed". The registry therefore does not record that the verifier depends on S003. The report's literal-contract caveat (`used-by` holds "knowledge entries or lessons", `SrcS003.md:56`) had a compliant fallback — `corpus/lessons/round-47.md`, which cites S003 at `:40-42` — and that was not used either.

**Not broken (attacked, survived):** the regex misses no realistic well-formed tag I could construct — `<x>`, `</x>`, `<x/>`, `<x a="b">`, `<x a=">">`, `<x >`, `<ns:x>`, `<?x`, `<!DOCTYPE`, `<![CDATA[`, folded `</Skills\n>`, uppercase, and backticked forms all FAIL; `a < b`, `<=`, `<500`, `cat <<EOF`, `1<2>0`, `<>`, `≤`, guillemets, entities and fullwidth `＜` do not false-red as tags (fullwidth is a named NFKC limit, not a native tag). The `name` half and the entity/backtick policy are sound.

## 4. Commands (exit codes are the observed ones)

| command | rc | key output |
|---|---|---|
| `curl -sSL …/best-practices.md` / `…/best-practices` | 0/0 | HTTP 200, 42,028 / 1,178,610 B; md sha `727f3fa1…` = round-46 record |
| `grep -n "Cannot contain XML tags" best-practices.md` | 0 | `155`, `162`; restated `1133-1134` |
| `curl …/specification.md`; `grep -c -i xml` | 0/1 | 0 matches (S001 silent) |
| `curl … adding-skills-support.md`; `grep -n -i xml` | 0/0 | only code-fence language `:167,169,280` |
| `python3 quick_validate.py /tmp/qv/plain-escape` | 0 | `Skill is valid!` (escaped `<` in a plain scalar) |
| `python3 quick_validate.py /tmp/qv/dq-gt` | 1 | `Description cannot contain angle brackets (< or >)` |
| `python3 -B verifiers/verify_skill_checklist.py --json` | 0 | 11 pass / 0 fail; `trigger.no_xml_tag` PASS evaluated 2 |
| `… --self-test` | 0 | `0 failure(s) over 1845 assertions` |
| `… --self-test` in `git archive c61a973` tree | 0 | `0 failure(s) over 1597 assertions` |
| `… --skill <BASE SKILL.md> --check trigger.no_xml_tag` | 1 | `FAIL … XML tag in description: '<skills>'` |
| `sed -n '/^---$/,/^---$/p' SKILL.md \| grep -c '<skills>'` | 1 (BASE 0) | BASE 1, HEAD 0 |
| mutants M-esc-gt / M-label / M-evaluated in full-tree copies | 0/0/0 | 0 failures each — all three **survive** |
| mutant "drop `name` from the scanned tuple" | 1 | 20 failures — caught |

## 5. What I did NOT check

- C1 (surfaces/pins/substrate) and C3 (GOODGOVERNANCE errata, corpus baselines, fault harness) — other seats; I did not re-run them.
- The 76-row `C2Battery.json` agreement rate; I only established it contains **no** YAML-escape row (`grep -c 'u003c|x3c'` → 0), so the escape arm's ground truth is only the DQ fixture, which cannot distinguish quote style.
- Whether omp/opencode actually decode YAML escapes before rendering (they read frontmatter through their own loaders; [INFERENCE] the practical exposure of this arm is the local gate, not the routers). No binary inspection this seat.
- The other three XML fixtures' internal `map.json` hashes beyond the self-test run.
- The S003 page's rendered text for non-English locales/CDN variants; only the canonical `.md` and the default HTML were fetched.
- `corpus/SOURCES.md` S001–S008 rows beyond the S001/S002/S003 XML question; no other row's freshness was re-derived here.
