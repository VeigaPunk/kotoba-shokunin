#!/usr/bin/env python3
"""check_freeze_gate.py — execute a plan's declared pre-freeze controls and refuse
the freeze when a declared expectation cannot be observed (round-89 claim C1).

Round 88 shipped a freeze containing the control ``w_added_red`` that had never been
executed and whose declared FAIL its own predicate could not produce (F1; round-88
verifier spotcheck routed defect 3). This gate mechanizes the refusal: it parses a
plan/fixture ``## Controls`` block, executes every declared control, and compares
declared vs observed.

Frozen predicate (plans/round-89.md § C1 — the same sentence in every receipt):

    python3 -B verifiers/check_freeze_gate.py --self-test
        -> prints "0 failure(s) over N assertions" (N >= floors floor), exit 0
    python3 -B verifiers/check_freeze_gate.py --plan verifiers/fixtures/freeze-gate/r88-controls.md
        -> exit 1, refusal names "w_added_red"
    python3 -B verifiers/check_freeze_gate.py --plan verifiers/fixtures/freeze-gate/r88-controls-fixed.md
        -> exit 0

Verdict ladder: 0 = every control held (freeze may proceed); 1 = refused, naming
the first violated control with declared-vs-observed text; 2 = could-not-evaluate
(a declared command missing/not executable/timeout, or the plan file unreadable);
3 = invalid spec (a control with no command or no expectation, an orphaned expect
line, an unrecognized expect clause, an unrecognized line inside the block, or an
empty/absent Controls block).

Grammar (line-based, inside a ``## Controls`` block):

    - control <name>: <command>
      expect: exit <rc>[; stdout contains <literal>]

``exit`` and ``stdout contains`` clauses are each optional but at least one must be
present; clauses are separated by ``;``. Blank lines and ``#`` comment lines are
skipped between entries (an ATX heading — ``#`` followed by whitespace — ends the
block). The expect line must directly follow its control entry: an expect line with
no pending control is invalid, which is what kills a plan that omits a declared
control line but keeps its expectation. Any other meaningful line inside the block
is an invalid spec. The whole plan is parsed before anything runs, so an invalid
spec never executes a control.

Execution: every declared control runs with cwd = the lane root (this file's
grandparent directory), TMPDIR pointed at a fresh directory under the process
TMPDIR (or under ``--work`` when given), a per-control timeout (default 120 s,
override with ``--timeout``), and captured stdout. Shell exit codes 126/127 (not
executable / not found) and timeouts read as could-not-evaluate; a control that
runs and exits nonzero is an OBSERVED result compared against the declaration
(fail-closed simulators exit 2 on a missing receipt, which a declared
``exit 0`` then refuses). ``--verbose`` records the per-control fresh TMPDIR and
observed stdout.
"""

import argparse
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from contextlib import redirect_stdout
from pathlib import Path

CONTROL_TIMEOUT_S = 120
LANE_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_REL = Path("verifiers") / "floors-registry.json"
FIXTURE_DIR = Path("verifiers") / "fixtures" / "freeze-gate"

EXIT_PASS = 0
EXIT_REFUSED = 1
EXIT_EVAL = 2
EXIT_SPEC = 3

_HEADING = re.compile(r"^#{1,6}\s+\S")
_CONTROLS_HEADING = re.compile(r"^##\s+Controls\b")
_CONTROL_LINE = re.compile(r"^\s*-\s+control\s+([A-Za-z0-9_.-]+)\s*:\s*(.*)$")
_EXPECT_LINE = re.compile(r"^\s*expect\s*:\s*(.*)$")


class SpecError(Exception):
    """The plan's Controls block does not satisfy the frozen grammar."""


class Control:
    __slots__ = ("name", "command", "expect_rc", "expect_stdout", "line_no")

    def __init__(self, name, command, line_no):
        self.name = name
        self.command = command
        self.expect_rc = None
        self.expect_stdout = None
        self.line_no = line_no

    def declared(self):
        parts = []
        if self.expect_rc is not None:
            parts.append("exit %d" % self.expect_rc)
        if self.expect_stdout is not None:
            parts.append("stdout contains %s" % self.expect_stdout)
        return "; ".join(parts)


