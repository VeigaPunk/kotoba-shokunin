# FalsifyE2cClass — scoped depth review

Reviewed assignment revision: `e6da78bbe420722dd18a13182a7c4b64ce02f005`. Axes attacked: depth; consistency/calibration and provenance as regression constraints. This is a critic's evidence report, not a round judgment or admission.

## Answer: both instances belong to E2c, but the successor does not implement the complete binding conditions

- **`e2c-wrong-supersedes-target` is genuinely condition (5).** The matrix supplies a full-SHA collision owned by S043 and an anchored declaration naming S096 (`verifiers/check_erratum_absorption.py:138-144,192-193`). Condition (5) requires the named base row itself to record the matching full SHA (`plans/round-61.md:226-230`); the round's addendum explicitly retains this obligation (`plans/round-62.md:278-293`). Arbitrary digest/id values make this an arm-level synthetic *instance*, not an out-of-class attack. Probe A also reproduces the concrete original seam against the actual committed BASE table: S043 owns the full digest, S048 has no full digest, and `supersedes S048 — byte-identical` is admitted by the frozen arm and rejected by the successor. It is not legitimate to dismiss this attack because an earlier frozen self-test deliberately admitted a wrong S096 name (`verifiers/check_scoped_rules.py:1987-1989`): that self-test contradicts the frozen condition, rather than superseding it.
- **`e2c-supersedes-with-fresh-fetch` is genuinely condition (6), but only its teaches-cell subtype.** Its synthetic collision map assigns the full digest to the same S048 named by the declaration, then adds `fetched 2026-10-23T12:00:00Z` in teaches (`verifiers/check_erratum_absorption.py:194-195`). It is intentionally not the actual prefix-only S048 record. The row-wide prohibition includes teaches, so this is in class. However, it does **not** reproduce the harder anchor/scope seam described by `plans/round-61.md:230-233`, `plans/round-62.md:284-285`, and `.ufo/waves/round-62/w1/ExecInstancesA4.md:99-115`. The matrix scorer cannot represent that seam: its entire interface passes only SHA, a collision map, and teaches (`verifiers/check_erratum_absorption.py:138-144`).

The frozen arm's implementation really has both absences: once a full-SHA collision exists, any anchored `SUPERSEDES_RE` match immediately returns `[]`, without target equality or fetch examination (`verifiers/check_scoped_rules.py:1186-1197`). The reproduced matrix counts and frozen survivor lines are factual (R1), and the successor really rejects these exact catalogue inputs (R2, Probe A). Neither fact establishes semantic closure for the full E2c class.

## Counterexample A — condition (6) still accepts the original anchor/scope seam

**Failure:** the v3.1 guard searches `FETCHED_ISO_RE` only in `teaches` (`verifiers/check_scoped_rules_v31.py:1249-1251`); the production row scorer still passes only teaches (`:1411,1439`). The full parsed source row is already available, but its other cells never reach this check.

Probe A uses the successor's own VS Code positive-fixture prose and page shape (`verifiers/check_scoped_rules_v31.py:2202-2203,2216-2220`). It invokes the unchanged production `judge` text/row-scoring path with a correctly matching full-SHA base target and a valid source row, then changes only the location of the identical fetch assertion. The synthetic page bytes and introduction stamps are explicitly supplied callbacks; this is a full-row semantic probe, not a claim about a newly committed fixture or authenticated fetch history. Exact command, complete inputs and output are below.

Observed in Probe A:

```text
no-fetch-control: frozen backed=True why=[]; successor backed=True why=[]
fetch-in-teaches: frozen backed=True why=[]; successor backed=False why=['entry row S901: A4: supersedes S043 declares byte identity but the teaches cell also asserts a fetched ISO timestamp']
fetch-in-anchor: frozen backed=True why=[]; successor backed=True why=[]
fetch-in-scope: frozen backed=True why=[]; successor backed=True why=[]
```

The same command also shows acceptance when the assertion moves to source, recheck, or used-by. This is the exact cell-scope failure frozen out in the original r61 condition, not a newly invented requirement: `.ufo/waves/round-61/wave/MutA4.md:364-376` explicitly contrasts teaches-only with whole-row scanning and records the anchor/scope seam.

The synthetic row uses a distinct, non-rendering-alias URL so that A3 cannot mask A4's result. The original S103 same-URL row could be rejected by A3 after replacing its `re-opens` prefix; that does not satisfy the promised independent A4 row-wide fetch guard. `MutA4.md:314-317` already explains this masking issue.

