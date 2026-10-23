# MutA3 — attack seat: C1 counter-v3 arm A3 (URL canonical)

Date: 2026-10-23. Seat: `kotoba-r61-wave-MutA3`. Lane repo read-only; base
`f3246d1493b60ea1c0d947a19c39f9e08e92f326`; observed lane tip `7827628` (plan freeze).
Only this report and `/fast/scratch/hyaku/kotoba-r61/MutA3/` were written. No lane,
fleet, sibling, `.ufo/state`, jj/git-index, or scratch-of-a-peer file was modified; no
subagent dispatched; no ask tool used; no network access.

**Result: one plausible defect probed (A3's comparison point). Mutant SURVIVED the
counted-predicate surface and was KILLED by the frozen-sentence surface. While
establishing the baseline I found that the frozen A3 sentence and the frozen
predicate's eligible-row clause are jointly unsatisfiable on committed bytes
(S108). That is the report's primary finding; it must be resolved by the L1 with
a pre-data erratum, not by a seat.**

**Follow-up (post-probe): F1 was resolved before any C1 data by erratum E2,
lane commit `3dbf007`, which adopts option (a) — A3 is now `url_key` identity
and the 11 canonical-equivalence spellings are a disclosed limit. The probe
receipts below are unchanged; §6b records the resolution and what it does to
each verdict.**

## 1. Ground and what was attacked

At read time the lane still carried counter v2, sha256
`ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a`
(`verifiers/check_scoped_rules.py`, identical at `f3246d14` and at tip
`7827628`); no v3 source existed to run. I therefore attacked the **frozen A3
sentence itself** with a literal candidate implementation of it, isolated in
scratch, and used the committed v2 helpers (`urls_of`, `url_key`, `reopen_why`,
`host_ok`, `fetch`) as the evidentiary oracle.

Committed v2 baseline (timestamped):

```sh
$ date -u
Fri 23 Oct 2026 07:13:09 PM UTC
$ timeout 600 python3 -B verifiers/check_scoped_rules.py --self-test
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a
self-test: 0 failure(s) over 318 assertions
exit=0
$ sha256sum verifiers/check_scoped_rules.py
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  verifiers/check_scoped_rules.py
```

Pinned bytes used by the probe (read-only captures):

```sh
$ git --no-optional-locks show f3246d1493b60ea1c0d947a19c39f9e08e92f326:verifiers/check_scoped_rules.py > probe/v2_committed.py
$ git --no-optional-locks show f3246d1493b60ea1c0d947a19c39f9e08e92f326:corpus/SOURCES.md      > probe/base-SOURCES.md
$ sha256sum probe/v2_committed.py probe/base-SOURCES.md
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  probe/v2_committed.py
ddc5bfe0e86c178a266457d045107ee952fd3dd5f022be721da9c782dfc711de  probe/base-SOURCES.md
```

### A3's domain on committed bytes

`A3 URL canonical — a re-open row's URL must be byte-identical to its base row's URL.`
A row is in A3's domain iff its SOURCES `teaches` cell matches
`^re-opens\s+S\d{3,}` (v2 `REOPEN_RE`, line 314). Of the four eligible r60 rows,
three are re-opens and one is not:

| row | committed URL (bytes) | teaches prefix | A3 domain |
|---|---|---|---|
| S103 | `https://code.claude.com/docs/en/memory.md` | `re-opens S043 — Claude Code documents …` | yes |
| S105 | `https://code.visualstudio.com/docs/agent-customization/custom-instructions.md` | `VS Code documents targeted files at …` | **no** |
| S106 | `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md` | `re-opens S048 — Copilot CLI's reposito…` | yes |
| S108 | `https://cursor.com/docs/rules` | `re-opens S049 — Cursor documents proje…` | yes |

Base rows: S043 `https://code.claude.com/docs/en/memory.md`;
S048 `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md`;
S049 `https://cursor.com/docs/rules.md`; S052 `https://cursor.com/help/customization/rules.md`.

Byte comparison of each eligible re-open against its named base row:

```text
S103 -> S043 byte_identical= True
S106 -> S048 byte_identical= True
S108 -> S049 byte_identical= False | new='https://cursor.com/docs/rules' | base='https://cursor.com/docs/rules.md'
base_url_keys has //cursor.com/docs/rules: True
```

## 2. Candidate A3 (literal frozen sentence), isolated scratch

Target path in the eventual integration: `verifiers/check_scoped_rules.py`, new
function used by `entry_row_verdict`; the comparison point is the single `if`
below. This is a draft for the L1, not a lane edit.

```python
# /fast/scratch/hyaku/kotoba-r61/MutA3/probe/a3_spec.py
"""A3 (URL canonical) candidate, literal frozen-sentence reading."""
import v2_committed as v2

REOPEN_RE = v2.REOPEN_RE
urls_of = v2.urls_of


def a3_why(teaches_cell: str, url: str, base_rows: dict[str, list[str]]) -> list[str]:
    """Reasons A3 rejects the row; empty means the A3 conjunct is satisfied."""
    m = REOPEN_RE.match(teaches_cell or "")
    if not m:
        return []  # not a re-open row: A3 has nothing to say
    target = m.group(1)
    base = base_rows.get(target)
    if not base:
        return ["re-open names no base row %s" % target]
    base_urls = urls_of(base[1])
    if url not in base_urls:  # <<< the behavior-bearing point: byte identity
        return ["re-open URL %r is not byte-identical to base row %s URL (%r)"
                % (url, target, base_urls)]
    return []
```

`urls_of` is the committed extractor (line 550): it only trims trailing
markdown sentence punctuation when the URL is read out of a cell. It is not a
normaliser.

## 3. Expected verdicts, one line per variant

`pristine` = the literal candidate above; `mutant` = the same function with the
comparison replaced by the committed v2 normaliser (`url_key`); `v2 committed`
= what the committed counter does today with the same URL (evidence column;
"not invoked" means `url_key(url)` is not a base key, so v2 never runs
`reopen_why` — check at lines 1054-1059).

| # | case | URL (target) | expected per frozen A3 | pristine | mutant | v2 committed |
|---|---|---|---|---|---|---|
| 1 | exact base bytes | `https://cursor.com/docs/rules.md` (S049) | accept | accept | accept | accept |
| 2 | trailing slash | `…/rules.md/` | reject | reject | **accept** | accept |
| 3 | `.md` suffix dropped | `…/rules` | reject | reject | **accept** | accept |
| 4 | query params | `…/rules.md?utm_source=hyaku` | reject | reject | **accept** | accept |
| 5 | fragment only | `…/rules.md#project-rules` | reject | reject | **accept** | accept |
| 6 | scheme case | `HTTPS://cursor.com/docs/rules.md` | reject | reject | **accept** | accept |
| 7 | host case | `https://Cursor.com/docs/rules.md` | reject | reject | **accept** | accept |
| 8 | `www.` alias | `https://www.cursor.com/docs/rules.md` | reject | reject | **accept** | accept |
| 9 | default port | `https://cursor.com:443/docs/rules.md` | reject | reject | **accept** | accept |
| 10 | percent-encoded path | `https://cursor.com/docs/%72ules.md` | reject | reject | **accept** | accept |
| 11 | http downgrade | `http://cursor.com/docs/rules.md` | reject | reject | **accept** | accept |
| 12 | path case | `https://cursor.com/docs/RULES.md` | reject | reject | **accept** | accept |
| 13 | default-host alias | `https://docs.claude.com/en/docs/claude-code/memory` (S043) | reject | reject | reject | not invoked |
| 14 | W2 Claude locale alias | `https://code.claude.com/docs/de/memory.md` (S043) | reject | reject | reject | not invoked |
| 15 | W2 Copilot enterprise alias | `https://docs.github.com/en/enterprise-cloud@latest/copilot/…/add-custom-instructions.md` (S048) | reject | reject | reject | not invoked |
| 16 | W4 redirect request URL | `https://cursor.com/docs/context/rules` (S052) | reject | reject | reject | not invoked |
| 17 | eligible row S103 | `https://code.claude.com/docs/en/memory.md` (S043) | accept (4 of 4) | accept | accept | accept |
| 18 | eligible row S106 | `https://docs.github.com/en/…/add-custom-instructions.md` (S048) | accept (4 of 4) | accept | accept | accept |
| 19 | eligible row S108 | `https://cursor.com/docs/rules` (S049) | accept (4 of 4) | **reject** | accept | accept |

Rows 14 and 15 are the exact W0b alias URLs recorded in
`.ufo/waves/round-60/w0b/RecensusClaudeCode.md:9` and
`RecensusCopilotCLI.md:9`; row 16 is the W4 request URL recorded in
`.ufo/waves/round-60/controls-v2/CtlReopenHeldKey.md:10`; row 13's alias is
documented at `RecensusClaudeCode.md:114` (`docs.claude.com/...` redirects to
the base `code.claude.com` page). Row 3's URL is byte-identical to committed
row S108's URL — that identity is finding F1.

## 4. Mutation and receipts

Mutation: one line in `a3_impl.py` (copy of the candidate), replacing
byte equality with the committed v2 normalisation. This is the plausible defect
an executor would introduce for consistency with the existing counter.

```diff
--- a3_spec.py
+++ a3_impl.py
@@ -25,7 +25,7 @@
     if not base:
         return ["re-open names no base row %s" % target]
     base_urls = urls_of(base[1])
-    if url not in base_urls:  # <<< the behavior-bearing point: byte identity
+    if v2.url_key(url) not in {v2.url_key(u) for u in base_urls}:  # <<< MUTANT: normalised, not byte identity
         return ["re-open URL %r is not byte-identical to base row %s URL (%r)"
                 % (url, target, base_urls)]
     return []
```

Hashes on the mutation target (`a3_impl.py`), same path throughout:

```text
before   (pristine)   4f58aa33a94ccb466cfd9e0d0d53511b5f2d5939d7d75f83c53fda73dc91a167
mutant                aef22bde037d99fd02ba38ad452eb86c3035732116dc702251923bd2d0999727
restored              4f58aa33a94ccb466cfd9e0d0d53511b5f2d5939d7d75f83c53fda73dc91a167
restore check         `cmp a3_spec.py a3_impl.py` -> "cmp: identical"
```

Detector: `probe/run_probe.py` reads only `probe/base-SOURCES.md`, loads an
implementation by path, and exits 0 iff every selected case matches the
expected verdict. Two surfaces:

- `--mode worlds` (D1, the counted-predicate surface): W2/W4 reject, the
  eligible re-open rows accept.
- `--mode spec` (D2, frozen-sentence fidelity): the exact base URL accepts,
  every canonical-equivalent variant rejects.

### 4.1 Pristine baseline

```sh
$ date -u
Fri 23 Oct 2026 07:12:32 PM UTC
$ python3 -B run_probe.py --impl a3_impl.py --mode spec
impl a3_impl.py sha256 4f58aa33a94ccb466cfd9e0d0d53511b5f2d5939d7d75f83c53fda73dc91a167
case                         group      expected  actual    match  v2 committed
spec-exact                   spec       accept    accept    ok     accept
spec-trailing-slash          spec       reject    reject    ok     accept
spec-md-suffix-dropped       spec       reject    reject    ok     accept
spec-query-params            spec       reject    reject    ok     accept
spec-fragment-only           spec       reject    reject    ok     accept
spec-scheme-upper            spec       reject    reject    ok     accept
spec-host-case               spec       reject    reject    ok     accept
spec-www-alias               spec       reject    reject    ok     accept
spec-default-port            spec       reject    reject    ok     accept
spec-percent-encoded-path    spec       reject    reject    ok     accept
spec-scheme-http-downgrade   spec       reject    reject    ok     accept
spec-path-case               spec       reject    reject    ok     accept
spec-default-host-alias      spec       reject    reject    ok     not invoked (url_key not a base URL)
cases 13 selected, 0 mismatched
exit=0
```

```sh
$ python3 -B run_probe.py --impl a3_impl.py --mode worlds
case                         group      expected  actual    match  v2 committed
W2-claude-locale-alias       worlds     reject    reject    ok     not invoked (url_key not a base URL)
W2-copilot-enterprise-alias  worlds     reject    reject    ok     not invoked (url_key not a base URL)
W4-redirect-request-url      worlds     reject    reject    ok     not invoked (url_key not a base URL)
eligible-row-S103            eligible   accept    accept    ok     accept
eligible-row-S106            eligible   accept    accept    ok     accept
eligible-row-S108            eligible   accept    reject    FAIL   accept
    why: re-open URL 'https://cursor.com/docs/rules' is not byte-identical to base row S049 URL (['https://cursor.com/docs/rules.md'])
cases 6 selected, 1 mismatched
exit=1
```

The baseline D1 failure is **not** a killed mutant and not a detector bug: it
is the spec/data contradiction F1.

### 4.2 Mutant

```sh
$ date -u
Fri 23 Oct 2026 07:12:37 PM UTC
$ python3 -B run_probe.py --impl a3_impl.py --mode worlds
impl a3_impl.py sha256 aef22bde037d99fd02ba38ad452eb86c3035732116dc702251923bd2d0999727
case                         group      expected  actual    match  v2 committed
W2-claude-locale-alias       worlds     reject    reject    ok     not invoked (url_key not a base URL)
W2-copilot-enterprise-alias  worlds     reject    reject    ok     not invoked (url_key not a base URL)
W4-redirect-request-url      worlds     reject    reject    ok     not invoked (url_key not a base URL)
eligible-row-S103            eligible   accept    accept    ok     accept
eligible-row-S106            eligible   accept    accept    ok     accept
eligible-row-S108            eligible   accept    accept    ok     accept
cases 6 selected, 0 mismatched
exit=0
```

```sh
$ python3 -B run_probe.py --impl a3_impl.py --mode spec
impl a3_impl.py sha256 aef22bde037d99fd02ba38ad452eb86c3035732116dc702251923bd2d0999727
case                         group      expected  actual    match  v2 committed
spec-exact                   spec       accept    accept    ok     accept
spec-trailing-slash          spec       reject    accept    FAIL   accept
spec-md-suffix-dropped       spec       reject    accept    FAIL   accept
spec-query-params            spec       reject    accept    FAIL   accept
spec-fragment-only           spec       reject    accept    FAIL   accept
spec-scheme-upper            spec       reject    accept    FAIL   accept
spec-host-case               spec       reject    accept    FAIL   accept
spec-www-alias               spec       reject    accept    FAIL   accept
spec-default-port            spec       reject    accept    FAIL   accept
spec-percent-encoded-path    spec       reject    accept    FAIL   accept
spec-scheme-http-downgrade   spec       reject    accept    FAIL   accept
spec-path-case               spec       reject    accept    FAIL   accept
spec-default-host-alias      spec       reject    reject    ok     not invoked (url_key not a base URL)
cases 13 selected, 11 mismatched
exit=1
```

### 4.3 Restored bytes, same detector

```sh
$ date -u
Fri 23 Oct 2026 07:12:48 PM UTC
$ cp a3_spec.py a3_impl.py && cmp a3_spec.py a3_impl.py && sha256sum a3_impl.py
4f58aa33a94ccb466cfd9e0d0d53511b5f2d5939d7d75f83c53fda73dc91a167  a3_impl.py
cmp: identical
$ python3 -B run_probe.py --impl a3_impl.py --mode worlds   # exit 1, 6 cases, 1 mismatched (S108, as before)
$ python3 -B run_probe.py --impl a3_impl.py --mode spec     # exit 0, 13 cases, 0 mismatched
$ python3 -B run_probe.py --impl a3_impl.py --mode all      # exit 1, 19 cases, 1 mismatched (S108)
```

## 5. Redirect chain — what A3 and the fetch guard do

W4 in the plan is "live redirect to a different base key". A chain that ends at
the *canonical* (own) URL is a different object. The committed guard is
`fetch()` lines 1218-1220: it rejects only when the final URL's key is a base
key **and** differs from `own_key` (erratum E1 allows a re-open to redirect to
its own URL). Probed network-free by replacing `run_curl` with canned
(status, final URL, body):

```sh
$ date -u
Fri 23 Oct 2026 07:12:18 PM UTC
$ python3 -B redirect_guard.py
chain-ends-at-own-canonical            expected accept actual accept ok
chain-md-to-no-md-canonical            expected accept actual accept ok
chain-ends-at-different-base           expected reject actual reject ok reached a base SOURCES URL https://cursor.com/docs/rules
chain-ends-off-pin-host                expected reject actual reject ok fetched off the pinned hosts at https://example.com/docs/rules
exit=0
```

**Verdict: ACCEPT is correct per the plan** for a chain ending at the canonical
URL when the recorded URL is byte-identical to its base row's URL. A3's sentence
constrains the recorded URL bytes only; the guard deliberately permits
redirect-to-own-key; W4 is defined by a *different* base key, which the guard
rejects. Limit (declared, not tested by a world): curl reports only the final
URL, so intermediate hops are invisible to both the guard and A3.

## 6. Findings

### F1 (blocking; resolved by erratum E2, see §6b) — the frozen A3 sentence contradicts the frozen "4 of 4" clause

Committed r60 row S108 records `https://cursor.com/docs/rules`; its named base
row S049 records `https://cursor.com/docs/rules.md`. Literal byte identity
rejects S108 (eligible-row case 19). The predicate requires
`eligible rows pass 4 of 4` and the kill rule says "any eligible row fails at
tip → C1 fails". The mutation of the sentence to `url_key` equality fixes
S108 and still rejects W2 (its locale/enterprise URLs have different keys), but
then admits all eleven canonical-equivalence variants (cases 2-12), i.e. the
assigned bypass classes.

So the two frozen artifacts cannot both hold. The L1 must resolve this **before
any data**, with a named erratum, choosing explicitly:

- **(a) Weaken A3 to the committed normalisation** (compare `url_key`): the
  counted predicate holds, W2 still rejects, and the arm's sentence becomes
  "byte-identical after the frozen `url_key` normalisation" with the admitted
  variants declared as a limit. This is the only option that keeps the four
  committed eligible rows untouched.
- **(b) Keep byte identity and change data** (e.g. re-record S108's URL with
  `.md`, or drop Cursor from the eligible set): both touch r60 committed
  evidence; S108's `.md`-less route is the live HTML route that was actually
  fetched, and the four-row count is the frozen claim. Not available to a seat.
- **(c) Keep byte identity and exempt the `.md` route suffix only**: still
  rejects W2, admits the `.md` bypass variant (case 3), and still contradicts
  any future row recorded on the HTML route. It is (a) with a narrower sentence.
  Either way, if the arm's *assigned bypass list* (trailing slash, query,
  fragment, etc.) must reject, the eligible row set has to change — the frozen
  data does not permit it.

