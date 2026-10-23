# ExecCalibInstrument
role: executor
item: Propose `verifiers/check_r63_routed_repairs.py` source for frozen C2; write only this report.

## Findings

1. `plans/round-63.md:97-109` names the five computed predicates and their source paths. The proposed source follows these checks; it does not widen them.
2. Command: `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 35d44b4b4dcdda234b5dbff7af37e432fec55f05:.ufo/waves/round-62/C2-successor-measure.txt`.
   Output token: `receipt_rev=3f911504ce76d9ca186f297d6d4a9cd8ed77508a`.
3. Command: `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 35d44b4b4dcdda234b5dbff7af37e432fec55f05:.ufo/waves/round-62/noharm-tip.txt`.
   Receipt output: `FAIL  reg_gate`; `tip: gate registry rows conformant 36 of 38 lane verifiers; phantom 0`; `FAIL  corpus-idx`. The parser keys on `reg_gate`, `corpus-idx`, and the measured `36 of 38`.
4. Command: `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 35d44b4b4dcdda234b5dbff7af37e432fec55f05:corpus/knowledge/erratum-absorption-round62.md | wc -l -w`.
   Output: `64 1044` (64 lines; 1,044 words).
5. Command: `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin ls-tree -r 35d44b4b4dcdda234b5dbff7af37e432fec55f05 -- .ufo/waves/round-62/w2/FalsifyC2HonestH1.md; status=$?; printf 'exit=%s\n' "$status"`.
   Output: no tree entry; `exit=0`. The plan records the path as untracked at base (`plans/round-63.md:17-19`). Base LOG blob: `git rev-parse 35d44b4b4dcdda234b5dbff7af37e432fec55f05:LOG.md` → `d075c3fab3718e6506894e3590cfaebd1f2416ac`. Per L1's pre-data erratum, check 4 reports both prefix and appended-line conjuncts: base has prefix equality but zero added lines, so it fails honestly.
6. The spot-check names the routed corrections at `corpus/lessons/round-62-verifier-spotcheck.md:159-175`; item 1 is tracked separately from the LOG citation and no-harm corrections. No tools were installed; no gates or self-tests were run.

## Artifacts

Proposed complete source (not written to the lane production path):

