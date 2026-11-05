import os, re, subprocess, json
from pathlib import Path
S = Path("/fast/scratch/hyaku/kotoba-r87/ScribeIndexR87")
LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin"); R = LANE / ".ufo/waves/round-87"
tracked = set(subprocess.run(["git","-C",str(LANE),"ls-files","--",".ufo/waves/round-87"],capture_output=True,text=True).stdout.split("\n"))
HEX = re.compile(r"\b[0-9a-f]{7,40}\b")
CMD = re.compile(r"(^\$ |python3 |\bbash |\bsh |git (show|rev-parse|checkout|status|diff|cat-file|log)|omp |sources-census|wc -[lc] )")
rows = []
for root, dirs, files in os.walk(R):
    for fn in files:
        p = Path(root) / fn; rel = p.relative_to(LANE)
        if rel.as_posix().startswith(".ufo/waves/round-87/w3/ScribeIndexR87/"): continue
        size = p.stat().st_size
        with open(p, "rb") as fh:
            raw = fh.read(65536)
        text = raw.decode("utf-8", "replace")
        first = next((l for l in text.splitlines() if l.strip()), "")
        first = re.sub(r"[^\x20-\x7e]", "?", first)[:110]
        hexes = []
        for m in HEX.finditer(text[:200000]):
            t = m.group(0)
            if t not in hexes: hexes.append(t)
            if len(hexes) >= 4: break
        cmds = [l.strip()[:120] for l in text.splitlines()[:400] if CMD.search(l)][:2]
        is_receipt = "/receipts/" in rel.as_posix() or fn.endswith(".txt") and "receipt" in rel.as_posix()
        rows.append({"path": rel.as_posix(), "bytes": size, "tracked": rel.as_posix() in tracked, "first": first,
                     "hex_named": hexes, "commands": cmds})
rows.sort(key=lambda r: r["path"])
json.dump(rows, open(S / "inventory.json", "w"), indent=1)
print(len(rows), "files")
for r in rows:
    print(f"{r['bytes']:>7} {'T' if r['tracked'] else 'U'} {r['path']} | {r['first'][:70]} | hex={r['hex_named'][:2]}")
