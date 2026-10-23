# ExecCalibBefore
role: C2 before-receipt executor; owned axis: calibration/consistency.
item: Run the five frozen C2 predicates at r62 close tip `35d44b4b4dcdda234b5dbff7af37e432fec55f05` using `/tmp` snapshots only.

## Findings

1. Frozen expectation: `plans/round-63.md:94-117` lists five checks; its per-check expected verdicts are FAIL, FAIL, FAIL, PASS, FAIL, but it declares `0 of 5`. Those five verdicts sum to **1 of 5**. Its later “0 of 5 on the four content checks” is consistent only when the vacuously passing append-only check is excluded.

2. Copied the four committed inputs from the required tip to `/tmp/kotoba-r63-exec-calib-before-35d44b4b/`:
   - `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 35d44b4b4dcdda234b5dbff7af37e432fec55f05:LOG.md > /tmp/kotoba-r63-exec-calib-before-35d44b4b/LOG.md`
   - Same command form for `.ufo/waves/round-62/C2-successor-measure.txt`, `corpus/knowledge/erratum-absorption-round62.md`, and `.ufo/waves/round-62/noharm-tip.txt`.
   - Each command exited 0 with no stdout. No lane file other than this report was written.

3. Late-write tree query, expected FAIL: `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin ls-tree -r 35d44b4b4dcdda234b5dbff7af37e432fec55f05 -- .ufo/waves/round-62/w2/FalsifyC2HonestH1.md` → no output (exit 0; zero rows). This matches `plans/round-63.md:97-98` and the spot-check at `corpus/lessons/round-62-verifier-spotcheck.md:34-37`.

4. Committed-byte inputs: copied receipt line 2 has `receipt_rev=3f911504ce76d9ca186f297d6d4a9cd8ed77508a`; `wc -lw /tmp/kotoba-r63-exec-calib-before-35d44b4b/erratum-absorption-round62.md` → `64 1044 ...`. The copied no-harm receipt has `FAIL reg_gate`, `36 of 38`, and `FAIL corpus-idx` naming `corpus/lessons/round-61-verifier-spotcheck.md` (`noharm-tip.txt:12-17`). The committed Round-62 LOG ends at its no-harm bullet (`LOG.md:2545-2566`); the target LOG is byte-identical to the copied baseline.

5. Predicate table. For checks 2–5, the command is `python3 -B /tmp/kotoba-r63-exec-calib-before-35d44b4b/check_c2_before.py --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05`; outputs below are its literal per-check lines. K is the cumulative count across all five checks.

| Check | Expected at r62 tip | Command | Real output | K of 5 |
|---|---|---|---|---:|
| `late-write-tracked` | FAIL | `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin ls-tree -r 35d44b4b4dcdda234b5dbff7af37e432fec55f05 -- .ufo/waves/round-62/w2/FalsifyC2HonestH1.md` | No rows (exit 0); probe: `late-write-tracked: FAIL; git ls-tree entries=0` | 0/5 |
| `receipt-rev-named` | FAIL | `python3 -B /tmp/kotoba-r63-exec-calib-before-35d44b4b/check_c2_before.py --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05` | `receipt-rev-named: FAIL; receipt_rev=3f911504ce76d9ca186f297d6d4a9cd8ed77508a; appended Round-62 correction line=absent` | 0/5 |
| `entry-size-named` | FAIL | `wc -lw /tmp/kotoba-r63-exec-calib-before-35d44b4b/erratum-absorption-round62.md` and the probe command above | `64 1044 /tmp/kotoba-r63-exec-calib-before-35d44b4b/erratum-absorption-round62.md`; `entry-size-named: FAIL; wc -l=64; wc -w=1044; appended Round-62 correction line=absent` | 0/5 |
| `append-only` | PASS | Probe command above; compares `git show <rev>:LOG.md` with the copied `git show 35d44b4b:LOG.md` snapshot | `append-only: PASS; base bytes=514498; rev bytes=514498; base is byte-prefix=True` | 1/5 |
| `noharm-arms-named` | FAIL | Probe command above | `noharm-arms-named: FAIL; reg_gate result='FAIL  reg_gate    expected exit 0 in both columns, got base=0 tip=1'; measure=36 of 38; corpus-idx result='FAIL  corpus-idx  tip leaves new corpus file(s) unindexed: corpus/lessons/round-61-verifier-spotcheck.md'; appended Round-62 correction line=absent` | 1/5 |

6. Full predicate-run command: `python3 -B /tmp/kotoba-r63-exec-calib-before-35d44b4b/check_c2_before.py --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05`. Real output; exit 1:
   ```text
   late-write-tracked: FAIL; git ls-tree entries=0
   receipt-rev-named: FAIL; receipt_rev=3f911504ce76d9ca186f297d6d4a9cd8ed77508a; appended Round-62 correction line=absent
   entry-size-named: FAIL; wc -l=64; wc -w=1044; appended Round-62 correction line=absent
   append-only: PASS; base bytes=514498; rev bytes=514498; base is byte-prefix=True
   noharm-arms-named: FAIL; reg_gate result='FAIL  reg_gate    expected exit 0 in both columns, got base=0 tip=1'; measure=36 of 38; corpus-idx result='FAIL  corpus-idx  tip leaves new corpus file(s) unindexed: corpus/lessons/round-61-verifier-spotcheck.md'; appended Round-62 correction line=absent
   r62 routed defects closed 1 of 5
   ```