I do not decide this and I do not change the contract; the report records that
an unamended literal A3 makes the C1 predicate fail on committed bytes.

### F2 — the r60 W2/W3 Cursor rows would be rejected by A3 for the wrong reason

The r60 held-key world's Cursor row records `https://cursor.com/docs/rules`
with `re-opens S049` (receipt line 292: `S106 URL 'https://cursor.com/docs/rules'
is already a base SOURCES URL`; W2's Cursor row is the same genuine S049
re-open, line 59). Those are the bytes of eligible S108. Under a literal A3,
W3 rejects because of the `.md` mismatch *before* the held-key conjunct runs;
if the rebuilt W3 fixture is scored by exit code alone, the held-key arm is
never exercised (the 7-of-7 count survives, the provenance of the rejection is
wrong). When the L1 rebuilds W3, the receipt should require the rejecting `why`
string to be the held-key message (`base row S049 already records key …`), not
the A3 byte message. Same applies to W2's Cursor row.

### F3 — A3 does not bind snapshot bytes to the recorded URL

A3 compares the *recorded URL* with the base row's URL. A world that records
the canonical URL but commits alias bytes (with the quote present on the alias
page) passes A3 and A4's internal-consistency checks; A4's declared limit
(committed bytes, not wall-clock fetch provenance) covers it. Consequently
W2's rejection exists only if the fixture records the alias URL. The r60 alias
world did exactly that (W0b URLs, actual locale/enterprise bytes), so the
fixture must preserve those URLs verbatim; a fixture that "canonicalises" the
recorded URL while keeping alias bytes makes A3's W2 rejection vacuous. Live
`--fetch` would likely fail the quote on the canonical page, but that is not
the offline world instrument.

