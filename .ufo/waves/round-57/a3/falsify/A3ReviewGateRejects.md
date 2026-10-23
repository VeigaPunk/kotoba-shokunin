Result: HOLDS — all six § Gate Rejected reasons are supported by the receipts they cite (6 agree, 0 disagree, 2 wording nits); the untrusted a2-candidate's claim that Copilot CLI's legacy `.github/plugin/plugin.json` "meets the counter's token grammar" is TRUE (harness output below).

Seat: KotobaR57A3.A3ReviewGateRejects · 2026-10-23 · lane read-only at `07c33d73ddce769d9cea2846a6313164401b5478`.
Sandbox: `/fast/scratch/hyaku/kotoba-r57a3/A3ReviewGateRejects` — fresh clone of the lane, `git checkout 07c33d73ddce769d9cea2846a6313164401b5478` (verified `HEAD` = that hash); `verifiers/check_plugin_manifests.py` there hashes `bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e`, the declared frozen v2 digest. No sandbox commit was made; the only hash cited from the clone is that file digest. Lane writes: this report only. Tooling: nothing installed or upgraded (none needed); no pacman transaction touched.

Everything under `.ufo/waves/round-57/a3/a2-candidate.patch` was treated as claims, never evidence.

## 1. Row-by-row discernment — `corpus/lessons/round-57.md:31-36`

### Row 1 · C2 claim (lesson :31) — AGREE

All four named controls re-opened; each met the frozen predicate (`N = T, T >= 120`, i.e. `120 of 120`, exit 0) without doing the claimed work:

- `controls/CtlC2GeneratorKeyed.md:1,34-37` — fence-blind 28-line patch keyed on the case-directory name (`skill-<8 hex>`) and the fixed `REAL_COMMANDS`: `120 of 120` exit 0 on the default seeds and on three chosen seeds; run D, six seeds, `correct 240 of 240`, exit 0.
- `controls/CtlC2DoNothingJunk.md:55,68-70` — the harness/extraction-path-keyed variant: counter `120 of 120` exit 0 while the measured instrument's `--self-test` is `0 failure(s) over 1852 assertions` exit 0 and the live lane run is byte-identical to base. Matches the lesson's "with the instrument self-test green and the live run byte-identical" clause for word.
- `controls/CtlC2CharShortcuts.md:31` — UNION+EMPTY (character skips plus ~7-line empty-fence echo fallback), sandbox `93c9610`: `120/120`, exit 0; the fallback flips H2/H4 because the counter's hard-negative rule is bare substring containment.
- `controls/MutC2Counter.md:1` — "the unmutated frozen counter scored a 50-line stub that replaces the whole verifier at 120 of 120, exit 0" (world S, R23). The lesson's "50-line stub" figure is the receipt's own wording.

The rejection reason — four pre-freeze controls met the frozen predicate without the claimed work — is exactly what these receipts show. AGREE. (Wording nit in §3.)

### Row 2 · C1 counter v1 as the claim's rule (lesson :32) — AGREE

All four cited worlds re-opened; every score matches the lesson cell:

- `controls/CtlC1RealNoForm.md:1,19` — `plugin manifests found on the live page 5 of 7; new ground 4`, exit 0; the five found tokens are a bare `plugin.json` backed by a CHANGELOG bullet, a site-nav label (`Extensions`), an extension source file (`extension.ts`), a docs link filename (`writing-extensions.md`), and a bare `plugins` — "a changelog line" and "nav text" witnessed.
- `controls/CtlC1HeldVariant.md:30` — `5 of 5; new ground 3`, exit 0; case/suffix variants of held words (`Plugins`, `Extensions`, `plugin.json`) quoted from navigation/boilerplate, unheld only because the v1 held test is case-sensitive.
- `controls/CtlC1DoNothingJunk.md:31` — world C, `5 of 7; new ground 4`, exit 0, bare words + 3–5-word nav fragments.
- `controls/CtlC1Fabricated.md:27` — W5-bareword, `7 of 7; new ground 3`, exit 0, verbatim nav quotes with bare-word tokens.

