Result: MIXED — The frozen counter checks the new Events cell, but neither its first-digest pin nor its live check proves that the committed bytes came from the row’s primary page.

# CriticR3Design — scoped R3 design review

## Scope and evidence boundary

- Axes at risk: **depth** (what the hook table actually teaches), **calibration** (what the counter proves), and **consistency** (source identity and the scope of the R3 repair). No axis score or admission decision is made here.
- Reviewed the counter at freeze `4b2125c91ea1868a83b7b28eb4bbbacc35f469fe` in `/fast/scratch/hyaku/kotoba-r59/CriticR3Design`. Its SHA-256 is `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71`. Committed lines 253–254 say `TARGET = 4`, `NEW_TARGET = 5`.
- These are read-only, in-memory **row-level probes**, not committed mutant worlds and not a full `--rev … --fetch` predicate receipt. `entry_reasons: []` means the entry/source/snapshot content conjunct passed the frozen function; it does not claim that a fixture was committed. No canonical judge was invoked.
- Frozen source line references below are to `verifiers/check_hook_files.py`; the clone and lane copies read during this review have the same frozen counter digest. The freeze addendum is read from `plans/round-59.md:93–98` in the lane.

## Direct answers

| Question | Observed answer | Effect on the frozen predicate |
|---|---|---|
| Can an earlier digest belonging to a different page win? | **Yes.** The real Claude guide snapshot passes the snapshot/content check while the source cell names the reference page. | That particular quote fails live, so it does **not** contribute F/G. A fabricated document retaining a real reference quote and real events passes both content checks; provenance remains unproved. |
| Can a redirect to another pinned page pass? | **Yes.** The real Codex developers URL redirects to the Learn URL; the frozen `fetch` accepts it. | Counts normally when snapshot/content checks pass. This is explicitly allowed by the frozen contract, not itself a defect. |
| Does a browser UA necessarily violate the bounds? | **No.** A fixed UA and Accept header on an ordinary public GET are not themselves a challenge solution. | Our requests returned normal docs without authentication or challenge handling. This does not authorize using UA changes to pass an actual bot/access-control challenge. |
| Does Events read the exact field named by the spot-check? | **No for the old `What a file sets` cells; yes for the new `Events` cell.** | Old command-cell corruption is outside C1. New event-name presence is checked, but event meaning is not. |

## 1. First-digest authority confusion: real different-page counterexample

`row_sha` searches **all cells joined together** and returns the first match (`:510–515`); `entry_row_verdict` takes the first URL only from the source cell (`:833–834`). Nothing associates the selected digest with that URL. This is deliberate frozen behavior: the docstring says first digest (`:129–136`) and a regression assertion fixes that choice (`:1792–1795`). It is a design/provenance limitation, not an implementation violation of the frozen spec.

Concrete hypothetical SOURCES row, not a proposed production edit:

```text
| S096 | Claude Code hooks — https://code.claude.com/docs/en/hooks.md | docs | A | hook configuration | Supporting guide https://code.claude.com/docs/en/hooks-guide.md sha256 004ded2fd87af2deee93d4ce7f47216a82b5e22fc76f345ea654eeb51b2bee3c; primary reference sha256 c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8 | client hook path and events | mined | 2026-10-23 | 90d | corpus/knowledge/hook-files-round59.md |
```