**Related inherited limit:** the no-fetch declared-byte-identity row is itself scored `backed=True` in Probe A. The freshness exclusion in condition (3), `plans/round-61.md:220-223`, says a declared byte-identity row is not a fresh eligible row. The row scorer checks whether its id was at base (`verifiers/check_scoped_rules_v31.py:1395-1396`), not whether its teaches declaration bars freshness. The no-fetch case is an A4-exemption positive, not proof that such a row is fresh. Any correction should keep the A4 exemption and fresh-eligibility decisions distinct, and assert fetch-arm attribution so an eligibility rejection cannot conceal the missing scan.

## Counterexample B — condition (5) changes target identity to the first SHA owner

**Failure:** the successor does not ask whether the *named* base row records the matching full SHA. `judge` collapses all equal digests to their first row with `base_shas.setdefault(bsha, bsid)` (`verifiers/check_scoped_rules_v31.py:1482-1486`), and `alias_sha_why` requires the declaration's target to equal that single retained id (`:1240-1248`). This over-rejects a different, equally valid base-table owner.

This is not merely a hypothetical duplicate. Probe B reads the actual committed `BASE = 31092dc6f875370bddd6eb1e4da4ca0d210c56af` table. Its S080/S086 records have the same full digest; so do S089/S102. With that actual collision map, the successor admits the first owner and rejects a declaration naming the other owner, despite its recorded full SHA equalling the counted SHA. The exact command and output are below. Current table locators corroborating those records are `corpus/SOURCES.md:93,99,102,114`; Probe B's authority is the committed BASE table, not the working-tree table.

This introduces an arbitrary row-order authority absent from condition (5). A declaration naming S086 should not have to lie and name S080 to satisfy the alias exemption. This is an arm-level honest-declaration false rejection, not a claim that a new live eligible row using S086 was tested end-to-end.

## Claim/ledger/registry wording at the assigned revision

- **`corpus/knowledge/erratum-absorption-round62.md:35`:** “adds ... the E2c/E2e guards” overstates the E2c implementation if read as the frozen binding conditions. The landed additions are a first-owner-id equality check and a teaches-only fetch scan. Name those narrower semantics and the surviving row-scan/duplicate-owner defects. Its following measured `survivors closed 5 of 6` is correct for the frozen catalogue (R2), not a count to silently rewrite.
- **`SCORECARD.md:36`:** “No axis harmed: the frozen counter is byte-identical ...” is an unsupported general no-harm conclusion. The successor's wrong rejection of valid duplicate-owner declarations (Probe B) is a concrete calibration regression that unchanged frozen bytes and the existing eligible-row sample do not rule out. This report supplies the counterexample; the canonical non-author judge owns the resulting axis decision.
- **`LOG.md:2550`:** no false E2c numeric result found. It explicitly reports the frozen survivor transitions and separates the successor from the counted predicate. Its only named surviving successor bound is G9, so it should gain an appended correction naming these E2c limitations rather than implying that the sole remaining semantic bound is compound-purpose. The observed headline need not be retracted.
- **`SCORECARD.md:36,369`:** the matrix and successor measurement statements are bounded, reproduced results; I found no basis to call their literal counts false. `SCORECARD.md:371` already keeps E2c conditions as future live-row work, which is not evidence that the complete guards landed.
- **`SKILL.md:488,490`:** the instruments are honestly registered as gates, not capabilities; the successor row expressly says it closes measured *instances*. That narrower statement survives this attack. **`SKILL.md:486`** still calls the frozen v3 arms “provenance-authenticating”; E2c's date clause is consistency-only (`plans/round-61.md:169-173`), and both missing declaration checks remain independently demonstrated here. Prefer the frozen arm's actual consistency/alias-check description, not acquisition authentication.

The entry's own `:31` caveat (“results for the frozen matrix, not universal guarantees”) is sound and should remain. The defect is expanding exact-instance results into complete guard/no-harm claims, not the existence of an explicitly arm-level synthetic matrix.

## Smallest safe correction

In the successor only, give the E2c decision the full parsed row and base rows indexed by id. Validate the anchored target with `base_rows[target]` and its recorded full `row_sha`, rather than equality to a lossy SHA-to-first-id representative. Scan the whole declared row for the existing fetched-ISO shape before granting an exemption. Preserve the separately required no-fresh-eligibility rule for declared byte identity. Migrate successor callers and its survivor tests to carry that necessary context; do not rewrite the frozen v3 file or its historical receipts.

Add arm-attributed anchor/scope fetch cases and honest alternate-owner controls drawn from Probe B, alongside the original wrong-target and teaches-fetch cases. Rejecting every `supersedes` declaration is not a safe correction: it would remove the explicitly allowed honest exemption. These are fixable implementation/test-context defects, not a justified scope/axis tradeoff; any decision to retain a tradeoff belongs to the canonical judge.

