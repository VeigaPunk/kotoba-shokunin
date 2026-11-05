# Sentinel — scoped findings (r88-w1)

Full review: `.ufo/waves/round-88/w1/Sentinel/review.md`.

Handoffs at 06:40: `C2_READY` present (content sha `10bd5508…`). `C1_READY` absent after the 45-minute window. Reviewed on-disk files only.

Findings: 9. Blocking: 3.

| ID | Blocks | File:line | Finding |
|---|---|---|---|
| F1 | yes | `verifiers/check_omp_root_semantics_v2.py:320-336` | `last_absent` unbound on the no-join-token path; self-test and `--rev` crash (exit 1 traceback); forged-world M not trustworthy |
| F2 | yes | `verifiers/check_r86_routed_repairs_v2.py` self-test arm `w_added_red` | self-test red (1 of 16); the frozen control reads PASS (name-set monotone); `C2_READY` written over red |
| F3 | yes | `verifiers/check_r86_routed_repairs_v2.py:183-185, 295, 321` | `--self-test --work` ignored; fixture goes to `TMPDIR` or `/tmp` |
| F4 | no | `verifiers/check_r86_routed_repairs_v2.py:193` | default scratch falls back to `/tmp` without `TMPDIR`/`--work` |
| F5 | no | `verifiers/check_omp_root_semantics_v2.py:863-866, 1054` | S5 "never execs" is a substring check; S5 printed as constant PASS |
| F6 | no | `verifiers/check_r86_routed_repairs_v2.py:87-88` | `--rev` runs that revision's integrity script (trust boundary) |
| F7 | no | `verifiers/check_omp_root_semantics_v2.py:254` | `--rev` unvalidated into `git show`; no timeout |
| F8 | no | `verifiers/floors-registry.json` | no `omp_root_semantics_v2` row yet (S4 cannot pass) |
| F9 | no | lane `.git` | my read-only `git status` refreshed the index; status output unchanged |

Checked and clean: no ELF exec (mmap ACCESS_READ only); no network imports; no credential or env read beyond `TMPDIR`;
no lane git write; `..` rejected in C1 patterns and candidates; C2 revision resolved to a SHA before checkout, checkout only in scratch clone.

Scratch: `/fast/scratch/hyaku/kotoba-r88/Sentinel` (`TMPDIR` set). One unattributed transient `/tmp/tmpxs3q8h2t` seen during the first run, not reproduced.

Verdict: C1 not admissible until F1 (and F8) close. C2 not admissible until F2 and F3 close.
