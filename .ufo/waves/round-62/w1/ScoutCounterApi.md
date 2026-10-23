# ScoutCounterApi — absorption-matrix guard API

Seat: `KotobaR62.ScoutCounterApi`. Read-only. Counter not edited.

Target: `verifiers/check_scoped_rules.py` (r61 freeze). Loaded sha256
`5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91`
(`self_sha()` == file bytes == `sha256sum`). Module name under the recipe is
`check_scoped_rules_frozen`, not `__main__`, so `main()` does not run
(import stdout/stderr empty). Stdlib only (`argparse` … `pathlib`). No
`claim` / `event` / `compound` function exists (grep `def .*(claim|event|compound)`
= 0; `dir` filter empty).

Patch rule, measured: every arm looks the helper up in the module global at
call time. `mod.<name> = stub` after `exec_module` is the patch. A reason-list
arm admits only on `[]`. A bool arm admits only on `True`. `url_key` admits
only on one hashable key for every non-empty URL. `lambda *a, **k: []` is the
wrong stub for `url_key` (TypeError, unhashable) and for `render_form`
(IndexError). `content_words = lambda text: set()` rejects harder; it does not
admit.

## Table

| erratum | guard(s) | lines | admitting stub | callers (production) | isolation risk |
|---|---|---|---|---|---|
| E2 A3 url_key | `url_key` (the guard); scored with `reopen_why` | `url_key` 651–669; check at `reopen_why` 1286 | `url_key = lambda url: "//x" if url else ""` | `reopen_why:1286`; `base_url_keys:679`; `entry_row_verdict:1362,1364`; `fetch:1543–1544`; `main:2528` | **High on `url_key`.** Same stub also disables E1 sub-rule 5 in `fetch` (measured: `url_key(final) in real_base_keys and != own` becomes False). Does **not** touch E2b/E2c/E2e/E2f. Do not stub `reopen_why` itself: that also admits E1 prefix / missing-target / key-already-present. |
| E2b A3(b) rendering alias | `render_form` (the guard); scored with `alias_why` | `render_form` 1117–1132; `alias_why` 1135–1152 | `render_form = lambda url: ("", "", False)` | `render_form` ← `alias_why:1143,1149` only. `alias_why` ← `entry_row_verdict:1369` only when `not reopens` | **Low.** `render_form` has no other caller. Stubbing it left an E2 `reopen_why` reject in place (measured). `alias_why = lambda *a, **k: []` also admits, and is no wider inside this arm. |
| E2c A4(iv) full-sha alias | `alias_sha_why` (no inner function) | 1186–1197 | `alias_sha_why = lambda *a, **k: []` | `entry_row_verdict:1382` only | **Low** among the five. `True` is the wrong stub: the call returns `True`, which `why.extend` would throw. Does not touch `intro_why` (A4 iii) or the sha-vs-bytes check (A4 i). |
| E2e A1 guarded key | **two** guards: `a1_conjunct`; `path_value` via `path_site` / `scope_conjunct` | `a1_conjunct` 1089–1100; `path_value` 1043–1050; `path_site` 1053–1065; `scope_conjunct` 1103–1112 | `a1_conjunct = lambda *a, **k: []` **and** `path_value = lambda text: True` | `a1_conjunct` ← `entry_row_verdict:1336` (unconditional). `path_value` ← `path_site:1063` only. `path_site` ← `scope_conjunct:1109`. `scope_conjunct` ← `entry_row_verdict:1401` (only after snapshot sha matches) | **Medium: the two guards do not cover each other** (measured). `path_value = True` does not admit a non-canonical key, a line with no `:`/`=`, an empty value, an embedded `xpaths`, or an out-of-range L. `path_site = lambda *a, **k: True` is wider (admits no-colon) but still does not admit out-of-range L. Live page uses `key_site`→`pattern_value`, **not** `path_value`. |
| E2f A2 guarded action | `action_conjunct` (no G7/G9 to patch) | 1010–1040 | `action_conjunct = lambda *a, **k: []` | `entry_row_verdict:1406` only. Helpers `content_words` / `page_words` / `fwd_need` / `rev_need` / `supported` / `covered` are not used by the other four arms | **Low cross-arm, hollow for the erratum.** The fraction checks are the whole landed guard. An event-claim cell the fractions accept already returns `[]` (measured); the stub does not change that verdict, so the mutation direction cannot show E2f absorbed. |