Until corrected and separately measured, retain the factual matrix and exact-instance successor results, append the E2c bounds in LOG, qualify the entry's guard wording, and remove the unqualified no-harm assertion. No product edit or integration was performed by this seat.

## S118 reopen

Reopened with `read({"path":"https://code.claude.com/docs/en/memory.md"})`. The live document still states under Rule frontmatter reference that `paths` accepts a YAML list or comma-separated string of glob patterns, and Path-specific rules shows the key binding a glob list. The committed snapshot was reopened at `.ufo/waves/round-62/snapshots/S118.page:194-200,244-250`; `corpus/SOURCES.md:129` is the S118 row. The snapshot SHA is pinned below. No live-response digest, byte identity, or runtime behavior is claimed. S118 supports the E2e source-form evidence, not E2c provenance.

## Re-run evidence

All script paths and repository operands below are absolute. Working script bytes were checked against the assigned committed objects before execution. Self-tests' git writes occur in their temporary repositories; no lane git/jj/index/product file was written. Every command had a per-command timeout and ran synchronously; no subagents, background jobs, additional models, or tool installs/updates were used. Only this report is written in the lane.

### Committed-byte pin commands

For every `relative` path in the output below, the executed operations were:

```python
p = subprocess.run(['git', '-C', '/home/vgpnk/Projects/shokunin/kotoba-shokunin',
                    'show', 'e6da78bbe420722dd18a13182a7c4b64ce02f005:' + relative],
                   capture_output=True, timeout=120)
digest = hashlib.sha256(p.stdout).hexdigest()
p2 = subprocess.run(['sha256sum', '/home/vgpnk/Projects/shokunin/kotoba-shokunin/' + relative],
                    capture_output=True, text=True, timeout=120)
```

```text
verifiers/check_scoped_rules.py: committed=5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91; working=5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91; match=True; git-show-exit=0; sha256sum-exit=0
verifiers/check_erratum_absorption.py: committed=afb4ff74c266803f4d6007407775a5c44387c84bf49b9ac1a9059d375178d56b; working=afb4ff74c266803f4d6007407775a5c44387c84bf49b9ac1a9059d375178d56b; match=True; git-show-exit=0; sha256sum-exit=0
verifiers/check_scoped_rules_v31.py: committed=a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858; working=a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858; match=True; git-show-exit=0; sha256sum-exit=0
verifiers/check_routed_repairs_v2.py: committed=de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7; working=de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7; match=True; git-show-exit=0; sha256sum-exit=0
verifiers/check_routed_repairs.py: committed=95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88; working=95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88; match=True; git-show-exit=0; sha256sum-exit=0
plans/round-61.md: committed=a9603b282b56ee49d48e02c0884524f9cd5db2e320c124094b7781a411455866; working=a9603b282b56ee49d48e02c0884524f9cd5db2e320c124094b7781a411455866; match=True; git-show-exit=0; sha256sum-exit=0
plans/round-62.md: committed=1fe6a02e905ebb13d2bac1ea33aa8e3529a33ba207a0eaff49ada3408fca996d; working=1fe6a02e905ebb13d2bac1ea33aa8e3529a33ba207a0eaff49ada3408fca996d; match=True; git-show-exit=0; sha256sum-exit=0
corpus/knowledge/erratum-absorption-round62.md: committed=9df6e1bb92d77ce82e7f2122fb7d8d43080498daa1592c09b8b0f51bdf8f6435; working=9df6e1bb92d77ce82e7f2122fb7d8d43080498daa1592c09b8b0f51bdf8f6435; match=True; git-show-exit=0; sha256sum-exit=0
LOG.md: committed=052167f0920e401cc522d8dbe579c311514f9a407f9c563b17d30b9ea08933a3; working=052167f0920e401cc522d8dbe579c311514f9a407f9c563b17d30b9ea08933a3; match=True; git-show-exit=0; sha256sum-exit=0
SCORECARD.md: committed=562be25d8d2f90c0e9e2c40cb20a3c40df4fd0ae2fd9e0d1e852fdb1d243f824; working=562be25d8d2f90c0e9e2c40cb20a3c40df4fd0ae2fd9e0d1e852fdb1d243f824; match=True; git-show-exit=0; sha256sum-exit=0
SKILL.md: committed=b3f976cd9a532ae8c1a2f52ed8c264857d241fdaf4545c4f54025c61df19adb6; working=b3f976cd9a532ae8c1a2f52ed8c264857d241fdaf4545c4f54025c61df19adb6; match=True; git-show-exit=0; sha256sum-exit=0
corpus/SOURCES.md: committed=842f901c41f05ad36e6178524ee865bbadc98b39ea047e738b692e0a7874b7c3; working=842f901c41f05ad36e6178524ee865bbadc98b39ea047e738b692e0a7874b7c3; match=True; git-show-exit=0; sha256sum-exit=0
.ufo/waves/round-62/snapshots/S118.page: committed=02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801; working=02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801; match=True; git-show-exit=0; sha256sum-exit=0
```

