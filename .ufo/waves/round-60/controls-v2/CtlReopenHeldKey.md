Result: DONE — CtlReopenHeldKey: held-key S=2/3 F=2/3 exits(no-fetch/fetch)=1/1; alias S=3/3 F=3/3 exits=1/0; redirect S=3/3 F=2/3 exits=1/1; predicate MET
## Findings and assigned scope

Control: `CtlReopenHeldKey`, C1 pre-data counter-v2 control. Axes: held-key discrimination, alias discrimination, redirect discrimination, frozen-counter identity, exact-byte restoration. Only this sandbox and this report were written; no lane code, sibling clone, fleet state, integration, or contract was changed. No tools were installed or updated. No other agent/runtime was invoked.

**Held-key: KILLED.** The smallest defect is one Scope-key cell at `SKILL.md:141`: Cursor `globs` (S106 :85) becomes `rules` (S106 :146). The page bytes, quote, Action, source URL, SHA pin and `re-opens S049 —` cell remain unchanged. S049 already holds the identifier `rules` in its frozen base line (`corpus/SOURCES.md:62`). The frozen counter rejects exactly that held key, not a missing key site: `base row S049 already records key rules`. S/F falls 3/3 → 2/2 and the fetched exit changes 0 → 1; exact restoration returns 3/3 and exit 0.

**Alias: SURVIVED, an expected coverage finding.** German Claude memory and enterprise-cloud Copilot CLI URLs from W0b, together with a genuine Cursor re-open, count S=F=3/3 and exit 0. **The L1 rejects these aliases by judgment** (`plans/round-60.md:134-145` at the freeze); the counter does not encode that judgment. This finding does not change the contract or admit either alias. The required one-line predicate-MET message was delivered to `agent://KotobaR60` immediately after this score.

**Different-base redirect: KILLED by the live guard.** Cursor S106 requests `https://cursor.com/docs/context/rules`, carries `re-opens S052 —`, and really redirects to `https://cursor.com/docs/rules` (S049), not S052’s `https://cursor.com/help/customization/rules.md` key. Everything else is the corrected pristine world. S=3/3 without fetching; fetching gives F=2/3 and exit 1 with `reached a base SOURCES URL https://cursor.com/docs/rules`. Important limit: the request URL is non-base, so the structural `reopen_why` check is skipped (`check_scoped_rules.py:1054-1059`); this is a row bearing a wrong re-open marker, not proof of a structurally validated cross-base re-open. The actual redirect guard is exercised (`:1218-1220`, `:2539-2540`).

## Counter and expected detector

Freeze: `b1cd64bb45eee744c4ec93be8631f1eddb28fddd`. `TARGET = 3` was read from the committed counter at `verifiers/check_scoped_rules.py:249`, not from the task text. Row format and snapshot assembly reuse the frozen self-test’s literal `src_row` via AST extraction (`:1730-1747`) and its `snapshot_path`, `OPENED`, and parsing helpers. `probe/prepare.py` contains that extraction. No self-test was run.

Lane committed-counter identity command (exit 0):

```sh
timeout 30 git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show b1cd64bb45eee744c4ec93be8631f1eddb28fddd:verifiers/check_scoped_rules.py | sha256sum
```

```text
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  -
```

Clone identity command (exit 0 before and after all controls):

```sh
sha256sum verifiers/check_scoped_rules.py
```

```text
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  verifiers/check_scoped_rules.py
```

The same bounded CLI detector is run on committed pristine, mutant and restored bytes, with and without `--fetch`; every exact command and full stdout follows below. Without `--fetch`, F=0 and exit 1 are contractual even for a satisfying snapshot world, not mutant kills. The decisive predicate is only fetched exit 0 iff F>=TARGET. No detector implementation was mutated.

Fetch recording is transparent and disclosed: `probe/bin/curl` forwards the frozen arguments unchanged to `/usr/bin/curl`, saves the raw body plus actual status/effective URL/date/byte count/hash, and returns curl stdout, stderr and exit unchanged. It does not supply stored pages, mock a request, alter a URL, or retry. `probe/score.py` supplies this environment to the exact commands below:

```text
PATH=/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey/probe/bin:/usr/local/bin:/usr/bin:/bin
CTL_FETCH_DIR=/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey/probe/fetches/<world>
```