class Outcome:
    __slots__ = ("rc", "stdout", "stderr", "eval_reason")

    def __init__(self, rc, out, err, eval_reason):
        self.rc = rc
        self.stdout = out
        self.stderr = err
        self.eval_reason = eval_reason


def parse_expect(control, body, line_no):
    parts = [p.strip() for p in body.split(";")]
    parts = [p for p in parts if p]
    if not parts:
        raise SpecError(
            "control %s (line %d): empty expect line" % (control.name, line_no))
    for part in parts:
        m = re.fullmatch(r"exit\s+(\d+)", part)
        if m:
            control.expect_rc = int(m.group(1))
            continue
        m = re.fullmatch(r"stdout\s+contains\s+(.+)", part)
        if m:
            literal = m.group(1).strip()
            if not literal:
                raise SpecError(
                    "control %s (line %d): stdout contains an empty literal"
                    % (control.name, line_no))
            control.expect_stdout = literal
            continue
        raise SpecError(
            "control %s (line %d): unrecognized expect clause %r"
            % (control.name, line_no, part))


def parse_plan(text):
    controls = []
    saw_block = False
    in_block = False
    pending = None
    for idx, raw in enumerate(text.splitlines(), 1):
        if _CONTROLS_HEADING.match(raw):
            if pending is not None:
                raise SpecError("control %s (line %d): no expect line"
                                % (pending.name, pending.line_no))
            saw_block = True
            in_block = True
            continue
        if _HEADING.match(raw):
            if pending is not None:
                raise SpecError("control %s (line %d): no expect line"
                                % (pending.name, pending.line_no))
            in_block = False
            continue
        if not in_block:
            continue
        stripped = raw.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            continue
        m = _CONTROL_LINE.match(raw)
        if m:
            if pending is not None:
                raise SpecError("control %s (line %d): no expect line"
                                % (pending.name, pending.line_no))
            name = m.group(1)
            command = m.group(2).strip()
            if not command:
                raise SpecError("control %s (line %d): no command" % (name, idx))
            pending = Control(name, command, idx)
            controls.append(pending)
            continue
        m = _EXPECT_LINE.match(raw)
        if m:
            if pending is None:
                raise SpecError(
                    "orphaned expect line (line %d): no preceding control entry "
                    "(a declared control line was omitted)" % idx)
            parse_expect(pending, m.group(1), idx)
            pending = None
            continue
        raise SpecError(
            "unrecognized line inside ## Controls block (line %d): %r"
            % (idx, stripped))
    if pending is not None:
        raise SpecError("control %s (line %d): no expect line"
                        % (pending.name, pending.line_no))
    if not saw_block:
        raise SpecError("no ## Controls block found")
    if not controls:
        raise SpecError("empty ## Controls block")
    return controls


def _fmt_secs(value):
    text = "%s" % value
    if text.endswith(".0"):
        text = text[:-2]
    return text


def _one_line(text, cap=400):
    flat = text.replace("\n", "\\n")
    if len(flat) > cap:
        flat = flat[:cap] + "..."
    return flat


def run_control(control, timeout_s, work_root, verbose, out):
    os.makedirs(work_root, exist_ok=True)
    tmpdir = tempfile.mkdtemp(prefix="freeze-gate-", dir=work_root)
    env = dict(os.environ)
    env["TMPDIR"] = tmpdir
    if verbose:
        print("[fg] control %s tmpdir=%s" % (control.name, tmpdir), file=out)
    try:
        try:
            proc = subprocess.run(
                control.command, shell=True, cwd=str(LANE_ROOT), env=env,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                text=True, errors="replace", timeout=timeout_s)
        except subprocess.TimeoutExpired as exc:
            caught = exc.stdout
            if isinstance(caught, bytes):
                caught = caught.decode("utf-8", "replace")
            return Outcome(None, caught or "", "", "timeout after %ss" % _fmt_secs(timeout_s))
        except OSError as exc:
            return Outcome(None, "", "", "oserror: %s" % exc)
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)
    if proc.returncode == 126:
        return Outcome(126, proc.stdout, proc.stderr,
                       "command not executable (rc=126)")
    if proc.returncode == 127:
        return Outcome(127, proc.stdout, proc.stderr,
                       "command not found (rc=127)")
    return Outcome(proc.returncode, proc.stdout, proc.stderr, None)


