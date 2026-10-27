# M03MutFloors — r76 instrumentation mutation probe

Scope: scratch-copy mutation testing of `check_assertion_floors.py` + `floors-registry.json` D4 floors (250, 47), the assertion-floors pin in `check_tip_battery.py`, and the multi-entry used-by arm in `check_skill_evals_v2.py`.

Scratch clone was made from lane HEAD `6523aced1ee0ebe07dca996213bdc645a6acbd1e`; verified clone root was `/fast/scratch/hyaku/kotoba-r77/M03MutFloors/clone`. Pristine detector commands all passed: floors `0 failure(s) over 165 assertions` exit 0; tip battery `0 failure(s) over 69 assertions` exit 0; skill evals `0 failure(s)` exit 0. Their direct command outputs and exit values are listed in the build artifact.

Ran 21 independent mutants. Informative survivors: six D4 floor/table mutations (lower either floor by one in EXPECTED_INSTRUMENTS, INSTRUMENTS, registry; delete either expected row) and four changed pin-byte mutants. The tip battery self-test resets `INSTRUMENT_PINS` to `{}` and checks a synthetic fixture pin, so production pin-byte changes escape that self-test. The floors guard self-test fixtures do not pin/assert D4 floor values or presence in its tables; changes to those source declarations escape the self-test. Skill-evals' exact multi-entry check is covered: substring and negated-member mutants are killed. Three malformed mutants also failed, but are not counted as meaningful kills. Full matrix and exact outputs: `.ufo/waves/round-77/build/M03MutFloors.survivors.md`.

Restoration evidence: every individual mutation was reverted; the final SHA-256 values exactly equal the captured pre-mutation values for all four files (listed in the build artifact). The working lane files were not changed. No tools installed.

VERDICT: 21 mutants probed; 12 informative survivors expose self-test gaps in D4 floor declarations and the production pin; skill-evals exact-member/negation behaviors are covered.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/M03MutFloors.survivors.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/M03MutFloors.md