# MutFixtures — generator-keying attack on the round-61 C1 world/fixture design

**Result: ATTACK DELIVERED (design probe).** All seven world fixtures (W1–W7) and all four
arm-killer classes (A1–A4) get a content-derived, source-blind, order-blind admission rule and
one concrete generator-keyed cheat that would make the rule hollow. Three high-risk frozen-design
seams found (S1–S3; four further fixture-design seams are in §5): **W2 is not rejectable by A3 as
worded**, **W1 cannot exercise A4 without a backdated blob-add commit**, and **W3 has two
simultaneous causes and therefore kills neither arm**.

Seat: `kotoba-r61-wave-MutFixtures` (mutation-tester). L1: `agent://KotobaR61`.
Base: `f3246d1493b60ea1c0d947a19c39f9e08e92f326`. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`
(read-only to this seat). No lane, fleet, sibling, `.ufo/state`, jj or git-index file was written;
the only lane write is this report. No subagent, ask tool, switch, install, or network fetch was used.
No counter CLI or `--self-test` was run: v3 does not exist at the base, so there is no
mutant/restore pair to record; v2 helper functions were imported read-only only for the key-site
sweep below.
The "expected detector" for this probe is the admission battery in §2; the "output" is this report;
"restoration evidence" is that no source byte changed (no write path other than this report).

## 0. Ground read, and the three measurements this seat ran

Read (all lane-committed bytes): `plans/round-61.md` §C1; `verifiers/check_scoped_rules.py` (v2,
sha256 `ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a`) at the self-test
(`:1270–2490`), the world helper (`:1668–1815`), `entry_row_verdict` (`:997–1099`), `reopen_why`
(`:972–995`), `scope_conjunct` (`:915`), `action_conjunct` (`:894`), and the CLI test (`:2278–2490`);
`.ufo/waves/round-60/controls-v2/SUMMARY.md`, `CtlReopenForged.md`, `CtlReopenHeldKey.md`,
`CtlRescoreV2.md`; `.ufo/waves/round-60/controls/SUMMARY.md`; `.ufo/waves/round-60/build/ExecKeyForms.md`;
`.ufo/waves/round-60/w0b/RecensusClaudeCode.md`, `RecensusCopilotCLI.md`;
`.ufo/waves/round-56/controls/CtlC2GeneratorKeyed.md` and `.ufo/waves/round-57/controls/CtlC2GeneratorKeyed.md`;
the four eligible rows at `SKILL.md:141,143,144,146`, `corpus/knowledge/scoped-rules-round60.md:15–18`,
and `corpus/SOURCES.md:115–120`.

Measurement 1 — the committed r60 snapshot pages (read-only, `date -u` `Fri 23 Oct 2026 07:13:34 PM UTC`):

```text
$ sha256sum .ufo/waves/round-60/snapshots/*
82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7  .ufo/waves/round-60/snapshots/S103.page
9d1f87a2d1cb55b4782b95abe710692b35b9659789c2db31a22c7074a3383e8e  .ufo/waves/round-60/snapshots/S104.page
a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f  .ufo/waves/round-60/snapshots/S105.page
00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980  .ufo/waves/round-60/snapshots/S106.page
e5fbfd6d580643a300b5ee0e622d9e2d8f97d4d23460e6b08e1c656251c2f2c2  .ufo/waves/round-60/snapshots/S107.page
884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8  .ufo/waves/round-60/snapshots/S108.page
dfb242d9a8c0cfb1c97cee74a895b56ba72cba64b558200f06eede4f5f93cb54  .ufo/waves/round-60/snapshots/S109.page
$ echo $?
0
```

Measurement 2 — held-out-key sweep with v2's own `key_site` over the four eligible pages
(`date -u` `Fri 23 Oct 2026 07:13:34 PM UTC`; read-only import of the lane counter):

```text
$ python3 -B - <<'PY'
import sys, re
sys.path.insert(0, 'verifiers')
import check_scoped_rules as c
pages = {
 'Claude Code': '.ufo/waves/round-60/snapshots/S103.page',
 'VS Code': '.ufo/waves/round-60/snapshots/S105.page',
 'Copilot CLI': '.ufo/waves/round-60/snapshots/S106.page',
 'Cursor': '.ufo/waves/round-60/snapshots/S108.page',
}
canon = {'Claude Code': {'paths'}, 'VS Code': {'applyTo'},
         'Copilot CLI': {'applyTo'}, 'Cursor': {'globs'}}
named = {'patterns','claudeMdExcludes','sessions','Sync','rules','order'}
for client, path in pages.items():
    lines = open(path, encoding='utf-8').read().splitlines()
    hits = []
    for L, line in enumerate(lines, 1):
        for m in re.finditer(r'[A-Za-z0-9_][A-Za-z0-9_-]*', line):
            tok = m.group(0)
            if tok in canon[client]:
                continue
            try:
                ok = c.key_site(lines, L, tok)
            except Exception:
                ok = False
            if ok:
                hits.append((tok, L))
    uniq = sorted(set(hits))
    extra = [h for h in uniq if h[0] not in named]
    print(client, 'passing non-canonical (K,L):', uniq)
    print(client, 'held-out candidates (not in ExecKeyForms names):', extra[:15])
PY
Claude Code passing non-canonical (K,L): [('claudeMdExcludes', 339), ('patterns', 238)]
Claude Code held-out candidates (not in ExecKeyForms names): []
VS Code passing non-canonical (K,L): [('Sync', 287), ('sessions', 32), ('sessions', 128), ('sessions', 221), ('sessions', 228)]
VS Code held-out candidates (not in ExecKeyForms names): []
Copilot CLI passing non-canonical (K,L): []
Copilot CLI held-out candidates (not in ExecKeyForms names): []
Cursor passing non-canonical (K,L): [('order', 307), ('rules', 146)]
Cursor held-out candidates (not in ExecKeyForms names): []
$ echo $?
0
```

Measurement 3 — the A3 same-key-different-bytes probe pair (`date -u` `Fri 23 Oct 2026 07:16:48 PM UTC`):

```text
$ python3 -B - <<'EOF'
import sys
sys.path.insert(0, 'verifiers')
import check_scoped_rules as c
for u in ('https://cursor.com/docs/rules', 'https://cursor.com/docs/rules.md',
          'https://code.claude.com/docs/de/memory.md',
          'https://code.claude.com/docs/en/memory.md'):
    print(u, '->', c.url_key(u))
EOF
https://cursor.com/docs/rules -> //cursor.com/docs/rules
https://cursor.com/docs/rules.md -> //cursor.com/docs/rules
https://code.claude.com/docs/de/memory.md -> //code.claude.com/docs/de/memory
https://code.claude.com/docs/en/memory.md -> //code.claude.com/docs/en/memory
$ echo $?
0
```

The pair `.../docs/rules` and `.../docs/rules.md` has one `url_key` and two byte-different URLs:
it is the concrete A3 byte-identity probe. The German and English pages have different keys, which
is why a `url_key`-based A3 accepts the alias (S1).

Restoration / no-mutation evidence (`date -u` `Fri 23 Oct 2026 07:17:56 PM UTC`):

```text
$ sha256sum verifiers/check_scoped_rules.py
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  verifiers/check_scoped_rules.py
$ echo $?
0
```

The v2 counter bytes are the r60 freeze bytes; no counter was mutated in this probe, so there is no
before/after mutant pair to restore. The only lane write is this report.

Consequence for the attack: on the four eligible pages the only form-valid non-canonical key
sites are exactly the six names the ExecKeyForms probe already published (`patterns`,
`claudeMdExcludes`, `sessions`, `Sync`, `rules`, `order`). **No seventh held-out form-valid key
exists on those pages**, so a W5 fixture built only from the recorded pages cannot detect a
deny-list of those six names. The A1 admission test therefore needs a synthetic held-out key
arm (§4 A1) or the risk must be declared.

## 1. The class, and why this fixture set is exposed

A **generator-keyed** fixture is one whose verdict is decided by metadata of the fixture
generator rather than by repository content: the counter's own source text, constants, reject
strings, fixture IDs/names/paths, enumeration order, shared work directories, or an oracle that
is the same code as the detector. The r56 and r57 controls are the precedents:

- r56 `CtlC2GeneratorKeyed` passed `5 of 9`, exit 0, on 10 of 10 seeds with a delegate that
  never opened a case file. It read the shared work directory: `ordinal =
  len(list(target.parent.parent.iterdir())) - 2`, then indexed a fixed PASS/FAIL schedule
  (`.ufo/waves/round-56/controls/CtlC2GeneratorKeyed.md:1,5` and its "WHY IT WORKS" §1–2).
  The counter ran cases in a fixed order and did not shuffle (`build_cases` did not shuffle).
- r57 `CtlC2GeneratorKeyed` passed `120 of 120` (240 of 240 over six seeds) with a 28-line patch
  keyed on three generator properties: the case-directory name `skill-<8 hex>`, the counter's
  fixed `REAL_COMMANDS` literals, and substring containment of the expected head in the detail
  (`.ufo/waves/round-57/controls/CtlC2GeneratorKeyed.md:1,5–24`).

The r61 C1 design is exposed for the same reasons:

1. The predicate is a **single printed sentence** (`worlds reject 7 of 7; eligible rows pass 4 of 4`)
   plus exit 0. That sentence can be printed without scoring the worlds.
2. The worlds are **reconstructed by the same wave that writes the counter**, from receipts the
   counter author reads; the fixture generator and the counter are the same author, same branch,
   same run.
3. The v2 self-test's fixture style is **in-source synthetic literals** (`world()` at
   `verifiers/check_scoped_rules.py:1734`, pages `:1670–1715`). Carrying that style into the seven
   worlds would make every world byte a generator byte.
4. The four "eligible rows" can be **substituted** by v2's easy synthetic S900–S903 world
   (`page900–903`, keys `paths`/`globs`/`applyTo`/`applyTo`), which passes without ever exercising
   the real r60 rows or A1's canonical set.
5. The self-test can read its own source (`Path(__file__).read_text()`), and v2 already does this
   for `self_sha()` (`:374`); nothing in the current style prevents the same read being used as a
   verdict.

The three admission constraints used below are: **content-derived** (the verdict is a function of
the same bytes, rows, page lines and git history the `--rev` path reads); **source-blind** (the
verdict path never reads the counter source, its constants, its reject strings, its arm names,
fixture IDs/paths, or a known r60 sandbox hash); **order-blind** (the verdict is invariant under
permutation, renaming, isolation, and shared-directory sibling count).

## 2. Admission battery — run these before any v3 freeze

Every test is adversarial: it should break a generator-keyed fixture, not merely pass a correct one.
`$C` is the candidate counter at `verifiers/check_scoped_rules.py`; `$F` is the committed fixture
root the self-test reads.

- **T1 permutation.** Score the seven worlds alone, in reverse, and in a seeded shuffle. Diff the
  `world -> verdict/cause` matrix. Any difference is an order-keyed fixture or an order-keyed counter.
  The r56 ordinal cheat (`len(iterdir())-2`) and the r57 case-name cheat both die here.
- **T2 identity scrub.** Rename every S-ID (`S103`→`S900`, …), every fixture directory (`W1`→`A`),
  every commit message, and reverse the row order inside each table. Re-score. The matrix must be
  identical. A verdict that changes is keyed to an identifier, not to content.
- **T3 source-token scan.** For every distinctive fixture token (IDs, page hash prefixes, wrong-key
  names, invented-cell phrases, alias URL fragments), `grep -n` the counter's **production** path
  (`entry_row_verdict`, `judge`, `fetch`, `reopen_why`, `scope_conjunct`, `action_conjunct`) — not
  the self-test data table. Any occurrence in a branch/condition is a red flag. Occurrences in the
  expected-value table are allowed only if they are data, never predicates.
- **T4 message reword.** Reword every reject message in `$C` (no semantic change). `--self-test`
  must still pass. If it fails, the test asserts source/message text, not behavior. The only literal
  that must stay exact is the frozen predicate sentence itself.
- **T5 arm ablation.** In a scratch copy, delete or invert exactly one arm (A1→warn-only,
  A2→no-op, A3→normalize, A4→skip the date walk). Run `--self-test`. Exactly the arm's world/killer
  must flip (reject→pass), and the self-test must fail naming it; all other worlds must keep their
  verdicts. If the world stays rejected, the world is double-caused and is not that arm's killer.
- **T6 oracle independence.** Commit the expected `world -> cause` table **before** v3 exists, derived
  from `plans/round-61.md` and the r60 receipts. No fixture manifest may carry an `expected`,
  `verdict`, `pass`, `fail` or `mutant` field the counter reads. Diff the expected table against the
  v3 output; equality must not be produced by running v3 once and saving its output.
- **T7 no self-source read in the verdict path.** `grep -n '__file__\|read_text\|inspect\.\|getsource\|__doc__' $C`.
  `self_sha()` is the only allowed use. The `judge`/`entry_row_verdict`/`fetch` path must contain none.
- **T8 no harness clock.** `grep -n 'time\.\|datetime\|now()\|date -u' $C` in the fixture/self-test
  builder. Every date is a receipt literal. The W1 fixture in particular must not derive its
  commit dates from the host clock.
- **T9 predicate sentence is computed.** Mutate one world (remove its defect) and require the
  sentence to change and the exit to become 1. A hard-coded
  `print("worlds reject 7 of 7; eligible rows pass 4 of 4"); return 0` fails this test.

## 3. W1–W7: rule and concrete cheat

Numbering follows the plan. "Cause" is the semantic reason the world must be rejected under v3,
not a printed string (the string may be reworded by T4).

### W1 — `CtlReopenForged d` (recycled round-53 bytes under a fresh-fetch claim)

**Frozen content.** The three d-world rows (Claude `paths`, Copilot `applyTo`, Cursor `globs`),
with the real quote/key/action lines recorded in `.ufo/waves/round-60/controls-v2/CtlReopenForged.md`;
S103 snapshot = the round-53 `memory.md` bytes `971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff`
(51,971 B), S104/S105 = the round-53 Copilot/Cursor files `00e45ea5…` and `884c67ca…`
(byte-identical to the r60 fetch, as the receipt discloses). These are the d world's own ids
(S104=Copilot, S105=Cursor); they are not the lane's r60 S104/S105 (Codex/VS Code). The rows retain the forged claim
`Fetched 2026-10-23T12:06:23Z`. **History:** a commit dated 2026-10-22 (the r53 acquisition day:
S043 `2026-10-22T20:04:43Z`, S048 `20:05:13Z`, S049 `20:09:33Z`) adds the three snapshot blobs;
a later commit dated 2026-10-23 adds the rows; A4 measures the row commit. A single-commit
fixture cannot exercise A4 (see S2).

**Expected v3 cause.** A4: earliest `git log --diff-filter=A` commit for each snapshot path is
older than the row's recorded `opened` date (`2026-10-23`). Every other A1–A3 conjunct is
satisfied: sha equals the committed old bytes, quote is verbatim, key is canonical, URL is the
base row URL byte-identically.

**Rule.**
- **content-derived:** the verdict is computed from the fixture repo's own history at the row
  commit and the row's `opened` cell. Both dates are literals from the r60/r53 receipts
  (`2026-10-22T20:0xZ` and `2026-10-23T12:06:23Z`), never from the host clock. A4 must be exercised
  through the `--rev`/git path, not `judge()` over in-memory bytes with no history.
- **source-blind:** no branch on `W1`, `forged`, `recycled`, `971d75bf`, the r53 fetch time, or any
  v3 reject string. Rename `S103`→`S900`, rename the fixture directory, re-commit the same tree
  under a new hash; the verdict must not change.
- **order-blind:** reject when scored first, last, alone, with a duplicate, and with the three
  snapshot paths added in any order. No expected value may be indexed by world number.

**Generator-keyed cheat — `W1-name-gate`.** Put the fixture under `W1-forged/` and make A4 start
`if "forged" in str(snapshot_path) or row_sha.startswith("971d75bf"): return ["recycled"]`. The
fixture is a single commit dated today, so there is no blob-add comparison at all; the self-test
still counts W1 rejected. Delete the date walk and the label/hash branch still rejects; the
arm-killer is hollow. A subtler variant: set `GIT_AUTHOR_DATE` for the blob commit and compute the
expected verdict from the same variable, so the comparison is a tautology that cannot fail.
**Detection:** T2/T5 plus a rebuild with a different old page (different hash, same 2026-10-22 add
date); a content-derived A4 rejects, the label cheat accepts.

### W2 — `CtlReopenHeldKey b` (locale/enterprise alias URLs with real content)

**Frozen content.** German Claude `https://code.claude.com/docs/de/memory.md` (the alias page
bytes hashed `c568aae2…` in `CtlReopenHeldKey.md`'s byte table) and enterprise Copilot
`https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md`
(alias page bytes `70aef679…`), with the real German/enterprise quote/key/action lines; Cursor is
the genuine S049 re-open. Base rows S043/S048 are the real `corpus/SOURCES.md` rows.

**Seam first (S1).** The recorded alias rows are **fresh non-base rows**, not re-open rows:
`CtlReopenHeldKey.md` says "Both aliases were fetched without redirect to a base URL" and "Cursor
remains a genuine S049 re-open." A3 as frozen ("a re-open row's URL must be byte-identical to its
base row's URL") therefore never evaluates the alias rows; v3 would accept W2 as recorded and the
`7 of 7` sentence would be false. The fixture cannot be fixed by silently adding a `re-opens`
prefix: that makes the base-row URL test fail structurally (the named base row's URL is not the
alias URL), so the world is no longer the recorded W2. Even with the prefix, v2's code calls
`reopen_why` only when `url_key(url)` is in the base URL set (`entry_row_verdict`, the
`url_key(url) in base_urls` branch); the alias URL's key is not in that set, so v3 must move the A3
check onto the re-open-prefix path for the alias to reach A3 at all. The L1 must resolve S1 before
freezing.

**Expected v3 cause (only if A3 is extended, see S1).** A3: the row's URL is not byte-identical to
the named base row's URL, though the page content is real. If the fixture stays fresh, the only
honest causes are elsewhere (e.g. a canonical-rendering rule), and the plan must say so.

**Rule.**
- **content-derived:** A3 compares the row URL cell to the named base row URL cell byte-for-byte
  from the fixture's own `SOURCES.md`; the alias pages must be the real fetched bytes (their real
  quote/key/action line numbers match the selected line numbers); the expected reject follows from
  the two URL strings plus the fact that no other conjunct fires. No `url_key`, no normalization.
- **source-blind:** no `/de/`, `enterprise-cloud`, `alias`, `locale`, host name, or receipt hash in
  the decision. The same byte difference moved to another pinned host/path must reject identically;
  a held-out alias must reject; a byte-identical re-open must pass.
- **order-blind:** score the byte-identical re-open (pass) and the alias (reject) as a pair in both
  orders; the verdict must not depend on which row is read first or on the row's position in the
  client list.

**Generator-keyed cheat — `W2-alias-deny-list`.** Implement A3 as
`if "/de/" in url or "enterprise-cloud@latest" in url: reject`. The fixture uses exactly the two
recorded aliases, so W2 rejects; a held-out `/docs/fr/memory.md` alias with real content passes, and
deleting the byte comparison leaves the token check. The same cheat in the self-test is asserting
`url_key(alias) != url_key(base)` (the v2 normalization) as the expected value, which tests the
generator's helper, not the byte-identity rule.
**Detection:** T5 (delete A3 → W2 must flip) plus the held-out alias, and the same-key-different-bytes
pair (`https://cursor.com/docs/rules` vs `https://cursor.com/docs/rules.md`, which normalize to the
same `url_key` `//cursor.com/docs/rules`) — byte-identity must reject the pair, key-equality accepts it.

### W3 — `CtlReopenHeldKey a` (re-open whose base row already holds K)

**Frozen content.** Cursor row key `rules` cited at S108/Cursor line 146 ("There are two ways to
create rules:", next line `- **…`, so `key_site` is true); the page bytes, quote, Action, URL, SHA
pin and `re-opens S049 —` cell are the real Cursor row; `corpus/SOURCES.md:62` (S049) contains
`rules` at identifier boundaries (verified: offsets 55/201/209/239/617 in the committed line).

**Double cause (S3).** Under v3 this world is rejected twice: A1 (`rules` is not in Cursor's
canonical set `{globs}`) and the retained v2 held-base rule (`base row S049 already records key
rules`, `reopen_why` at `check_scoped_rules.py:972–995`). Deleting either arm leaves the other
rejecting. W3 is therefore a valid world-level reject but **not an arm-killer for either arm**.

**Rule.**
- **content-derived:** the world-level verdict is reject; the self-test must assert the cause set it
  actually got, and must not claim W3 proves the held-base rule while A1 also fires. If W3 is used
  as an arm-killer, the fixture must be single-caused (a synthetic base row that contains a
  canonical key, or the held-base rule ablated with A1 present and a different key).
- **source-blind:** no hard-coded `(S049, rules)` pair; the held-base rule scans the named base
  row's own line. Rename S049→S900 with the same line text and the held-base cause must persist.
- **order-blind:** score alone/permuted; the base-row scan must not depend on the row's position in
  the base table or on the order of the worlds.

**Generator-keyed cheat — `W3-source-grep-held-key`.** The self-test asserts
`check("W3 held key", "already records key" in Path(__file__).read_text(), True)`, or compares the
world's `why` list to a literal containing the held-base message; since A1 also rejects, the test is
green even when the held-base rule is deleted. The pair-gate variant
`if key == "rules" and base_id == "S049": reject` never reads the base line; rename the base id and
the held-base cause disappears (A1 still rejects, so only a cause-level assertion exposes it).
**Detection:** T4 (reword messages) and a cause-level ablation: delete the held-base rule, keep A1,
and require the self-test to report a missing cause for W3 rather than merely "rejected".

### W4 — `CtlReopenHeldKey c` (live redirect to a different base key)

**Frozen content.** Request `https://cursor.com/docs/context/rules`, teaches `re-opens S052 —`,
recorded live final URL `https://cursor.com/docs/rules` (the S049 base key), not S052's
`https://cursor.com/help/customization/rules.md`; real Cursor page bytes at the final URL; real
quote/key/action. The r60 receipt notes the request URL is non-base, so the structural
`reopen_why` check is skipped (`check_scoped_rules.py:1054–1059` in the receipt's numbering); the
kill came from the live redirect guard.

**Expected v3 cause.** The fetch guard: the final URL is a base SOURCES key
(`//cursor.com/docs/rules`, S049) while the row names S052 as its base row
(`//cursor.com/help/customization/rules`); the request URL is non-base, so the structural
`reopen_why` check is skipped and the guard rejects the base final URL. The `--self-test` must
replay the recorded `url_effective` through the `run_curl` seam (v2 already patches `run_curl` at
`:2278–2290`), not touch the network.

**Rule.**
- **content-derived:** the expected reject follows from the recorded final URL being a base key
  (S049's `//cursor.com/docs/rules`) while the row's request URL is non-base and its named base row
  is S052 (`//cursor.com/help/customization/rules`); a same-key redirect must pass. The replay must
  use the receipt's recorded request/final strings, not a fresh fetch.
- **source-blind:** no `cursor.com`, `docs/context/rules`, `S052`, or receipt hash in the guard; a
  held-out request on another pinned host that redirects to a different base key must reject
  identically. The general rule is: a base final URL is accepted only when the row's request URL is
  itself that base key (its own key); a non-base request has no own key, so any base final URL is
  rejected.
- **order-blind:** score the benign same-key redirect (pass) and the cross-base redirect (reject) in
  both orders; the verdict must not depend on which is first or on the world's index.

**Generator-keyed cheat — `W4-request-path-literal`.** `if "docs/context/rules" in request_url:
reject`, or the self-test's `run_curl` returns `"https://cursor.com/docs/rules"` from a literal that
also appears in the guard. Deleting the own-key comparison leaves the literal; a held-out request on
another path passes. **Detection:** T5 and a moved-request case; also a same-key redirect that must
pass, which an always-reject literal fails.

### W5 — wrong scope-key (ExecKeyForms)

**Frozen content.** The real Claude S103 page with Scope key `patterns` (S103 :238; the line is
`…expanded patterns: \`src/*.{ts,tsx}\`…`, and `key_site` is true) or `claudeMdExcludes` (:339); or
VS Code `sessions` (:32/128/221/228), `Sync` (:287); or Cursor `order` (:307). The real quote and
Action; the row otherwise eligible. Canonical per-client set: Claude `paths`, VS Code/Copilot
`applyTo`, Cursor `globs`. The page's canonical key (`paths` :198) is the positive control.

**Expected v3 cause.** A1: the key is not in the client's canonical set, although it is in key
form with a path-like value. The key form alone (v2's `key_site`) must not be the reject reason.

**Rule.**
- **content-derived:** the reject follows from the key cell, the client, and the canonical set
  grounded in S112–S115; the same page's canonical key passes. The canonical set must be a
  per-client membership rule, not a copy of the fixture's names.
- **source-blind:** no deny-list of the six ExecKeyForms names (`sessions`, `Sync`, `patterns`,
  `claudeMdExcludes`, `rules`, `order`); no literal in `scope_conjunct`/`entry_row_verdict`. A
  held-out form-valid key not named in any r60 report must reject too. **Because the four eligible
  pages have no seventh form-valid key (measurement 2), W5 alone cannot detect a six-name deny-list
  — add a synthetic held-out-key arm or declare the residual risk.**
- **order-blind:** reject regardless of world position; membership must not depend on the row's
  index in `CLIENTS` or on table row order.

**Generator-keyed cheat — `W5-probe-deny-list`.** `NONCANONICAL = {"sessions", "Sync", "patterns",
"claudeMdExcludes", "rules", "order"}` copied from `ExecKeyForms.md`; W5's key is a member; the
self-test asserts `"patterns" in NONCANONICAL` (or the fixture path contains the key). A held-out
`excludes:` key passes; a per-client wrong assignment (e.g. `globs` on a Claude row with a synthetic
`globs:` line — canonical for Cursor, not Claude) also passes if the set is not keyed by client.
**Detection:** the held-out-key arm, the cross-client key assignment, and T3 (no deny-list literal in
the production path).

### W6 — invented Action cell

**Frozen content.** The real Claude S103 page; the invented cell
`Create the rule file in the project and add frontmatter so it loads only for the matching files.`
cited at Claude :209 (the line says "Rules without a `paths` field are loaded unconditionally…");
the real `paths` key at :198; the real quote, SHA, URL. The cell passes v2's lexical gate
(6 of 12 invented cells did; `ExecKeyForms.md` Part 2), so A2 is the only reject. The real Action
cell (`Scope rules to specific files using YAML frontmatter…`, S103 :194) is the passing control.

**Expected v3 cause.** A2: the cell's load/event claim ("loads only for the matching files") is
contradicted by the cited line ("loaded unconditionally"); the reject follows from the cell text and
the cited page line, not from word counts.

**Rule.**
- **content-derived:** A2 parses the Action's load/event claim and checks support/contradiction on
  the cited line. The fixture must include the real cell (pass), the invented cell at its
  **best-scoring** line (:209, where v2's lexical gate passed it), and a held-out paraphrase
  (reject). A cell cited at a line v2's word-overlap already rejects is not admissible as the A2
  killer: the world would reject for the old reason and A2 could be deleted unnoticed.
- **source-blind:** no substring of the recorded cell (`frontmatter so it loads only`), no list of
  the 12 ExecKeyForms cells, no reuse of `content_words`/`action_need` as the oracle.
- **order-blind:** score the real and invented cells in both orders and alone; the reject must not
  depend on the invented cell being case 6.

**Generator-keyed cheat — `W6-phrase-key`.** `if "frontmatter so it loads only" in cell: reject`;
the fixture uses the exact recorded sentence; a held-out paraphrase
("Add YAML metadata so the rule applies exclusively to files it matches.") passes. The subtler
variant is **oracle reuse**: the expected value is `action_conjunct(...)` from v2, so the test
asserts the old lexical result and never exercises A2; with the best-line cell the old gate passes,
so the test can only go green if it keys on a phrase.
**Detection:** T5 (delete A2 → W6 must flip to pass), the held-out paraphrase, and T4.

### W7 — v1-hollow rescore world (regression)

**Frozen content.** One exact revision from `CtlRescoreV2.md`: `43513eeaa274098f8d0b98941016b4418f854d20`
(CtlNoReader probe, S 1/4, F 1/4, exit 1) or `a2893fa26d08cda5a866875af121046573b699fa`
(CtlFabSnapshot pristine, 1/4, 1/4). The tree is copied from the receipt's saved clone; it is not
regenerated from a template. `W0` is the base/no-section world (exit 1).

**Expected v3 cause.** The content that made the v1 world hollow (missing snapshot or invented
quote/action/URL class, as the chosen receipt reports); the S/F counts and exit come from
`CtlRescoreV2.md`, not from v3. Exit 1 alone is not evidence: every v1 world exits 1.

**Rule.**
- **content-derived:** the verdict is computed from the world's own rows/pages; the fixture must be
  re-committed under a new commit hash with renamed IDs and still reject; a fresh hollow world of
  the same class must reject; `W0` must exit 1. The expected S/F/exit table is a receipt value.
- **source-blind:** no known r60 sandbox hash (`43513ee`, `a2893fa`, …), no `CtlNoReader`/
  `CtlFabSnapshot` label, no `S9xx` ID-range rule, no v3 reject string in the decision.
- **order-blind:** reject alone and in any permutation; `W0` and `W7` must be scored separately; no
  index-based expected list.

**Generator-keyed cheat — `W7-known-rev-gate`.** `if rev in KNOWN_HOLLOW: return 1`, or
`if all(sid.startswith("S9") for sid in ids): reject`; the fixture is the recorded rev and IDs, so
it rejects without reading content. A fresh hollow world with `S5xx` IDs passes. **Detection:** the
re-commit-under-new-hash/renamed-ID case and a fresh hollow world; T2.

## 4. A1–A4 arm-killers: rule and concrete cheat

Each arm-killer is a **single-defect fixture that fails only if its arm is deleted or inverted**
(the plan's `ExecSelftestArms` requirement). The killer must be scored through the same
`judge`/`--rev` path as real rows; the expected value is the verdict **and** the arm cause; the
paired positive control must pass in the same run.

### A1 — canonical scope-key set

**Fixture.** A row whose only defect is a form-valid, page-backed key outside the client's
canonical set; every other conjunct satisfied. Use a real recorded key (`patterns` at Claude :238)
for the world, and a **held-out synthetic key** (e.g. `excludes: "**/*.test.ts"` in a self-contained
synthetic page, or a key canonical for another client) for the killer; the positive control is the
same page/client with the canonical key.

