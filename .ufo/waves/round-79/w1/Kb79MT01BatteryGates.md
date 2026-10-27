Axes: consistency, calibration, operability.

Scratch: clone of lane at `2c56622375641193a03bb97c0624e6536f3dffba`; validated clone top-level. Scratch removed by trap. Base gate outputs (commands run with `--repo <clone>` where supported): integrity exit 1, `4/9 checks pass`; independent exit 1, `unindexed=6` and `exit 1`; registry `--rev HEAD` exit 1, `60 of 62` conformant; checklist (this clone path as repo) exit 1 due name-directory mismatch plus citation-resolution failures. These base failures make any binary pass/fail mutation judgment inconclusive; they are not kills. The checklist clone-path error is a fixture artifact. No tip-battery invocation was possible as a meaningful count probe: the counter requires committed measured bytes, and no mutations were committed; therefore each battery-count effect is unmeasured.

Observed integrity probe commands, exact summary outputs:
- pristine: `python3 -B <clone>/verifiers/verify_corpus_integrity.py --repo <clone>` → exit 1, `4/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed, corpus.pointers.report_total, corpus.pointers.report_dead, corpus.pointers.commit_total`.
- Append coverage row promising `missing-ghost.md` to `corpus/README.md` → same exit and summary as pristine (inconclusive, baseline already red; not adjudicated as survivor).
- Append `.ufo/reports/round-79/nope.md` pointer to non-author lesson `corpus/knowledge/anatomy-and-compression.md` → same exit and summary (inconclusive; expected report-dead diagnostic not seen in aggregate because baseline state masks discrimination; further JSON-level per-observation compare not performed).
- Append `commit `abcdef0123456789abcdef0123456789abcdef01`` to that lesson → exit 1, summary adds `corpus.pointers.commit_unresolvable`, 3/9 pass. This is a detected semantic defect despite already-red gate (fault arm works).
- “Reordered” control attempted as byte-identical replacement of an existing README token (thus it was not an actual reordered-equivalent world) → same output; invalid control, do not count.
- CRLF-rewrapped `LOG.md` → same output; no drift attributable to this formatting change.

The assigned 4–6 mutations per gate and 3 valid semantics-preserving controls were not completed: per-file findings from the brief probe do not establish full mutation coverage. No conclusions about the independent gate, registry gate, or checklist governance subcheck's mutation sensitivity beyond their actual baseline outputs. Outputs are direct command captures from this scratch run; no tests or other runtime invoked.

VERDICT: INCONCLUSIVE overall (baseline gates are red); nonresolving commit mutation was detected, while other probes were not adequately adjudicated. Battery-count effects unmeasured.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/w1/Kb79MT01BatteryGates.md
