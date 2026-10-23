Result: MIXED — All six committed snapshots match their Src fetch receipts and their own row's sole/first full digest; the frozen counter alone does not establish page identity if the row is repinned to different bytes.

# Scope and authority

Reviewed revision `c63ccc6823e1f6a8577acbb43d19551eadbbee9a` only, in `/fast/scratch/hyaku/kotoba-r59/CriticSnapshotProvenance`. Primary axis: depth; related evidence-calibration and source-identity consistency risks are identified, not scored. This is an adversarial review, not admission or a canonical judgment.

Counter SHA-256 observed: `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71`. Committed `verifiers/check_hook_files.py:253-254` says `TARGET = 4`, `NEW_TARGET = 5`. Neither the counter, rule, targets nor lane content was changed.

# Per-row ruling: current committed provenance HOLDS

For every row below, the full digest shown is simultaneously (1) the Src report's successful fetched-body digest, (2) SHA-256 over `git show c63ccc6823e1f6a8577acbb43d19551eadbbee9a:.ufo/waves/round-59/snapshots/<id>.page` bytes, and (3) the frozen `row_sha` function's first full digest. Each row contains exactly one matching full `sha256 <64 hex>` pin anywhere across its cells. Thus no supporting-page digest precedes or supplants the primary pin in these six rows.

All build-report pointers below are relative to `.ufo/waves/round-59/build/`; source-row pointers refer to `corpus/SOURCES.md` at the reviewed revision.

| Row/client | Committed bytes | Receipt evidence | SOURCES line | Three-way equal full SHA-256 | Ruling |
|---|---:|---|---:|---|---|
| S096 Claude Code | 274129 | `SrcClaudeCode.md:9-11` | 108 | `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8` | HOLDS |
| S097 Codex | 47133 | `SrcCodex.md:8,14-18` | 109 | `57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92` | HOLDS |
| S098 VS Code | 15152 | `SrcVSCode.md:14,17` | 110 | `98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08` | HOLDS |
| S099 Copilot CLI | 8428 | `SrcCopilotCLI.md:38-44` | 111 | `23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4` | HOLDS |
| S100 Gemini CLI | 17650 | `SrcGeminiCLI.md:10,13` | 112 | `fb44fbcfaccc3cdb7895d989f3808bed66cfa6516411535c4c4d9077d242e7bc` | HOLDS |
| S101 Cursor | 69145 | `SrcCursor.md:14,17` | 113 | `8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d` | HOLDS |

This answers the requested seat-report-SHA versus committed-file-SHA comparison. It is not an independent historical network capture or proof that a seat report cannot lie.

## Requested/effective source identity in the Src receipts

These are the existing seats' reported requests and outputs, not new fetches by this seat. Each successful fetch reports HTTP 200, curl exit 0, the byte count and digest above. The recorded effective URL equals the row's primary URL for every row with an effective-URL receipt. S098's successful save command records its requested URL, status and bytes, but does not print an effective URL; its later counter fetch reports that same URL at `SrcVSCode.md:74-77`.

| Row | Primary requested URL | Existing receipt's exact `date -u` line |
|---|---|---|
| S096 | https://code.claude.com/docs/en/hooks.md | `Fri 23 Oct 2026 09:34:52 AM UTC` |
| S097 | https://learn.chatgpt.com/docs/hooks.md | `Fri Oct 23 09:35:05 AM UTC 2026` |
| S098 | https://code.visualstudio.com/docs/agent-customization/hooks.md | `Fri Oct 23 09:35:04 AM UTC 2026` |
| S099 | https://docs.github.com/en/copilot/concepts/customizations/hooks.md | `Fri Oct 23 09:34:55 AM UTC 2026` |
| S100 | https://geminicli.com/docs/hooks/best-practices.md | `Fri Oct 23 09:34:48 AM UTC 2026` |
| S101 | https://cursor.com/docs/hooks | `Fri 23 Oct 2026 09:35:23 AM UTC` |

