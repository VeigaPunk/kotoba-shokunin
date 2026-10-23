# ExecAbsorbInstrument — round 62 C1

Date: 2026-10-23. Scope: draft and measure the arm-level erratum matrix. The lane remained read-only except for this exclusive report; `verifiers/check_erratum_absorption.py`, the counter, fleet/sibling state, and jj/git metadata were not written. The complete source deliverable for `verifiers/check_erratum_absorption.py` is below.

## Frozen counter identity and functions used

Command:

```sh
date -u '+%Y-%m-%dT%H:%M:%SZ'; sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py
```

Output, 2026-10-23T21:00:26Z; exit code 0:

```text
2026-10-23T21:00:26Z
5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91  /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py
```

The digest matches the r61 pin. The draft hashes the sibling counter before `importlib.util.spec_from_file_location`, rechecks the imported module's `self_sha()`, and exits 2 on either mismatch. The actual tested import was the pinned lane file through a scratch-only sibling symlink; `python3 -B` prevented bytecode writes.

Exact counter arm signatures read before drafting:

```python
def url_key(url: str | None) -> str: ...
def reopen_why(row: list[str], url: str, key: str | None,
               base_rows: dict[str, list[str]],
               base_lines: dict[str, str]) -> list[str]: ...
def render_form(url: str) -> tuple[str, str, bool]: ...
def alias_why(url: str, others: list[tuple[str, str]]) -> list[str]: ...
def alias_sha_why(sha: str, base_shas: dict[str, str],
                  teaches: str | None) -> list[str]: ...
def a1_conjunct(client: str, key: str | None,
                keys: dict[str, frozenset[str]]) -> list[str]: ...
def path_value(text: str) -> bool: ...
def path_site(lines: list[str], L: int, key: str | None) -> bool: ...
def scope_conjunct(lines: list[str], key: str | None,
                   L: int | None) -> list[str]: ...
def action_conjunct(lines: list[str], cell: str, L: int | None,
                    page_text: str | None = None) -> list[str]: ...
```

The exact admitting replacements used in-process were: E2 `url_key = lambda url: "//x" if url else ""`; E2b `render_form = lambda url: ("", "", False)`; E2c `alias_sha_why = lambda *args, **kwargs: []`; E2e both `a1_conjunct = lambda *args, **kwargs: []` and `path_value = lambda text: True`; E2f `action_conjunct = lambda *args, **kwargs: []`. The original module attributes are restored in `finally`; the frozen counter file is never changed.

## Measurement

Command:

```sh
date -u '+%Y-%m-%dT%H:%M:%SZ' && python3 -B /fast/scratch/hyaku/kotoba-r62/KotobaR62.ExecAbsorbInstrument/verifiers/check_erratum_absorption.py --self-test
```

Output, 2026-10-23T20:59:31Z; exit code 0:

```text
2026-10-23T20:59:31Z
counter sha256 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91
instances per direction: committed attacks 10; guard-disabled 10 per sweep (50 total); controls 4 committed + 4 disabled; content variant 2
guard flips: E2 2; E2b 2; E2c 0; E2e 0; E2f 0
errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2
survivor E2c e2c-wrong-supersedes-target: []
survivor E2c e2c-supersedes-with-fresh-fetch: []
survivor E2e e2e-negated-path-key: []
survivor E2e e2e-commented-equals-key: []
survivor E2f e2f-backticked-event-claim: []
survivor E2f e2f-compound-purpose-outside-citation: []
EXIT_CODE=0
```

The two seed controls scored as required: two rejected URL-mismatch instances became accepted under the E2 URL-key stub; two canonical URL-key reopens remained accepted before and after. Each of the five guard-disabled sweeps scored all ten matrix instances; every off-diagonal class verdict vector stayed unchanged. For E2c/E2e/E2f, both committed instances already pass, so their disabled directions are recorded as zero flips and do not count as kills. No class was replaced or relabeled based on the observed counts. The expected verdict annotations are part of the frozen instance catalogue; the emitted K/N values are computed from the arm calls.

The content-variant arm changes only E2's first instance URL from `https://h.example/b` to the named base URL `https://h.example/a.md`; the actual arm result changes from reject to accept. The same-ID label auditor returns the same verdict for both values and fails this arm. The constant-printing hollow auditor is rejected as lacking run records; a reject-only auditor with no mutation observations is rejected for missing the disabled direction. These are bounded checks against those particular shortcuts, not universal guarantees against arbitrary replacement programs.