Each detector command is capped at 900 seconds; curl retains the frozen 30-second cap and maximum three attempts. Observed request maxima are recorded below (the redirect world uses exactly three Cursor attempts). The initial six-page collection used at most four concurrent ordinary curl requests and exited 0 under `timeout 180`. No browser or access-control bypass was used.

## World content and evidence locations

All worlds are sandbox commits descended from the freeze in the assigned clone. They use new IDs S103, S104 and S106, all within S103–S112. K=3: Claude Code, Copilot CLI and Cursor. The four other clients are absent and appear as explicit rejections; they are not counted. No VS Code row is used (its separately collected source is auxiliary and recorded honestly below).

- `SKILL.md:135-141`: exact section/header and three Scope/Action rows.
- `corpus/knowledge/scoped-rules-round60.md:7-11`: exact entry header and three quotes.
- `corpus/SOURCES.md:115-117`: rows, URL, full page SHA, opened date and teaches.
- `corpus/lessons/round-60.md:3-19`: Gate, source URLs and quotations.
- `.ufo/waves/round-60/snapshots/S103.page`: Claude quote :168, key :198 and Action :194; alias quote :18, key :198 and German Action :194.
- `.ufo/waves/round-60/snapshots/S104.page`: Copilot quote :18, key :66 and Action :60 in both variants.
- `.ufo/waves/round-60/snapshots/S106.page`: real Cursor quote :32, key `globs` :85 and Action :131; held-key citation `rules` :146.

Pristine re-opens S043, S048 and S049 respectively. The alias world replaces Claude/Copilot with their actual W0b non-base URLs and actual fetched locale/enterprise bytes, updates their pins, and uses the German quote/Action rather than pretending the English text was present. Cursor remains a genuine S049 re-open. Both aliases were fetched without redirect to a base URL.

### Actual held-key key-form result

At Cursor fetched line 146, the unchanged page literally says:

```text
There are two ways to create rules:
```

The next nonblank line (:148) starts with the verbatim prefix `- **` followed by a backticked command. The frozen parser treats the leading Markdown emphasis as first value token `**`, so `key_site(...,146,"rules")` is True even though this is prose, not the client’s real scope key. This supplies the requested held identifier with a passing machine key form on a real page, without fabricating snapshot bytes. The held-base guard still kills it. Direct helper output (`probe/held-detail.json`):

```json
{
  "scope_cell": "`rules` (S106 :146)",
  "cited_line": "There are two ways to create rules:",
  "key_site": true,
  "first_value_token": "**",
  "scope_conjunct": [],
  "base_key_occurrences": [
    [
      55,
      60
    ],
    [
      201,
      206
    ],
    [
      209,
      214
    ],
    [
      239,
      244
    ],
    [
      617,
      622
    ]
  ],
  "reopen_why": [
    "base row S049 already records key rules"
  ],
  "redirect_named_base_key_S052": "//cursor.com/help/customization/rules",
  "redirect_final_base_key_S049": "//cursor.com/docs/rules"
}
```

### Verbatim source quotes and shaping

Quotes below are byte-exact contiguous spans at the cited fetched-byte lines, each at most 25 words. No Markdown bytes were stripped. The Copilot quote is the whole 16-word table line; inside the entry table, every literal `|` is encoded as `&#124;` and the exact same serialization is also recorded in Gate, while the raw quote is preserved there too.

S103 / `claude` line 168 (14 words):

```text
For larger projects, you can organize instructions into multiple files using the `.claude/rules/` directory.
```

S104 / `copilot` line 18 (16 words):

```text
| `.github/instructions/**/*.instructions.md`              | Modular repository instructions, discovered in the standard locations but not intermediate directories.                                                         |
```

S106 / `cursor-redirect` line 32 (11 words):

```text
Project rules live in `.cursor/rules` as `.mdc` files and are version-controlled.
```

S103 alias / `claude-alias` line 18 (8 words):

```text
* [Regeln auf bestimmte Dateitypen beschränken](#organize-rules-with-claude/rules/) mit `.claude/rules/`
```

The S104 enterprise alias uses the same verbatim quote on its actual line 18. The German quote’s outside `rules` match is an untranslated anchor slug, not German prose, as already disclosed by W0b.

## Full detector receipts

### Initial fixture — INCONCLUSIVE, before any mutation