S096's receipt additionally reports byte-for-byte copy and `cmp -s` exit 0. S101's selected primary is `/docs/hooks`, not the `.md` route whose 404 digest is separately reported at `SrcCursor.md:22`; the committed snapshot is not that error response. S097 uses the final Learn URL directly; the developers-to-Learn redirect example in `CriticR3Design.md:76-111` is not the production source row.

# Could a different page pass? Distinguish unchanged pins from repinned rows

## 1. With the actual committed row unchanged: HOLDS against substitution

Read-only, in-memory row-level probes imported the frozen counter from this sandbox and used the actual committed source rows, entry rows, Gate, Events cells, base source IDs and base URL keys.

For each row:

- Its own committed snapshot returned `baseline_entry_reasons: []`.
- Substituting each of the other five committed snapshots returned a nonempty rejection: 5 of 5 rejected per row, 30 of 30 total.
- Independently testing only quote/token/events on those other pages produced `other_snapshot_content_passes: []` for every row.
- A newly constructed different document retaining the genuine quote and all checked event names was also rejected with the actual pin, specifically for SHA mismatch.

No different-byte snapshot can meet the unchanged pin without the same SHA-256; a hash collision was not attempted or observed. This is not evidence of current cross-page substitution.

## 2. If an earlier supporting digest becomes authoritative: stronger provenance implication BREAKS

Implementation evidence, all in `verifiers/check_hook_files.py`:

- `:510-515`: `row_sha` searches all row cells and selects the first full digest.
- `:833-847`: primary URL comes independently from the source cell and receives URL/host/type checks.
- `:848-865`: the chosen digest is compared with snapshot bytes, followed by quote/token/event-presence checks. There is no URL-bearing capture receipt check.
- `:2388-2397`: live checking calls `fetch` and `page_why`; it never compares live-body SHA-256 with the snapshot pin.

For each of the six real rows, I constructed a small, explicitly synthetic document in memory, retained the production entry quote and every checked Events span, and changed only the in-memory source row's anchor to:

`Supporting synthetic critic fixture sha256 <fixture SHA>; primary fetched-page sha256 <real SHA>`

The primary URL, production quote, Gate, Events, source ID, kind, tier, status, date and base inputs were unchanged. The frozen first-digest function selected the synthetic digest. All six row-level snapshot/content checks then returned `fixture_with_first_pin_reasons: []`. The primary committed page also returned `primary_page_content_reasons: []` for the unchanged quote/token/events. These are different documents, not fetched vendor responses.

| Row | Original-pin synthetic snapshot | Synthetic bytes | Synthetic SHA selected after earlier-pin insertion | Repinned entry reasons | Primary-page content reasons |
|---|---|---:|---|---|---|
| S096 | SHA mismatch | 228 | `6b6bff30a073d6d87dbf1dc37b95ffba31392dbadea903e51c61089112884940` | `[]` | `[]` |
| S097 | SHA mismatch | 339 | `849e8acb44d48b9393f6b4e7de24c58b210ed47a3c6c0541bebfb928b8f01e00` | `[]` | `[]` |
| S098 | SHA mismatch | 195 | `e70af7f91a9d5a8afde324027068746b4efa51df6984e4e29a18db674d7e28f3` | `[]` | `[]` |
| S099 | SHA mismatch | 157 | `1b9cf22bca16897c85ef28934fedbaa28a5dadfca37bcc0719007aaa32483224` | `[]` | `[]` |
| S100 | SHA mismatch | 155 | `071398433e8e2526901acac803f6e69f6eb0f685084a8900a4249c4ee0e1176f` | `[]` | `[]` |
| S101 | SHA mismatch | 235 | `2d900f346266aa4a7b1a0854b7c7da123542d7ea2573a1b4e428546bbba60670` | `[]` | `[]` |

[INFERENCE] A committed world built from these repinned rows and quote-preserving documents would satisfy the tested snapshot/content conjuncts; a live page still serving the observed authentic content would satisfy its content conjunct too. I did not commit these fixtures, fetch live pages in this probe, run a full mutant `--fetch` command, or produce a full-predicate exit-0 witness. The existing L1 measurement at `.ufo/waves/round-59/C1-measure.txt:3-11` separately reports live 6/6 at the reviewed revision; it is not this mutation's receipt.