def run_gate(plan_path, work_root=None, verbose=False, timeout_s=None, out=None):
    out = sys.stdout if out is None else out
    if timeout_s is None:
        timeout_s = CONTROL_TIMEOUT_S
    if work_root is None:
        work_root = os.environ.get("TMPDIR") or tempfile.gettempdir()
    if verbose:
        print("[fg] work_root=%s" % work_root, file=out)
    plan_path = Path(plan_path)
    try:
        text = plan_path.read_text(encoding="utf-8")
    except OSError as exc:
        print("COULD-NOT-EVALUATE: cannot read plan %s: %s" % (plan_path, exc),
              file=out)
        return EXIT_EVAL
    try:
        controls = parse_plan(text)
    except SpecError as exc:
        print("INVALID SPEC: %s" % exc, file=out)
        return EXIT_SPEC
    for control in controls:
        oc = run_control(control, timeout_s, work_root, verbose, out)
        if oc.eval_reason is not None:
            print("COULD-NOT-EVALUATE control %s (line %d): %s"
                  % (control.name, control.line_no, oc.eval_reason), file=out)
            return EXIT_EVAL
        issues = []
        if control.expect_rc is not None and oc.rc != control.expect_rc:
            issues.append("exit mismatch: declared %d, observed %s"
                            % (control.expect_rc, oc.rc))
        if control.expect_stdout is not None \
                and control.expect_stdout not in oc.stdout:
            issues.append("stdout literal %r absent from observed stdout"
                            % control.expect_stdout)
        if issues:
            print('REFUSED control %s (line %d): declared "%s"; '
                  "observed exit=%s stdout=%s (%s)"
                  % (control.name, control.line_no, control.declared(), oc.rc,
                     _one_line(oc.stdout), "; ".join(issues)), file=out)
            return EXIT_REFUSED
        if verbose:
            print("[fg] control %s rc=%s held (stdout=%s)"
                  % (control.name, oc.rc, _one_line(oc.stdout)), file=out)
    print("freeze gate: %d control(s) held — freeze may proceed" % len(controls),
          file=out)
    return EXIT_PASS


class _Parser(argparse.ArgumentParser):
    # argparse's usage errors would exit 2 and collide with the ladder's
    # could-not-evaluate rung; invalid invocations are invalid specs (exit 3).
    def error(self, message):
        self.print_usage(sys.stderr)
        print("INVALID SPEC: %s" % message, file=sys.stderr)
        sys.exit(EXIT_SPEC)


def _run_cli(args, env_extra=None):
    env = dict(os.environ)
    if env_extra:
        env.update(env_extra)
    proc = subprocess.run(
        [sys.executable, "-B", str(Path(__file__).resolve())] + list(args),
        cwd=str(LANE_ROOT), env=env,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        text=True, errors="replace", timeout=300)
    return proc.returncode, proc.stdout