### R1 — matrix, exact output and exit

```text
$ python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_erratum_absorption.py --self-test
counter sha256 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91
instances per direction: committed attacks 10; guard-disabled 10 per sweep (50 total); controls 4 committed + 4 disabled; content variant 2
guard flips: E2 2; E2b 2; E2c 0; E2e 0; E2f 0
errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2
survivor E2c e2c-wrong-supersedes-target: []
survivor E2c e2c-supersedes-with-fresh-fetch: []
survivor E2e e2e-negated-path-key: []
survivor E2e e2e-commented-equals-key: []
survivor E2f e2f-backticked-event-claim: []
survivor E2f e2f-compound-purpose-outside-citation: []
exit=0
```

### R2 — successor self-test, exact output and exit

```text
$ python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules_v31.py --self-test
counter sha256 a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858
world W1: Claude Code reject=True arm=A4 line='entry row S900: A4: snapshot sha256 06277eb1ae94... is already recorded by base row S010 and the teaches cell declares no supersedes'
world W2: Claude Code reject=True arm=A3 line="entry row S900: A3: URL 'https://code.claude.com/docs/de/memory.md' is a rendering alias of the committed row S112 URL 'https://code.claude.com/docs/e"
world W3: Cursor reject=True arm=A1 line="entry row S903: A1: scope key 'rules' is not a canonical key for Cursor (canonical: globs); S903 URL 'https://cursor.com/docs/rules' is already a base"
world W4: Cursor reject=True arm=live line='live page: not found'
world W5: Claude Code reject=True arm=A1 line="entry row S900: A1: scope key 'patterns' is not a canonical key for Claude Code (canonical: paths)"
world W6: Claude Code reject=True arm=A2 line='entry row S900: snapshot .ufo/waves/round-60/snapshots/S900.page: A2: action cell supports 5 of its 8 content word(s) at line 6 (need >= 6)'
world W7: all reject=True arm=A1
world W0: exit=1
worlds reject 7 of 7; eligible rows pass 4 of 4
survivor e2c-wrong-supersedes-target: before accepted; after rejected
survivor e2c-supersedes-with-fresh-fetch: before accepted; after rejected
survivor e2e-negated-path-key: before accepted; after rejected
survivor e2e-commented-equals-key: before accepted; after rejected
survivor e2f-backticked-event-claim: before accepted; after rejected
survivor e2f-compound-purpose-outside-citation: before accepted; after accepted
survivors closed 5 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
bound: G9 remains unimplemented; e2f-compound-purpose-outside-citation survives per CriticC1Hollow.
self-test: 0 failure(s) over 201 assertions
exit=0
```

### R3 — frozen world/eligible self-test, exact output and exit

```text
$ python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py --self-test
counter sha256 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91
world W1: Claude Code reject=True arm=A4 line='entry row S900: A4: snapshot sha256 06277eb1ae94... is already recorded by base row S010 and the teaches cell declares no supersedes'
world W2: Claude Code reject=True arm=A3 line="entry row S900: A3: URL 'https://code.claude.com/docs/de/memory.md' is a rendering alias of the committed row S112 URL 'https://code.claude.com/docs/e"
world W3: Cursor reject=True arm=A1 line="entry row S903: A1: scope key 'rules' is not a canonical key for Cursor (canonical: globs); S903 URL 'https://cursor.com/docs/rules' is already a base"
world W4: Cursor reject=True arm=live line='live page: not found'
world W5: Claude Code reject=True arm=A1 line="entry row S900: A1: scope key 'patterns' is not a canonical key for Claude Code (canonical: paths)"
world W6: Claude Code reject=True arm=A2 line='entry row S900: snapshot .ufo/waves/round-60/snapshots/S900.page: A2: action cell supports 5 of its 8 content word(s) at line 6 (need >= 6)'
world W7: all reject=True arm=A1
world W0: exit=1
worlds reject 7 of 7; eligible rows pass 4 of 4
self-test: 0 failure(s) over 189 assertions
exit=0
```

### Probe A — catalogue class, real-base original seam, and whole-row fetch relocation