Control: `CtlReopenHeldKey`. Commit: sandbox 42061b8511faeb32b169fdda9000ea43e1b2d475 (/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey). Counter SHA256 run: `ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a`.

This setup run fails because Gate initially contained only literal pipes while the entry quote contained `&#124;`. It is **inconclusive, not a killed mutant**. The only correction before mutation was adding the identical encoded quote to Gate. The corrected baseline below passes; the initial failure is retained rather than omitted.

#### Without --fetch

Cwd: `/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey`. Actual `date -u`:

```text
Fri Oct 23 12:09:34 PM UTC 2026
```

Exact command:

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 42061b8511faeb32b169fdda9000ea43e1b2d475
```

Full stdout:

```text
scoped rule files backed on committed snapshots 2 of 3; live not run
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 42061b8511faeb32b169fdda9000ea43e1b2d475
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: entry row S104: round-60 Gate does not record this quote
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Stderr: empty. Exit code: `1`.

#### With --fetch

Cwd: `/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey`. Actual `date -u`:

```text
Fri Oct 23 12:09:34 PM UTC 2026
```

Exact command:

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 42061b8511faeb32b169fdda9000ea43e1b2d475 --fetch
```

Full stdout:

```text
scoped rule files backed on committed snapshots 2 of 3; found on the live page 2 of 3
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 42061b8511faeb32b169fdda9000ea43e1b2d475
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: entry row S104: round-60 Gate does not record this quote
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Stderr: empty. Exit code: `1`.

C1 predicate: --fetch exit 0 (F>=TARGET) — NOT MET

Evidence files: `/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey/probe/scores/pristine/{nofetch,fetch}.{stdout,stderr,json}`.

### Corrected pristine baseline

Control: `CtlReopenHeldKey`. Commit: sandbox 5e126aa62f8e3b8e30024c00c81fb13be0b0d000 (/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey). Counter SHA256 run: `ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a`.

#### Without --fetch

Cwd: `/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey`. Actual `date -u`:

```text
Fri Oct 23 12:10:12 PM UTC 2026
```

Exact command:

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 5e126aa62f8e3b8e30024c00c81fb13be0b0d000
```

Full stdout:

```text
scoped rule files backed on committed snapshots 3 of 3; live not run
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 5e126aa62f8e3b8e30024c00c81fb13be0b0d000
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Stderr: empty. Exit code: `1`.

#### With --fetch

Cwd: `/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey`. Actual `date -u`:

```text
Fri Oct 23 12:10:12 PM UTC 2026
```

Exact command:

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 5e126aa62f8e3b8e30024c00c81fb13be0b0d000 --fetch
```

Full stdout:

```text
scoped rule files backed on committed snapshots 3 of 3; found on the live page 3 of 3
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 5e126aa62f8e3b8e30024c00c81fb13be0b0d000
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Stderr: empty. Exit code: `0`.

C1 predicate: --fetch exit 0 (F>=TARGET) — MET

Evidence files: `/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey/probe/scores/baseline/{nofetch,fetch}.{stdout,stderr,json}`.

### (a) Held-key mutant

Control: `CtlReopenHeldKey`. Commit: sandbox d65dca039f7235d70de77e51219453e3f5968452 (/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey). Counter SHA256 run: `ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a`.

#### Without --fetch

Cwd: `/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey`. Actual `date -u`:

```text
Fri Oct 23 12:10:24 PM UTC 2026
```

Exact command:

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev d65dca039f7235d70de77e51219453e3f5968452
```

Full stdout:

```text
scoped rule files backed on committed snapshots 2 of 3; live not run
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev d65dca039f7235d70de77e51219453e3f5968452
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: entry row S106: S106 URL 'https://cursor.com/docs/rules' is already a base SOURCES URL; base row S049 already records key rules
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Stderr: empty. Exit code: `1`.

#### With --fetch

Cwd: `/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey`. Actual `date -u`:

```text
Fri Oct 23 12:10:24 PM UTC 2026
```

Exact command:

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev d65dca039f7235d70de77e51219453e3f5968452 --fetch
```

Full stdout:

```text
scoped rule files backed on committed snapshots 2 of 3; found on the live page 2 of 3
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev d65dca039f7235d70de77e51219453e3f5968452
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: entry row S106: S106 URL 'https://cursor.com/docs/rules' is already a base SOURCES URL; base row S049 already records key rules
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Stderr: empty. Exit code: `1`.