def self_test(out):
    scratch = Path(tempfile.mkdtemp(
        prefix="fg-selftest-", dir=os.environ.get("TMPDIR") or None))
    failures = []

    def check(label, fn):
        try:
            fn()
        except AssertionError as exc:
            failures.append("%s: %s" % (label, exc))
        except Exception as exc:  # unexpected — still one named failing arm
            failures.append("%s: unexpected %r" % (label, exc))

    def gate(plan, **kw):
        buf = io.StringIO()
        rc = run_gate(plan, work_root=str(scratch), out=buf, **kw)
        return rc, buf.getvalue()

    def wplan(name, text):
        p = scratch / name
        p.write_text(text, encoding="utf-8")
        return p

    fixed = LANE_ROOT / FIXTURE_DIR / "r88-controls-fixed.md"
    unsat = LANE_ROOT / FIXTURE_DIR / "r88-controls.md"
    sim_healed = "bash verifiers/fixtures/freeze-gate/sim-w-healed.sh"

    def arm_floor_row():
        data = json.loads((LANE_ROOT / REGISTRY_REL).read_text(encoding="utf-8"))
        rows = data["instruments"]
        assert "freeze_gate" in rows, "floors-registry.json has no freeze_gate row"
        row = rows["freeze_gate"]
        assert row["path"] == "verifiers/check_freeze_gate.py", \
            "freeze_gate row path drifted: %r" % row["path"]
        assert row["floor"] == len(ARMS), \
            "freeze_gate floor %r != self-test assertion count %d" % (
                row["floor"], len(ARMS))

    def arm_source_tmpdir():
        src = Path(__file__).resolve().read_text(encoding="utf-8")
        assert ("/" + "tmp") not in src, "source carries a hardcoded temp literal"
        assert "TMPDIR" in src, "source never honours TMPDIR"

    def arm_plan_missing():
        rc, _ = gate(LANE_ROOT / FIXTURE_DIR / "no-such-plan.md")
        assert rc == EXIT_EVAL, "missing plan read as rc=%r" % rc

    def arm_grammar_no_block():
        rc, text = gate(wplan("no-block.md", "# a plan\nwith no controls section\n"))
        assert rc == EXIT_SPEC and "no ## Controls block" in text, (rc, text)

    def arm_grammar_empty_block():
        rc, text = gate(wplan("empty.md", "## Controls\n"))
        assert rc == EXIT_SPEC and "empty ## Controls block" in text, (rc, text)

    def arm_grammar_no_command():
        rc, text = gate(wplan(
            "nocmd.md", "## Controls\n- control broken:\n  expect: exit 0\n"))
        assert rc == EXIT_SPEC and "no command" in text, (rc, text)

    def arm_grammar_no_expect():
        rc, text = gate(wplan(
            "noexpect.md",
            "## Controls\n- control a: true\n- control b: true\n  expect: exit 0\n"))
        assert rc == EXIT_SPEC and "no expect line" in text, (rc, text)

    def arm_grammar_orphan_expect():
        rc, text = gate(wplan("orphan.md", "## Controls\n  expect: exit 0\n"))
        assert rc == EXIT_SPEC and "orphaned expect line" in text, (rc, text)

    def arm_omitted_control():
        text = fixed.read_text(encoding="utf-8").replace(
            "- control w_healed: bash verifiers/fixtures/freeze-gate/sim-w-healed.sh\n",
            "", 1)
        assert "control w_healed" not in text.split("## Controls")[1], \
            "omission arm did not remove the control line"
        rc, out2 = gate(wplan("omitted.md", text))
        assert rc == EXIT_SPEC and "orphaned expect line" in out2, (rc, out2)

    def arm_grammar_bad_clause():
        rc, text = gate(wplan(
            "badclause.md",
            "## Controls\n- control c: %s\n  expect: stderr contains x\n" % sim_healed))
        assert rc == EXIT_SPEC and "unrecognized expect clause" in text, (rc, text)

    def arm_grammar_prose_line():
        rc, text = gate(wplan(
            "prose.md",
            "## Controls\n- control d: %s\n  expect: exit 0\nthis is prose\n" % sim_healed))
        assert rc == EXIT_SPEC and "unrecognized line" in text, (rc, text)

    def arm_exit_only_expect_holds():
        rc, text = gate(wplan(
            "exitonly.md",
            "## Controls\n- control healed: %s\n  expect: exit 0\n" % sim_healed))
        assert rc == EXIT_PASS and "1 control(s) held" in text, (rc, text)

    def arm_exit_mismatch_refuses():
        rc, text = gate(wplan(
            "exitmismatch.md",
            "## Controls\n- control healed: %s\n  expect: exit 7\n" % sim_healed))
        assert rc == EXIT_REFUSED, (rc, text)
        assert "exit mismatch: declared 7, observed 0" in text, text
        assert "REFUSED control healed" in text, text

    def arm_stdout_pattern_miss():
        rc, text = gate(wplan(
            "patternmiss.md",
            "## Controls\n- control healed: %s\n"
            "  expect: exit 0; stdout contains ABSENT-FREEZE-TOKEN\n" % sim_healed))
        assert rc == EXIT_REFUSED, (rc, text)
        assert "REFUSED control healed" in text and "ABSENT-FREEZE-TOKEN" in text, text

    def arm_expectation_sign_flip():
        text = fixed.read_text(encoding="utf-8").replace(
            "- control w_tip: bash verifiers/fixtures/freeze-gate/sim-w-tip.sh\n"
            "  expect: exit 0; stdout contains D5=PASS",
            "- control w_tip: bash verifiers/fixtures/freeze-gate/sim-w-tip.sh\n"
            "  expect: exit 0; stdout contains D5=FAIL", 1)
        rc, out2 = gate(wplan("flipped.md", text))
        assert rc == EXIT_REFUSED, (rc, out2)
        assert "REFUSED control w_tip" in out2, out2
        assert 'declared "exit 0; stdout contains D5=FAIL"' in out2, out2
        assert "stdout=w_tip D5=PASS" in out2, out2

    def arm_timeout_path():
        rc, text = gate(wplan(
            "slow.md", "## Controls\n- control slow: sleep 200\n  expect: exit 0\n"),
            timeout_s=1.0)
        assert rc == EXIT_EVAL, (rc, text)
        assert "timeout after 1s" in text, text

    def arm_missing_command():
        rc, text = gate(wplan(
            "gone.md",
            "## Controls\n- control gone: verifiers/fixtures/freeze-gate/no-such-sim-xyz.sh\n"
            "  expect: exit 0\n"))
        assert rc == EXIT_EVAL, (rc, text)
        assert "rc=127" in text and "not found" in text, text

    def arm_predicate_fixed_exit0():
        rc, text = _run_cli(["--plan", str(fixed)])
        assert rc == EXIT_PASS, "fixed fixture read rc=%d: %s" % (rc, text)

    def arm_predicate_fixed_summary():
        _, text = _run_cli(["--plan", str(fixed)])
        assert "freeze gate: 4 control(s) held" in text, text

    def arm_fixed_all_held_verbose():
        _, text = _run_cli(["--plan", str(fixed), "--verbose"])
        for name in ("w_added_red", "w_silenced", "w_healed", "w_tip"):
            assert "[fg] control %s rc=0 held" % name in text, (name, text)

    def arm_fixed_observed_verdicts():
        _, text = _run_cli(["--plan", str(fixed), "--verbose"])
        for verdict in ("w_added_red D5=PASS",
                        "w_silenced D5=FAIL-world-unreachable",
                        "w_healed D5=PASS",
                        "w_tip D5=PASS"):
            assert verdict in text, (verdict, text)

    def arm_predicate_unsat_exit1():
        rc, _ = _run_cli(["--plan", str(unsat)])
        assert rc == EXIT_REFUSED, "unsatisfiable fixture read rc=%r" % rc

    def arm_unsat_names_w_added_red():
        _, text = _run_cli(["--plan", str(unsat)])
        assert "REFUSED control w_added_red" in text, text

    def arm_unsat_declared_vs_observed():
        _, text = _run_cli(["--plan", str(unsat)])
        assert 'declared "exit 0; stdout contains D5=FAIL"' in text, text
        assert "observed exit=0" in text and "D5=PASS" in text, text

    def arm_unsat_single_refusal():
        _, text = _run_cli(["--plan", str(unsat)])
        assert text.count("REFUSED control") == 1, text

    def arm_tmpdir_honoured():
        tdir = scratch / "tmproot"
        tdir.mkdir()
        rc, text = _run_cli(["--plan", str(fixed), "--verbose"],
                            env_extra={"TMPDIR": str(tdir)})
        assert rc == EXIT_PASS, (rc, text)
        assert ("[fg] work_root=%s" % tdir) in text, text
        for path in re.findall(r"tmpdir=(\S+)", text):
            assert path.startswith(str(tdir)), (path, str(tdir))

    ARMS = [
        ("arm grammar-no-block", arm_grammar_no_block),
        ("arm grammar-empty-block", arm_grammar_empty_block),
        ("arm grammar-no-command", arm_grammar_no_command),
        ("arm grammar-no-expect", arm_grammar_no_expect),
        ("arm grammar-orphan-expect", arm_grammar_orphan_expect),
        ("arm omitted-control (fixed plan minus one control line)", arm_omitted_control),
        ("arm grammar-unrecognized-clause", arm_grammar_bad_clause),
        ("arm grammar-prose-line", arm_grammar_prose_line),
        ("arm exit-only-expect holds", arm_exit_only_expect_holds),
        ("arm exit-mismatch refuses", arm_exit_mismatch_refuses),
        ("arm stdout-pattern-miss refuses", arm_stdout_pattern_miss),
        ("arm expectation-sign-flip refuses", arm_expectation_sign_flip),
        ("arm timeout-path could-not-evaluate", arm_timeout_path),
        ("arm missing-command could-not-evaluate", arm_missing_command),
        ("arm plan-missing could-not-evaluate", arm_plan_missing),
        ("arm tmpdir-honoured (verbose records the per-control TMPDIR)", arm_tmpdir_honoured),
        ("arm source-has-no-hardcoded-temp-literal", arm_source_tmpdir),
        ("arm predicate fixed-fixture exits 0", arm_predicate_fixed_exit0),
        ("arm predicate fixed-fixture summary", arm_predicate_fixed_summary),
        ("arm fixed-fixture all four controls held", arm_fixed_all_held_verbose),
        ("arm fixed-fixture observed verdicts (receipts-grounded)", arm_fixed_observed_verdicts),
        ("arm predicate r88-controls world exits 1", arm_predicate_unsat_exit1),
        ("arm unsatisfiable world names w_added_red", arm_unsat_names_w_added_red),
        ("arm unsatisfiable world declared-vs-observed text", arm_unsat_declared_vs_observed),
        ("arm unsatisfiable world single refusal (first violation wins)", arm_unsat_single_refusal),
        ("arm floors-row freeze_gate (path + floor == assertion count)", arm_floor_row),
    ]

    def make_failclosed_arm(sim_name):
        def arm():
            dst = scratch / "failclosed" / sim_name
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(LANE_ROOT / FIXTURE_DIR / sim_name, dst)
            proc = subprocess.run(["bash", str(dst)], stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE, text=True,
                                  errors="replace", timeout=60, cwd=str(scratch))
            assert proc.returncode == EXIT_EVAL, \
                "%s outside the lane read rc=%d (want 2)" % (sim_name, proc.returncode)
            assert "receipt missing" in proc.stderr, proc.stderr
        return arm

    for sim_name in ("sim-w-added-red.sh", "sim-w-silenced.sh",
                     "sim-w-healed.sh", "sim-w-tip.sh"):
        ARMS.append(("arm simulator fail-closed %s (receipt absent -> 2)" % sim_name,
                     make_failclosed_arm(sim_name)))

    for label, fn in ARMS:
        check(label, fn)

    try:
        shutil.rmtree(scratch, ignore_errors=True)
    except OSError:
        pass

    total = len(ARMS)
    if failures:
        for line in failures:
            print("FAIL %s" % line, file=out)
        print("%d failure(s) over %d assertions" % (len(failures), total), file=out)
        return EXIT_REFUSED
    print("0 failure(s) over %d assertions" % total, file=out)
    return EXIT_PASS


def main(argv):
    parser = _Parser(description=__doc__.splitlines()[0])
    parser.add_argument("--self-test", action="store_true",
                        help="run the assertion suite and print its tally")
    parser.add_argument("--plan", metavar="FILE",
                        help="execute the plan's declared ## Controls")
    parser.add_argument("--work", metavar="DIR",
                        help="root for per-control fresh TMPDIRs (default: TMPDIR)")
    parser.add_argument("--timeout", type=float, metavar="SECS",
                        default=None,
                        help="per-control timeout override (default: %ds)"
                             % CONTROL_TIMEOUT_S)
    parser.add_argument("--verbose", action="store_true",
                        help="record per-control TMPDIR and observed stdout")
    args = parser.parse_args(argv)
    if args.self_test and args.plan:
        parser.error("--self-test and --plan are mutually exclusive")
    if not args.self_test and not args.plan:
        parser.error("one of --self-test or --plan is required")
    if args.self_test:
        return self_test(sys.stdout)
    return run_gate(args.plan, work_root=args.work, verbose=args.verbose,
                    timeout_s=args.timeout)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
