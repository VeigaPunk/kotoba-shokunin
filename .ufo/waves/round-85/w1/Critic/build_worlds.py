#!/usr/bin/env python3
"""Build the six required attack worlds (plus W6/W7 cheapest worlds)."""
from __future__ import annotations

import json
import textwrap
from pathlib import Path

S = Path("/fast/scratch/hyaku/kotoba-r85/Critic")

CANDIDATE = (
    "Use this skill when auditing or rewriting a skill file or prompt. "
    "Triggers: \"skill file\", \"SKILL.md\", \"frontmatter description\", "
    "\"trigger words\", \"prompt craft\", \"write a skill\", \"audit this skill\", "
    "\"skill quality\". Anti-triggers: general prompt engineering for model "
    "outputs (not skill files), runtime code changes, and domain content inside "
    "a skill's reference/ tree. Sibling boundary: kagi, kake, kasegi, kengaku "
    "and kumitate own their own SKILL.md content — this skill audits and "
    "reports; fixes route to the owning lane. chousa owns the research method; "
    "kama owns endpoint verification; tameshi owns the fixture and mutation "
    "method; tsukuroi owns host package and initramfs hooks. NOT "
    "kotodama-shokunin: kotodama owns naming and language for fictional worlds "
    "despite the similar name. Note: shokunin files sit outside the omp "
    "discovery roots, so omp never reads this text."
)

TOKEN_EVAL = """label\tquery
should-trigger\tskill file
should-trigger\tSKILL.md
should-trigger\tfrontmatter description
should-trigger\ttrigger words
should-trigger\tprompt craft
should-trigger\twrite a skill
should-trigger\taudit this skill
should-trigger\tskill quality
should-not-trigger\tquality of the audio output
should-not-trigger\tfile a bug report
should-not-trigger\tdescription of the weather
should-not-trigger\tprompt the model
should-not-trigger\ttrigger a rebuild
should-not-trigger\twrite a poem
should-not-trigger\taudit the database
should-not-trigger\tfrontmatter of the book
"""

CONFORMING_EVAL = """label\tquery
should-trigger\tthe loader cuts the catalogue at a hundred characters
should-trigger\thow do I make my agent load the right instructions
should-trigger\tdecision density in dispatch prompts
should-trigger\trewrite the frontmatter so the catalogue shows the domain
should-trigger\taudit a description for the omp listing cut
should-trigger\thelp me write a skill file for my project
should-trigger\taudit this skill for trigger fidelity
should-trigger\twhat belongs in an agent definition versus an always-on file
should-not-trigger\tquality of the audio output
should-not-trigger\tfile a bug report
should-not-trigger\tdescription of the weather
should-not-trigger\tprompt the model
should-not-trigger\ttrigger a rebuild
should-not-trigger\twrite a poem
should-not-trigger\taudit the database
should-not-trigger\tfrontmatter of the book
"""

ENTRY = """# Description trigger discipline — round 85 (S213)

source: S213
verified-at: 2026-11-04
recheck: re-run verifiers/check_description_render.py after every SKILL.md description edit
locator: S213, Optimizing skill descriptions, Testing whether a description triggers / Running multiple times; registry corpus/SOURCES.md:153
quote: A should-trigger query passes if its trigger rate is above a threshold (0.5 is a reasonable default).

## Why

The router renders a fixed-width cut of the frontmatter description; the first
sentence must carry the domain inside that cut. Trigger terms belong behind an
imperative invocation and an explicit `Triggers:` clause so the full
description stays machine-auditable.
"""