The following is the exact shell-quoted `python3 -B -c` invocation and its output. The unused synthetic duplicate-owner tail is also retained; Probe B below strengthens that observation using actual BASE rows.

```text
$ python3 -B -c 'import sys, importlib.util, hashlib, subprocess
from pathlib import Path
sys.dont_write_bytecode = True
lane = Path('"'"'/home/vgpnk/Projects/shokunin/kotoba-shokunin'"'"')
def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, lane / relative)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module
frozen = load('"'"'e2c_frozen_probe'"'"', '"'"'verifiers/check_scoped_rules.py'"'"')
successor = load('"'"'e2c_successor_probe'"'"', '"'"'verifiers/check_scoped_rules_v31.py'"'"')
matrix = load('"'"'e2c_matrix_probe'"'"', '"'"'verifiers/check_erratum_absorption.py'"'"')
for group in matrix.ERRATA:
    if group.name == '"'"'E2c'"'"':
        for attack in group.attacks:
            print(attack.ident + '"'"': frozen='"'"' + repr(attack.score(frozen)) + '"'"'; successor='"'"' + repr(attack.score(successor)))
p = subprocess.run(['"'"'git'"'"', '"'"'-C'"'"', str(lane), '"'"'show'"'"', frozen.BASE + '"'"':corpus/SOURCES.md'"'"'], capture_output=True, text=True, timeout=120)
print('"'"'base SOURCES git-show exit='"'"' + str(p.returncode))
p.check_returncode()
base_rows = frozen.sources_table(p.stdout)
base_shas = {}
owners = {}
for sid, row in base_rows.items():
    sha = frozen.row_sha(row)
    if sha:
        base_shas.setdefault(sha, sid)
        owners.setdefault(sha, []).append(sid)
for sid in ('"'"'S043'"'"', '"'"'S048'"'"', '"'"'S096'"'"'):
    print('"'"'actual-base '"'"' + sid + '"'"' full-sha='"'"' + repr(frozen.row_sha(base_rows.get(sid, []))))
print('"'"'actual-base duplicate full-sha owners='"'"' + repr([ids for ids in owners.values() if len(ids) > 1]))
sha = frozen.row_sha(base_rows['"'"'S043'"'"'])
for label, teaches in (
    ('"'"'real-base-prefix-only-wrong-target'"'"', '"'"'supersedes S048 — byte-identical'"'"'),
    ('"'"'real-base-matching-target'"'"', '"'"'supersedes S043 — byte-identical'"'"'),
    ('"'"'real-base-matching-target-fetch-teaches'"'"', '"'"'supersedes S043 — fetched 2026-10-23T12:00:00Z'"'"'),
):
    print(label + '"'"': frozen='"'"' + repr(frozen.alias_sha_why(sha, base_shas, teaches)) + '"'"'; successor='"'"' + repr(successor.alias_sha_why(sha, base_shas, teaches)))
quote = ('"'"'VS Code targeted instruction files live in '"'"'
         '"'"'`.github/instructions/**/*.instructions.md` for a workspace'"'"')
action = '"'"'Use multiple instruction files per topic and apply them selectively.'"'"'
page = ('"'"'VS Code targeted instruction files\n'"'"' + quote + '"'"'.\n'"'"'
        "applyTo: '"'"'**/*.py'"'"'\n" + action + '"'"'\n'"'"').replace('"'"'\\n'"'"', '"'"'\n'"'"')
page = page.replace('"'"'\\n'"'"', '"'"'\n'"'"')
# Literal newline conversion above is intentionally explicit for the -c transcript.
page = page.replace(chr(92) + '"'"'n'"'"', chr(10))
page_bytes = page.encode()
sha = hashlib.sha256(page_bytes).hexdigest()
url = '"'"'https://code.visualstudio.com/docs/agent-customization/custom-instructions.md'"'"'
header = '"'"'| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |\n'"'"'.replace(chr(92) + '"'"'n'"'"', chr(10))
def row(cells):
    return '"'"'| '"'"' + '"'"' | '"'"'.join(cells) + '"'"' |'"'"' + chr(10)
base = header + row(['"'"'S043'"'"', '"'"'https://code.visualstudio.com/docs/previous-article'"'"', '"'"'docs'"'"', '"'"'A'"'"', '"'"'s'"'"', '"'"'sha256 '"'"' + sha, '"'"'t'"'"', '"'"'mined'"'"', '"'"'2026-10-22'"'"', '"'"'90d'"'"', '"'"'y'"'"'])
current = ['"'"'S901'"'"', '"'"'VS Code docs — '"'"' + url, '"'"'docs'"'"', '"'"'A'"'"', '"'"'VS Code'"'"', '"'"'§ (S901.page:2); sha256 '"'"' + sha, '"'"'supersedes S043 — byte-identical correction'"'"', '"'"'mined'"'"', '"'"'2026-10-23'"'"', '"'"'90d'"'"', '"'"'corpus/knowledge/scoped-rules-round60.md'"'"']
decl = ['"'"'S113'"'"', '"'"'VS Code docs — '"'"' + url, '"'"'docs'"'"', '"'"'A'"'"', '"'"'VS Code rule key'"'"', '"'"'§ (S113:1)'"'"', '"'"'scope-key[VS Code]=applyTo'"'"', '"'"'mined'"'"', '"'"'2026-10-23'"'"', '"'"'90d'"'"', '"'"'corpus/knowledge/scoped-rules-round60.md'"'"']
skill = ('"'"'# x'"'"' + chr(10) * 2 + successor.SKILL_HEADING + chr(10) * 2 + '"'"'| Client | Rule files | Scope key | Action |'"'"' + chr(10) + '"'"'|---|---|---|---|'"'"' + chr(10) + '"'"'| VS Code | `.github/instructions/**/*.instructions.md` (S901 :2) | `applyTo` (S901 :3) | '"'"' + action + '"'"' (S901 :4) |'"'"' + chr(10))
entry = '"'"'# e'"'"' + chr(10) * 2 + '"'"'| Client | Rule files | Source | Quote |'"'"' + chr(10) + '"'"'|---|---|---|---|'"'"' + chr(10) + '"'"'| VS Code | .github/instructions/**/*.instructions.md | S901 | "'"'"' + quote + '"'"'" |'"'"' + chr(10)
lesson = '"'"'## Gate'"'"' + chr(10) * 2 + '"'"'| S901 | '"'"' + url + '"'"' | "'"'"' + quote + '"'"'" |'"'"' + chr(10)
fetch = '"'"'fetched 2026-10-23T12:00:00Z'"'"'
print('"'"'synthetic page lines='"'"' + str(len(page.splitlines())) + '"'"'; parsed row cells='"'"' + str(len(current)))
for label, index in (('"'"'no-fetch-control'"'"', None), ('"'"'fetch-in-teaches'"'"', 6), ('"'"'fetch-in-anchor'"'"', 5), ('"'"'fetch-in-scope'"'"', 4), ('"'"'fetch-in-source'"'"', 1), ('"'"'fetch-in-recheck'"'"', 9), ('"'"'fetch-in-used-by'"'"', 10)):
    cells = current.copy()
    if index is not None:
        cells[index] += '"'"'; '"'"' + fetch
    sources = base + row(cells) + row(decl)
    results = []
    for name, counter in (('"'"'frozen'"'"', frozen), ('"'"'successor'"'"', successor)):
        report = counter.judge(skill, entry, sources, lesson, base,
                               snapshot_of=lambda sid: page_bytes,
                               intro_of=lambda sid: ('"'"'2026-10-23T12:00:00+00:00'"'"', '"'"'2026-10-23T12:00:00+00:00'"'"'))
        r = next(x for x in report if x['"'"'client'"'"'] == '"'"'VS Code'"'"')
        results.append(name + '"'"' backed='"'"' + repr(r['"'"'backed'"'"']) + '"'"' why='"'"' + repr(r['"'"'why'"'"']))
    print(label + '"'"': '"'"' + '"'"'; '"'"'.join(results))
# Condition 5 requires any named base row to carry the matching full sha,
# not the first row retained by a sha->single-id dictionary.
duplicate_base = base + row(['"'"'S096'"'"', '"'"'https://code.visualstudio.com/docs/another-previous-article'"'"', '"'"'docs'"'"', '"'"'A'"'"', '"'"'s'"'"', '"'"'sha256 '"'"' + sha, '"'"'t'"'"', '"'"'mined'"'"', '"'"'2026-10-22'"'"', '"'"'90d'"'"', '"'"'y'"'"'])
duplicate_rows = successor.sources_table(duplicate_base)
collapsed = {}
for sid, cells in duplicate_rows.items():
    digest = successor.row_sha(cells)
    if digest:
        collapsed.setdefault(digest, sid)
print('"'"'valid-second-owner target-recorded-full-sha-equals='"'"' + repr(successor.row_sha(duplicate_rows['"'"'S096'"'"']) == sha) + '"'"'; successor='"'"' + repr(successor.alias_sha_why(sha, collapsed, '"'"'supersedes S096 — byte-identical correction'"'"')))
'
e2c-wrong-supersedes-target: frozen=[]; successor=['A4: supersedes target S096 differs from base row S043 that owns the snapshot sha256']
e2c-supersedes-with-fresh-fetch: frozen=[]; successor=['A4: supersedes S048 declares byte identity but the teaches cell also asserts a fetched ISO timestamp']
base SOURCES git-show exit=0
actual-base S043 full-sha='971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff'
actual-base S048 full-sha=None
actual-base S096 full-sha='c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8'
actual-base duplicate full-sha owners=[['S080', 'S086'], ['S089', 'S102']]
real-base-prefix-only-wrong-target: frozen=[]; successor=['A4: supersedes target S048 differs from base row S043 that owns the snapshot sha256']
real-base-matching-target: frozen=[]; successor=[]
real-base-matching-target-fetch-teaches: frozen=[]; successor=['A4: supersedes S043 declares byte identity but the teaches cell also asserts a fetched ISO timestamp']
synthetic page lines=4; parsed row cells=11
no-fetch-control: frozen backed=True why=[]; successor backed=True why=[]
fetch-in-teaches: frozen backed=True why=[]; successor backed=False why=['entry row S901: A4: supersedes S043 declares byte identity but the teaches cell also asserts a fetched ISO timestamp']
fetch-in-anchor: frozen backed=True why=[]; successor backed=True why=[]
fetch-in-scope: frozen backed=True why=[]; successor backed=True why=[]
fetch-in-source: frozen backed=True why=[]; successor backed=True why=[]
fetch-in-recheck: frozen backed=True why=[]; successor backed=True why=[]
fetch-in-used-by: frozen backed=True why=[]; successor backed=True why=[]
valid-second-owner target-recorded-full-sha-equals=True; successor=['A4: supersedes target S096 differs from base row S043 that owns the snapshot sha256']
exit=0
```