**Rule.**
- **content-derived:** the verdict and the A1 cause come from the key cell, the client, and the
  per-client set; the key must be in key form (`key_site` true) so the old form test cannot be the
  cause; the positive control must pass.
- **source-blind:** no key literal, client name, line number, fixture ID, or self-source read in
  A1; the set is membership by client, not a deny-list; the held-out key must reject.
- **order-blind:** the killer rejects alone and in any position; the positive control passes in the
  same run; no ordinal/index.

**Generator-keyed cheat — `A1-source-grep-tautology`.** The self-test does
`src = Path(__file__).read_text(); check("A1 killer", "canonical" in src and "patterns" not in
CANONICAL["Claude Code"], True)` — it never scores the world; delete the A1 check and the test is
still green. This is the r57 `GEN_CASE_NAME_RE` class applied to the test itself, and the exact
"greps its own source for mutant texts" pattern in the assignment. **Detection:** T5 (delete A1 →
the self-test must fail), T7 (no `__file__`/`read_text` in the verdict path), and T4.

### A2 — semantic Action support

**Fixture.** A real page, canonical key, correct SHA/quote, and an Action cell whose load/event
claim is contradicted by the cited line, while the cell passes v2's lexical gate. Pair with the real
Action cell (pass) and a held-out paraphrase (reject).

