#!/usr/bin/env python3
"""Kb81S14WaveRegistry generator: index every round-81 w1 seat report and build file."""
import json, re, os, sys, subprocess, datetime, hashlib

LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
WAVE = LANE + "/.ufo/waves/round-81"
W1 = WAVE + "/w1"
BUILD = WAVE + "/build"
SNAP = WAVE + "/snapshots"
DISP = WAVE + "/dispositions"
REC = WAVE + "/receipts"

GROUPS = {
 "C1": ["Kb81E01Integrity","Kb81E02Independent","Kb81E03ExtManifest","Kb81E04Baseline",
        "Kb81E05Erratum","Kb81E06Controls","Kb81E10Battery","Kb81E11Receipts",
        "Kb81E14PinAudit","Kb81E15Order","Kb81S15FreezeShas","Kb81L01Grammar",
        "Kb81L03Pointer","Kb81R02TipRecon","Kb81R05FleetCheck","Kb81C01C1",
        "Kb81V01C1","Kb81M01Instruments","Kb81M02Battery"],
 "C2": ["Kb81E07C2Worlds","Kb81E08C2Entry","Kb81E09C2Counter","Kb81S11GateQuotes",
        "Kb81R01NegSweep","Kb81R03ReopenS248","Kb81C02C2","Kb81V02C2","Kb81M03C2"],
 "frontier": ["Kb81S01Lesson","Kb81S02Log","Kb81S03Scorecard","Kb81S04Report",
        "Kb81S05SourcesEdits","Kb81S06Shonen","Kb81S07Quality","Kb81S08ReadmeRows",
        "Kb81S09SkillRule","Kb81S10Province","Kb81S12AssimDisp","Kb81S13L0",
        "Kb81S14WaveRegistry","Kb81S16CensusLog","Kb81S17ReceiptIndex",
        "Kb81E12Census","Kb81E16Shokuknow","Kb81R04SiblingScan","Kb81R07ClosureLearn",
        "Kb81R08SourcesAudit","Kb81K01Overlap","Kb81K02Patterns","Kb81K03Considerthese"],
 "attack": ["Kb81C03Residual","Kb81C04Honesty","Kb81C05Closure","Kb81L02Ctl",
        "Kb81V03Instruments","Kb81V04Gates","Kb81V05Report","Kb81Z01Sec",
        "Kb81M04Registry","Kb81N01Sentinel","Kb81Y01Simplify","Kb81G01Revenge",
        "Kb81E13FixtureGuard"],
}

SHARED = {  # build file -> owning seat(s)
 "run-battery.sh": "Kb81E10Battery",
 "refresh-corpus-baseline.py": "Kb81E04Baseline",
 "base-battery": "Kb81E10Battery",
 "c1_controls.py": "Kb81E06Controls",
 "c1_controls.txt": "Kb81E06Controls",
 "c2_controls.py": "Kb81E07C2Worlds",
 "c2_controls.txt": "Kb81E07C2Worlds",
 "check_sdk_allowed_tools.py": "Kb81E09C2Counter / Kb81E07C2Worlds",
 "allowed-tools-sdk-round81.md": "Kb81E08C2Entry",
 "Kb81R03Reopen-fetch.json": "Kb81R03ReopenS248",
}

PREFIX_SHARED = [
 ("c1_controls", "Kb81E06Controls"),
 ("c2_controls", "Kb81E07C2Worlds"),
]

SKIP_BOILER = re.compile(r"^(seat:|lane:|base:|date:|round:|author:|wave:)", re.I)

def oneline(text, limit=150):
    for ln in text.splitlines():
        s = ln.strip()
        if not s or s in ("```", "---", "==="):
            continue
        s = re.sub(r"\s+", " ", s)
        return s[:limit] + ("..." if len(s) > limit else "")
    return ""

