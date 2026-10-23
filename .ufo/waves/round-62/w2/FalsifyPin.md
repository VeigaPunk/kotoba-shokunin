# Round 62 W2 — C1 counter-pin falsification

**Severity:** Medium — a conditional local TOCTOU bypass is reproducible. The ordinary modified-file and symlink checks fail closed.

**Scope/evidence:** Audited the landed bytes at `e6da78bbe420722dd18a13182a7c4b64ce02f005`. The instrument hash was `afb4ff74c266803f4d6007407775a5c44387c84bf49b9ac1a9059d375178d56b`; the frozen counter hash was `5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91`. `check_erratum_absorption.py` resolves its sibling counter at line 16, hashes `path.read_bytes()` at lines 81–86, imports it from the path at 87–91, then trusts the imported `counter.self_sha()` at 92–97. The counter's `self_sha()` reads `__file__` at `check_scoped_rules.py:465–468`.

## Requested checks

Test fixtures were under `/tmp/kotoba-r62-pin.wZWb2c`; lane verifier/counter files were not modified.

### (a) Copied instrument beside a one-byte-modified counter

The fixture copied both landed files, then appended exactly one ASCII space to the counter (`124987` → `124988` bytes). Its SHA-256 changed from the pinned `5a5adc…` to `2a527dbe8358d39ac3b8e610d5431f79ac4ee9b9201483d75a8ba8f1c7fd5495`.

```sh
set +e; python3 -B /tmp/kotoba-r62-pin.wZWb2c/modified/check_erratum_absorption.py --self-test; rc=$?; printf 'exit=%s\n' "$rc"
```

```text
counter sha256 mismatch: expected 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91; got 2a527dbe8358d39ac3b8e610d5431f79ac4ee9b9201483d75a8ba8f1c7fd5495
exit=2
```

### (b) Counter symlinks

`real-link/check_scoped_rules.py` was a symlink to the landed counter. This succeeds and reports the pinned digest:

```sh
set +e; python3 -B /tmp/kotoba-r62-pin.wZWb2c/real-link/check_erratum_absorption.py --self-test; rc=$?; printf 'exit=%s\n' "$rc"
```

```text
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
exit=0
```

`modified-link/check_scoped_rules.py` was a symlink to the one-byte-modified copy:

```sh
set +e; python3 -B /tmp/kotoba-r62-pin.wZWb2c/modified-link/check_erratum_absorption.py --self-test; rc=$?; printf 'exit=%s\n' "$rc"
```

```text
counter sha256 mismatch: expected 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91; got 2a527dbe8358d39ac3b8e610d5431f79ac4ee9b9201483d75a8ba8f1c7fd5495
exit=2
```

### (c) Post-import `self_sha()` recheck

A loader hook appended one space **after** the instrument's initial digest check but before executing the counter. The imported original counter's `self_sha()` observed those changed bytes, and the post-import check rejected them:

```sh
set +e; python3 -B -c 'import importlib.util, pathlib, sys
root = pathlib.Path("/tmp/kotoba-r62-pin.wZWb2c/recheck")
tool = root / "check_erratum_absorption.py"
counter_path = root / "check_scoped_rules.py"
spec = importlib.util.spec_from_file_location("absorb_pin_probe", tool)
instrument = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = instrument
spec.loader.exec_module(instrument)
original_spec = importlib.util.spec_from_file_location
class LoaderProxy:
    def __init__(self, inner): self.inner = inner
    def create_module(self, spec): return self.inner.create_module(spec)
    def exec_module(self, module):
        with counter_path.open("ab") as f: f.write(b" ")
        self.inner.exec_module(module)
def mutate_after_precheck(name, path):
    spec = original_spec(name, path)
    spec.loader = LoaderProxy(spec.loader)
    return spec
instrument.importlib.util.spec_from_file_location = mutate_after_precheck
try:
    instrument.load_counter(counter_path)
except instrument.CounterPinMismatch as exc:
    print(str(exc), file=sys.stderr)
    raise SystemExit(2)
print("unexpectedly accepted post-import mutation", file=sys.stderr)
raise SystemExit(1)'; rc=$?; printf 'exit=%s\n' "$rc"
```

```text
imported counter self_sha mismatch: expected 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91; got 2a527dbe8358d39ac3b8e610d5431f79ac4ee9b9201483d75a8ba8f1c7fd5495
exit=2
```

## Different-counter bypass found

The post-import check is not independent: it trusts code loaded from the path it is meant to authenticate. A writer able to replace the counter between `read_bytes()` and `exec_module()` can supply modified code that overrides `self_sha()` to return the pinned literal. I reproduced this entirely in `/tmp`: the injected counter also changed `url_key()` for an unmeasured sentinel, while leaving the measured matrix inputs unchanged. The CLI self-test accepted and exited 0 even though the on-disk counter hash differed.

Command (the loader hook writes the added code only after the instrument's pre-import pin succeeds):

```sh
set +e; python3 -B -c 'import hashlib, importlib.util, pathlib, sys
root = pathlib.Path("/tmp/kotoba-r62-pin.wZWb2c/lie")
tool = root / "check_erratum_absorption.py"
counter_path = root / "check_scoped_rules.py"
spec = importlib.util.spec_from_file_location("absorb_pin_race", tool)
instrument = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = instrument
spec.loader.exec_module(instrument)
original_spec = importlib.util.spec_from_file_location
payload = ("\n" + """
_original_url_key = url_key
def url_key(url):
    if url == "https://attack-pin.invalid/":
        return "untrusted-counter-behavior"
    return _original_url_key(url)
def self_sha():
    return "5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91"
""").encode()
loaded = []
class LoaderProxy:
    def __init__(self, inner): self.inner = inner
    def create_module(self, spec): return self.inner.create_module(spec)
    def exec_module(self, module):
        counter_path.write_bytes(counter_path.read_bytes() + payload)
        self.inner.exec_module(module)
        loaded.append(module)
def replace_after_precheck(name, path):
    spec = original_spec(name, path)
    spec.loader = LoaderProxy(spec.loader)
    return spec
instrument.importlib.util.spec_from_file_location = replace_after_precheck
rc = instrument.main(["--self-test"])
print("on-disk sha256 after import: " + hashlib.sha256(counter_path.read_bytes()).hexdigest())
print("imported self_sha(): " + loaded[0].self_sha())
print("unmeasured url_key probe: " + loaded[0].url_key("https://attack-pin.invalid/"))
raise SystemExit(rc)'; rc=$?; printf 'exit=%s\n' "$rc"
```

```text
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
on-disk sha256 after import: bbff4dd827be6067bd8610e6de0492fcdc10141a0de689f2479af8e39d7b5cac
imported self_sha(): 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91
unmeasured url_key probe: untrusted-counter-behavior
exit=0
```

**Exploit path / impact:** With concurrent write access to the counter path, pass the original bytes at the first `read_bytes()`, then replace/append modified Python before the loader opens the path. The modified module lies in its own `self_sha()` and is accepted; code outside the frozen measurement can differ without exit 2. The symlink checks do not close this check/use window.

**Smallest remediation:** Hash and execute the same already-read byte buffer (e.g. compile the verified bytes into the module namespace); do not use an imported counter's own `self_sha()` as the independent pin. No lane code was changed; this is a report-only finding.