### Probe B — actual BASE duplicate-owner counterexample

```text
$ python3 -B -c 'import sys, importlib.util, subprocess
from pathlib import Path
sys.dont_write_bytecode = True
lane = Path('"'"'/home/vgpnk/Projects/shokunin/kotoba-shokunin'"'"')
spec = importlib.util.spec_from_file_location('"'"'actual_base_e2c_v31'"'"', lane / '"'"'verifiers/check_scoped_rules_v31.py'"'"')
v = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = v
spec.loader.exec_module(v)
argv = ['"'"'git'"'"', '"'"'-C'"'"', str(lane), '"'"'show'"'"', v.BASE + '"'"':corpus/SOURCES.md'"'"']
p = subprocess.run(argv, capture_output=True, text=True, timeout=120)
print('"'"'base='"'"' + v.BASE + '"'"'; git-show exit='"'"' + str(p.returncode))
p.check_returncode()
rows = v.sources_table(p.stdout)
base_shas = {}
for sid, cells in rows.items():
    sha = v.row_sha(cells)
    if sha:
        base_shas.setdefault(sha, sid)
for first, second in (('"'"'S080'"'"', '"'"'S086'"'"'), ('"'"'S089'"'"', '"'"'S102'"'"')):
    sha = v.row_sha(rows[second])
    print(first + '"'"'/'"'"' + second + '"'"': same-recorded-full-sha='"'"' + repr(v.row_sha(rows[first]) == sha) + '"'"'; sha='"'"' + str(sha))
    print(first + '"'"' target: '"'"' + repr(v.alias_sha_why(sha, base_shas, '"'"'supersedes '"'"' + first + '"'"' — byte-identical correction'"'"')))
    print(second + '"'"' target: '"'"' + repr(v.alias_sha_why(sha, base_shas, '"'"'supersedes '"'"' + second + '"'"' — byte-identical correction'"'"')))
'
base=31092dc6f875370bddd6eb1e4da4ca0d210c56af; git-show exit=0
S080/S086: same-recorded-full-sha=True; sha=c37e330df8f040df8ee2f48035992b37c6a7decf6c3f5640822ca0907118c4e1
S080 target: []
S086 target: ['A4: supersedes target S086 differs from base row S080 that owns the snapshot sha256']
S089/S102: same-recorded-full-sha=True; sha=6b070e872dea28905a7ea7f45c4d5960f5bdf28cc73ac808799af6d50435ffbd
S089 target: []
S102 target: ['A4: supersedes target S102 differs from base row S089 that owns the snapshot sha256']
exit=0
```

