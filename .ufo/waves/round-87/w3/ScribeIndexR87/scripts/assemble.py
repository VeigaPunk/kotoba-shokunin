import json, subprocess, re, os, datetime
from pathlib import Path
S = Path("/fast/scratch/hyaku/kotoba-r87/ScribeIndexR87")
LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin"); FLEET = Path("/home/vgpnk/Projects/shokunin")
TIP = subprocess.run(["git","-C",str(LANE),"rev-parse","master"],capture_output=True,text=True).stdout.strip()
inv = json.load(open(S/"inventory.json"))
inv = [r for r in inv if not r["path"].startswith(".ufo/waves/round-87/w3/ScribeIndexR87/")]
scan = json.load(open(S/"index_scan.json"))
now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
def cell(s): return str(s).replace("|", "\\|").replace("\n", " ")
def obj_kind(h):
    for repo, tag in ((LANE,"lane"),(FLEET,"fleet")):
        t = subprocess.run(["git","-C",str(repo),"cat-file","-t",h],capture_output=True,text=True)
        if t.returncode == 0: return t.stdout.strip(), tag
    return None, None
out = []
out.append(f"# Round 87 evidence index (w3, seat ScribeIndexR87)\n")
out.append(f"Snapshot: {now}. Lane `master` = `{TIP}`. Every row below was produced by a stat, a read, or a `git cat-file` at the snapshot; the tree is live (peer seats still write under `w3/`), so counts are for this snapshot only.\n")
out.append("Legend: `T` tracked at lane master, `U` untracked or modified. \"Revisions/hashes named\" lists the first hex tokens (7–40 chars) in the file; \"commands recorded\" lists the first lines that look like a command.\n")
out.append(f"## 1. Round-87 tree: {len(inv)} files\n")
out.append("| path | bytes | trk | first line | revisions/hashes named | commands recorded |")
out.append("|---|---:|:-:|---|---|---|")
for r in inv:
    hx = ", ".join(r["hex_named"][:4]) or "—"
    cm = " ; ".join(c[:90] for c in r["commands"]) or "none recorded"
    out.append(f"| `{r['path']}` | {r['bytes']} | {'T' if r['tracked'] else 'U'} | {cell(r['first'][:90])} | {cell(hx)} | {cell(cm)} |")
out.append("")
out.append("Receipt command provenance: `receipts/base-battery.txt` and `after-battery.txt` carry no command lines; their commands are the scripts `build-base-battery.sh` and `build-after-battery.sh` (in the tree). `receipts/c1-*.txt`, `c2-*.txt` and `census-after.txt` name no command; the C1 counter's own `--rev` line and the C2 PASS lines are the only provenance inside the file.\n")
# section 2
out.append("## 2. Section headings with line numbers\n")
docs = scan["docs"]
for d in ["corpus/lessons/round-87.md","plans/round-87.md","plans/round-87-addendum-1.md","plans/round-87-addendum-2.md"]:
    out.append(f"### `{d}` ({docs[d]['lines']} lines)\n")
    out.append("| line | heading |"); out.append("|---:|---|")
    for ln, h in docs[d]["headings"]:
        out.append(f"| {ln} | {cell(h)} |")
    out.append("")
# section 3
out.append("## 3. LOG.md and SCORECARD.md round-87 entries\n")
out.append("`grep -n 'Round 87' LOG.md` → 3298 (`## Round 87 — two claims`), 3351 (`### Round 87, attempt 2`). `grep -n 'Round 87' SCORECARD.md` → 601 (`## Round 87 — two claims`).\n")
b = scan["block"]
out.append(f"- LOG.md round-87 block: lines {b['LOG.md']['start']}–{b['LOG.md']['end']} (to end of file; no later `##` heading).")
out.append(f"- SCORECARD.md round-87 block: lines {b['SCORECARD.md']['start']}–{b['SCORECARD.md']['end']} (to end of file; no later `##` heading).\n")
out.append("Commit-hash resolution for every hash cited in the two blocks and in the four round documents (`git cat-file -t`, lane first then fleet; a blob is an object, not a commit):\n")
out.append("| cited at | token | object type | repo |"); out.append("|---|---|---|---|")
hash_rows = {}
for path, ln, kind, tok, st in scan["pointers"]:
    if kind != "commit": continue
    if tok not in hash_rows:
        hash_rows[tok] = obj_kind(tok)
    typ, repo = hash_rows[tok]
    out.append(f"| `{path}:{ln}` | `{tok}` | {typ or 'ABSENT'} | {repo or 'neither lane nor fleet'} |")