`entry_row_verdict` (1293–1412) is the only production function that calls every arm. Score the arm functions, not the row, or a second arm's reason keeps the row rejected after the stub.

## Signatures

```python
def url_key(url: str | None) -> str: ...
def reopen_why(row: list[str], url: str, key: str | None,
               base_rows: dict[str, list[str]],
               base_lines: dict[str, str]) -> list[str]: ...
def render_form(url: str) -> tuple[str, str, bool]: ...          # (host, path, stripped)
def alias_why(url: str, others: list[tuple[str, str]]) -> list[str]: ...
def alias_sha_why(sha: str, base_shas: dict[str, str],
                  teaches: str | None) -> list[str]: ...
def a1_conjunct(client: str, key: str | None,
                keys: dict[str, frozenset[str]]) -> list[str]: ...
def path_value(text: str) -> bool: ...
def path_site(lines: list[str], L: int, key: str | None) -> bool: ...
def scope_conjunct(lines: list[str], key: str | None, L: int | None) -> list[str]: ...
def action_conjunct(lines: list[str], cell: str, L: int | None,
                    page_text: str | None = None) -> list[str]: ...
```

`reopen_why` reads `row[6]` (teaches) and `base_rows[target][1]` (URL cell, fed to `urls_of`). That is the `sources_table` layout: index 6 teaches, index 1 source (`sources_table` 609–616). `base_lines[target]` is the raw line for `key_occurrences`.

## Smallest inputs (measured)

Reject = the committed counter's attack class. Accept = the smallest neighbour it already lets through. Vacuous accepts must not be used as instances: the committed counter already returns `[]`, so the stub cannot demonstrate absorption.

### E2 — `reopen_why(row, url, key, base, lines)`

`row = ["S900","x","docs","A","s","a","re-opens S010 — x","mined","2026-10-23","90d","y"]`
`base = {"S010": ["S010", "https://h.example/a.md", ...]}`
`lines = {"S010": "| S010 | https://h.example/a.md | t |"}`

| input | result |
|---|---|
| url `https://h.example/a` (`.md` dropped), `key=None` | `[]` accept. `url_key` both sides `//h.example/a` |
| url `https://h.example/b`, `key=None` | `['re-open names no base row with this URL']` reject |
| same reject after `url_key = lambda url: "//x" if url else ""` | `[]` |
| urls already match (`https://h.example/a`) but line contains `paths` and `key="paths"` | `['base row S010 already records key paths']` — E1.4, **not** flipped by the url_key stub |
| `url_key = lambda *a, **k: []` | `TypeError: cannot use 'list' as a set element` |

The url_key check is step 3. Steps 1–2 (no `re-opens S### —` prefix, target missing) and step 4 (key already on the base line) still reject after the stub. An E2 instance has to be a real re-open of a real base row whose key is absent, and whose only fault is path divergence `url_key` does not collapse.

### E2b — `alias_why(url, [(sid, other)])`