def summarize(path):
    name = os.path.basename(path)
    if os.path.isdir(path):
        kids = sorted(os.listdir(path))
        n = sum(len(f) for _, _, f in os.walk(path))
        shown = ", ".join(kids[:6]) + (" ..." if len(kids) > 6 else "")
        return f"directory, {n} file(s): {shown}"
    try:
        raw = open(path, "rb").read()
    except Exception as e:
        return f"UNREADABLE ({e.__class__.__name__})"
    if len(raw) > 400_000:
        raw = raw[:400_000]
    try:
        txt = raw.decode("utf-8", "replace")
    except Exception:
        return f"binary, {len(raw)} B"
    ext = os.path.splitext(name)[1].lower()
    if ext == ".patch":
        paths = re.findall(r"^diff --git a/(\S+) b/\S+$", txt, re.M)
        files = len(paths)
        uniq = []
        for p in paths:
            if p not in uniq:
                uniq.append(p)
        return f"{files} file diff(s): " + (", ".join(uniq) if uniq else oneline(txt, 100))
    if ext in (".py", ".sh"):
        m = re.search(r'"""(.*?)"""', txt, re.S)
        if m:
            return "script: " + re.sub(r"\s+", " ", m.group(1)).strip()[:140]
        for ln in txt.splitlines():
            if ln.startswith("#!"):
                continue
            s = ln.strip()
            if s.startswith("#") and len(s) > 3:
                return "script: " + s.lstrip("# ")[:140]
            if s and not s.startswith("#"):
                break
        return "script: " + oneline(txt, 120)
    if ext == ".json":
        try:
            d = json.loads(txt)
        except Exception:
            return "invalid JSON: " + oneline(txt, 120)
        if isinstance(d, list):
            keys = sorted({k for o in d if isinstance(o, dict) for k in o})
            return f"JSON array, {len(d)} entr(y/ies), fields {','.join(keys[:8])}"
        if isinstance(d, dict):
            return f"JSON object, keys {','.join(list(d)[:8])}"
        return "JSON scalar"
    # md / txt
    for ln in txt.splitlines():
        s = ln.strip()
        if s.startswith("#"):
            return re.sub(r"\s+", " ", s.lstrip("# "))[:150]
    for ln in txt.splitlines():
        s = ln.strip()
        if not s or SKIP_BOILER.match(s):
            continue
        return re.sub(r"\s+", " ", s)[:150]
    return "empty"

def mt(p):
    try:
        return datetime.datetime.fromtimestamp(os.path.getmtime(p)).strftime("%H:%M:%S")
    except OSError:
        return "-"

def limit_line():
    return 190

def verdict(seat):
    p = os.path.join(W1, seat + ".md")
    if not os.path.exists(p):
        return None, None, 0
    txt = open(p, encoding="utf-8", errors="replace").read()
    m = re.search(r"^VERDICT:\s*(.+)$", txt, re.M)
    v = m.group(1).strip() if m else "(no VERDICT: line)"
    title = ""
    for ln in txt.splitlines():
        if ln.startswith("# "):
            title = ln[2:].strip()
            break
    return v, title, os.path.getsize(p)


CONFLICTS = [
 ("Kb81E11Receipts", "with one plan disagreement: the independent gate reads `report_dead 0` at base, not 1"),
 ("Kb81K02Patterns", "Plan's independent-gate base premise is wrong (report_dead 0 measured, not 1)"),
 ("Kb81R08SourcesAudit", "S230's anchor is verifiably wrong (hash is mistral-vibe's head, not pi-mono's — supersede via S250 per rule 2, never rewrite)"),
 ("Kb81K03Considerthese", "the plan's C1 kill-rule controls (W8 as written, citing-repo forgery, lane-authored manifest), the E6 headroom arithmetic and the S230/S231 receipt pointer need fixing before freeze"),
 ("Kb81K03Considerthese", "C2 should promote S248 rather than add a duplicate S249"),
 ("Kb81C04Honesty", "claims admissible after six pre-freeze corrections"),
 ("Kb81S02Log", "three source conflicts reported unmodified (31-vs-32 W04, pi-mono head moved, base exit code not receipted)"),
]