**Rule.**
- **content-derived:** the cause is computed from the cell text and the cited line (support or
  contradiction); the fixture uses the best-scoring line (:209), not a line the old word-overlap
  already rejects; the paraphrase pair proves the rule is semantic, not lexical.
- **source-blind:** no recorded-cell phrase, no list of probe cells, no `content_words`/
  `action_need` reuse as oracle.
- **order-blind:** real and invented cells scored in both orders; no case index.

**Generator-keyed cheat — `A2-oracle-reuse`.** The self-test's expected value is
`action_conjunct(lines, cell, line)` (the v2 helper) or a hard-coded set of the 12 ExecKeyForms
cells; the test asserts the old lexical result. With the best-line cell, the old gate passes, so the
test can only be green by keying on the phrase; with a thin cell, the old gate rejects, so deleting
A2 leaves the old gate rejecting and the killer never flips. Either way A2 is not tested.
**Detection:** T5 (delete A2 → the killer must pass), T4, and a held-out paraphrase.

### A3 — URL byte-identity

**Fixture.** A re-open row whose URL is a real alias (German Claude / enterprise Copilot) or the
same-key-different-bytes pair (`https://cursor.com/docs/rules` vs
`https://cursor.com/docs/rules.md`), with real content and every other conjunct satisfied; the
paired positive is the base row URL byte-identically. The base URL is read from the named base row.
**Use the same-key pair for the killer, not the German alias:** v2's structural `reopen_why` accepts
`rules` vs `rules.md` because `url_key` normalizes `.md`, so A3's byte check is the only reject;
the German alias has a different key and is rejected earlier by the structural rule, which masks A3.