| input | result |
|---|---|
| `https://h.example/a` vs itself | `[]` |
| `https://h.example/a` vs `https://h.example/a.md` | `[]` (not a rendering; `.md` is E2's job) |
| `https://h.example/de/a` vs `https://h.example/a` | one `A3:` reason. `render_form` → `('h.example','a',True)` vs `('h.example','a',False)` |
| `https://h.example/v@1/a` vs `https://h.example/a` | one `A3:` reason |
| `https://h.example/enterprise/a` vs `https://h.example/a` | one `A3:` reason |
| `https://h.example/de/a` vs `https://h.example/b` | `[]` (stripped, but path `a` ≠ `b`) |
| `render_form = lambda url: ("", "", False)` on the `/de/` pair | `[]` |
| `render_form = lambda *a, **k: []` | `IndexError: list index out of range` |

`alias_why` returns `[]` immediately when `render_form(url)[2]` is False. A rejecting instance **must** contain a `LOCALE_SEGMENTS` segment (`de`, `en`, `ja`, …), an `@`, or a segment whose lowercase form starts with `enterprise`. Byte-identical `other == url` is skipped before the compare.

### E2c — `alias_sha_why(sha, base_shas, teaches)`

`sha = "ab"*32` (64 hex).

| input | result |
|---|---|
| `{sha: "S043"}`, teaches `"the row"` | one `A4:` reason naming `S043` |
| same, teaches `"supersedes S096 — x"` | `[]` (`SUPERSEDES_RE` is anchored `^supersedes`) |
| same, teaches `"note supersedes S096 — x"` | still the `A4:` reason (unanchored does not exempt) |
| `{("cd"*32): "S043"}` or `{}` | `[]` |
| stub `lambda *a, **k: []` | `[]` |
| stub `lambda *a, **k: True` | returns `True`, not a list |

The function does not check hex length. `row_sha` (633–638, `SHA256_RE`) is what refuses a prefix. A rejecting instance is a sha that is a key of `base_shas` whose teaches does not match `^supersedes\s+(S\d{3,})\b`.

### E2e — two independent rejects

Canonical half, `keys = {"Claude Code": frozenset({"paths"})}`:

| call | result |
|---|---|
| `a1_conjunct("Claude Code", "paths", keys)` | `[]` |
| `a1_conjunct("Claude Code", "patterns", keys)` | one `A1:` reason, canonical listed as `paths` |
| `a1_conjunct("Codex", "paths", {})` | one `A1:` reason, rows `S112/S113/S114/S115` absent |
| `a1_conjunct("Claude Code", None, keys)` | `[]` **vacuous** (`if key and key not in allowed`) |
| stub `a1_conjunct = lambda *a, **k: []` | `[]` on the `patterns` call; bold `scope_conjunct` still rejects |

Path-like half:

| call | result |
|---|---|
| `path_value("a/*/b")`, `path_value(" '**/*.py'")` | `True` |
| `path_value("**")`, `path_value("*.py")` | `False` |
| `pattern_value("**")` (v2, live-page path) | `True` — the bold hole v3 closed only on the snapshot side |
| `path_site(["globs: a/*/b"], 1, "globs")` | `True` |
| `path_site(["globs: **"], 1, "globs")` | `False`; `scope_conjunct` of the same → one `A1:` "not in key form with a path-like glob" |
| `path_site(["paths:", '  - "a/*/b"'], 1, "paths")` | `True` (block lookahead is landed) |
| `path_site(["globs=a/*/b"], 1, "globs")` | `True` — E2e's "no equals-form" is **not** landed (`KEY_SUFFIX_RE` allows `=` ) |
| `path_site(["# globs: a/*/b"], 1, "globs")` | `True` — "no commented keys" is **not** landed |
| `path_site(["globs a/*/b"], 1, "globs")` | `False` (no key form) |
| `path_site(["paths:"], 1, "paths")` | `False` (`value_after` is None; `path_value` is not called) |
| `path_site(['xpaths: "a/*/b"'], 1, "paths")` | `False` (identifier boundary) |
| `scope_conjunct(["globs: **"], None, 1)` | `[]` **vacuous** |
| `scope_conjunct(["globs: **"], "globs", 9)` | `A1: snapshot has no line 9` — **not** flipped by `path_value` or `path_site` stubs |
| `path_value = lambda text: True` | bold site → `True`, bold `scope_conjunct` → `[]`; no-colon, empty value, no-line, and `a1_conjunct("…","patterns")` stay rejected |
| `key_site(["globs: **"], 1, "globs")` while `path_value` is stubbed | still `True` (live arm never called `path_value`) |

Not landed from the E2e letter, from the function bodies (equals and comment also measured above): no one-key-per-cell check (`path_site` returns on the first hit), no negation window, no example/unchecked-cell test. `path_value = lambda text: True` is the stub that admits the bold / no-slash class and nothing coarser.

### E2f — `action_conjunct(lines, cell, L, page_text=None)`

| call | result |
|---|---|
| line = cell = `"Scope rules to specific files using matching patterns."`, L=1 | `[]` |
| `"Scope rules."`, L=1 | `['A2: action cell holds 2 distinct content word(s) (need >= 3)']` |
| lines `["aaaa bbbb cccc"]`, cell `"xxxx yyyy zzzz"`, L=1 | `['A2: action cell supports 0 of its 3 content word(s) at line 1 (need >= 2)']` (forward arm) |
| line = cell = `"xxxx yyyy zzzz"`, `page_text="nothing relevant here at all"` | `['A2: action word(s) xxxx, yyyy, zzzz do not occur on the committed snapshot']` |
| L `None`, or cell `""` | `[]` **vacuous** |
| line `"When agent reads file runtime emits event and loads matching rule files."`, cell the same with `` `InstructionsLoaded` `` backticked, L=1, page=line | `[]` **survivor**. `content_words` dropped `InstructionsLoaded` (4-letter backtick strip). No claim-verb symbol to stub |
| `action_conjunct = lambda *a, **k: []` | the 2-word reject becomes `[]` |
| `content_words = lambda text: set()` on the supported cell | `['A2: action cell holds 0 distinct content word(s) (need >= 3)']` — wrong direction |

E2f is unabsorbed for an event-claim instance: the committed arm already accepts it, so disabling `action_conjunct` does not change its verdict. The fraction rejects above are a different class; flipping them does not absorb G7.

## 10-line import recipe

Does not run `main`. `-B` / `dont_write_bytecode` so the lane gets no `__pycache__`.

```python
import hashlib, importlib.util, sys
sys.dont_write_bytecode = True
p = "/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py"
spec = importlib.util.spec_from_file_location("check_scoped_rules_frozen", p)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)  # __name__ != "__main__"; main() does not run
sha = hashlib.sha256(open(p, "rb").read()).hexdigest()
assert sha == mod.self_sha() == "5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91"
print(sha)
print(mod.url_key("https://cursor.com/docs/rules.md"))  # //cursor.com/docs/rules
```

## Measurement

Command (scratch probe, then `sha256sum`):

```
date -u; python3 -B /fast/scratch/hyaku/kotoba-r62/ScoutCounterApi/probe_api.py; echo PROBE_EXIT:$?
sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py
```

`date -u`: `Fri 23 Oct 2026 08:52:10 PM UTC`. Probe exit 0. `sha256sum` exit 0.

```
FILE_SHA 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91
SELF_SHA 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91
SHA_MATCH True
MODULE_NAME check_scoped_rules_frozen
IMPORT_STDOUT ''
IMPORT_STDERR ''
HAS_MAIN_RAN False
RECIPE_CALL //cursor.com/docs/rules
5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91  verifiers/check_scoped_rules.py
```

Follow-up (`python3 -B -` from the scratch dir; page-arm, E1.4, `render_form` list stub, fetch predicate): `Fri 23 Oct 2026 08:52:29 PM UTC`, exit 0. Outputs are the rows marked measured above. Lane `verifiers/` root listing after the load shows no `__pycache__`.

installs: no installs
blockers: none
Attacked the frozen counter's five erratum guards (`url_key`, `render_form`, `alias_sha_why`, `a1_conjunct`+`path_value`, `action_conjunct`) and recorded the admitting stub, smallest accept/reject, and caller isolation for each.