### F4 — observed v2 behavior (evidence, not a verdict)

Committed v2 accepts every canonical-equivalent variant (it compares
`url_key`, lines 560-577 and 990) and never invokes `reopen_why` for the W2
alias URLs or W4's request URL (gate at 1054-1059), which is why W2 survived v2
and W4 needed the live guard. This is consistent with the r60 receipts
(`controls-v2/SUMMARY.md`, `CtlReopenHeldKey.md:8,10`).

## 6b. Resolution — erratum E2 (lane commit `3dbf007`, before any C1 data)

The L1 resolved F1 by adopting option (a). Committed text
(`plans/round-61.md:123-143`; abridged, elisions marked `…`):

> **A3 (amended)** — a re-open row's URL must have the same `url_key` as its
> base row's URL, where `url_key` is the counter's existing canonicalization
> (host lowercased, scheme/default-port/www normalized, a single trailing `.md`
> dropped). The C1 predicate sentence is unchanged.
>
> Limit (disclosed before data): url_key identity admits 11
> canonical-equivalence URL spellings of the same document (trailing slash,
> `.md` drop, query, fragment, scheme/host case, www, default port, percent
> path, http downgrade, path case); alias renderings whose path differs
> (locale `/de/`, enterprise `@latest`, the W2/W4 worlds) keep distinct
> url_keys and stay rejected. …
>
> Fixture rule: every rebuilt world's receipt pins the rejecting arm and
> printed line (literal A3 would have rejected W3's Cursor rows before the
> held-key arm ran — receipts must name which arm fired).