Use the real guide bytes as `.ufo/waves/round-59/snapshots/S096.page`; use `.claude/settings.json`, Events `PreToolUse`, `PostToolUse`, and an action of at least three words. The entry and Gate quote is this byte-exact six-word slice of the [guide](https://code.claude.com/docs/en/hooks-guide.md), fetched bytes line 284 (no bytes stripped):

```text
Add a `PreToolUse` hook to `.claude/settings.json`
```

Observed successful probe process exit 0:
```text
selected_sha = 004ded2fd87af2deee93d4ce7f47216a82b5e22fc76f345ea654eeb51b2bee3c
snapshot_sha = 004ded2fd87af2deee93d4ce7f47216a82b5e22fc76f345ea654eeb51b2bee3c
primary_live_sha = c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8
entry_reasons = []
live_reasons = ["the quote is not on the page"]
```

**Predicate significance:** this is a false primary-page snapshot association, but not a live false positive: the reference does not carry this guide quotation. The live conjunct kills this particular row. Do not turn “snapshot backed” into “snapshot is the primary URL’s bytes.”

## 2. Stronger counterexample: preserve true words, fabricate everything else

The live check compares quote/token/events, **not the live body digest** against the snapshot digest (`:2388–2397`). The existing fabricated-snapshot control changes the quotes to invented sentences (`controls/CtlFabSnapshot.md:35–52`) and therefore tests a weaker adversary than a fabricated snapshot preserving authentic words.

Use this 227-byte synthetic document B. It is explicitly a critic fixture, never fetched or represented here as vendor bytes:

```text
Synthetic critic fixture; not a vendor response.
<p>This `PreToolUse` hook in `.claude/settings.json` runs a project script before each Bash command, and blocks the command if the script fails:</p><p>PreToolUse PostToolUse</p>
```

B SHA-256: `1aa80e5eb01942f2419b71a08eaae504a3b02582fd72424608713d4c4cbf578b`. The 21-word quotation inside it is byte-exact from the [real reference](https://code.claude.com/docs/en/hooks.md), fetched bytes line 910; no quote bytes were stripped. Both event identifiers are real Claude events.

Concrete hypothetical row:
```text
| S096 | Claude Code hooks — https://code.claude.com/docs/en/hooks.md | docs | A | hook configuration | Supporting fixture B (synthetic) sha256 1aa80e5eb01942f2419b71a08eaae504a3b02582fd72424608713d4c4cbf578b; primary fetched page sha256 c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8 | client hook path and events | mined | 2026-10-23 | 90d | corpus/knowledge/hook-files-round59.md |
```

With B as the snapshot callback bytes, that quote in entry/Gate, and the ordinary valid hook row:
```text
entry_reasons = []
live_reasons = []
```

**Predicate significance:** [INFERENCE] committing these exact content-equivalent fixture files would satisfy this row’s snapshot and live content conjuncts even though B is not the fetched page. No full mutant commit or predicate exit 0 was produced here. This does not fabricate a hook fact—the live fact is true—but it defeats the stronger provenance inference that the artifact is a captured vendor page. The frozen predicate only binds author-supplied bytes to an author-supplied pin and corroborates selected content online.

**Smallest safe current correction for 1–2:** keep exactly one primary full digest in each production row, make it the first digest, and ensure the source receipt names that primary URL/effective URL and the exact fetched bytes used for its snapshot. Put supporting-page receipts outside that pin-bearing row (S102 only if a supporting source is actually needed; this review requests none). Disclose the counter’s content-only provenance limit. Do **not** edit this frozen counter or claim a redesigned measurement.

## 3. Redirect acceptance: real example, not automatically a hole

Concrete S097 fixture:
```text
| S097 | Codex hooks — https://developers.openai.com/codex/hooks.md | docs | A | hook configuration | final https://learn.chatgpt.com/docs/hooks.md sha256 57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92 | client hook path and events | mined | 2026-10-23 | 90d | corpus/knowledge/hook-files-round59.md |
```

Its byte-exact 22-word quote is from the fetched [Learn page](https://learn.chatgpt.com/docs/hooks.md), lines 38–44; no bytes stripped:
```text
a default `hooks/hooks.json` file. See [Build
plugins](https://developers.openai.com/plugins/build/plugins#bundled-mcp-servers-and-lifecycle-hooks) for the
plugin packaging rules.

In practice, the four most useful locations are:

- `~/.codex/hooks.json`
```

The entry/Gate retained that raw quote; table storage can collapse whitespace as documented, but the quotation above does not. Events are `PreToolUse` and `SessionStart`.

Observed actual `fetch` call, process exit 0, stderr empty:
```text
url = https://developers.openai.com/codex/hooks.md
date -u: Fri Oct 23 09:41:47 AM UTC 2026
HTTP 200; effective = https://learn.chatgpt.com/docs/hooks.md
47133 bytes; sha256 57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92
requested_and_effective_url_keys_differ = true
effective_host_pinned = true; effective_is_base = false
entry_reasons = []; events_cell_reasons = []; live_reasons = []
```

The frozen rule explicitly permits redirects (`:168–180`). `fetch` checks final HTTP 200, client pins, BASE URLs, change-note paths and size (`:1093–1106`), but it does not require final URL identity with the source URL. Thus a legitimate cross-pinned-host canonical migration passes. A final BASE URL is rejected, so redirecting to an already-held source is not the obvious novelty bypass. Final-body/snapshot equality is still absent (finding 2).

Additional static redirect edge: `entry_row_verdict` rejects tracker paths (`:842–844`), but `fetch` does not repeat `url_is_tracker(final)`. For example, a hypothetical S097 documentation alias ending at `https://github.com/openai/codex/issues/1` passes the final *host* test and is not rejected *as a tracker* by `fetch`; it would still need real quote/token/event content and all other checks. [INFERENCE] this could matter for F if such a redirect/content combination existed. No such redirect was observed or simulated; this is not a claimed predicate witness.

**Smallest safe correction:** record both requested and effective URL and label aliases as aliases; prefer the opened final canonical URL for production. Do not count an alias as additional evidence or assert URL identity. The tracker asymmetry is a limit to disclose, not permission to change the frozen rule.

## 4. Browser UA and the access-control boundary

`run_curl` uses ordinary curl, `-sSL --max-time 30`, a fixed Chrome UA, and Accept; its argv includes no credentials, cookies, challenge solver, headless browser, or TLS-verification bypass (`:316–319,1058–1082`). Our three initial public requests and the actual redirect call below returned the expected docs bodies. No challenge interaction or UA rotation was performed.

The row in finding 3 is a concrete successful, bounds-conforming example. It does **not** establish that every 403 may safely be retried with a different identity. The earlier urllib-403/curl-200 observation (`corpus/lessons/round-58-verifier-spotcheck.md:89–95,258–262`) does not itself identify why the server denied urllib. If the response is an actual bot challenge, captcha, authentication or access-control denial, using any tool/header maneuver to pass that denial is outside the bounds. The frozen UA is not blanket authorization to do that.

**Predicate significance:** normal public representation negotiation is not a predicate hole or a demonstrated bounds breach. The counter cannot certify research-process compliance from a final HTTP 200. Smallest correction: retain ordinary-request receipts; stop at an actual challenge and report that row unavailable instead of solving it.

## 5. The named field is not the field now being checked

The spot-check names **`What a file sets`** in the round-58 command table (`corpus/lessons/round-58-verifier-spotcheck.md:96–104,258–262`; frozen `SKILL.md:111–119`). The new counter selects only `### Hook files by client` / its first table (`:471–481`) and obtains Events from `sr[2]` (`:891–914`). It never opens the old command table’s third cell.

Concrete negative change to the old Codex row:
```text
| Codex | `~/.codex/prompts/` | binary SQLite; required `fabricatedField` | Migrate commands to skills |
```
An otherwise-identical input with the real field versus this false field produced:
```text
extracted_hook_rows_identical = true
extracted_hook_rows = [["Claude Code", "`.claude/settings.json`", "`PreToolUse`, `PostToolUse`", "Move invariant checks into hooks"]]
```

**Predicate significance:** no effect on C1; that old cell is outside its frozen scope. The original routed request allows **next counters** to cover their fields or explicitly named seats, so this is not automatically a failure of the allowed forward-looking route. It is, however, not evidence that the old `What a file sets` checker was repaired. Smallest correction: describe R3 as the new hook-table presence/snapshot route, not as retroactive coverage of old command fields; retain/name manual field-check evidence if claiming those old fields checked.

## 6. Events presence is not event semantics (known frozen limitation)

Concrete new hook row:
```text
| Claude Code | `.claude/settings.json` | `Bash`, `JSON` | Move invariant checks into hooks |
```
The reference prints `Bash` as a tool/matcher (e.g. fetched line 73) and `JSON` as a format (e.g. line 7), not hook lifecycle events. Using the real reference bytes, its true line-910 quote and its correct digest produced:
```text
events_cell_reasons = []
entry_reasons = []
live_reasons = []
```

The code proves identifier syntax and case-sensitive page presence only (`:705–763,1042–1055`). This behavior is already explicitly disclosed in the freeze addendum (`plans/round-59.md:93–98`) and assigned to `Cells<Client>` semantics seats. It is not newly fixed by the fabricated-events control, which tests identifiers absent from the pages (`controls/CtlFabEvents.md:81–104`).

**Predicate significance:** these non-events would pass the measured content conjunct and could supply a found/new token row if committed; the real-event requirement would still fail the human semantic route. Correct the **row**, not the frozen rule: use actual documented events, and keep the per-client semantic receipt. Do not claim the counter itself certifies event meaning or arbitrary unbackticked Events prose.

## Receipts, limits and hygiene

Actual sandbox setup argv, exit 0, no output:
```sh
timeout 90 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r59/CriticR3Design && timeout 30 git -C /fast/scratch/hyaku/kotoba-r59/CriticR3Design checkout -q 4b2125c91ea1868a83b7b28eb4bbbacc35f469fe
```
From the clone, `timeout 30 sha256sum verifiers/check_hook_files.py`, exit 0:
```text
f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71  verifiers/check_hook_files.py
```

Initial source collection executed three `timeout 50 python3 -B -c <fetch-source> <URL>` processes concurrently (not more than three); each exited 0, stderr empty. `fetch-source` below calls the frozen `run_curl`, not a different fetch implementation. Every request’s `date -u` line was exactly:
```text
Fri Oct 23 09:36:40 AM UTC 2026
```
| Requested URL | HTTP | Effective URL | Bytes | SHA-256 |
|---|---|---|---:|---|
| https://code.claude.com/docs/en/hooks.md | 200 | https://code.claude.com/docs/en/hooks.md | 274129 | `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8` |
| https://code.claude.com/docs/en/hooks-guide.md | 200 | https://code.claude.com/docs/en/hooks-guide.md | 62917 | `004ded2fd87af2deee93d4ce7f47216a82b5e22fc76f345ea654eeb51b2bee3c` |
| https://developers.openai.com/codex/hooks.md | 200 | https://learn.chatgpt.com/docs/hooks.md | 47133 | `57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92` |

Initial source-collection inline Python (exact source):
```python
import hashlib,json,runpy,subprocess,sys
c=runpy.run_path("verifiers/check_hook_files.py")
when=subprocess.run(["timeout","5","date","-u"],capture_output=True,text=True,check=True).stdout.strip()
status,final,body=c["run_curl"](sys.argv[1])
print(json.dumps({"requested":sys.argv[1],"date_u":when,"http":status,"effective":final,"bytes":len(body),"sha256":hashlib.sha256(body).hexdigest(),"body":body.decode("utf-8",errors="replace")}))
```

Scoped API probe argv was `timeout 60 python3 -B -c <scoped-source>` in the clone, with JSON stdin containing those exact captured bodies/metadata. Exit 0; stderr empty; its `date -u` output was `Fri Oct 23 09:40:45 AM UTC 2026`. Findings 1, 2, 5 and 6 reproduce its output fields. Its first Codex quote was incorrectly constructed and correctly yielded `the quote is not on the page`; that diagnostic is not a redirect failure. I extracted the actual byte slice at lines 38–44 and retried **only the Codex case** with the second source below, exit 0, producing finding 3.

A prior wrapper construction attempt exited 1 with `SyntaxError: unterminated string literal (detected at line 26)` (and an input-pipe EPIPE); it executed no counter checks. The corrected source below is the successful wrapper, not a counter patch.

No full predicate run, self-test, build, lint, formatter, sandbox commit, push, paid model call, headless browser, challenge bypass, tool installation or update was performed. Only this report is written in the lane; no lane Git/jj write was made. No S102 source is proposed. Counter, targets, census and acceptance rule remain unchanged.

## Exact successful scoped-probe source

All fixtures in this source are data in memory; no fixture or source files were written.
```python
import hashlib,importlib.util,json,subprocess,sys
from pathlib import Path
spec=importlib.util.spec_from_file_location("frozen_counter","verifiers/check_hook_files.py")
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
x=json.load(sys.stdin)
base=m.git_show(Path.cwd(),m.BASE,m.SOURCES)
at_base=m.source_ids(base);base_urls=m.base_url_keys(base)
ref=x["ref"];guide=x["guide"];codex=x["codex"]
q="This \u0060PreToolUse\u0060 hook in \u0060.claude/settings.json\u0060 runs a project script before each Bash command, and blocks the command if the script fails:"
qg="Add a \u0060PreToolUse\u0060 hook to \u0060.claude/settings.json\u0060"
events=["PreToolUse","PostToolUse"];token=".claude/settings.json"
def row(sid,client,url,anchor):
    return "| "+" | ".join([sid,client+" hooks — "+url,"docs","A","hook configuration",anchor,"client hook path and events","mined","2026-10-23","90d","corpus/knowledge/hook-files-round59.md"])+" |"
def entry_reasons(source,sid,client,tok,quote,ev,page):
    return m.entry_row_verdict([client,"\u0060"+tok+"\u0060",sid,quote],client,tok,m.sources_table(source),at_base,base_urls,m.ws(quote),m.ws(quote.replace("\u0060","")),ev,lambda s:page)[0]
source_guide=row("S096","Claude Code",ref["requested"],"Supporting guide "+guide["requested"]+" sha256 "+guide["sha256"]+"; primary reference sha256 "+ref["sha256"])
r1={"case":"real different page first pin","source_row":source_guide,"selected_sha":m.row_sha(m.sources_table(source_guide)["S096"]),"snapshot_sha":guide["sha256"],"primary_live_sha":ref["sha256"],"quote":qg,"quote_lines_in_snapshot":[i for i,l in enumerate(guide["body"].splitlines(),1) if qg in l],"entry_reasons":entry_reasons(source_guide,"S096","Claude Code",token,qg,events,guide["body"].encode()),"live_reasons":m.page_why(ref["body"],qg,token,events)}
clipped=("Synthetic critic fixture; not a vendor response.\n<p>"+q+"</p><p>PreToolUse PostToolUse</p>\n").encode()
h=hashlib.sha256(clipped).hexdigest()
source_clipped=row("S096","Claude Code",ref["requested"],"Supporting fixture B (synthetic) sha256 "+h+"; primary fetched page sha256 "+ref["sha256"])
r2={"case":"synthetic different document preserving real quotation","source_row":source_clipped,"snapshot_bytes":len(clipped),"snapshot_sha":h,"snapshot_utf8":clipped.decode(),"primary_live_sha":ref["sha256"],"quote":q,"quote_lines_in_primary":[i for i,l in enumerate(ref["body"].splitlines(),1) if q in l],"entry_reasons":entry_reasons(source_clipped,"S096","Claude Code",token,q,events,clipped),"live_reasons":m.page_why(ref["body"],q,token,events)}
source_exact=row("S096","Claude Code",ref["requested"],"primary fetched page sha256 "+ref["sha256"])
false_events=["Bash","JSON"]
r3={"case":"printed but not hook event identifiers","skill_row":"| Claude Code | \u0060.claude/settings.json\u0060 | \u0060Bash\u0060, \u0060JSON\u0060 | Move invariant checks into hooks |","events_cell_reasons":m.events_cell_why(false_events),"entry_reasons":entry_reasons(source_exact,"S096","Claude Code",token,q,false_events,ref["body"].encode()),"live_reasons":m.page_why(ref["body"],q,token,false_events),"printed_identifier_locations":{e:[i for i,l in enumerate(ref["body"].splitlines(),1) if m.event_on_page(l,e)][:6] for e in false_events}}
header="### Hook files by client\n\n| Client | Hook config | Events | Action |\n|---|---|---|---|\n"
hookrow="| Claude Code | \u0060.claude/settings.json\u0060 | \u0060PreToolUse\u0060, \u0060PostToolUse\u0060 | Move invariant checks into hooks |\n"
oldhead="### Custom command files by client\n\n| Client | Command files | What a file sets | Action |\n|---|---|---|---|\n"
oldgood="| Codex | \u0060~/.codex/prompts/\u0060 | Markdown; frontmatter \u0060description\u0060 | Migrate commands to skills |\n\n"
oldbad="| Codex | \u0060~/.codex/prompts/\u0060 | binary SQLite; required \u0060fabricatedField\u0060 | Migrate commands to skills |\n\n"
r4={"case":"old command field wholly outside this counter","changed_row":oldbad.strip(),"extracted_hook_rows_identical":m.skill_rows(oldhead+oldgood+header+hookrow)==m.skill_rows(oldhead+oldbad+header+hookrow),"extracted_hook_rows":m.skill_rows(oldhead+oldbad+header+hookrow)}
qc="a default \u0060hooks/hooks.json\u0060 file. Hooks are loaded from those installed plugin manifests in addition to: - \u0060~/.codex/hooks.json\u0060"
ctok="~/.codex/hooks.json";cevents=["PreToolUse","SessionStart"]
cs=row("S097","Codex",codex["requested"],"final "+codex["effective"]+" sha256 "+codex["sha256"])
r5={"case":"real same-client pinned-host redirect","source_row":cs,"entry_reasons":entry_reasons(cs,"S097","Codex",ctok,qc,cevents,codex["body"].encode()),"live_reasons":m.page_why(codex["body"],qc,ctok,cevents),"effective_host_pinned":m.host_ok(codex["effective"],m.HOSTS["Codex"]),"effective_is_base":m.url_key(codex["effective"]) in base_urls,"effective_is_change_note":m.url_is_change_note(codex["effective"]),"quote":qc}
print(json.dumps({"date_u":subprocess.run(["timeout","5","date","-u"],capture_output=True,text=True,check=True).stdout.strip(),"counter_sha256":m.self_sha(),"target":m.TARGET,"new_target":m.NEW_TARGET,"cases":[r1,r2,r3,r4,r5]},indent=2))
```

## Exact corrected Codex-only probe source

Its JSON stdin is the already fetched Codex metadata/body and the byte-exact 22-word quote printed in finding 3. The wrapper records the real `run_curl` result before returning it unchanged; it does not mock a redirect.
```python
import hashlib,importlib.util,json,subprocess,sys
from pathlib import Path
spec=importlib.util.spec_from_file_location("frozen_counter","verifiers/check_hook_files.py")
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
x=json.load(sys.stdin);c=x["codex"];q=x["quote"];tok="~/.codex/hooks.json";events=["PreToolUse","SessionStart"]
base=m.git_show(Path.cwd(),m.BASE,m.SOURCES);keys=m.base_url_keys(base)
source="| S097 | Codex hooks — "+c["requested"]+" | docs | A | hook configuration | final "+c["effective"]+" sha256 "+c["sha256"]+" | client hook path and events | mined | 2026-10-23 | 90d | corpus/knowledge/hook-files-round59.md |"
raw=m.run_curl;receipt=[]
def observed(url):
    when=subprocess.run(["timeout","5","date","-u"],capture_output=True,text=True,check=True).stdout.strip()
    status,final,body=raw(url)
    receipt.append({"url":url,"date_u":when,"http":status,"effective":final,"bytes":len(body),"sha256":hashlib.sha256(body).hexdigest()})
    return status,final,body
m.run_curl=observed
live=m.fetch(c["requested"],m.HOSTS["Codex"],keys)
why=m.entry_row_verdict(["Codex","\u0060"+tok+"\u0060","S097",q],"Codex",tok,m.sources_table(source),m.source_ids(base),keys,m.ws(q),m.ws(q.replace("\u0060","")),events,lambda s:c["body"].encode())[0]
print(json.dumps({"source_row":source,"quote":q,"quote_words":len(q.replace("\u0060","").split()),"quote_lines":"38-44","entry_reasons":why,"events_cell_reasons":m.events_cell_why(events),"live_reasons":m.page_why(live,q,tok,events),"requested_and_effective_url_keys_differ":m.url_key(c["requested"])!=m.url_key(c["effective"]),"effective_host_pinned":m.host_ok(c["effective"],m.HOSTS["Codex"]),"effective_is_base":m.url_key(c["effective"]) in keys,"fetch_receipt":receipt},indent=2))
```