C1 predicate: --fetch exit 0 (F>=TARGET) — NOT MET

Evidence files: `/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey/probe/scores/held-key/{nofetch,fetch}.{stdout,stderr,json}`.

### Exact restoration after held-key mutant

Control: `CtlReopenHeldKey`. Commit: sandbox 6de16f9c0f83da6f9420a6eec4f6d3ab262045a3 (/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey). Counter SHA256 run: `ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a`.

#### Without --fetch

Cwd: `/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey`. Actual `date -u`:

```text
Fri Oct 23 12:10:43 PM UTC 2026
```

Exact command:

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 6de16f9c0f83da6f9420a6eec4f6d3ab262045a3
```

Full stdout:

```text
scoped rule files backed on committed snapshots 3 of 3; live not run
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 6de16f9c0f83da6f9420a6eec4f6d3ab262045a3
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Stderr: empty. Exit code: `1`.

#### With --fetch

Cwd: `/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey`. Actual `date -u`:

```text
Fri Oct 23 12:10:43 PM UTC 2026
```

Exact command:

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 6de16f9c0f83da6f9420a6eec4f6d3ab262045a3 --fetch
```

Full stdout:

```text
scoped rule files backed on committed snapshots 3 of 3; found on the live page 3 of 3
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 6de16f9c0f83da6f9420a6eec4f6d3ab262045a3
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Stderr: empty. Exit code: `0`.

C1 predicate: --fetch exit 0 (F>=TARGET) — MET

Evidence files: `/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey/probe/scores/restored-held/{nofetch,fetch}.{stdout,stderr,json}`.

### (b) Locale/enterprise alias world

Control: `CtlReopenHeldKey`. Commit: sandbox 4560334d43679dbb52795748441c1510d493558f (/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey). Counter SHA256 run: `ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a`.

#### Without --fetch

Cwd: `/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey`. Actual `date -u`:

```text
Fri Oct 23 12:11:20 PM UTC 2026
```

Exact command:

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 4560334d43679dbb52795748441c1510d493558f
```

Full stdout:

```text
scoped rule files backed on committed snapshots 3 of 3; live not run
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 4560334d43679dbb52795748441c1510d493558f
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Stderr: empty. Exit code: `1`.

#### With --fetch

Cwd: `/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey`. Actual `date -u`:

```text
Fri Oct 23 12:11:20 PM UTC 2026
```

Exact command:

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 4560334d43679dbb52795748441c1510d493558f --fetch
```

Full stdout:

```text
scoped rule files backed on committed snapshots 3 of 3; found on the live page 3 of 3
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 4560334d43679dbb52795748441c1510d493558f
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Stderr: empty. Exit code: `0`.

C1 predicate: --fetch exit 0 (F>=TARGET) — MET

Evidence files: `/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey/probe/scores/alias/{nofetch,fetch}.{stdout,stderr,json}`.

### (c) Different-base redirect world

Control: `CtlReopenHeldKey`. Commit: sandbox 062742c165e5a7eb9a22ed0f5b33b9ef11720c4a (/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey). Counter SHA256 run: `ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a`.

#### Without --fetch

Cwd: `/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey`. Actual `date -u`:

```text
Fri Oct 23 12:12:00 PM UTC 2026
```

Exact command:

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 062742c165e5a7eb9a22ed0f5b33b9ef11720c4a
```

Full stdout:

```text
scoped rule files backed on committed snapshots 3 of 3; live not run
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 062742c165e5a7eb9a22ed0f5b33b9ef11720c4a
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Stderr: empty. Exit code: `1`.

#### With --fetch

Cwd: `/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey`. Actual `date -u`:

```text
Fri Oct 23 12:12:00 PM UTC 2026
```

Exact command:

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 062742c165e5a7eb9a22ed0f5b33b9ef11720c4a --fetch
```

Full stdout:

```text
scoped rule files backed on committed snapshots 3 of 3; found on the live page 2 of 3
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 062742c165e5a7eb9a22ed0f5b33b9ef11720c4a
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: live fetch failed: reached a base SOURCES URL https://cursor.com/docs/rules
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Stderr: empty. Exit code: `1`.