7. Ad-hoc wording limits: checks 2–3 treat any matching appended line in the Round-62 LOG suffix as a “correction line”; they do not require an explicit correction/erratum marker. Check 5 parses and prints the full `reg_gate` and `corpus-idx` result lines, but its pass predicate requires only both identifiers and the extracted `36 of 38` on one appended line, not exact reproduction of each result line. These differences do not affect this before-state because the suffix is empty. Check 4 directly implements the byte-prefix predicate. Independently, the frozen headline is arithmetically inconsistent: counting passing check 4 yields **1 of 5**, while the four content checks alone yield **0 of 4**. I did not falsify the measured five-check count to match the stated `0 of 5`.

## Artifacts

Ad-hoc probe at `/tmp/kotoba-r63-exec-calib-before-35d44b4b/check_c2_before.py`:

```python
#!/usr/bin/env python3
import argparse
import re
import subprocess
from pathlib import Path

REPO = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
SNAP = Path("/tmp/kotoba-r63-exec-calib-before-35d44b4b")
LATE = ".ufo/waves/round-62/w2/FalsifyC2HonestH1.md"


def git_bytes(*args):
    return subprocess.run(
        ["git", "-C", REPO, *args], check=True, stdout=subprocess.PIPE
    ).stdout


def r62_suffix_lines(suffix):
    section_is_r62 = True  # BASE ends inside the Round-62 LOG entry.
    for line in suffix.decode("utf-8").splitlines():
        if line.startswith("## "):
            section_is_r62 = bool(re.search(r"\bRound 62\b", line))
        elif section_is_r62:
            yield line


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rev", required=True)
    rev = parser.parse_args().rev

    tree_rows = git_bytes("ls-tree", "-r", rev, "--", LATE).decode().splitlines()
    late_ok = bool(tree_rows)

    receipt = (SNAP / "C2-successor-measure.txt").read_text(encoding="utf-8")
    receipt_match = re.search(r"(?m)^receipt_rev=(\S+)\s*$", receipt)
    if not receipt_match:
        raise SystemExit("missing receipt_rev in copied C2 receipt")
    receipt_rev = receipt_match.group(1)

    base_log = (SNAP / "LOG.md").read_bytes()
    tip_log = git_bytes("show", f"{rev}:LOG.md")
    append_only = tip_log.startswith(base_log)
    suffix = tip_log[len(base_log):] if append_only else b""
    correction_lines = list(r62_suffix_lines(suffix))

    size_output = subprocess.run(
        ["wc", "-lw", str(SNAP / "erratum-absorption-round62.md")],
        check=True, stdout=subprocess.PIPE, text=True,
    ).stdout.split()
    line_count, word_count = int(size_output[0]), int(size_output[1])
    line_re = re.compile(rf"(?<!\d){line_count}\s+lines?\b", re.I)
    word_re = re.compile(rf"(?<!\d)(?:{word_count}|{word_count:,})\s+words?\b", re.I)
    size_ok = any(line_re.search(line) and word_re.search(line) for line in correction_lines)
    receipt_ok = any(receipt_rev in line for line in correction_lines)

    noharm = (SNAP / "noharm-tip.txt").read_text(encoding="utf-8")
    reg_line = next((line.strip() for line in noharm.splitlines()
                     if re.search(r"\breg_gate\b", line)), "MISSING")
    idx_line = next((line.strip() for line in noharm.splitlines()
                     if re.search(r"\bcorpus-idx\b", line)), "MISSING")
    reg_count_match = re.search(r"gate registry rows conformant\s+(\d+ of \d+)", noharm)
    reg_count = reg_count_match.group(1) if reg_count_match else "MISSING"
    noharm_ok = any(
        "reg_gate" in line and "corpus-idx" in line and reg_count in line
        for line in correction_lines
    ) and reg_count != "MISSING"

    checks = [late_ok, receipt_ok, size_ok, append_only, noharm_ok]
    print(f"late-write-tracked: {'PASS' if late_ok else 'FAIL'}; git ls-tree entries={len(tree_rows)}")
    print(f"receipt-rev-named: {'PASS' if receipt_ok else 'FAIL'}; receipt_rev={receipt_rev}; appended Round-62 correction line={'present' if receipt_ok else 'absent'}")
    print(f"entry-size-named: {'PASS' if size_ok else 'FAIL'}; wc -l={line_count}; wc -w={word_count}; appended Round-62 correction line={'present' if size_ok else 'absent'}")
    print(f"append-only: {'PASS' if append_only else 'FAIL'}; base bytes={len(base_log)}; rev bytes={len(tip_log)}; base is byte-prefix={append_only}")
    print(f"noharm-arms-named: {'PASS' if noharm_ok else 'FAIL'}; reg_gate result={reg_line!r}; measure={reg_count}; corpus-idx result={idx_line!r}; appended Round-62 correction line={'present' if noharm_ok else 'absent'}")
    passed = sum(checks)
    print(f"r62 routed defects closed {passed} of 5")
    return 0 if passed == 5 else 1


if __name__ == "__main__":
    raise SystemExit(main())
```

## Verdict

INFORMS — at the r62 tip the five actual predicate verdicts sum to **1 of 5** (four content checks 0/4); check 4 passes vacuously. To change this conclusion, the frozen definition must explicitly state whether K counts all five checks or only the four content checks, or a committed-byte replay must produce different per-check outcomes.