out.append("")
# section 4 missing evidence
out.append("## 4. Missing evidence (pointer named in a round-87 record, not on disk)\n")
out.append("| cited at | pointer text | status |"); out.append("|---|---|---|")
missing = [
 ("LOG.md:3370", "`.ufo/waves/round-87/w3/l1/census-now.txt`", "absent from the tree (dangling)"),
 ("plans/round-87.md (§ No-harm battery, Q73 sweep line)", "`receipts/q73-sweep.txt`", "absent; the sweep is a `q73_sweep` section inside `receipts/base-battery.txt` (build-base-battery.sh), so the promised separate receipt does not exist"),
 ("corpus/lessons/round-87.md:96", "`Sentinel.md` (w1 attack seat, named with `ReviewerC1.md`)", "absent: `.ufo/waves/round-87/w1/Sentinel.md` does not exist; `w1/ReviewerC1.md` does"),
 ("corpus/lessons/round-87.md:89 and plans/round-87-addendum-2.md:27", "commit `8b1cc1b00a9322cd8e231d87e015e1d75d20adc1`", "absent from lane and fleet; dangling by design and disclosed (D5 disclosure), so not a defect of the record"),
 ("plans/round-87.md:185–187 (Assimilation)", "`/home/vgpnk/Projects/shokuknow/merge/kotoba/` reported \"absent on this host\"", "PRESENT: the directory exists (MERGE-REPORT.json, MERGE-REPORT.md, SOURCES.append.md; mtime 2026-10-24T23:33), so the plan's stated premise for `Assimilation: none` is false; the lesson carries no `Assimilation:` line at all"),
]
for row in missing: out.append("| " + " | ".join(cell(x) for x in row) + " |")
out.append("")
out.append("Pointers that are not dangling but resolve only at the fleet root (not in the lane): `.ufo/l0-questions.md` (plans/round-87.md:18), `scripts/hyaku/ufo-wave-policy.json` (plans/round-87.md:195), `.ufo/watchdog.log` (LOG.md:3353), `.ufo/reports/round-84/kama.md` (lesson:61, lesson:86, addendum-2:22, LOG.md:3360, SCORECARD.md:641). The three `/home/u/proj/…` tokens at plans/round-87.md:65 are the frozen synthetic ancestor chain, not pointers, and are excluded from the count.\n")
# counts
sites = []
for path, ln, kind, tok, st in scan["pointers"]:
    if kind == "path" and tok in ("/home/u", "/home/u/proj", "/home/u/proj/sub"): continue
    sites.append((path, ln, kind, tok, st))
resolved = dangling = 0
for path, ln, kind, tok, st in sites:
    if kind == "commit":
        typ, repo = hash_rows[tok]
        if typ: resolved += 1
        else: dangling += 1
    else:
        if st in ("exists",) or tok in (".ufo/l0-questions.md","scripts/hyaku/ufo-wave-policy.json",".ufo/watchdog.log"): resolved += 1
        else: dangling += 1
manual_dangling = 2  # bare-name sites: receipts/q73-sweep.txt (plan), Sentinel.md (lesson:96)
total = resolved + dangling + manual_dangling
out.append(f"Pointer sites counted: {total} (scan {len(sites)} path/hash citation sites + 2 bare-name sites found by reading). Resolved {resolved}, dangling {dangling + manual_dangling} (of which 2 are the disclosed `8b1cc1b…` by design).\n")
out.append(f"index: {len(inv)} files, {resolved} resolved pointers, {dangling + manual_dangling} dangling")
open(LANE / ".ufo/waves/round-87/w3/ScribeIndexR87/INDEX.md","w",encoding="utf-8").write("\n".join(out) + "\n")
print("wrote INDEX.md", len(inv), "files", resolved, "resolved", dangling + manual_dangling, "dangling")