No matrix instance or seeded control was skipped. The prediction about an E2f survivor count is not an output gate: the observed per-instance reasons and computed summary are printed unchanged. No live fetch, seven-world counter run, C2 check, build, lint, or other test was requested or run here.

## Full source deliverable

Target path: `verifiers/check_erratum_absorption.py`

```python
#!/usr/bin/env python3
"""Measure round-62 C1 erratum arms against the pinned r61 counter."""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import importlib.util
import sys
from dataclasses import dataclass
from pathlib import Path
from types import ModuleType
from typing import Callable, Iterator

COUNTER_SHA256 = "5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91"
COUNTER_PATH = Path(__file__).resolve().with_name("check_scoped_rules.py")


class CounterPinMismatch(Exception):
    pass


class MatrixFailure(Exception):
    pass


@dataclass(frozen=True)
class Attack:
    ident: str
    score: Callable[[ModuleType], list[str]]
    expected_rejected: bool
    variant_score: Callable[[ModuleType], list[str]] | None = None
    variant_expected_rejected: bool | None = None


@dataclass(frozen=True)
class GroupObservation:
    ids: tuple[str, ...]
    reasons: tuple[tuple[str, ...], ...]


@dataclass(frozen=True)
class ControlObservation:
    before: GroupObservation
    after: GroupObservation


@dataclass(frozen=True)
class MatrixRun:
    baseline: dict[str, GroupObservation]
    mutations: dict[str, dict[str, GroupObservation]]
    controls: dict[str, ControlObservation]


@dataclass(frozen=True)
class Survivor:
    erratum: str
    ident: str
    reasons: tuple[str, ...]


@dataclass(frozen=True)
class Summary:
    measured: int
    absorbed: int
    flips: dict[str, int]
    survivors: tuple[Survivor, ...]
    controls: int


@dataclass(frozen=True)
class Erratum:
    name: str
    attacks: tuple[Attack, ...]
    patches: tuple[tuple[str, Callable], ...]


def load_counter(path: Path) -> ModuleType:
    """Pin bytes before importing the frozen counter by file path."""
    sys.dont_write_bytecode = True
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != COUNTER_SHA256:
        raise CounterPinMismatch(
            "counter sha256 mismatch: expected %s; got %s" %
            (COUNTER_SHA256, digest))
    assert digest == COUNTER_SHA256
    spec = importlib.util.spec_from_file_location("check_scoped_rules_frozen", path)
    if spec is None or spec.loader is None:
        raise MatrixFailure("could not create importlib loader for %s" % path)
    counter = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(counter)
    module_digest = counter.self_sha()
    if module_digest != COUNTER_SHA256:
        raise CounterPinMismatch(
            "imported counter self_sha mismatch: expected %s; got %s" %
            (COUNTER_SHA256, module_digest))
    assert module_digest == COUNTER_SHA256
    return counter


def _reopen_score(counter: ModuleType, url: str) -> list[str]:
    row = ["S900", "x", "docs", "A", "s", "a",
           "re-opens S010 — fresh re-open", "mined", "2026-10-23", "90d", "y"]
    base_rows = {"S010": ["S010", "https://h.example/a.md"]}
    base_lines = {"S010": "| S010 | https://h.example/a.md | no key |"}
    # Exercise the normalizer directly and through reopen_why.
    counter.url_key(url)
    return counter.reopen_why(row, url, None, base_rows, base_lines)


def reopen_attack(ident: str, url: str, expected_rejected: bool,
                  variant_url: str | None = None,
                  variant_expected_rejected: bool | None = None) -> Attack:
    def score(counter: ModuleType) -> list[str]:
        return _reopen_score(counter, url)

    variant_score = None
    if variant_url is not None:
        def variant(counter: ModuleType) -> list[str]:
            return _reopen_score(counter, variant_url)
        variant_score = variant
    return Attack(ident, score, expected_rejected, variant_score,
                  variant_expected_rejected)


def alias_attack(ident: str, url: str, base_url: str) -> Attack:
    others = [("S043", base_url)]

    def score(counter: ModuleType) -> list[str]:
        counter.render_form(url)
        for _sid, other in others:
            counter.render_form(other)
        return counter.alias_why(url, others)

    return Attack(ident, score, True)


def sha_attack(ident: str, sha: str, sid: str, teaches: str) -> Attack:
    base_shas = {sha: sid}

    def score(counter: ModuleType) -> list[str]:
        return counter.alias_sha_why(sha, base_shas, teaches)

    return Attack(ident, score, False)


def key_attack(ident: str, line: str) -> Attack:
    lines = [line]
    keys = {"Claude Code": frozenset({"paths"})}

    def score(counter: ModuleType) -> list[str]:
        reasons = counter.a1_conjunct("Claude Code", "paths", keys)
        reasons.extend(counter.scope_conjunct(lines, "paths", 1))
        return reasons

    return Attack(ident, score, False)


def action_attack(ident: str, lines: list[str], cell: str,
                  page_text: str | None = None) -> Attack:
    def score(counter: ModuleType) -> list[str]:
        return counter.action_conjunct(lines, cell, 1, page_text)

    return Attack(ident, score, False)


# Frozen instance catalogue: verdict predictions belong to these data rows,
# not to the scorer. The content variant below changes only the E2 URL value.
ERRATA = (
    Erratum(
        "E2",
        (
            reopen_attack("e2-url-unrelated-path", "https://h.example/b", True,
                          "https://h.example/a.md", False),
            reopen_attack("e2-url-different-document", "https://h.example/c", True),
        ),
        (("url_key", lambda url: "//x" if url else ""),),
    ),
    Erratum(
        "E2b",
        (
            alias_attack("e2b-locale-rendering", "https://h.example/de/a",
                         "https://h.example/a"),
            alias_attack("e2b-version-rendering", "https://h.example/v@1/a",
                         "https://h.example/a"),
        ),
        (("render_form", lambda url: ("", "", False)),),
    ),
    Erratum(
        "E2c",
        (
            sha_attack("e2c-wrong-supersedes-target", "ab" * 32, "S043",
                       "supersedes S096 — wrong source"),
            sha_attack("e2c-supersedes-with-fresh-fetch", "cd" * 32, "S048",
                       "supersedes S048 — fetched 2026-10-23T12:00:00Z"),
        ),
        (("alias_sha_why", lambda *args, **kwargs: []),),
    ),
    Erratum(
        "E2e",
        (
            key_attack("e2e-negated-path-key",
                       "Do not use paths: src/legacy/**/*.ts"),
            key_attack("e2e-commented-equals-key",
                       "# paths=src/legacy/**/*.ts"),
        ),
        (
            ("a1_conjunct", lambda *args, **kwargs: []),
            ("path_value", lambda text: True),
        ),
    ),
    Erratum(
        "E2f",
        (
            action_attack(
                "e2f-backticked-event-claim",
                ["When agent reads file runtime emits event and loads matching rule files."],
                "When agent reads file runtime emits event and loads matching rule files "
                "`InstructionsLoaded`.",
                "When agent reads file runtime emits event and loads matching rule files."),
            action_attack(
                "e2f-compound-purpose-outside-citation",
                ["The configuration stores project rules using glob syntax."],
                "The configuration stores project rules using glob syntax and secretly "
                "uploads files.",
                "The configuration stores project rules using glob syntax.\n\n"
                "## Unrelated section\nThe agent secretly uploads files."),
        ),
        (("action_conjunct", lambda *args, **kwargs: []),),
    ),
)


def control_pairs() -> dict[str, tuple[Attack, ...]]:
    return {
        "absorbed-control": (
            reopen_attack("control-absorbed-path-b", "https://h.example/b", True),
            reopen_attack("control-absorbed-path-c", "https://h.example/c", True),
        ),
        "surviving-control": (
            reopen_attack("control-surviving-md-drop", "https://h.example/a", False),
            reopen_attack("control-surviving-query-fragment",
                           "https://h.example/a.md?ref=seed#section", False),
        ),
    }


def score_one(counter: ModuleType, attack: Attack,
              scorer: Callable[[ModuleType, Attack], list[str]]) -> tuple[str, ...]:
    reasons = scorer(counter, attack)
    if not isinstance(reasons, list) or any(not isinstance(item, str) for item in reasons):
        raise MatrixFailure("%s returned a non-list or non-string reason" % attack.ident)
    return tuple(reasons)


def real_scorer(counter: ModuleType, attack: Attack) -> list[str]:
    return attack.score(counter)


def label_scorer(_counter: ModuleType, attack: Attack) -> list[str]:
    """Deliberately wrong auditor: classify by fixture label, not counter behavior."""
    return ["label-only rejection"] if attack.ident.startswith("e2") else []


def score_group(counter: ModuleType, attacks: tuple[Attack, ...],
                scorer: Callable[[ModuleType, Attack], list[str]]) -> GroupObservation:
    return GroupObservation(
        tuple(attack.ident for attack in attacks),
        tuple(score_one(counter, attack, scorer) for attack in attacks),
    )


@contextlib.contextmanager
def patched(counter: ModuleType,
           replacements: tuple[tuple[str, Callable], ...]) -> Iterator[None]:
    previous: dict[str, object] = {}
    try:
        for name, replacement in replacements:
            previous[name] = getattr(counter, name)
            setattr(counter, name, replacement)
        yield
    finally:
        for name, original in reversed(tuple(previous.items())):
            setattr(counter, name, original)


def run_matrix(counter: ModuleType,
               scorer: Callable[[ModuleType, Attack], list[str]] = real_scorer,
               execute_mutations: bool = True) -> MatrixRun:
    baseline = {
        erratum.name: score_group(counter, erratum.attacks, scorer)
        for erratum in ERRATA
    }
    if not execute_mutations:
        # This is the reject-only fake auditor: it never runs the admitting direction.
        return MatrixRun(baseline, {}, {})

    mutations: dict[str, dict[str, GroupObservation]] = {}
    for target in ERRATA:
        with patched(counter, target.patches):
            mutations[target.name] = {
                erratum.name: score_group(counter, erratum.attacks, scorer)
                for erratum in ERRATA
            }

    controls: dict[str, ControlObservation] = {}
    for name, attacks in control_pairs().items():
        before = score_group(counter, attacks, scorer)
        with patched(counter, ERRATA[0].patches):
            after = score_group(counter, attacks, scorer)
        controls[name] = ControlObservation(before, after)
    return MatrixRun(baseline, mutations, controls)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise MatrixFailure(message)


def validate_run(run: object) -> MatrixRun:
    if not isinstance(run, MatrixRun):
        raise MatrixFailure("auditor supplied a label/constant, not arm-level run records")
    names = {erratum.name for erratum in ERRATA}
    require(set(run.baseline) == names, "baseline did not measure exactly five errata")
    for erratum in ERRATA:
        expected_ids = tuple(attack.ident for attack in erratum.attacks)
        observation = run.baseline[erratum.name]
        require(observation.ids == expected_ids and len(observation.reasons) == 2,
                "%s did not run its two frozen instances" % erratum.name)
    require(set(run.mutations) == names,
            "guard-mutation direction is missing for one or more errata")
    for target in ERRATA:
        changed = run.mutations[target.name]
        require(set(changed) == names, "%s mutation did not rescore every class" % target.name)
        for erratum in ERRATA:
            expected_ids = tuple(attack.ident for attack in erratum.attacks)
            observation = changed[erratum.name]
            require(observation.ids == expected_ids and len(observation.reasons) == 2,
                    "%s mutation omitted %s instances" % (target.name, erratum.name))
    require(set(run.controls) == {"absorbed-control", "surviving-control"},
            "both seeded controls were not run in both directions")
    for name, observation in run.controls.items():
        expected_ids = tuple(attack.ident for attack in control_pairs()[name])
        require(observation.before.ids == expected_ids and
                observation.after.ids == expected_ids and
                len(observation.before.reasons) == 2 and
                len(observation.after.reasons) == 2,
                "%s did not score both seeded instances in both directions" % name)
    return run


def verdicts(observation: GroupObservation) -> tuple[bool, ...]:
    return tuple(bool(reasons) for reasons in observation.reasons)


def summarize(raw_run: object) -> Summary:
    run = validate_run(raw_run)
    for target in ERRATA:
        changed = run.mutations[target.name]
        for other in ERRATA:
            if other.name != target.name:
                require(verdicts(changed[other.name]) == verdicts(run.baseline[other.name]),
                        "%s guard mutation changed %s verdicts" % (target.name, other.name))

    absorbed = 0
    flips: dict[str, int] = {}
    survivors: list[Survivor] = []
    for erratum in ERRATA:
        before = run.baseline[erratum.name]
        after = run.mutations[erratum.name][erratum.name]
        # The disabled direction is vacuous for any pair not rejected twice.
        flips[erratum.name] = (
            sum(bool(old) and not bool(new)
                for old, new in zip(before.reasons, after.reasons))
            if all(before.reasons) else 0
        )
        if all(before.reasons) and all(not reasons for reasons in after.reasons):
            absorbed += 1
        for ident, reasons in zip(before.ids, before.reasons):
            if not reasons:
                survivors.append(Survivor(erratum.name, ident, reasons))

    absorbed_control = run.controls["absorbed-control"]
    survivor_control = run.controls["surviving-control"]
    control_results = (
        all(absorbed_control.before.reasons) and
        all(not reasons for reasons in absorbed_control.after.reasons),
        all(not reasons for reasons in survivor_control.before.reasons) and
        all(not reasons for reasons in survivor_control.after.reasons),
    )
    return Summary(len(run.baseline), absorbed, flips, tuple(survivors),
                   sum(control_results))


def variant_attack(attack: Attack) -> Attack:
    require(attack.variant_score is not None and
            attack.variant_expected_rejected is not None,
            "%s has no frozen content variant" % attack.ident)
    return Attack(attack.ident, attack.variant_score,
                  attack.variant_expected_rejected)


def check_content_variant(counter: ModuleType,
                          scorer: Callable[[ModuleType, Attack], list[str]]) -> None:
    variants = [attack for erratum in ERRATA for attack in erratum.attacks
                if attack.variant_score is not None]
    require(len(variants) == 1, "frozen catalogue must contain one content variant")
    original = variants[0]
    alternative = variant_attack(original)
    original_reasons = score_one(counter, original, scorer)
    variant_reasons = score_one(counter, alternative, scorer)
    require(bool(original_reasons) == original.expected_rejected,
            "content-variant original differs from its frozen expected verdict")
    require(bool(variant_reasons) == alternative.expected_rejected,
            "content variant differs from its frozen expected verdict")
    require(bool(original_reasons) != bool(variant_reasons),
            "changing the frozen URL input did not change the arm verdict")


def hollow_label_auditor() -> str:
    """A print-only auditor: returns the claimed line without scoring any arm."""
    return "errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2"


def self_test(counter: ModuleType) -> Summary:
    run = run_matrix(counter)
    summary = summarize(run)
    require(summary.measured == 5, "not all five erratum classes were measured")
    require(summary.controls == 2, "seeded controls did not classify in both directions")
    check_content_variant(counter, real_scorer)

    # A hollow label/constant cannot be accepted as a run, even if its text looks right.
    try:
        summarize(hollow_label_auditor())
    except MatrixFailure:
        pass
    else:
        raise MatrixFailure("hollow label auditor unexpectedly passed")

    # A label table keyed by instance ID misses the same-ID content variant.
    try:
        check_content_variant(counter, label_scorer)
    except MatrixFailure:
        pass
    else:
        raise MatrixFailure("label auditor passed the content-variant arm")

    # A reject-only instrument that omits mutation observations fails closed.
    try:
        summarize(run_matrix(counter, execute_mutations=False))
    except MatrixFailure:
        pass
    else:
        raise MatrixFailure("reject-only-without-mutation auditor unexpectedly passed")
    return summary


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)
    if not args.self_test:
        parser.error("--self-test is required")
    try:
        counter = load_counter(COUNTER_PATH)
        summary = self_test(counter)
    except CounterPinMismatch as exc:
        print(str(exc), file=sys.stderr)
        return 2
    except (MatrixFailure, OSError, ImportError, AttributeError) as exc:
        print("absorption self-test failed: %s" % exc, file=sys.stderr)
        return 1

    attack_instances = sum(len(erratum.attacks) for erratum in ERRATA)
    control_instances = sum(len(pair) for pair in control_pairs().values())
    print("counter sha256 %s" % COUNTER_SHA256)
    print("instances per direction: committed attacks %d; guard-disabled %d per sweep "
          "(%d total); controls %d committed + %d disabled; content variant 2" %
          (attack_instances, attack_instances,
           attack_instances * len(ERRATA), control_instances, control_instances))
    print("guard flips: " + "; ".join("%s %d" % (name, summary.flips[name])
                                      for name in (e.name for e in ERRATA)))
    print("errata measured %d of 5; absorbed %d of 5; surviving %d; controls %d of 2" %
          (summary.measured, summary.absorbed, len(summary.survivors), summary.controls))
    for survivor in summary.survivors:
        print("survivor %s %s: %s" %
              (survivor.erratum, survivor.ident, list(survivor.reasons)))
    if summary.measured != 5 or summary.controls != 2:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

## Files, risks, blockers

Files changed: this exclusive report only. The named verifier source is delivered in full above, but was not created in the read-only lane. No attack instance or seeded control was unrun. The sampled fixed instances and single content variant only falsify the specific hollow/label/reject-only shortcuts exercised here; they are not a claim of general adversarial resistance or Q47 non-fixed-equivalent coverage. No install/update was made.

Blockers: none.

Produced the full C1 absorption-instrument source draft and measured its five-class, two-direction matrix against the pinned counter.
