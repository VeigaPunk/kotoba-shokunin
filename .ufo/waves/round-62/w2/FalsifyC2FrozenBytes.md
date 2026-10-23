# FalsifyC2FrozenBytes — C2 frozen identity

Seat: `L1kotoba62.FalsifyC2FrozenBytes`. Lane read-only except this report. No tool installed. `date -u` at the attribution step: `Fri 23 Oct 2026 09:36:38 PM UTC` (exit 0). `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD` was `e6da78bbe420722dd18a13182a7c4b64ce02f005` (exit 0), the assigned tip. Python for the import probes: `3.14.8`.

## Verdict

The three requested whole-file identities are **not one hash**. Tip and `a745411c` are the receipt's `95ade9be…` file. `7827628a` is a different file (`61d8c583…`).

`check_repairs` at tip equals `check_repairs` at `a745411c`. It does **not** equal `check_repairs` at `7827628a`. The only statement that differs inside that function is R-d, introduced by `ee19e9c9`. R-a, R-b, R-c, R-e, and R-f statement text is the same at `7827628a` and at tip.

v2's own `check_repairs` is **not** those six checks. The script form of v2 does import the committed tip file and calls that function for the self-test's before-scores. That import is not path-pinned and not digest-pinned. On this host, script invocation still bound the committed file (no `sitecustomize`). A non-script import with the verifiers directory already on `sys.path` bound a cwd shadow instead.

## 1. Whole-file sha256 (three pins)

Command (exit 0 on every `rev-parse`, `cat-file -e`, and `show | sha256sum`):

```text
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse e6da78bbe420722dd18a13182a7c4b64ce02f005
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse 7827628a
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse a745411c
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show <full>:verifiers/check_routed_repairs.py | sha256sum
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse <full>:verifiers/check_routed_repairs.py
```

| pin | resolved commit | sha256 of `verifiers/check_routed_repairs.py` | git blob |
|---|---|---|---|
| tip | `e6da78bbe420722dd18a13182a7c4b64ce02f005` | `95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88` | `56b86f61004ff2e9d319d8cc87459b5cd702b51f` |
| `7827628a` | `7827628a939b0333c89892dfcedc72e390ccfb60` | `61d8c5831d1904cba921ccc547b8308753c1726e704d4cc2b5cec10d60c77356` | `5d277dc61fb53915558ea88968659bdf960e038e` |
| `a745411c` | `a745411c66d4765e9ac0ce48f1d96c34f425dab4` | `95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88` | `56b86f61004ff2e9d319d8cc87459b5cd702b51f` |

Worktree file, same seat:

```text
$ sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs.py
95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88  /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs.py
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin hash-object /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs.py
56b86f61004ff2e9d319d8cc87459b5cd702b51f
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin status --porcelain -- verifiers/check_routed_repairs.py verifiers/check_routed_repairs_v2.py
```

`sha256sum` exit 0, `hash-object` exit 0, `status` exit 0, porcelain empty. Worktree bytes match the tip blob and the `a745411c` blob. They do not match `7827628a`.

`git diff --stat a745411c66d4765e9ac0ce48f1d96c34f425dab4 e6da78bbe420722dd18a13182a7c4b64ce02f005 -- verifiers/check_routed_repairs.py` printed no lines (exit 0).

Receipt `.ufo/waves/round-62/C2-successor-measure.txt:4` says `frozen=verifiers/check_routed_repairs.py sha256 95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88`. That matches tip and `a745411c`. It does not match `7827628a`. The receipt line does not claim the `7827628a` digest.

`git log --oneline 7827628a..e6da78bbe420722dd18a13182a7c4b64ce02f005 -- verifiers/check_routed_repairs.py` (exit 0):

```text
ee19e9c round-61: C2 R-d arm empty-file guard (ExecReceiptsDesign T8 — empty census-after scores missing, no IndexError crash)
daf4ad7 round-61: errata E2c/E2d pre-data — A4 full-sha alias conjunct (MutA4/MutWorldW1), C1 base-discriminating mechanism (key set from committed rows), per-client key set; C2 self-test exemplar command now prints 29 (ExecC2Audit/RevRa count-basis trap)
eb5e149 round-61: C2 checker self-test hardened pre-data (MutC2: 12 arms, kills m1/m2/m5/m7; two-point residual disclosed; frozen six checks untouched)
```

Full ids (`git rev-parse`, exit 0): `eb5e149aa352aa857cb2b332621a61e24c8adb83`, `daf4ad71b2a36bcfc64e1a58461120f79c202f53`, `ee19e9c98f2ba6f5a4e5e8aa226569437c963b0d`.

## 2. Function-body diff of the six checks

AST `ast.get_source_segment` of `FunctionDef check_repairs`, then sha256 of that source text:

