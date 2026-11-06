#!/usr/bin/env python3
"""Build the C2 forgery/isolation worlds W1..W10 on top of the freeze commit.

Every world starts from b53e2096 and applies the same honest corpus/checklist
edits as W0, then a world-specific variation.  Scratch clone only.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

BASE = "b53e209603e7c480cd975ea543e415b66f695438"
D = Path(sys.argv[1]).resolve()
ONLY = sys.argv[2:] if len(sys.argv) > 2 else None


def sh(*args, check=True):
    p = subprocess.run(["git", "-C", str(D), *args], capture_output=True, text=True)
    if check and p.returncode != 0:
        raise SystemExit("git %s: %s" % (args, p.stderr))
    return p


def reset():
    sh("reset", "--hard", "-q", BASE)


def read(p):
    return (D / p).read_text(encoding="utf-8")


def write(p, s):
    (D / p).write_text(s, encoding="utf-8")


def commit(msg):
    sh("add", "-A")
    sh("commit", "-q", "-m", msg)
    return sh("rev-parse", "HEAD").stdout.strip()


def common(glob_row=False):
    lines = read("corpus/README.md").splitlines()
    idx = next(i for i, l in enumerate(lines) if l.startswith("| Round-98 lesson |"))
    if glob_row:
        rows = ["| Round-91..98 verifier spot-checks (indexed round 99) | "
                "`lessons/round-9*-verifier-spotcheck.md` | the non-author closures "
                "of rounds 91-98, written by the hyaku closure and never edited "
                "here; one glob row denotes all eight tracked files |"]
    else:
        rows = ["| Round-%d verifier spot-check (indexed round 99) | "
                "`lessons/round-%d-verifier-spotcheck.md` | the non-author closure "
                "of round %d, written by the hyaku closure and never edited here; "
                "indexed at round 99 so the coverage map denotes every tracked "
                "corpus file |" % (n, n, n) for n in range(91, 99)]
    lines[idx + 1:idx + 1] = rows
    write("corpus/README.md", "\n".join(lines) + "\n")
    t = read("corpus/lessons/round-81.md")
    old = "a real commit `8b1cc1b00a9322cd8e231d87e015e1d75d20adc1`"
    assert t.count(old) == 1
    write("corpus/lessons/round-81.md",
          t.replace(old, "a real `commit 8b1cc1b00a9322cd8e231d87e015e1d75d20adc1`"))
    b = json.loads(read("verifiers/corpus-baseline.json"))
    b["checks"]["corpus.index.tracked_files"]["expect"] = 203
    b["checks"]["corpus.pointers.report_total"]["expect"] = 166
    b["checks"]["corpus.pointers.commit_total"]["expect"] = 72
    b["as_of"] = "2026-11-06"
    write("verifiers/corpus-baseline.json",
          json.dumps(b, indent=1, ensure_ascii=False) + "\n")


def row(line, digest, sfile, sline, stale, corrected):
    return ('    (%d,\n     "%s",\n     "%s", %d, "%s",\n     "%s"),'
            % (line, digest, sfile, sline, stale, corrected))


def checklist(rows, horizon, force_pass=False):
    c = read("verifiers/verify_skill_checklist.py")
    assert c.count('"SCORECARD.md", 158, ".ufo/reports/round-60/kotoba.md",') == 1
    c = c.replace('"SCORECARD.md", 158, ".ufo/reports/round-60/kotoba.md",',
                  '"SCORECARD.md", 161, ".ufo/reports/round-60/kotoba.md",')
    anchor = ")\nEMPTY_SCALARS = frozenset("
    assert c.count(anchor) == 1
    c = c.replace(anchor, "\n".join(rows) + "\n" + anchor)
    assert c.count("GOVERNANCE_CORRECTIONS_HORIZON = 2723\n") == 1
    c = c.replace("GOVERNANCE_CORRECTIONS_HORIZON = 2723\n",
                  "GOVERNANCE_CORRECTIONS_HORIZON = %d\n" % horizon)
    if force_pass:
        old = '''        elif cid == "governance.citation_resolves":
            if governance_enabled:
                st, ev, detail = check_governance_citations(
                    repo, corrections=GOVERNANCE_CORRECTIONS)
            else:
                st, ev, detail = (
                    "N/A", 0,
                    "governance files are checked only with the repo SKILL.md")'''
        new = '''        elif cid == "governance.citation_resolves":
            st, ev, detail = ('PASS', 1, 'forged'); governance_enabled = False
            if governance_enabled:
                st, ev, detail = check_governance_citations(
                    repo, corrections=GOVERNANCE_CORRECTIONS)
            elif False:
                pass'''
        assert c.count(old) == 1
        c = c.replace(old, new)
    write("verifiers/verify_skill_checklist.py", c)


def append_notice(pairs):
    lines = read("LOG.md").splitlines()
    no = len(lines) + 1
    parts = ['%s:%d token "%s" -> "%s"' % (sf, sl, st, co)
             for sf, sl, st, co in pairs]
    notice = ("- **Round-99 C2 correction notice (scratch control; append-only).** "
              "Superseded citations corrected by this appended notice: "
              + "; ".join(parts) + ".")
    assert "\n" not in notice
    with (D / "LOG.md").open("a", encoding="utf-8") as fh:
        fh.write(notice + "\n")
    return no, hashlib.sha256(notice.encode("utf-8")).hexdigest()


def pin(blob=None):
    if blob is None:
        blob = sh("hash-object", "verifiers/verify_skill_checklist.py").stdout.strip()
    b = read("verifiers/check_tip_battery.py")
    anchor = '    "verifiers/verify_skill_checklist.py": (\n'
    assert b.count(anchor) == 1
    write("verifiers/check_tip_battery.py", b.replace(anchor, anchor + '        "%s",\n' % blob))
    return blob


def quote_token(path, lineno, token):
    lines = read(path).splitlines()
    i = lineno - 1
    line = lines[i]
    assert token in line, (path, lineno, token, line[:120])
    if "`%s`" % token in line:
        line = line.replace("`%s`" % token, '"%s"' % token)
    if token in line:
        line = line.replace(token, '"%s"' % token)
    lines[i] = line
    write(path, "\n".join(lines) + "\n")


RECEIPT = ".ufo/waves/round-82/receipts/before-tip-battery-win-dot.txt"
R82 = ".ufo/reports/round-82/kotoba.md"
R83 = ".ufo/reports/round-83/kotoba.md"
R84 = ".ufo/reports/round-84/kotoba.md"
R81 = ".ufo/reports/round-81/kotoba.md"
KAMA = ".ufo/reports/round-84/kama.md"
WATCH = ".ufo/watchdog.log"
L0 = ".ufo/l0-questions.md"
SPOT80 = "corpus/lessons/round-80-verifier-spotcheck.md:30,37"
DESC = "verifiers/check_description_render.py"

# (subject file, subject line, stale, corrected)
SCORECARD_DEAD = [
    ("SCORECARD.md", 186, R82, "../" + R82),
    ("SCORECARD.md", 204, R83, "../" + R83),
    ("SCORECARD.md", 222, R84, "../" + R84),
    ("SCORECARD.md", 527, ".ufo/wapes", "../.ufo/waves"),
    ("SCORECARD.md", 529, SPOT80, "corpus/lessons/round-80-verifier-spotcheck.md"),
    ("SCORECARD.md", 531, R81, "../" + R81),
    ("SCORECARD.md", 538, DESC, "verifiers/check_description_thresholds.py"),
    ("SCORECARD.md", 646, KAMA, "../" + KAMA),
]
LOG_DEAD = [
    ("LOG.md", 2881, RECEIPT, "../.ufo/waves"),
    ("LOG.md", 2947, RECEIPT, "../.ufo/waves"),
    ("LOG.md", 2958, R82, "../" + R82),
    ("LOG.md", 3353, WATCH, "../" + WATCH),
    ("LOG.md", 3360, KAMA, "../" + KAMA),
    ("LOG.md", 3512, L0, "../" + L0),
    ("LOG.md", 3561, WATCH, "../" + WATCH),
]


def w0_like(dead, pairs=None, glob_row=False, horizon=None, force_pass=False,
            do_pin=True, pin_blob=None):
    common(glob_row=glob_row)
    pairs = dead if pairs is None else pairs
    if horizon is None:
        no, digest = append_notice(pairs)
        horizon = no
    else:
        no, digest = horizon
    rows = [row(no, digest, sf, sl, st, co) for sf, sl, st, co in dead]
    checklist(rows, horizon, force_pass=force_pass)
    if do_pin:
        pin(pin_blob)
    return no, digest


def world_w1():
    dead = list(LOG_DEAD) + list(SCORECARD_DEAD)
    pairs = []
    for sf, sl, st, co in dead:
        if st == RECEIPT:
            pairs.append((sf, sl, st, "SKILL.md"))  # unrelated replacement
        else:
            pairs.append((sf, sl, st, co))
    # the rows must carry the corrected token that is on the notice line
    dead2 = [(sf, sl, st, "SKILL.md" if st == RECEIPT else co) for sf, sl, st, co in dead]
    w0_like(dead2, pairs)


def world_w2():
    # non-literal corrections block: the notice digest is computed at import
    common()
    lines = read("LOG.md").splitlines()
    no = len(lines) + 1
    parts = ['%s:%d token "%s" -> "%s"' % e for e in LOG_DEAD + SCORECARD_DEAD]
    notice = ("- **Round-99 C2 correction notice (scratch control; append-only).** "
              "Superseded citations corrected by this appended notice: "
              + "; ".join(parts) + ". (edited after the fact)")
    with (D / "LOG.md").open("a", encoding="utf-8") as fh:
        fh.write(notice + "\n")
    expr = ('__import__("hashlib").sha256(Path("LOG.md").read_text('
            'encoding="utf-8").splitlines()[%d].encode("utf-8")).hexdigest()'
            % (no - 1))
    rows = []
    for sf, sl, st, co in LOG_DEAD + SCORECARD_DEAD:
        rows.append('    (%d,\n     %s,\n     "%s", %d, "%s",\n     "%s"),'
                    % (no, expr, sf, sl, st, co))
    checklist(rows, no)
    pin()


def world_w3():
    # horizon raised past rows that do not exist
    common()
    no, digest = append_notice(LOG_DEAD + SCORECARD_DEAD)
    rows = [row(no, digest, sf, sl, st, co) for sf, sl, st, co in LOG_DEAD + SCORECARD_DEAD]
    rows.append(row(4000, "0" * 64, "LOG.md", 2881, RECEIPT, "../.ufo/waves"))
    checklist(rows, 999999)
    pin()


def world_w4():
    # INSTRUMENT_PINS entry computed by code
    common()
    no, digest = append_notice(LOG_DEAD + SCORECARD_DEAD)
    rows = [row(no, digest, sf, sl, st, co) for sf, sl, st, co in LOG_DEAD + SCORECARD_DEAD]
    checklist(rows, no)
    b = read("verifiers/check_tip_battery.py")
    anchor = '    "verifiers/verify_skill_checklist.py": (\n'
    assert b.count(anchor) == 1
    expr = ('        __import__("subprocess").check_output('
            '["git", "hash-object", "verifiers/verify_skill_checklist.py"], '
            'text=True).strip(),\n')
    write("verifiers/check_tip_battery.py", b.replace(anchor, anchor + expr))


def world_w5():
    # 11 PASS lines from a forged path, self-test still holds
    w0_like(LOG_DEAD + SCORECARD_DEAD, force_pass=True)


def world_w6():
    # one glob coverage row hides the eight unindexed files
    w0_like(LOG_DEAD + SCORECARD_DEAD, glob_row=True)


def world_w7():
    # rewrite the earlier LOG.md lines instead of appending notices for them
    for sf, sl, st, co in LOG_DEAD:
        quote_token("LOG.md", sl, st)
    w0_like(SCORECARD_DEAD)


def world_w8():
    # pin the correction rows to pre-existing LOG.md lines (no appended notice
    # for those subjects): line 2620 carries ../.ufo/watchdog.log, line 779
    # carries ../.ufo/l0-questions.md
    common()
    notice_pairs = [e for e in LOG_DEAD + SCORECARD_DEAD
                    if e[2] not in (WATCH, L0)]
    no, digest = append_notice(notice_pairs)
    rows = [row(no, digest, sf, sl, st, co) for sf, sl, st, co in notice_pairs]
    log_lines = read("LOG.md").splitlines()
    d2620 = hashlib.sha256(log_lines[2619].encode("utf-8")).hexdigest()
    d779 = hashlib.sha256(log_lines[778].encode("utf-8")).hexdigest()
    rows.append(row(2620, d2620, "LOG.md", 3353, WATCH, "../" + WATCH))
    rows.append(row(2620, d2620, "LOG.md", 3561, WATCH, "../" + WATCH))
    rows.append(row(779, d779, "LOG.md", 3512, L0, "../" + L0))
    checklist(rows, no)
    pin()


def world_w9():
    # guards isolation: the changed checklist blob is not pinned
    w0_like(LOG_DEAD + SCORECARD_DEAD, do_pin=False)


def world_w10():
    # selftests isolation: a committed self-test fixture is altered
    w0_like(LOG_DEAD + SCORECARD_DEAD)
    fx = read("verifiers/fixtures/checklist/clean/SKILL.md")
    assert "name: clean" in fx
    write("verifiers/fixtures/checklist/clean/SKILL.md",
          fx.replace("name: clean", "name: not-clean", 1))


WORLDS = {
    "W1": world_w1, "W2": world_w2, "W3": world_w3, "W4": world_w4,
    "W5": world_w5, "W6": world_w6, "W7": world_w7, "W8": world_w8,
    "W9": world_w9, "W10": world_w10,
}

out = {}
for name, fn in WORLDS.items():
    if ONLY and name not in ONLY:
        continue
    reset()
    fn()
    rev = commit(name)
    out[name] = rev
    print(name, rev)
print(json.dumps(out))