### R4 — successor committed-row/live count

```text
$ python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules_v31.py --rev 43fe01804708d65e53965b4be31e9dc7dce793e4 --fetch
scoped rule files backed on committed snapshots 4 of 4; found on the live page 4 of 4
counter sha256 a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858; rev 43fe01804708d65e53965b4be31e9dc7dce793e4
canonical scope keys (S112/S113/S114/S115): Claude Code=paths; VS Code=applyTo; Copilot CLI=applyTo; Cursor=globs
reject Codex: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject Gemini CLI: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client
exit=0
```

### R5 — frozen committed-row/live count

```text
$ python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py --rev 43fe01804708d65e53965b4be31e9dc7dce793e4 --fetch
scoped rule files backed on committed snapshots 4 of 4; found on the live page 4 of 4
counter sha256 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91; rev 43fe01804708d65e53965b4be31e9dc7dce793e4
canonical scope keys (S112/S113/S114/S115): Claude Code=paths; VS Code=applyTo; Copilot CLI=applyTo; Cursor=globs
reject Codex: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject Gemini CLI: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client
exit=0
```

### R6 — C2 counting predicate (rerun only; no C2 semantic certification)

```text
$ python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs_v2.py --self-test
successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6
[stderr]
G-a paired population control: 29 names/committed 29=6; 30 names/committed 29=5; 30 names/committed 30=6; frozen=6/6/5
label-only constants fail controls: constant 6 vs base 0; constant 0 vs H1 6; constant 0 vs H2 6
frozen counter before: D1 6 of 6; D2 6 of 6; D3 6 of 6; D4 6 of 6; D5 6 of 6; D6 6 of 6; H1 4 of 6; H2 tip 6 of 6
self-test base CLI output:
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after body: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
self-test tip CLI output:
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after body: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
self-test CLI exits: base rev f3246d1493b60ea1c0d947a19c39f9e08e92f326 exit 1; tip rev 45a7ecfac9e203297f3146c45d63f5e79367470c exit 0; unreadable rev routed-repairs-v2-no-such-revision exit 2
exit=0
```