**Rule.**
- **content-derived:** byte comparison of the row URL cell and the named base row URL cell; both
  directions scored (identical→pass, different→reject); no normalization.
- **source-blind:** no alias token/host/path, no `url_key`, no receipt hash; the base URL comes from
  the fixture's base row; a held-out byte difference on another host must reject.
- **order-blind:** both pair members scored in either order; no positional expectation.

**Generator-keyed cheat — `A3-normalization-equivalence`.** Use `url_key(row) != url_key(base)` in
the arm (or in the self-test's expected value). The alias has a different key, so W2/the killer
passes; the same-key-different-bytes pair (`rules` vs `rules.md`) is accepted although byte-identity
must reject it; deleting the byte comparison leaves the key comparison. **Detection:** the
same-key pair, T5, and T3 (no `url_key` in A3's decision).

### A4 — snapshot provenance date

**Fixture.** A snapshot whose bytes, sha256 and quote are internally consistent, but whose
blob-add commit is older than the row's recorded `opened` date; every other conjunct satisfied.
Paired pass: blob-add on/after the opened date. The history is a real fixture repo (or a temp repo
built from a committed manifest with fixed dates), measured at the row commit via
`git log --diff-filter=A --format=… -- <snapshot path>`.

**Rule.**
- **content-derived:** the date comparison reads the fixture repo's own history at the row commit
  and the row's `opened` cell; both dates are receipt literals; the paired pass proves the arm does
  not reject everything; a single-commit fixture is inadmissible (it cannot reject).
- **source-blind:** no r53 hash (`971d75bf…`), no `W1`/`forged` literal, no `OPENED` constant in
  place of the row cell, no wall clock, no self-source read.
- **order-blind:** the blob-add and row commits may be scored in any construction order; the verdict
  must not depend on commit count or position; score alone.

**Generator-keyed cheat — `A4-constant-date-tautology`.** Set the row's `opened` cell from the
counter's `OPENED[0]` constant and the blob date from a literal that is always older; compute the
expected reject from the same literal. Without the paired pass, an always-reject stub
(`return ["recycled"]`) passes every case. The hash-gate variant (`if blob_sha.startswith("971d75bf"):
reject`) is the same class. **Detection:** the paired pass, the two-direction date pair
(blob 2026-10-21 / opened 2026-10-22 → reject; blob 2026-10-23 / opened 2026-10-23 → pass), and T2.

## 5. Frozen-design seams the L1 must resolve before freezing v3

- **S1 — W2 is not covered by A3 as worded.** A3 says "a re-open row's URL must be byte-identical
  to its base row's URL". The recorded W2 rows are fresh non-base rows (`CtlReopenHeldKey.md`:
  aliases "fetched without redirect to a base URL"; only Cursor is a genuine S049 re-open). A3 never
  evaluates them, so v3 accepts the recorded W2 and `7 of 7` cannot be printed. If the fixture adds a
  `re-opens S043/S048` prefix, the world is no longer the recorded W2 (v2's `reopen_why` rejects a
  base row whose URL is not the alias URL; and for the non-base alias key v2 never calls
  `reopen_why` at all). Either extend A3 to "a row whose URL is another
  rendering of a base row's article must be byte-identical to the base row URL" with a
  content-derivable notion of "rendering", or narrow/re-record W2. This is the highest-risk seam.
- **S2 — W1 needs a backdated blob-add commit.** The r53 bytes were fetched 2026-10-22; a
  single-commit fixture committed today has its earliest blob-add commit today, which is not older
  than the row's 2026-10-23 opened date, so A4 accepts and W1 never rejects. The fixture must carry
  commit A (2026-10-22, blobs) and commit B (2026-10-23, rows) with fixed receipt dates; the
  self-test must score B through the git path. Also disclose that S104/S105 are byte-identical to
  the r60 fetch, so only S103's content differs; the date arm is what rejects them, and it must be
  measured per row.
- **S3 — W3 has two causes.** A1 (`rules` ∉ `{globs}`) and the retained held-base rule both reject;
  deleting either leaves the other. W3 is a world-level reject but not an arm-killer. For the
  held-base arm, use a single-cause fixture (a synthetic base row that contains a canonical key, or
  ablate the held-base rule with A1 present and assert the missing cause).
- **S4 — W4 is a live-fetch reject.** The structural `reopen_why` check is skipped for a non-base
  request URL; the kill is the redirect guard. The offline `--self-test` must replay the recorded
  `url_effective` through `run_curl` (v2 already patches it at `:2278–2290`); otherwise W4 either
  depends on the network or is rejected by an unrelated conjunct, and the cause is not exercised.
- **S5 — W7 selection is ambiguous.** `CtlRescoreV2.md` lists two 1/4 worlds (`CtlNoReader` probe
  `43513ee…`, `CtlFabSnapshot` pristine `a2893fa…`). "The best v1-hollow rescore world (found F=1)"
  must pin one revision and its tree; a regenerated look-alike is not the receipt. Exit 1 alone is
  not discriminating (every v1 world exits 1); assert the content cause and keep W0 as the
  do-nothing control.
- **S6 — the four eligible rows must be the real r60 rows.** `4 of 4` must be Claude S103 `paths`,
  VS Code S105 `applyTo`, Copilot S106 `applyTo`, Cursor S108 `globs` from `SKILL.md:141,143,144,146`
  and `corpus/knowledge/scoped-rules-round60.md:15–18`, with their committed snapshots. Substituting
  v2's synthetic S900–S903 world (`check_scoped_rules.py:1670–1715`, keys `paths`, `globs`,
  `applyTo`, `applyTo`; its clients are Claude/Gemini/VS Code/Copilot, not the r60
  Claude/VS Code/Copilot/Cursor) prints `4 of 4` without exercising the real rows or A1's canonical
  set — the counter's own helper is the generator. Verify byte-identity of the four rows and the four
  page sha256 values.