```python
#!/usr/bin/env python3
"""Computed counter for round 62's five routed defects."""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
BASE_REV = "35d44b4b4dcdda234b5dbff7af37e432fec55f05"
LATE = ".ufo/waves/round-62/w2/FalsifyC2HonestH1.md"
MEASURE = ".ufo/waves/round-62/C2-successor-measure.txt"
NOHARM = ".ufo/waves/round-62/noharm-tip.txt"
ENTRY = "corpus/knowledge/erratum-absorption-round62.md"
LOG = "LOG.md"
ARMS = ("reg_gate", "corpus-idx")

@dataclass(frozen=True)
class Result:
    name: str
    passed: bool
    evidence: str

def git_bytes(repo: Path, *args: str) -> tuple[bytes | None, str]:
    try:
        p = subprocess.run(["git", "-C", str(repo), *args], stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE, timeout=10, check=False)
    except subprocess.TimeoutExpired:
        return None, "timeout"
    except OSError as exc:
        return None, type(exc).__name__
    if p.returncode:
        return None, f"git-exit-{p.returncode}"
    return p.stdout, "ok"

def show(repo: Path, rev: str, path: str) -> tuple[bytes | None, str]:
    return git_bytes(repo, "show", f"{rev}:{path}")

def wc_counts(data: bytes) -> tuple[int, int] | None:
    try:
        p = subprocess.run(["wc", "-l", "-w"], input=data, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE, timeout=10, check=False)
    except (OSError, subprocess.TimeoutExpired):
        return None
    fields = p.stdout.split()
    if p.returncode or len(fields) < 2:
        return None
    try:
        return int(fields[0]), int(fields[1])
    except ValueError:
        return None

def correction_lines(base_log: bytes | None, log: bytes | None) -> list[str]:
    if base_log is None or log is None or not log.startswith(base_log):
        return []
    lines = log.decode("utf-8", "replace").splitlines()
    added_from = len(base_log.decode("utf-8", "replace").splitlines())
    heading = re.compile(r"^(#{1,6})[ \t]+")
    start = next((i for i, line in enumerate(lines)
                  if heading.match(line) and re.search(r"\bround[ -]*62\b", line, re.I)), None)
    if start is None:
        return []
    level = len(heading.match(lines[start]).group(1))
    end = len(lines)
    for i in range(start + 1, len(lines)):
        match = heading.match(lines[i])
        if match and len(match.group(1)) <= level:
            end = i
            break
    return [line for i, line in enumerate(lines) if added_from <= i < end
            and start < i and re.search(r"\b(?:correction|corrected)\b", line, re.I)]

def has_label(line: str, label: str) -> bool:
    return re.search(r"(?<![A-Za-z0-9_-])" + re.escape(label) +
                     r"(?![A-Za-z0-9_-])", line) is not None

def states_count(line: str, count: int, unit: str) -> bool:
    forms = {str(count), f"{count:,}"}
    return any(re.search(r"(?<!\d)" + re.escape(form) + r"(?!\d)\s+" +
                         unit + r"\b", line, re.I) for form in forms)


def evaluate(repo: Path, rev: str, base_rev: str = BASE_REV) -> list[Result]:
    tree, tree_err = git_bytes(repo, "ls-tree", "-r", rev, "--", LATE)
    receipt, _ = show(repo, rev, MEASURE)
    noharm, _ = show(repo, rev, NOHARM)
    entry, entry_err = show(repo, rev, ENTRY)
    log, log_err = show(repo, rev, LOG)
    base_log, base_err = show(repo, base_rev, LOG)
    corrections = correction_lines(base_log, log)

    rows = tree.decode("utf-8", "replace").splitlines() if tree is not None else []
    tree_token = rows[0].split("\t", 1)[0].replace(" ", ":") if rows else ("missing" if tree is not None else tree_err)
    results = [Result("late-write-tracked", bool(rows), f"tree={tree_token}")]

    token_match = re.search(rb"(?m)^receipt_rev=([0-9a-fA-F]{40})[ \t]*$", receipt or b"")
    receipt_rev = token_match.group(1).decode("ascii") if token_match else "missing"
    named_rev = receipt_rev != "missing" and any(re.search(rf"(?<![0-9a-fA-F]){re.escape(receipt_rev)}(?![0-9a-fA-F])", line) for line in corrections)
    results.append(Result("receipt-rev-named", named_rev,
                          f"receipt_rev={receipt_rev};correction={'named' if named_rev else 'missing'}"))

    counts = wc_counts(entry) if entry is not None else None
    if counts is None:
        size_ok, size_token = False, f"wc={entry_err if entry is None else 'unavailable'}"
    else:
        lines_n, words_n = counts
        size_ok = any(states_count(line, lines_n, "lines") and
                      states_count(line, words_n, "words") for line in corrections)
        size_token = f"wc_l={lines_n};wc_w={words_n};correction={'both' if size_ok else 'missing'}"
    results.append(Result("entry-size-named", size_ok, size_token))

    if base_log is None or log is None:
        prefix, added = False, 0
        append_token = f"base={base_err};log={log_err}"
    else:
        prefix = log.startswith(base_log)
        suffix = log[len(base_log):] if prefix else b""
        added = len(suffix.splitlines())
        append_token = f"prefix={'yes' if prefix else 'no'};appended_lines={added}"
    results.append(Result("append-only", prefix and added >= 1, append_token))

    text = noharm.decode("utf-8", "replace") if noharm is not None else ""
    present = [arm for arm in ARMS if re.search(
        r"(?im)^\s*(?:PASS|FAIL)\s+" + re.escape(arm) + r"(?=\s|$)", text)]
    gate = re.search(r"(?i)gate registry rows conformant\s+(\d+)\s+of\s+(\d+)\s+lane verifiers", text)
    gate_pair = (int(gate.group(1)), int(gate.group(2))) if gate else None
    named_arms = len(present) == len(ARMS)
    noharm_ok = named_arms and gate_pair is not None and any(
        all(has_label(line, arm) for arm in ARMS) and
        re.search(r"(?<!\d)" + str(gate_pair[0]) + r"\s+of\s+" +
                  str(gate_pair[1]) + r"(?!\d)", line)
        for line in corrections)
    gate_token = f"{gate_pair[0]}_of_{gate_pair[1]}" if gate_pair else "missing"
    results.append(Result("noharm-arms-named", noharm_ok,
                          f"arms={','.join(present) or 'missing'};measure={gate_token};"
                          f"correction={'named' if noharm_ok else 'missing'}"))
    return results


def emit(results: list[Result]) -> int:
    for result in results:
        print(f"{result.name} {'PASS' if result.passed else 'FAIL'} evidence={result.evidence}")
    passed = sum(result.passed for result in results)
    print(f"r62 routed defects closed {passed} of 5")
    return passed


def git_mut(repo: Path, *args: str) -> bytes:
    p = subprocess.run(["git", "-C", str(repo), *args], stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE, timeout=10, check=False)
    if p.returncode:
        raise RuntimeError(f"git-exit-{p.returncode}")
    return p.stdout


def self_test() -> int:
    receipt_rev = "a" * 40
    entry = b"alpha beta\ngamma delta\n"
    base_log = b"## 2026-10-23 - Round 62\nOriginal entry.\n"
    with tempfile.TemporaryDirectory(prefix="r63-routed-") as tmp:
        repo = Path(tmp) / "repo"
        repo.mkdir()
        try:
            git_mut(repo, "init", "--quiet")
            git_mut(repo, "config", "user.name", "Counter self-test")
            git_mut(repo, "config", "user.email", "self-test@example.invalid")
            for path, data in {
                MEASURE: f"receipt_rev={receipt_rev}\n".encode(),
                NOHARM: (b"FAIL  reg_gate\n tip: gate registry rows conformant 36 of 38 lane verifiers; phantom 0\n"
                         b"FAIL  corpus-idx\n"),
                ENTRY: entry,
                LOG: base_log,
            }.items():
                target = repo / path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
            git_mut(repo, "add", "-A")
            git_mut(repo, "commit", "--quiet", "-m", "unrepaired fixture")
            base = git_mut(repo, "rev-parse", "HEAD").decode().strip()
            print("self-test unrepaired:")
            bad = emit(evaluate(repo, base, base))

            line_count, word_count = wc_counts(entry)
            report = repo / LATE
            report.parent.mkdir(parents=True, exist_ok=True)
            report.write_text("H1 fixture\n", encoding="utf-8")
            log_path = repo / LOG
            log_path.write_bytes(log_path.read_bytes() + (
                f"- Appended correction: receipt_rev={receipt_rev}; entry size "
                f"{word_count:,} words / {line_count:,} lines; interim reds "
                "reg_gate 36 of 38 and corpus-idx.\n").encode())
            git_mut(repo, "add", "-A")
            git_mut(repo, "commit", "--quiet", "-m", "repaired fixture")
            tip = git_mut(repo, "rev-parse", "HEAD").decode().strip()
            print("self-test repaired:")
            good = emit(evaluate(repo, tip, base))
        except (OSError, RuntimeError, subprocess.TimeoutExpired, TypeError) as exc:
            print(f"self-test setup failed: {type(exc).__name__}", file=sys.stderr)
            return 1
    passed = bad == 0 and good == 5
    print(f"self-test: unrepaired={bad}/5; repaired={good}/5; {'PASS' if passed else 'FAIL'}")
    return 0 if passed else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--rev", help="full 40-hex commit id to measure")
    group.add_argument("--self-test", action="store_true", help="exercise both fixture directions")
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    if re.fullmatch(r"[0-9a-fA-F]{40}", args.rev or "") is None:
        parser.error("--rev must be a full 40-hex commit id")
    return 0 if emit(evaluate(LANE, args.rev)) == 5 else 1


if __name__ == "__main__":
    raise SystemExit(main())
```

## Verdict
PROPOSES — the full source is provided above for L1 integration; production paths remain untouched. Need change my mind only if the integrated check diverges from the frozen computed predicates or an independent counterexample shows a false status. Risks: `receipt_rev` and no-harm figures are consistency-checked against bytes at the same target revision, not independently authenticated; the frozen check 1 only proves the late-write path is tracked, not that its H1 bound was incorporated. No blockers to the scoped proposal.
