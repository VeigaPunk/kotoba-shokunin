import json, os, subprocess, sys

D = "/tmp/k72w1-ExecIndexBaseline.dew8/ctl"
INT = os.path.join(D, "verifiers", "verify_corpus_integrity.py")
IND = os.path.join(D, "verifiers", "verify_corpus_independent.py")
TARGET = os.path.join(D, "corpus", "lessons", "ctl.md")

CASES = [
    ("A real truncated id (the r71 file's shape)", "ref: commit `955ffd5d\u2026`\n"),
    ("B six hex + ellipsis", "ref: commit `955ffd\u2026`\n"),
    ("C bytes after the ellipsis", "ref: commit `955ffd5d\u2026x`\n"),
    ("D word + ellipsis", "ref: commit `round-99\u2026`\n"),
    ("E plant_b's exact token (fault harness b)", "ref: commit `round-99`\n"),
    ("F eight hex, no ellipsis", "ref: commit `955ffd5d`\n"),
    ("G quoted truncated id", 'ref: "commit `955ffd5d\u2026`"\n'),
]

for label, body in CASES:
    with open(TARGET, "w", encoding="utf-8") as fh:
        fh.write(body)
    subprocess.run(["git", "-C", D, "add", "-A"], check=True,
                   capture_output=True)
    a = subprocess.run([sys.executable, "-B", INT, "--repo", D,
                        "--no-baseline", "--json"],
                       capture_output=True, text=True)
    b = subprocess.run([sys.executable, "-B", IND, "--repo", D, "--json"],
                       capture_output=True, text=True)
    oa = json.loads(a.stdout)["observed"]["corpus"] if a.stdout.strip() else {}
    ob = json.loads(b.stdout)["observed"]["commits"] if b.stdout.strip() else {}
    print("%-44s integrity exit=%d nonhash=%s truncated=%s unresolvable=%s "
          "quoted=%s | independent exit=%d nonhash=%s truncated=%s "
          "citations=%s unresolvable=%s quoted=%s"
          % (label, a.returncode, oa.get("commit_nonhash"),
             oa.get("commit_truncated"), oa.get("commit_unresolvable"),
             oa.get("commit_quoted_excluded"), b.returncode,
             ob.get("commit_nonhash"), ob.get("commit_truncated"),
             ob.get("commit_total"), ob.get("commit_unresolvable"),
             ob.get("commit_quoted")))
    if not a.stdout.strip() or not b.stdout.strip():
        print("  STDERR int:", a.stderr[-300:], "| ind:", b.stderr[-300:])