### R7 — C2 base count (expected rejection), exact output and exit

```text
$ python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs_v2.py --rev f3246d1493b60ea1c0d947a19c39f9e08e92f326
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after body: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
exit=1
```

### R8 — C2 data-revision count, exact output and exit

```text
$ python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs_v2.py --rev 3e7aed9b61bbfd83e0c800213b6dfc6da6191f85
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after body: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
exit=0
```

### R9 — frozen scoped-rule base count (expected rejection)

```text
$ python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py --rev f3246d1493b60ea1c0d947a19c39f9e08e92f326 --fetch
scoped rule files backed on committed snapshots 0 of 4; found on the live page 0 of 4
counter sha256 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91; rev f3246d1493b60ea1c0d947a19c39f9e08e92f326
canonical scope keys (S112/S113/S114/S115): none at this revision (A1 rejects every row)
reject Claude Code: entry row S103: A1: no canonical scope key is declared for Claude Code (rows S112/S113/S114/S115 absent or undecorated at the measured revision)
reject Codex: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject VS Code: entry row S105: A1: no canonical scope key is declared for VS Code (rows S112/S113/S114/S115 absent or undecorated at the measured revision)
reject Copilot CLI: entry row S106: A1: no canonical scope key is declared for Copilot CLI (rows S112/S113/S114/S115 absent or undecorated at the measured revision)
reject Gemini CLI: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject Cursor: entry row S108: A1: no canonical scope key is declared for Cursor (rows S112/S113/S114/S115 absent or undecorated at the measured revision)
reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client
exit=1
```

### R10 — successor scoped-rule base count (expected rejection)

```text
$ python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules_v31.py --rev f3246d1493b60ea1c0d947a19c39f9e08e92f326 --fetch
scoped rule files backed on committed snapshots 0 of 4; found on the live page 0 of 4
counter sha256 a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858; rev f3246d1493b60ea1c0d947a19c39f9e08e92f326
canonical scope keys (S112/S113/S114/S115): none at this revision (A1 rejects every row)
reject Claude Code: entry row S103: A1: no canonical scope key is declared for Claude Code (rows S112/S113/S114/S115 absent or undecorated at the measured revision)
reject Codex: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject VS Code: entry row S105: A1: no canonical scope key is declared for VS Code (rows S112/S113/S114/S115 absent or undecorated at the measured revision)
reject Copilot CLI: entry row S106: A1: no canonical scope key is declared for Copilot CLI (rows S112/S113/S114/S115 absent or undecorated at the measured revision)
reject Gemini CLI: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject Cursor: entry row S108: A1: no canonical scope key is declared for Cursor (rows S112/S113/S114/S115 absent or undecorated at the measured revision)
reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client
exit=1
```