C1 predicate: --fetch exit 0 (F>=TARGET) — NOT MET

Evidence files: `/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey/probe/scores/redirect/{nofetch,fetch}.{stdout,stderr,json}`.

### Final exact pristine restoration

Control: `CtlReopenHeldKey`. Commit: sandbox 41590b73d3bceb3c31dcb24d7bc92ef841d0812f (/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey). Counter SHA256 run: `ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a`.

#### Without --fetch

Cwd: `/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey`. Actual `date -u`:

```text
Fri Oct 23 12:12:15 PM UTC 2026
```

Exact command:

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 41590b73d3bceb3c31dcb24d7bc92ef841d0812f
```

Full stdout:

```text
scoped rule files backed on committed snapshots 3 of 3; live not run
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 41590b73d3bceb3c31dcb24d7bc92ef841d0812f
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Stderr: empty. Exit code: `1`.

#### With --fetch

Cwd: `/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey`. Actual `date -u`:

```text
Fri Oct 23 12:12:15 PM UTC 2026
```

Exact command:

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 41590b73d3bceb3c31dcb24d7bc92ef841d0812f --fetch
```

Full stdout:

```text
scoped rule files backed on committed snapshots 3 of 3; found on the live page 3 of 3
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 41590b73d3bceb3c31dcb24d7bc92ef841d0812f
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Stderr: empty. Exit code: `0`.

C1 predicate: --fetch exit 0 (F>=TARGET) — MET

Evidence files: `/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey/probe/scores/restored-final/{nofetch,fetch}.{stdout,stderr,json}`.

## Source access receipts

Initial ordinary collection command (exit 0):

```sh
timeout 180 env CTL_FETCH_DIR=/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey/probe/fetches/collect PATH=/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey/probe/bin:/usr/local/bin:/usr/bin:/bin python3 -B probe/collect.py
```

Every subsequent live request was made by the exact frozen counter commands above. The following is derived from the recorder’s actual per-request JSON, not from planned values. Each JSON preserves the full `/usr/bin/curl` argv and matching `.page` bytes under `probe/fetches/<world>/`. URL labels are fully expanded here:

- `claude`: https://code.claude.com/docs/en/memory.md
- `claude-alias`: https://code.claude.com/docs/de/memory.md
- `copilot`: https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md
- `copilot-alias`: https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md
- `cursor-canonical`: https://cursor.com/docs/rules
- `cursor-redirect`: https://cursor.com/docs/context/rules
- `vscode`: https://code.visualstudio.com/docs/agent-customization/custom-instructions.md

In the table, “same” means the full final URL equals that row’s expanded requested URL. Each UTC cell is the literal `date -u` line for that request.