The real different-page example already recorded in `build/CriticR3Design.md:25-46` is narrower: the actual Claude guide body, SHA `004ded2fd87af2deee93d4ce7f47216a82b5e22fc76f345ea654eeb51b2bee3c`, passes the snapshot conjunct when its earlier supporting pin wins over the reference digest; that guide-specific quote fails the reference live check. Therefore that real-page witness is not a found/new-ground false positive. The quote-preserving constructed documents above test the stronger provenance inference without pretending they were fetched.

# Impact and smallest safe correction

- **Depth:** current six-row evidence survives the receipt/blob/pin attack. No hook-file fact was shown false here. The risk is teaching that selected-word corroboration proves the identity/provenance of an entire captured page.
- **Calibration:** counter-only wording such as “the checker proves these are the primary page's fetched bytes” is unsupported. The receipt-to-blob audit is a separate necessary evidence route.
- **Consistency/source identity:** multiple full digests create duplicate candidate authorities; production S096-S101 avoid that ambiguity with exactly one primary pin each.

No correction to these six committed rows or snapshots is warranted by this review. Keep their sole primary digest first; keep supporting-page capture receipts outside that pin-bearing row. The smallest safe documentation correction, if the aggregate report describes a stronger guarantee, is to say: “The counter pins committed bytes and corroborates quote/token/events; Src fetch receipts separately establish the reviewed snapshot provenance.” Do not change the frozen counter, rule or targets, and do not treat the hypothetical repinning hole as an observed production substitution. Whether the declared measurement is acceptable despite this disclosed design limit belongs only to the canonical judge.

# Executed commands and evidence boundary

Sandbox setup, exit 0, no output:

```sh
timeout 120 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r59/CriticSnapshotProvenance && timeout 60 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /fast/scratch/hyaku/kotoba-r59/CriticSnapshotProvenance checkout -q c63ccc6823e1f6a8577acbb43d19551eadbbee9a
```

From that sandbox, this command exited 0:

```sh
timeout 20 sha256sum .ufo/waves/round-59/snapshots/S096.page .ufo/waves/round-59/snapshots/S097.page .ufo/waves/round-59/snapshots/S098.page .ufo/waves/round-59/snapshots/S099.page .ufo/waves/round-59/snapshots/S100.page .ufo/waves/round-59/snapshots/S101.page verifiers/check_hook_files.py
```

Output:

```text
c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8  .ufo/waves/round-59/snapshots/S096.page
57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92  .ufo/waves/round-59/snapshots/S097.page
98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08  .ufo/waves/round-59/snapshots/S098.page
23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4  .ufo/waves/round-59/snapshots/S099.page
fb44fbcfaccc3cdb7895d989f3808bed66cfa6516411535c4c4d9077d242e7bc  .ufo/waves/round-59/snapshots/S100.page
8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d  .ufo/waves/round-59/snapshots/S101.page
f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71  verifiers/check_hook_files.py
```

The scoped probe ran as `timeout 60 python3 -B -c <source below>` in the same sandbox with `GIT_DIR`, `GIT_WORK_TREE`, and `GIT_INDEX_FILE` removed from its environment. Exit 0; stderr empty. Its JSON output supplies the per-row values above: `three_way_match: true`, `full_pin_count: 1`, `baseline_entry_reasons: []`, five rejected swaps, no other-page content passes, SHA rejection under the original pin, and empty reasons under the synthetic first pin for every row. `network_fetches: 0`, `disk_mutations: 0`. Exact executed source:

```python
import hashlib, importlib.util, json, re
from pathlib import Path
spec = importlib.util.spec_from_file_location("frozen_counter", "verifiers/check_hook_files.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
lane = Path.cwd()
rev = "c63ccc6823e1f6a8577acbb43d19551eadbbee9a"
sources = m.git_show(lane, rev, m.SOURCES)
table = m.sources_table(sources)
base = m.git_show(lane, m.BASE, m.SOURCES)
at_base = m.source_ids(base)
base_urls = m.base_url_keys(base)
entry = m.git_show(lane, rev, m.ENTRY)
skill = m.git_show(lane, rev, m.SKILL)
lesson = m.git_show(lane, rev, m.LESSON)
gate = m.gate_section(lesson)
gate_raw, gate_plain = m.ws(gate), m.ws(gate.replace("`", ""))
entries = {r[2].strip(): r for r in m.entry_rows(entry)}
skills = {r[0]: r for r in m.skill_rows(skill)}
receipts = {"S096": ("SrcClaudeCode.md", 11), "S097": ("SrcCodex.md", 18), "S098": ("SrcVSCode.md", 17), "S099": ("SrcCopilotCLI.md", 44), "S100": ("SrcGeminiCLI.md", 13), "S101": ("SrcCursor.md", 17)}
snaps = {sid: m.git_show_bytes(lane, rev, m.snapshot_path(sid)) for sid in receipts}
def verdict(er, token, events, source_table, snapshot):
    return m.entry_row_verdict(er, er[0], token, source_table, at_base, base_urls, gate_raw, gate_plain, events, lambda sid: snapshot)[0]
results = []
for sid, (seat, line) in receipts.items():
    snapshot = snaps[sid]
    digest = hashlib.sha256(snapshot).hexdigest()
    receipt_text = m.git_show(lane, rev, ".ufo/waves/round-59/build/" + seat)
    receipt_line = receipt_text.splitlines()[line - 1]
    receipt_sha = re.search(r"[0-9a-f]{64}", receipt_line).group(0)
    er = entries[sid]
    sr = skills[er[0]]
    token = m.BACKTICK_RE.findall(sr[1])[0]
    events = m.event_spans(sr[2])
    quote = m.strip_quotes(er[3])
    fixture = ("Synthetic critic fixture; not a vendor response.\n<p>" + quote + "</p><p>" + " ".join(events) + "</p>\n").encode()
    fixture_sha = hashlib.sha256(fixture).hexdigest()
    mutant_table = {key: row.copy() for key, row in table.items()}
    mutant_table[sid][5] = "Supporting synthetic critic fixture sha256 " + fixture_sha + "; primary fetched-page sha256 " + digest
    swaps = {other: verdict(er, token, events, table, data) for other, data in snaps.items() if other != sid}
    results.append({"row": sid, "client": er[0], "bytes": len(snapshot), "receipt": seat + ":" + str(line), "receipt_sha": receipt_sha, "committed_sha": digest, "first_pin": m.row_sha(table[sid]), "full_pin_count": len(m.SHA256_RE.findall(" | ".join(table[sid]))), "three_way_match": receipt_sha == digest == m.row_sha(table[sid]), "baseline_entry_reasons": verdict(er, token, events, table, snapshot), "unchanged_pin_other_snapshots_rejected": sum(bool(why) for why in swaps.values()), "unchanged_pin_swap_count": len(swaps), "other_snapshot_content_passes": [other for other, data in snaps.items() if other != sid and not m.page_why(data.decode("utf-8", errors="replace"), quote, token, events)], "fixture_bytes": len(fixture), "fixture_sha": fixture_sha, "fixture_with_original_pin_reasons": verdict(er, token, events, table, fixture), "fixture_selected_first_pin": m.row_sha(mutant_table[sid]), "fixture_with_first_pin_reasons": verdict(er, token, events, mutant_table, fixture), "primary_page_content_reasons": m.page_why(snapshot.decode("utf-8", errors="replace"), quote, token, events)})
print(json.dumps({"revision": rev, "counter_sha": m.self_sha(), "TARGET": m.TARGET, "NEW_TARGET": m.NEW_TARGET, "network_fetches": 0, "disk_mutations": 0, "cases": results}, indent=2))
```

No full counter invocation, self-test, build, formatter, no-harm suite, canonical runtime, fresh network fetch, sandbox commit, paid model call, browser or tool installation/update was performed. Only this report was written in the lane. The clone and all code execution were confined to the named sandbox; fixtures existed only in memory. Broader milestone checks remain the owning seats' evidence, not asserted here.

Report: .ufo/waves/round-59/falsify/CriticSnapshotProvenance.md
