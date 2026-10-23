# Falsify C2 `--rev` argument handling

**Severity:** No exploitable finding on the assigned surface (operability pass).

**Exploit path tested:** Feed shell metacharacters, a tree or blob object ID, `--`, a path-bearing revision, an empty revision, and an unreadable repository to `--rev`; check for shell execution, traceback, or scoring of a non-commit.

**Evidence:** At lane tip `e6da78bbe420722dd18a13182a7c4b64ce02f005`, the verifier SHA-256 was `de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7`, matching the C2 receipt. `resolve_commit` calls `subprocess.run(["git", "-C", str(repo), "rev-parse", "--verify", f"{rev}^{{commit}}"], capture_output=True)` (source lines 118–125); no shell is requested. The CLI stops with exit 2 when resolution fails, before `git_tree_names` and `check_repairs` (lines 619–646). The tested tree/blob IDs were independently typed with:

```text
$ /usr/bin/git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin cat-file -t 23475c49e35018a2e311c496bc21900b54a53d09 && /usr/bin/git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin cat-file -t 4e45f660d87b81dc0467f9951f657641b9ab8101
 tree
 blob
```

Both CLI object-type tests exited 2 before scoring. All test outputs below contained no traceback.

| Command | Result |
|---|---|
| `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs_v2.py --rev 'HEAD; touch /tmp/kotoba-r62-c2revarg.PoECLU/injected'` | `routed repairs verified could-not-evaluate: unreadable rev`; exit 2; `injection_marker=absent` |
| `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs_v2.py --rev 23475c49e35018a2e311c496bc21900b54a53d09` (tree) | `routed repairs verified could-not-evaluate: unreadable rev`; exit 2 |
| `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs_v2.py --rev 4e45f660d87b81dc0467f9951f657641b9ab8101` (blob) | `routed repairs verified could-not-evaluate: unreadable rev`; exit 2 |
| `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs_v2.py --rev=--` | `routed repairs verified could-not-evaluate: unreadable rev`; exit 2 |
| `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs_v2.py --rev=HEAD:LOG.md` | `routed repairs verified could-not-evaluate: unreadable rev`; exit 2 |
| `/usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs_v2.py --rev=` | `routed repairs verified could-not-evaluate: unreadable rev`; exit 2 |

For the unreadable-repository case, a temporary `/tmp` copy of the verifier and its frozen import was placed in a sandbox with `.git` mode `000`; no lane files were changed. The explicit-rev command `/usr/bin/python3 -B /tmp/kotoba-r62-c2-unreadable.ubRkGX/verifiers/check_routed_repairs_v2.py --rev HEAD` printed `routed repairs verified could-not-evaluate: unreadable rev`, exit 2. Without `--rev`, the same script printed `routed repairs verified could-not-evaluate: no rev`, exit 2. Neither produced a traceback. The first attempt to use `runuser` did not execute the verifier (`runuser: may not be used by non-root users`, exit 1); the same-UID permission-restricted sandbox above exercised the target successfully.

**Impact:** No shell execution occurred; the marker was absent. Tree, blob, path, option-like, empty, and unreadable-repository inputs failed closed with the named diagnostics and exit 2. No tested non-commit reached scoring.

**Smallest remediation:** None required for the observed behavior. The existing self-test covers a nonexistent revision; adding these adversarial `--rev` cases there would preserve this result as regression coverage, but no product fix is indicated by this attack.