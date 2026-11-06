import importlib.util, json, shutil, sys, tempfile
from pathlib import Path
SRC = Path(sys.argv[1])
def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
h = load(SRC, "h")
root = Path(tempfile.mkdtemp(prefix="proof-"))
try:
    proof = root / "proof"; fx = proof / "fixtures" / "dispatch-prompts"
    fx.mkdir(parents=True); (proof / "verifiers").mkdir(parents=True)
    skill_src = SRC.parent.parent / h.SKILL_NAME
    (proof / h.SKILL_NAME).write_text(skill_src.read_text(encoding="utf-8"), encoding="utf-8")
    cases = h._proof_fixture_corpus(fx)
    (fx / "manifest.json").write_text(json.dumps({"schema": "kotoba-dispatch-fixtures-v1", "cases": cases, "note": "probe"}), encoding="utf-8")
    def write_map(disp=None, sha=None):
        bm = {"schema": "kotoba-checklist-map-v1", "boxes": [
            {"box_id": cid, "section": "Dispatch-prompt fidelity checklist",
             "text_sha256": (sha or {}).get(cid, h.PINNED_BOX_SHA[cid]),
             "disposition": (disp or {}).get(cid, "delegated:" + h.DELEGATION_TARGET)}
            for cid in h.CHECK_IDS]}
        mp = proof / "verifiers" / h.BASELINE_NAME
        mp.write_text(json.dumps(bm, indent=2, sort_keys=True), encoding="utf-8")
        return mp
    mp = write_map()
    print("honest base proof rc", h.box_proof(mp, fx))
    # t04: a non-delegation disposition
    mp4 = write_map(disp={"dispatch.04": "executed:somebody-else"})
    print("t04 honest rc", h.box_proof(mp4, fx))
    text = SRC.read_text(encoding="utf-8")
    a, b = '        if entry.get("disposition") != want:', '        if entry.get("disposition") is None:'
    assert text.count(a) == 1
    m4 = load(root / "m4.py", "m4") if False else None
    (root / "m4.py").write_text(text.replace(a, b), encoding="utf-8")
    m4 = load(root / "m4.py", "m4")
    print("t04 mutant rc", m4.box_proof(mp4, fx))
    # t05: a reworded live dispatch.04 box
    skill = (proof / h.SKILL_NAME).read_text(encoding="utf-8")
    assert "Report path is literal" in skill
    (proof / h.SKILL_NAME).write_text(skill.replace("Report path is literal", "Report path is literal-ish", 1), encoding="utf-8")
    mp5 = write_map()
    print("t05 honest rc", h.box_proof(mp5, fx))
    a5, b5 = "        if live.get(cid) != pinned:", "        if live.get(cid) is None:"
    assert text.count(a5) == 1
    (root / "m5.py").write_text(text.replace(a5, b5), encoding="utf-8")
    m5 = load(root / "m5.py", "m5")
    print("t05 mutant rc", m5.box_proof(mp5, fx))
finally:
    shutil.rmtree(root, ignore_errors=True)