def render_conflicts():
    rows, bad = [], []
    for seat, quote in CONFLICTS:
        p = os.path.join(W1, seat + ".md")
        if not os.path.exists(p):
            rows.append((seat, "PENDING", quote, "report absent"))
            continue
        lines = open(p, encoding="utf-8", errors="replace").read().splitlines()
        hit = next((i + 1 for i, ln in enumerate(lines) if quote in ln), None)
        if hit is None:
            bad.append((seat, quote))
            rows.append((seat, "-", quote, "QUOTE-NOT-FOUND"))
        else:
            rows.append((seat, f"L{hit}", quote, "verbatim"))
    return rows, bad

def main():
    spec = json.load(open(WAVE + "/w1-spec.json"))
    items = {it["name"]: it for it in spec["items"]}
    build_files = sorted(os.listdir(BUILD)) if os.path.isdir(BUILD) else []
    reports = {f[:-3] for f in os.listdir(W1) if f.endswith(".md")} if os.path.isdir(W1) else set()
    snaps = sorted(os.listdir(SNAP)) if os.path.isdir(SNAP) else []
    disps = sorted(os.listdir(DISP)) if os.path.isdir(DISP) else []
    recs = sorted(os.listdir(REC)) if os.path.isdir(REC) else []

    # attribute build files
    owned = {s: [] for s in items}
    orphan = []
    seat_names = sorted(items, key=len, reverse=True)
    stem = {}
    for sn in items:
        stem.setdefault(sn[:7], []).append(sn)
    stem = {k: v[0] for k, v in stem.items() if len(v) == 1}
    for f in build_files:
        if f == "__pycache__" or f.endswith(".pyc"):
            continue
        hit = next((sn for sn in seat_names if f.startswith(sn)), None) or stem.get(f[:7])
        if hit:
            owned[hit].append(f)
        elif next((sn for p, sn in PREFIX_SHARED if f.startswith(p)), None):
            owned[next(sn for p, sn in PREFIX_SHARED if f.startswith(p))].append(f)
        elif f in SHARED:
            for s in SHARED[f].split(" / "):
                if s in owned:
                    owned[s].append(f)
        else:
            orphan.append(f)

    grouped = [s for g in GROUPS.values() for s in g]
    assert sorted(grouped) == sorted(items), (
        "grouping mismatch; missing=%s extra=%s" %
        (sorted(set(items) - set(grouped)), sorted(set(grouped) - set(items))))
    assert len(grouped) == len(set(grouped)), "duplicate seat in GROUPS"
    n_rep = len([s for s in items if s in reports])
    out = []
    A = out.append
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    A("# Kb81S14WaveRegistry — round-81 w1 wave evidence index")
    A("")
    A(f"Seat: Kb81S14WaveRegistry (leaf scribe, wave evidence index). Generated: {ts}.")
    A(f"Scope: `plans/round-81.md` wave w1 (`kotoba-r81-w1`, 64 seats), base `b284223105f4d106f7e8f56ed4fd296c643cda0e`.")
    A("Index of every seat report (`w1/<Seat>.md`) and every build/snapshot/disposition/receipt artifact present at generation")
    A("time. Expected-but-absent seat = `PENDING`. Summaries are the artifact's own first heading/line (one line); verdicts are")
    A("the seat report's own `VERDICT:` line, quoted — this index adds no judgment and scores no after-value.")
    A("")
    try:
        head = subprocess.run(["git", "-C", LANE, "rev-parse", "--short=8", "HEAD"],
                              capture_output=True, text=True, timeout=15).stdout.strip() or "-"
    except Exception:
        head = "-"
    A(f"Lane HEAD read at generation (read-only): `{head}`. The wave dir `.ufo/waves/round-81/` is untracked at that")
    A("commit; the L1 is the only committer and reconciles this index at integration.")
    A("")
    A(f"Counts at generation: reports **{n_rep}/64** · build files **{len(build_files)}** · snapshots **{len(snaps)}** · "
      f"dispositions **{len(disps)}** · receipts **{len(recs)}**.")
    A("")
    A("Lane-relative paths: `w1/` = `.ufo/waves/round-81/w1/`, `build/` = `.ufo/waves/round-81/build/`, "
      "`snapshots/` = `.ufo/waves/round-81/snapshots/`, `dispositions/` = `.ufo/waves/round-81/dispositions/`, "
      "`receipts/` = `.ufo/waves/round-81/receipts/`.")
    A("")

    for gname, seats in GROUPS.items():
        present = [s for s in seats if s in reports]
        A(f"## {gname} — {len(seats)} seat(s), {len(present)} report(s) landed")
        A("")
        A("| Seat | Role | Report | Artifacts | One-line content | Seat verdict |")
        A("|---|---|---|---|---|---|")
        for s in seats:
            role = items[s]["role"] if s in items else "?"
            v, title, size = verdict(s)
            if v is None:
                rep = "PENDING"
                summ = "PENDING (no build output yet)" if not owned.get(s) else "PENDING report; build outputs present"
                verd = "PENDING"
            else:
                rep = f"`w1/{s}.md` ({size} B)"
                summ = title or summarize(os.path.join(W1, s + ".md"))
                verd = v
            arts = owned.get(s, [])
            art_cell = "<br>".join(f"`build/{a}`" for a in arts) if arts else "—"
            summ = summ.replace("|", "/")
            verd = verd.replace("|", "/")
            if len(verd) > 260:
                verd = verd[:257] + "..."
            A(f"| {s} | {role} | {rep} | {art_cell} | {summ} | {verd} |")
        A("")
        # per-artifact one-liners
        rows = []
        for s in seats:
            for a in owned.get(s, []):
                p = os.path.join(BUILD, a)
                sz = (sum(len(f) for _, _, f in os.walk(p)) if os.path.isdir(p) else os.path.getsize(p))
                rows.append((f"`build/{a}`", s, f"{sz} B", summarize(p)))
        if rows:
            A(f"### {gname} build artifacts — {len(rows)} file(s)")
            A("")
            A("| Artifact | Owning seat | Size | mtime | One-line content |")
            A("|---|---|---|---|---|")
            for a, s, sz, sm in rows:
                A(f"| {a} | {s} | {sz} | {mt(os.path.join(BUILD, a[7:-1]))} | {sm.replace('|', '/')} |")
            A("")

    if orphan:
        A(f"## Unattributed build files — {len(orphan)}")
        A("")
        A("| Artifact | Size | mtime | One-line content |")
        A("|---|---|---|---|")
        for a in orphan:
            p = os.path.join(BUILD, a)
            A(f"| `build/{a}` | {os.path.getsize(p)} B | {mt(p)} | {summarize(p).replace('|', '/')} |")
        A("")

    junk = [f for f in build_files if f == "__pycache__" or f.endswith(".pyc")]
    if junk:
        A("## Hygiene observations (not seat deliverables)")
        A("")
        for j in junk:
            A(f"- `build/{j}` — bytecode cache written into the wave build dir "
              f"(mtime {mt(os.path.join(BUILD, j))}); a seat byproduct, reported not removed by this index.")
        A("")

    A("## Freeze state (quoted from `.ufo/waves/round-81/receipts/freeze-shas.txt`)")
    A("")
    fz = os.path.join(REC, "freeze-shas.txt")
    if not os.path.exists(fz):
        A("- `receipts/freeze-shas.txt` — PENDING (absent at generation).")
    else:
        txt = open(fz, encoding="utf-8", errors="replace").read().splitlines()
        keep = [ln.strip() for ln in txt if re.search(r"LINE_CAP|base-spent|Plan freeze commit|post-image blob|pin-table membership", ln)]
        for ln in keep:
            A(f"> {ln}")
            A(">")
        A(f"sha256: `{hashlib.sha256(open(fz,'rb').read()).hexdigest()}` ({os.path.getsize(fz)} B).")
    A("")

    # disposition files carried only inside patches
    disp_refs = []
    for f in build_files:
        if not f.endswith(".patch"):
            continue
        for ln in open(os.path.join(BUILD, f), encoding="utf-8", errors="replace"):
            m = re.search(r"^diff --git a/(\.ufo/waves/round-81/dispositions/\S+) b/", ln)
            if m:
                disp_refs.append((m.group(1), f))
    if disp_refs:
        A("### Disposition files carried inside patches (absent on disk until integrated)")
        A("")
        A("| Target path | Carried by | On disk now |")
        A("|---|---|---|")
        for p, f in sorted(set(disp_refs)):
            A(f"| `{p}` | `build/{f}` | {'yes' if os.path.exists(os.path.join(LANE, p)) else 'no — PENDING'} |")
        A("")

    A("## Snapshots / dispositions / receipts")
    A("")
    A("| Artifact | Size | mtime | One-line content |")
    A("|---|---|---|---|")
    for base, lst, pre in ((SNAP, snaps, "snapshots"), (DISP, disps, "dispositions"), (REC, recs, "receipts")):
        for f in lst:
            p = os.path.join(base, f)
            sz = os.path.getsize(p) if os.path.isfile(p) else sum(len(x) for _, _, x in os.walk(p))
            A(f"| `{pre}/{f}` | {sz} B | {mt(p)} | {summarize(p).replace('|', '/')} |")
    A("")

    rows, bad = render_conflicts()
    if bad:
        raise SystemExit("CONFLICT QUOTES NOT FOUND VERBATIM: %r" % (bad,))
    A("## Conflicts / pre-freeze corrections flagged by seats (verbatim, not adjudicated)")
    A("")
    A("Quotes verified byte-for-byte against the named report at generation time; absence of a seat here is not evidence")
    A("that it raised nothing (see its verdict in the tables above).")
    A("")
    A("| Seat | Report line | Verbatim quote | Check |")
    A("|---|---|---|---|")
    for seat, line, quote, chk in rows:
        A(f"| {seat} | {line} | {quote.replace('|', '/')} | {chk} |")
    A("")

    A("## Integration inputs (what the L1 applies to the lane tree)")
    A("")
    patches = sorted(f for f in build_files if f.endswith(".patch"))
    if patches:
        A(f"- Patches ({len(patches)}): " + ", ".join(f"`build/{p}`" for p in patches) + ".")
    else:
        A("- Patches: PENDING (none published at generation).")
    cand = [("Kb81E03ExtManifest.json", "`verifiers/external-commits.json` (candidate manifest)"),
            ("allowed-tools-sdk-round81.md", "`corpus/knowledge/allowed-tools-sdk-round81.md` (C2 entry)"),
            ("check_sdk_allowed_tools.py", "`verifiers/check_sdk_allowed_tools.py` (C2 counter)"),
            ("refresh-corpus-baseline.py", "baseline re-record tool, run against the lane"),
            ("run-battery.sh", "reusable no-harm battery runner")]
    A("")
    A("| Candidate tree file | Destination (per seat spec) | Present |")
    A("|---|---|---|")
    for f, dest in cand:
        A(f"| `build/{f}` | {dest} | {'yes' if f in build_files else 'PENDING'} |")
    A("")

    A("## Coverage ledger")
    A("")
    missing = [s for g in GROUPS.values() for s in g if s not in reports]
    A(f"- Seats with a report: {n_rep}/64 (per-group landed counts in the section headings above).")
    A(f"- PENDING seats ({len(missing)}): {', '.join(missing) if missing else 'none'}.")
    A("- Seat verdicts above are quotations of the seat's own report trailer; the L1 reconciles at integration.")
    A("")
    A("VERDICT: wave index generated; see counts and PENDING ledger above.")
    A("DELIVERABLES: " + BUILD + "/Kb81S14WaveRegistry.md")
    open(BUILD + "/Kb81S14WaveRegistry.md", "w").write("\n".join(out) + "\n")
    print(f"wrote {BUILD}/Kb81S14WaveRegistry.md: reports {n_rep}/64, build {len(build_files)}, orphan {len(orphan)}")

if __name__ == "__main__":
    main()