Flip cell "v2 (erratum 1), re-scored by the same five seats: best hollow world `found 1 of 7`": exactly five files match `controls/CtlC1*.md` and each carries a `## v2 re-score` section — RealNoForm (`0 of 0`), Fabricated (W5 `0 of 0`), HeldVariant (`0 of 0`; its F=3-of-K=3 adaptation uses real tokens/quotes, so it is not a hollow world), DoNothingJunk (adapted hollow world D `found 1 of 7, G=1`, exit 1, `:190`), KeyedLabels (original world `0 of 6`, best hollow variant `found 1 of 6; new ground 1`, exit 1, `:185`). "Best hollow world `found 1 of 7`" is correct (DoNothingJunk world D). `MutC1Counter.md` contains zero occurrences of `v2`/`01312a77`/`bf11a4ef` (`grep -c -i` = 0), consistent with the five re-scorers being the five `CtlC1*` seats, not the counter-mutation seat. AGREE.

### Row 3 · VS Code row token `.plugin/plugin.json` (lesson :33) — AGREE

- The draft is real: `build/SrcVSCode.md` drafts `| VS Code | `.plugin/plugin.json` (Legacy OpenPlugin; …)` and shows the source lines 103–104 (`| Legacy OpenPlugin | `.plugin/plugin.json` |`), fetched 2026-10-23T04:47:13Z, HTTP 200, 21,972 B, sha256 `d6e10328…` (= S081's recorded bytes).
- "Would pass the counter": verified — my harness below prints `token_well_formed('.plugin/plugin.json', 'VS Code') -> True` (2 segments, final segment ends `.json` with the plugin word; the `vscode` marker is not required at ≥2 segments).
- "VS Code's default manifest is the root `plugin.json` (`agent-plugin-reference.md:97`)": `build/CriticC1Rows.md:50` quotes the page — "The Copilot format is used as the default when no other format marker is found." (`agent-plugin-reference.md:97`) — and concludes the Legacy OpenPlugin path is "the rarest format".
- The landed row took the consequence: `C1-measure.txt` rejects VS Code (`SKILL.md manifest token 'plugin.json' is not well-formed; … shared by rows Copilot CLI, VS Code`) — the L1 chose the true-but-uncounted token over the countable legacy one, which is precisely the trade the rejection reason describes ("say less than the truth"). Flip cell ("VS Code documents a VS Code-named manifest path") has no live trigger: S081's four documented formats (root `plugin.json`, `.claude-plugin/…`, `.plugin/…`, Copilot root) contain no `vscode`-marked path [INFERENCE from the cited page bytes].

### Row 4 · opencode `package.json` as the row token (lesson :34) — AGREE, one nuance

- `build/Srcopencode.md` shows the seat itself drafted `package.json` evidence-only and predicted the reject: the token "fails the frozen token rule because its final segment has no `plugin`/`extension` word and it does not contain the opencode marker". Confirmed mechanically: `token_well_formed("package.json", "opencode") -> False` (harness below; also the frozen self-test arm at `verifiers/check_plugin_manifests.py:1145` for VS Code). `C1-measure.txt` shows the landed folder token `.opencode/plugins/` also rejected (trailing slash → empty final segment).
- Nuance: the vendor build guide literally labels it a manifest — "A minimal manifest is:" followed by ```` ```json title="package.json" ```` (`build/Srcopencode.md:5,15,40`, bytes `index.mdx:1770-1773`, sha256 `e505931a…` = S085's recorded fetch). The lesson's "not a plugin manifest" is right in the plugin-specific sense (npm package metadata: name/version/exports/deps), and the landed row's flat "no JSON manifest" is the imprecise phrasing the a2 candidate corrects to "no plugin-specific JSON manifest … the only file its docs call a manifest". The rejection of the token stands regardless.

### Row 5 · GFM spec as a new row for C2 (lesson :35) — AGREE

- "C2 was withdrawn": erratum 1 (`01312a77`) withdrew C2 before data; the re-control request `controls/v2-recontrol-message.txt` is stamped 04:35Z, before `build/ScoutC2Source.md`'s fetches (04:46:46–04:47:01Z) and the 04:55Z reject time.
- "the CommonMark spec is already row S005": `corpus/SOURCES.md:18` (S005, `https://spec.commonmark.org/0.31.2/`, opened 2026-10-19); the scout found the same collision and routed the free GFM URL as the alternative.
- "neither spec states that an info-less fence declares no language": the scout's own conclusion — its phrase-set grep returns zero hits, and it writes that the step from "no info string" to "no language declared" "is not in either spec" and would be the seat's [INFERENCE]; the specs say only that the info string is optional and its first word is *typically* the language, while expressly declining to mandate renderer treatment. Admitting the row would have grounded C2's claim on inference. AGREE.

### Row 6 · Copilot CLI legacy manifest paths (lesson :36) — AGREE

- "they are listed on the CLI plugin reference, base row S028": `build/CriticC1Rows.md:37` quotes the S028 page (cli-plugin-reference.md, 47,200 B, sha256 `d0d362cc…` — byte-identical to S028's recorded fetch, `corpus/SOURCES.md:41`), line 402: "Legacy plugins: `.plugin/plugin.json`, `plugin.json`, `.github/plugin/plugin.json`, or `.claude-plugin/plugin.json` (checked in this order)." Both lesson-named paths are there.
- "re-citing a base URL for a counted row is barred": enforced mechanically — `controls/CtlC1HeldVariant.md` World A2 rows are rejected solely on `S### URL '…' is already a base SOURCES URL`, and `build/SrcCopilotCLI.md` states the reference path "is not a permitted new SOURCES URL for C1".
- "the creation guide S082 names only the root `plugin.json`": `build/SrcCopilotCLI.md:5` — the guide "does not enumerate those legacy paths. Its exact manifest token is `plugin.json`" (fetch 2026-10-23T04:47:14Z, HTTP 200, 7,711 B, sha256 `c0642867…` = S082's recorded bytes, `corpus/SOURCES.md:95`). AGREE.

## 2. Candidate-patch claim check — `.github/plugin/plugin.json` "meets the counter's token grammar": TRUE

Claim under test (`.ufo/waves/round-57/a3/a2-candidate.patch:68`): Copilot CLI's legacy "`.github/plugin/plugin.json`, … meets the counter's token grammar (base row S028)".

Harness (import of the frozen v2 counter in my sandbox clone, `07c33d73` checkout, counter sha256 `bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e`):

```sh
$ cd /fast/scratch/hyaku/kotoba-r57a3/A3ReviewGateRejects && python3 -B -c '
import importlib.util as u
s = u.spec_from_file_location("c2counter", "verifiers/check_plugin_manifests.py")
m = u.module_from_spec(s); s.loader.exec_module(m)
for cl in ("Copilot CLI", "VS Code"):
    for t in (".github/plugin/plugin.json", ".plugin/plugin.json", "plugin.json"):
        print("token_well_formed(%r, %r) -> %s" % (t, cl, m.token_well_formed(t, cl)))
'
token_well_formed('.github/plugin/plugin.json', 'Copilot CLI') -> True
token_well_formed('.plugin/plugin.json', 'Copilot CLI') -> True
token_well_formed('plugin.json', 'Copilot CLI') -> False
token_well_formed('.github/plugin/plugin.json', 'VS Code') -> True
token_well_formed('.plugin/plugin.json', 'VS Code') -> True
token_well_formed('plugin.json', 'VS Code') -> False
exit 0
```

Supplement from the same harness: `token_well_formed("package.json", "opencode") -> False`; `MARKERS = {'Claude Code': 'claude', 'Codex': 'codex', 'VS Code': 'vscode', 'Copilot CLI': 'copilot', 'Gemini CLI': 'gemini', 'Cursor': 'cursor', 'opencode': 'opencode'}`.

Why True (`verifiers/check_plugin_manifests.py:535-558`): TOKEN_RE accepts it; no `marketplace` segment; a segment word splits to `plugin`; body splits into 3 parts (`.github`, `plugin`, `plugin.json`), no internal dot in a non-final segment (`.github` leading dot is exempt); final segment ends `.json` and carries the plugin word; `len(parts) >= 2` so the own-marker requirement (`copilot`) never applies. Corroboration: the frozen counter's own self-test asserts the same at `:1137` (`token_well_formed(".github/plugin/plugin.json", "Copilot CLI"), True`), `build/CriticC1Rows.md:37` shows the path documented on the S028 page, and `controls/CtlC1KeyedLabels.md` (v2 probe) found the token well-formed and `found_on_page=True` on a live docs.github.com page that says "The manifest may also live at .github/plugin.json or .github/plugin/plugin.json so plugins can sit inside an existing repository without changing its root layout."

The candidate's parenthetical is therefore true, and it does not contradict the lesson's rejection: the candidate itself says the path is "neither own-format nor the default its creation guide names", which is the row-reject's actual basis (S028 base-URL bar + S082), not the grammar.

## 3. Wording nits (no verdict changes)

1. Lesson :31, C2 reason: "`CtlC2GeneratorKeyed`, 120 of 120 on six seeds" — the receipt's six-seed score is `240 of 240` (six seeds × 40 cases; `CtlC2GeneratorKeyed.md:37`); `120 of 120` is the per-three-seed-batch score (`:34-35`). Suggested old→new: "120 of 120 on six seeds" → "120 of 120 (240 of 240 over six seeds)".
2. Lesson :34, opencode reason: "a published package's metadata file, not a plugin manifest" — the vendor page calls it "A minimal manifest" (`build/Srcopencode.md:5,15`). The rejection is still right (npm package metadata; token fails the frozen grammar); if the L1 wants the lesson airtight against the vendor label: "not a plugin manifest" → "the package's npm manifest, not a plugin-specific one".

## 4. Peer coordination note received (no action taken)

`ChousaR32A2.CtlC2WeakReaderB` reported a C2 gate-layout hazard (flat `scratch/gate.sh` + `C2_TMP=scratch` lets the counter's `../outside` files fall inside allowed LANE_ROOT, so E7 is missed, 0/6). Out of scope for this report: none of the four C2 controls behind lesson :31 used such a layout — each ran the frozen counter by its standard CLI (`python3 -B verifiers/check_infoless_fences.py --rev …`), so their scores are unaffected. Per session bounds (message target: my L1 only) no reply was sent to that peer.

## 5. Residual risk and verification gaps

- I re-opened the committed receipts (`.ufo/waves/round-57/controls/`, `…/build/`) and cross-checked their recorded fetch sha256s against the S-rows (S028 `d0d362cc…`, S081 `d6e10328…`, S082 `c0642867…`, S085 `e505931a…`); I did not re-fetch those live pages myself in this seat. A live re-open could in principle diverge today; nothing in my findings depends on post-2026-10-23 page state.
- The "50-line" stub size is quoted from `MutC2Counter.md:1` (the receipt the lesson cites); I did not recount the stub's lines from its sandbox bytes.
- HeldVariant's v2 adaptation (`F=3 of K=3`, exit 1) is a real-claims partial world, not hollow; a reader of the lesson's "best hollow world `found 1 of 7`" should not take it as the best v2 adaptation overall.
- Flip-cell conditionals (e.g. "VS Code documents a VS Code-named manifest path") are counterfactuals I could only falsify for today's page state, not prove unreachable forever.
- Out of my scope: the rest of the a2 candidate (S086–S088 rows, ship cells, quote notes) — other seats hold those items; I verified only the Copilot CLI grammar parenthetical assigned to me.