| revision | lines | function-source sha256 | bytes |
|---|---|---|---|
| `7827628a939b0333c89892dfcedc72e390ccfb60` | 63–112 | `9c3876422aa0a0493e1b5533820da4910864b583f829952d1bca6fe33ffe74dc` | 1763 |
| `a745411c66d4765e9ac0ce48f1d96c34f425dab4` | 71–119 | `2ea30b2d17705e64ab3b6c3b6249ada5ad7feaadcbc474c9970cf3cfa9fa1045` | 1786 |
| tip `e6da78bb…` | 71–119 | `2ea30b2d17705e64ab3b6c3b6249ada5ad7feaadcbc474c9970cf3cfa9fa1045` | 1786 |

Statement compare of that function, `7827628a` vs tip: `ra`, `rb`, `rc`, `re_`, `rf`, the five `why.append` lines, `census`, `lesson`, `ancestry`, the docstring, and the `return` are the same source text. `rd` is not.

Per-commit `git diff -U0` (the `rev-parse` of two names in one call failed with `fatal: Needed a single revision`; the diffs themselves ran):

- `7827628a` → `eb5e149a`: docstring plus `self_test` arms. No `check_repairs` hunk.
- `eb5e149a` → `daf4ad71`: `self_test` exemplar lines only (hunks at the `self_test` line numbers). No `check_repairs` hunk.
- `daf4ad71` → `ee19e9c9`: the R-d statement inside `check_repairs`.
- `ee19e9c9` → `a745411c`: `diff_lines 0`.

R-d at `7827628a` (`verifiers/check_routed_repairs.py` in that blob):

```python
rd = (
        census is not None
        and [ln for ln in census.splitlines() if ln.strip()][-1].strip() == "exit=0"
        if census is not None
        else False
    )
```

R-d at tip / `a745411c` (worktree lines 95–99):

```python
if census is None:
        rd = False
    else:
        census_lines = [ln for ln in census.splitlines() if ln.strip()]
        rd = census_lines[-1].strip() == "exit=0" if census_lines else False
```

Source reading, not a scored run: the `7827628a` expression indexes `[-1]` of the non-empty-line list, so an empty or whitespace-only census raises `IndexError` instead of returning a score. The tip expression sets `rd = False` when that list is empty. For a census that already has a non-empty last line, both expressions compare that line to `exit=0`. This is a verdict-path change, not a comment-only edit. Calling `7827628a` the freeze of "the six repair definitions" (`LOG.md:2554`) is wrong for R-d. The other five definitions are unchanged source text from `7827628a` through tip.

`eb5e149a`'s commit subject says "frozen six checks untouched". That subject matches the diff for **that** commit only. `ee19e9c9` later changed R-d.

## 3. v2's six checks are not that function

Worktree and tip blob of the successor:

```text
git show e6da78bbe420722dd18a13182a7c4b64ce02f005:verifiers/check_routed_repairs_v2.py | sha256
de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7
```

Same digest as the worktree file and as `.ufo/waves/round-62/C2-successor-measure.txt:3`. `git show` exit 0.

v2 `check_repairs` (`verifiers/check_routed_repairs_v2.py:302-329`) source sha256 `3dc453b4aeb9607cf59576edb9b4edbd2efd6ba142516e95134f9c098bce5edd`. Arguments: `blobs`, `tree_names`, `census_is_regular`. It is not equal to the frozen function source. It dispatches to `r_a_count_correction`, `r_b_landed_scope`, `r_c_pointer_direction`, `r_d_census_body`, `r_e_exact_ids`, `r_f_owned_ancestry`. None of those names exist in the frozen module. Frozen defs are only `git_show`, `check_repairs`, `main`, `self_test`.

Public `main` scores with v2's `check_repairs` (`:642`), not with `frozen.check_repairs`. The frozen symbol is used only in `self_test`: `:450`, `:473`, `:500`, `:501`, `:502`, `:519`.

`LOG.md:2554` says the successor "imports those six checks unchanged and adds its own G-a…G-f hardening". The second clause matches the source: v2 adds a different scorer. The first clause is true only as "calls whatever `check_repairs` the import bound, and does not edit that file". The bound function at tip is the post-`ee19e9c9` body, not the `7827628a` body. v2 does not re-load the `7827628a` blob.

## 4. Import binding (script path vs shadow)

Import site, `verifiers/check_routed_repairs_v2.py:24-27`:

```python
VERIFIERS = Path(__file__).resolve().parent
if str(VERIFIERS) not in sys.path:
    sys.path.insert(0, str(VERIFIERS))
import check_routed_repairs as frozen  # noqa: E402
```

There is no `importlib` load by file path and no `hashlib` check anywhere in v2 (the only matches for those ideas are this block). The lane path and `verifiers/` are not symlinks. `PYTHONPATH`, `PYTHONSAFEPATH`, `PYTHONSTARTUP`, `PYTHONHOME`, and `PYTHONNOUSERSITE` were unset in the probe environment. `sys.flags.safe_path` was false. `-B` set `dont_write_bytecode` and does **not** skip reading an existing timestamp-matched `.pyc`.