- **S7 — the predicate sentence must be computed.** T9: mutate one world's defect and require the
  sentence to change. A hard-coded print plus `return 0` is the cheapest hollow self-test and is not
  caught by any of the world fixtures.

## 6. Summary

| fixture | causal reject under v3 | anti-generator-keying rule (one line) | concrete generator-keyed cheat |
|---|---|---|---|
| W1 `CtlReopenForged d` | A4 date: blob-add 2026-10-22 < opened 2026-10-23 | verdict from the fixture repo's git log + row `opened`; receipt dates only; rename/rebuild invariant | `W1-name-gate`: reject on `forged`/`971d75bf` with no history |
| W2 `CtlReopenHeldKey b` | A3 byte-identity (only if S1 resolved) | byte-compare row URL to named base row URL; no normalization, no alias tokens; held-out alias rejects | `W2-alias-deny-list`: `/de/`/`enterprise-cloud` literals |
| W3 `CtlReopenHeldKey a` | A1 **and** held-base (double; S3) | cause computed from key cell + base row line; no `(S049,rules)` pair; cause-level assertion | `W3-source-grep-held-key`: test greps its own source / hard-coded pair |
| W4 `CtlReopenHeldKey c` | fetch guard: base final URL, row has no own key | replay recorded final URL; compare to named base row key; no path literals; same-key redirect passes | `W4-request-path-literal`: reject on `docs/context/rules` |
| W5 wrong key | A1: key ∉ client's canonical set | per-client membership from S112–S115; held-out key rejects; no six-name deny-list | `W5-probe-deny-list`: the six ExecKeyForms names |
| W6 invented action | A2: cell contradicted by cited line | semantic support from the line; best-scoring line; paraphrase rejects; no phrase list | `W6-phrase-key`: substring `frontmatter so it loads only` |
| W7 v1 hollow | content cause from the pinned r60 revision | new hash/IDs still reject; fresh hollow rejects; W0 exit 1; no known-hash/ID-range gate | `W7-known-rev-gate`: `rev in KNOWN_HOLLOW` / `S9*` |
| A1 killer | A1 only | single defect; form-valid held-out key; canonical positive passes; no source grep | `A1-source-grep-tautology`: `Path(__file__).read_text()` |
| A2 killer | A2 only | single defect; best-line cell passes v2's lexical gate; paraphrase pair; no `action_conjunct` oracle | `A2-oracle-reuse`: expected value from v2 helper |
| A3 killer | A3 only | byte-identity both directions; same-key-different-bytes pair; no `url_key` | `A3-normalization-equivalence`: key equality instead of bytes |
| A4 killer | A4 only | blob-add vs opened from fixture history; paired pass; no constants/clock/hash gate | `A4-constant-date-tautology`: always-reject or constant dates |