PATH_EDITS = {
    "verifiers/check_substrate_pins.py": [
        ('"omp": "/home/vgpnk/.local/bin/omp.real",',
         '"omp": "/home/vgpnk/.local/bin/omp",'),
    ],
    "verifiers/verify_surfaces.py": [
        ('"omp": "/home/vgpnk/.local/bin/omp.real",',
         '"omp": "/home/vgpnk/.local/bin/omp",'),
    ],
    "verifiers/verify_harness_claims.py": [
        ('OMP_BIN = HOME / ".local/bin/omp.real"',
         'OMP_BIN = HOME / ".local/bin/omp"'),
    ],
    "verifiers/verify_harness_independent.py": [
        ('DEFAULT_OMP_BINARY = Path("/home/vgpnk/.local/bin/omp.real")',
         'DEFAULT_OMP_BINARY = Path("/home/vgpnk/.local/bin/omp")'),
    ],
}

PIN_EDITS = [
    ('  "omp_binary_sha256": "85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4",',
     '  "omp_binary_sha256": "6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f",'),
    ('  "omp_binary_mtime": "2026-10-21T20:37:24.615549837-03:00",',
     '  "omp_binary_mtime": "2026-11-01T17:11:07.281808804-03:00",'),
]


def replace_description(skill: Path, desc: str) -> None:
    lines = skill.read_text().splitlines()
    start = next(i for i, ln in enumerate(lines) if ln.startswith("description:"))
    end = start + 1
    while end < len(lines) and lines[end].startswith((" ", "\t")):
        end += 1
    wrapped = textwrap.wrap(desc, width=74, break_long_words=False,
                            break_on_hyphens=False)
    block = ["description: >"] + ["  " + w for w in wrapped]
    skill.write_text("\n".join(lines[:start] + block + lines[end:]) + "\n")


def apply(repo: Path, rel: str, edits) -> None:
    path = repo / rel
    text = path.read_text()
    for old, new in edits:
        assert old in text, (rel, old[:60])
        text = text.replace(old, new)
    path.write_text(text)


def main() -> None:
    candidate_len = len(CANDIDATE)

    # W1: candidate description only.
    replace_description(S / "W1/SKILL.md", CANDIDATE)

    # W2: candidate description + token-dump eval set.
    replace_description(S / "W2/SKILL.md", CANDIDATE)
    (S / "W2/verifiers/fixtures").mkdir(parents=True, exist_ok=True)
    (S / "W2/verifiers/fixtures/description-eval-round85.tsv").write_text(TOKEN_EVAL)

    # W3: conforming eval set + sourced entry, base description.
    (S / "W3/verifiers/fixtures").mkdir(parents=True, exist_ok=True)
    (S / "W3/verifiers/fixtures/description-eval-round85.tsv").write_text(CONFORMING_EVAL)
    (S / "W3/corpus/knowledge/description-trigger-discipline-round85.md").write_text(ENTRY)

    # W4: four omp path constants only.
    for rel, edits in PATH_EDITS.items():
        apply(S / "W4", rel, edits)

    # W5: candidate pin values, base path constants.
    apply(S / "W5", "verifiers/baseline.json", PIN_EDITS)

    # W6 (cheapest C2): the two constants the predicate reads + pin values.
    for rel in ("verifiers/check_substrate_pins.py", "verifiers/verify_surfaces.py"):
        apply(S / "W6", rel, PATH_EDITS[rel])
    apply(S / "W6", "verifiers/baseline.json", PIN_EDITS)

    # W7 (cheapest C1): candidate description + conforming eval set + entry.
    replace_description(S / "W7/SKILL.md", CANDIDATE)
    (S / "W7/verifiers/fixtures").mkdir(parents=True, exist_ok=True)
    (S / "W7/verifiers/fixtures/description-eval-round85.tsv").write_text(CONFORMING_EVAL)
    (S / "W7/corpus/knowledge/description-trigger-discipline-round85.md").write_text(ENTRY)

    print(json.dumps({"candidate_chars": candidate_len,
                      "token_eval_rows": TOKEN_EVAL.count("\n") - 1,
                      "conforming_eval_rows": CONFORMING_EVAL.count("\n") - 1},
                     indent=1))


if __name__ == "__main__":
    main()