Consequences for this probe:

- The **mutant in §4 is now the specified implementation**, not a defect. Its
  D1 run (6 cases, 0 mismatched) is the expected pass. Its D2 run (11 of 13
  mismatched) is the guard for the *literal-bytes* implementation; it stays in
  the report so a later re-tightening of the sentence is a visible contract
  change, not a silent edit.
- The **literal-bytes candidate is now the deviant implementation**: it fails
  D1 on S108 and would fail the amended arm at integration.
- §3 rows 2-12 are now accepted **by declared limit**, not rejected. Rows
  14-16 (locale/enterprise/redirect-request aliases) stay rejected because
  their path differs.
- F2 is adopted as the fixture rule; F3 remains a declared A4 limit. No
  contract change beyond E2.

## 7. Hand-off to the L1 (concrete self-test arms)

Under E2 the v3 `--self-test` must assert:

- W2 alias rejection by key difference: the two W0b URLs in §3 rows 14-15
  reject, and the reason names the A3/url_key mismatch (not an A1/A2 message);
- W4's recorded `https://cursor.com/docs/context/rules` against its named base
  S052 rejects;
- eligible rows S103/S106/S108 accept (S108's `.md`-less URL has the same
  `url_key` as S049);
- the disclosed limit is machine-locked with at least one canonical-equivalence
  spelling (e.g. a trailing-slash spelling of a base URL is accepted), so the
  limit cannot silently tighten or widen without failing a test;