| World | Requested URL label | date -u (actual) | HTTP | Final URL | Bytes | SHA256 | curl exit |
|---|---|---|---|---|---:|---|---:|
| collect | `copilot` | Fri Oct 23 12:07:23 PM UTC 2026 | 200 | same | 8730 | `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980` | 0 |
| collect | `vscode` | Fri Oct 23 12:07:23 PM UTC 2026 | 200 | same | 23715 | `a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f` | 0 |
| collect | `copilot-alias` | Fri Oct 23 12:07:23 PM UTC 2026 | 200 | same | 8826 | `70aef6793ae9896ad98f12c75eb3d8c3cae504c6ea728c257b794d2f00c09e8e` | 0 |
| collect | `claude-alias` | Fri Oct 23 12:07:23 PM UTC 2026 | 200 | same | 63447 | `c568aae2c633029aa6a8b612de437f275bbe8f39c5866ef7382f89073e7f9c43` | 0 |
| collect | `claude` | Fri Oct 23 12:07:23 PM UTC 2026 | 200 | same | 54043 | `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7` | 0 |
| collect | `cursor-redirect` | Fri Oct 23 12:07:23 PM UTC 2026 | 200 | https://cursor.com/docs/rules | 17403 | `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` | 0 |
| pristine | `claude` | Fri Oct 23 12:09:34 PM UTC 2026 | 200 | same | 54043 | `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7` | 0 |
| pristine | `cursor-canonical` | Fri Oct 23 12:09:35 PM UTC 2026 | 200 | same | 17403 | `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` | 0 |
| baseline | `claude` | Fri Oct 23 12:10:12 PM UTC 2026 | 200 | same | 54043 | `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7` | 0 |
| baseline | `copilot` | Fri Oct 23 12:10:12 PM UTC 2026 | 200 | same | 8730 | `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980` | 0 |
| baseline | `cursor-canonical` | Fri Oct 23 12:10:12 PM UTC 2026 | 200 | same | 17403 | `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` | 0 |
| held-key | `claude` | Fri Oct 23 12:10:24 PM UTC 2026 | 200 | same | 54043 | `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7` | 0 |
| held-key | `copilot` | Fri Oct 23 12:10:24 PM UTC 2026 | 200 | same | 8730 | `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980` | 0 |
| restored-held | `claude` | Fri Oct 23 12:10:44 PM UTC 2026 | 200 | same | 54043 | `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7` | 0 |
| restored-held | `copilot` | Fri Oct 23 12:10:44 PM UTC 2026 | 200 | same | 8730 | `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980` | 0 |
| restored-held | `cursor-canonical` | Fri Oct 23 12:10:44 PM UTC 2026 | 200 | same | 17403 | `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` | 0 |
| alias | `claude-alias` | Fri Oct 23 12:11:20 PM UTC 2026 | 200 | same | 63447 | `c568aae2c633029aa6a8b612de437f275bbe8f39c5866ef7382f89073e7f9c43` | 0 |
| alias | `copilot-alias` | Fri Oct 23 12:11:21 PM UTC 2026 | 200 | same | 8826 | `70aef6793ae9896ad98f12c75eb3d8c3cae504c6ea728c257b794d2f00c09e8e` | 0 |
| alias | `cursor-canonical` | Fri Oct 23 12:11:21 PM UTC 2026 | 200 | same | 17403 | `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` | 0 |
| redirect | `claude` | Fri Oct 23 12:12:00 PM UTC 2026 | 200 | same | 54043 | `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7` | 0 |
| redirect | `copilot` | Fri Oct 23 12:12:00 PM UTC 2026 | 200 | same | 8730 | `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980` | 0 |
| redirect | `cursor-redirect` | Fri Oct 23 12:12:00 PM UTC 2026 | 200 | https://cursor.com/docs/rules | 17403 | `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` | 0 |
| redirect | `cursor-redirect` | Fri Oct 23 12:12:01 PM UTC 2026 | 200 | https://cursor.com/docs/rules | 17403 | `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` | 0 |
| redirect | `cursor-redirect` | Fri Oct 23 12:12:01 PM UTC 2026 | 200 | https://cursor.com/docs/rules | 17403 | `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` | 0 |
| restored-final | `claude` | Fri Oct 23 12:12:15 PM UTC 2026 | 200 | same | 54043 | `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7` | 0 |
| restored-final | `copilot` | Fri Oct 23 12:12:15 PM UTC 2026 | 200 | same | 8730 | `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980` | 0 |
| restored-final | `cursor-canonical` | Fri Oct 23 12:12:15 PM UTC 2026 | 200 | same | 17403 | `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` | 0 |

Observed request counts (each URL at most three GET attempts per invocation):

```json
{
  "alias": {
    "requests": 3,
    "max_per_url": 1
  },
  "baseline": {
    "requests": 3,
    "max_per_url": 1
  },
  "collect": {
    "requests": 6,
    "max_per_url": 1
  },
  "held-key": {
    "requests": 2,
    "max_per_url": 1
  },
  "pristine": {
    "requests": 2,
    "max_per_url": 1
  },
  "redirect": {
    "requests": 5,
    "max_per_url": 3
  },
  "restored-final": {
    "requests": 3,
    "max_per_url": 1
  },
  "restored-held": {
    "requests": 3,
    "max_per_url": 1
  }
}
```

## Before/after hashes and restoration

Hashes are over exact working bytes, recorded before and after each detector pair. `probe/restoration-summary.json` records that every detector pair preserved all eight files. No counter bytes changed at any point. Both the intermediate held-key restoration and final restoration equal the corrected pristine bytes for every affected file. The report and probe receipts are outside the scored world; they remain as evidence.

Baseline versus final restored SHA256:

| Path | Baseline | Final restored |
|---|---|---|
| `SKILL.md` | `55329286c674f324d5a8e9a07b13d4bd0b816423b2f39a9a0eef6728c197d18b` | `55329286c674f324d5a8e9a07b13d4bd0b816423b2f39a9a0eef6728c197d18b` |
| `corpus/SOURCES.md` | `6eef67c3a3bedcb6c136b5619061c9ae4137d23e82f1fe6aed2373fce24c348a` | `6eef67c3a3bedcb6c136b5619061c9ae4137d23e82f1fe6aed2373fce24c348a` |
| `corpus/knowledge/scoped-rules-round60.md` | `4791bea447d68e9238a180eef49f4c6c0b64420f33ae3bfb966b2341b26403df` | `4791bea447d68e9238a180eef49f4c6c0b64420f33ae3bfb966b2341b26403df` |
| `corpus/lessons/round-60.md` | `e956d384622f4d3cb9402f3924a122261ce72a8b4f3c1cefdd9ec7421c805197` | `e956d384622f4d3cb9402f3924a122261ce72a8b4f3c1cefdd9ec7421c805197` |
| `.ufo/waves/round-60/snapshots/S103.page` | `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7` | `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7` |
| `.ufo/waves/round-60/snapshots/S104.page` | `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980` | `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980` |
| `.ufo/waves/round-60/snapshots/S106.page` | `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` | `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` |
| `verifiers/check_scoped_rules.py` | `ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a` | `ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a` |

Actual changed-file hashes for each assigned control (before = corrected pristine):

| World | Path | Before | Mutated |
|---|---|---|---|
| held-key | `SKILL.md` | `55329286c674f324d5a8e9a07b13d4bd0b816423b2f39a9a0eef6728c197d18b` | `e32e1565aa601d39d6b85308becf26fa8e03ff61fe0c607a16a7015943185b6d` |
| alias | `SKILL.md` | `55329286c674f324d5a8e9a07b13d4bd0b816423b2f39a9a0eef6728c197d18b` | `02ec3142d5a2a3ed0a0f5b3e6718fe225920b866779b2a45a8cd75401d860040` |
| alias | `corpus/SOURCES.md` | `6eef67c3a3bedcb6c136b5619061c9ae4137d23e82f1fe6aed2373fce24c348a` | `2f9df4c650cbe9faa4d2b8e68aa280684cf422349ff8e1198615c6b6cf015e70` |
| alias | `corpus/knowledge/scoped-rules-round60.md` | `4791bea447d68e9238a180eef49f4c6c0b64420f33ae3bfb966b2341b26403df` | `44c4e0e792d6149174d63680643c6eea05097c3f56604ef885599ea79af7d277` |
| alias | `corpus/lessons/round-60.md` | `e956d384622f4d3cb9402f3924a122261ce72a8b4f3c1cefdd9ec7421c805197` | `c85b0142d807db3599d5578230b3f627eedcef6cbe6e0c3d06430b1c055e7a47` |
| alias | `.ufo/waves/round-60/snapshots/S103.page` | `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7` | `c568aae2c633029aa6a8b612de437f275bbe8f39c5866ef7382f89073e7f9c43` |
| alias | `.ufo/waves/round-60/snapshots/S104.page` | `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980` | `70aef6793ae9896ad98f12c75eb3d8c3cae504c6ea728c257b794d2f00c09e8e` |
| redirect | `corpus/SOURCES.md` | `6eef67c3a3bedcb6c136b5619061c9ae4137d23e82f1fe6aed2373fce24c348a` | `714a5b6ce247080fd11319724a6ffaa2470ad280bc37ea816bbd1b58b61c7848` |
| redirect | `corpus/lessons/round-60.md` | `e956d384622f4d3cb9402f3924a122261ce72a8b4f3c1cefdd9ec7421c805197` | `d21a8ad5c18a4b1a30e93b06ed36ba20812c37be463f2685d7f82a12a1ba5752` |

Actual restoration output:

```text
Held-key restoration all eight byte hashes equal baseline: True
Final restored all eight byte hashes equal baseline: True
```

All three assigned worlds were committed and measured. Held-key and wrong-final-base are killed; aliases survive exactly as expected and still require the L1’s explicit judgment rejection. No contract, counter, or lane implementation change is proposed or made by this seat.

C1 predicate: --fetch exit 0 (F>=TARGET) — MET

Report: .ufo/waves/round-60/controls-v2/CtlReopenHeldKey.md