## 7. What I could not verify (honesty)

- v3 does not exist at `f3246d14`, and no W1–W7 fixture files are committed yet; I could not run
  `--self-test`, mutate an arm, or measure a restore. The per-item verdicts above are design
  judgments against the frozen sentences, not observed v3 output.
- The A3/W2 casting is an inference from A3's wording and the r60 receipt; the plan does not state
  how a fresh alias row is rejected. Flagged as S1, not asserted as a fact about the intended v3.
- W7's "best F=1 hollow" is ambiguous between two receipt revisions; I named both rather than pick
  one for the L1. The receipt's S/F/exit values are quoted as recorded.
- I did not fetch any live page. The alias page hashes (`c568aae2…`, `70aef679…`) are read from
  `CtlReopenHeldKey.md`'s byte table, not re-derived by me.
- The held-out-key sweep used v2's `key_site` as a form oracle; it is a read-only read of the lane
  counter and the committed pages, not a fixture admission test. It shows no seventh form-valid key
  on the four eligible pages, which is why the A1 held-out arm must be synthetic or the risk declared.

installs: no installs (no tool/version/channel changed; pacman untouched).
blockers: none (S1–S7 are design findings for the L1, not execution blockers).
Attacked the generator-keying surface of the W1–W7 world fixtures and A1–A4 arm-killers; produced eleven anti-keying rules, eleven concrete cheats, nine admission tests, and seven frozen-design seams; wrote no lane byte except this report.