- each rebuilt-world receipt prints the firing arm and line (F2: W3 must print
  the held-key reason `base row S049 already records key rules`, not an A3
  message).

The §3 literal-bytes negative arms are retained only as the D2 detector for
any future attempt to re-tighten A3; they must not be added to v3 while E2
stands.

## 7b. Original hand-off text (superseded by E2; kept as the pre-resolution record)

If F1 resolves toward (a)/(c), the v3 `--self-test` must contain the W2 alias
rejection arms (already satisfied by key equality) and, per (c), an explicit
statement that the canonical-equivalence variants are admitted. If F1 resolves
toward byte identity by changing the eligible-row reality, the self-test must
add these negative arms (the exact cases my detector asserts):

```python
base = "https://cursor.com/docs/rules.md"
check("A3: exact base bytes accepted", a3_ok("S049", base), True)
for name, url in [
    ("trailing slash", base + "/"),
    ("query", base + "?utm_source=x"),
    ("fragment", base + "#frag"),
    ("scheme case", "HTTPS://cursor.com/docs/rules.md"),
    ("host case", "https://Cursor.com/docs/rules.md"),
    ("www alias", "https://www.cursor.com/docs/rules.md"),
    ("default port", "https://cursor.com:443/docs/rules.md"),
    ("percent path", "https://cursor.com/docs/%72ules.md"),
    ("http downgrade", "http://cursor.com/docs/rules.md"),
    ("path case", "https://cursor.com/docs/RULES.md"),
]:
    check("A3: %s is not byte-identical" % name, a3_ok("S049", url), False)
```

These arms cannot coexist with eligible row S108 as committed; that is F1.

## 8. What I did not verify

- No integrated v3 source existed at read time; I did not run v3, any world
  fixture beyond the committed-row cases above, or `--fetch`. The seven-world
  count and the four eligible rows were not re-measured end-to-end; only the A3
  conjunct was probed.
- The redirect probe exercises the committed guard with canned responses, not
  real redirects; intermediate hops are not observable.
- A3's interaction with A1/A2/A4 is out of scope; my candidate is the A3
  conjunct in isolation.
- I made no claim about whether the L1's rebuilt fixtures preserve the r60
  URLs; F2/F3 are requirements on that rebuild.

installs: none
blockers: none
Attacked the frozen A3 (URL canonical) sentence with a one-line mutation of its comparison point (byte identity → committed `url_key` normalisation), ran a bounded committed-bytes detector on pristine/mutant/restored bytes in scratch, and produced 19 documented verdicts plus the S108 contradiction, the W2/W3 fixture hazards, and the redirect-chain ruling.