### What the frozen predicate's shape binds

`python3 -B -v /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs_v2.py --help`, cwd `/tmp/c2frozen-probe/shadowcwd` (a directory that contains a probe `check_routed_repairs.py`), including once with `PYTHONPATH=/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers`. Exit 0 both times. Stderr:

```text
# /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/__pycache__/check_routed_repairs.cpython-314.pyc matches /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs.py
# code object from '/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/__pycache__/check_routed_repairs.cpython-314.pyc'
import 'check_routed_repairs' # <_frozen_importlib_external.SourceFileLoader object at ...>
```

`runpy.run_path` of the same v2 file with `run_name="v2_script_probe"`, same shadow cwd, `python3 -B` (exit 0): `sys.path[0]` was `/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers`, `frozen.__file__` was `/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs.py`, `samefile` True, sha256 `95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88`, loader `SourceFileLoader`, marker absent. `sitecustomize` and `usercustomize` were not in `sys.modules`.

So the committed script command binds the committed module even if the cwd holds another `check_routed_repairs.py`, and even if `PYTHONPATH` names `verifiers/`. Reason: script `sys.path[0]` is the script directory, which is that `verifiers/` directory, and it is searched first. The `if str(VERIFIERS) not in sys.path` guard then does nothing, because the directory is already at index 0.

### Shadow that the same three lines do accept

Probe file, not a lane file: `/tmp/c2frozen-probe/shadowcwd/check_routed_repairs.py`, sha256 `30cb40f5f669e53d1c79ec308a9a2c03f88f1c8cdd14053e362fdc1d5f78dc61`, body `MARKER='SHADOW'` and `check_repairs` returning `(6, ['shadow'])`.

```text
cd /tmp/c2frozen-probe/shadowcwd
PYTHONPATH=/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers \
  python3 -B -c 'import check_routed_repairs_v2 as v2; print(v2.frozen.__file__)'
```

Exit 0. `sys.path` was `''` (cwd), then the verifiers directory, then the stdlib/site entries. Result: `frozen_file /tmp/c2frozen-probe/shadowcwd/check_routed_repairs.py`, `marker SHADOW`, sha256 `30cb40f5…`, `samefile` against the committed file False.

Cause: `str(VERIFIERS)` was already on `sys.path` via `PYTHONPATH`, so lines 25–26 did not insert it at 0, and the bare import searched cwd first. The same shape is what `self_test` trusts when it requires `frozen.check_repairs(...) == 6` on the dishonest trees (`:450-453`). A shadow that always returns 6 satisfies that arm without running the committed six. The successor's own rejection arm does not use `frozen`. The plan's frozen command is the script form, which did **not** take this path in the probes above. The hazard is real for any non-script import (python `-c`, another verifier importing v2) whenever the absolute `verifiers` directory is already on `sys.path` behind an earlier entry that provides `check_routed_repairs`.

No second `check_routed_repairs.py` and no `check_routed_repairs/` package were found under the lane, under `site.getsitepackages()`, or under the user site. The only lane copy is `verifiers/check_routed_repairs.py`.

### sitecustomize / pth / pyc

`python3 -B` inventory (exit 0): absent

- `/usr/lib/python3.14/sitecustomize.py`
- `/usr/lib/python3.14/usercustomize.py`
- `/usr/lib/python3.14/site-packages/sitecustomize.py`
- `/usr/lib/python3.14/site-packages/usercustomize.py`
- `/home/vgpnk/.local/lib/python3.14/site-packages/sitecustomize.py`
- `/home/vgpnk/.local/lib/python3.14/site-packages/usercustomize.py`

`ENABLE_USER_SITE` True. User site exists and has 0 `.pth` files. System site has one `.pth`, `/usr/lib/python3.14/site-packages/distutils-precedence.pth`, whose only line is the setuptools distutils shim (`import os; … __import__('_distutils_hack').add_shim()`). It does not name `check_routed_repairs` or insert this lane on `sys.path`. No `sitecustomize` hook is present for this interpreter, so none injected `sys.modules['check_routed_repairs']` during the probes.

`verifiers/__pycache__/check_routed_repairs.cpython-314.pyc` is timestamp-based (`flags=0`), not hash-based. Header `mtime=1792786187` and `size=9940` equal the source `stat` (`st_size=9940`, `int(st_mtime)=1792786187`). `marshal.loads` of the code object: `check_repairs.co_code` equals `compile()` of the current source (`co_firstlineno` 71, `co_code` length 1242, equal True). The on-disk pyc is not a second implementation. It is still a trust point: `-B` loaded that code object after the timestamp/size match (`-v` line above). A pyc whose header mtime and size were set to the source's, with different bytecode, would be loaded. That is not the current file.

## What was not run

`--self-test` and `--rev` scoring were not re-run here. Empty-census R-d was not executed; the IndexError-vs-`False` note is a reading of the two expressions. No claim is made about another host's `sitecustomize`.
