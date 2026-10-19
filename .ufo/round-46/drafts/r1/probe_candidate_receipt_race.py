from __future__ import annotations

import ctypes
import hashlib
import importlib.util
import json
import os
import select
import struct
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DRAFT = Path(__file__).resolve().parent
RUN = DRAFT / "run-15"
INPUTS = RUN / "inputs"
CARRIER = RUN / "cases" / "probe-carrier"
OUTPUTS = RUN / "outputs"
FIXTURE = ROOT / "verifiers/fixtures/compare-harness-independent/scope-file-cwd"
SCOPE_REL = Path("verifiers/harness-independent-scope.json")
CANDIDATE = DRAFT / "run-14/inputs/compare_candidate.py"
TARGET_BYTES = FIXTURE / "carrier/surface.jsonl"
IN_OPEN = 0x00000020
IN_NONBLOCK = os.O_NONBLOCK
IN_CLOEXEC = getattr(os, "O_CLOEXEC", 0)
EVENT = struct.Struct("iIII")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    for path in (INPUTS, CARRIER, OUTPUTS):
        path.mkdir(parents=True, exist_ok=False)
    candidate_bytes = CANDIDATE.read_bytes()
    candidate = INPUTS / "compare_candidate.py"
    candidate.write_bytes(candidate_bytes)

    module_spec = importlib.util.spec_from_file_location("candidate_compare", candidate)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    source_carrier = (FIXTURE / "carrier").resolve()
    for i in range(1500):
        (CARRIER / f"session-{i:04d}.jsonl").symlink_to(TARGET_BYTES.resolve())
    probe = module.recompute_probe({"kind": "rule-spread-census", "target": str(CARRIER)})
    independent = json.loads((FIXTURE / "independent.json").read_text())
    payload_text = json.dumps(independent, sort_keys=True).replace(
        "@fixture:carrier@", str(CARRIER.resolve())
    )
    independent = json.loads(payload_text)
    reason = independent["scoped_out"]["a.c"]
    for record in independent["results"]:
        if record.get("check") == "a.c":
            record["evidence"] = "SCOPED_OUT: " + reason
            record["probe"]["target"] = str(CARRIER.resolve())
            record["probe"]["observable"] = probe["observable"]
    independent["scoped_out_probes"]["a.c"]["target"] = str(CARRIER.resolve())
    independent["scoped_out_probes"]["a.c"]["observable"] = probe["observable"]
    live_path = INPUTS / "live.json"
    ind_path = INPUTS / "independent.json"
    live_path.write_bytes((FIXTURE / "live.json").read_bytes())
    ind_path.write_text(json.dumps(independent, indent=2, sort_keys=True) + "\n")

    planted_doc = json.loads((FIXTURE / "scope.json").read_text())
    planted_doc["probe_contract"]["target"] = str(CARRIER.resolve())
    planted = (json.dumps(planted_doc, indent=2, sort_keys=True) + "\n").encode()
    honest = (FIXTURE / "honest-scope.json").read_bytes()
    scope_path = INPUTS / "scope-under-test.json"
    scope_path.write_bytes(planted)
    honest_alt = INPUTS / "honest-replacement.json"
    honest_alt.write_bytes(honest)
    planted_sha, honest_sha = sha(planted), sha(honest)

    libc = ctypes.CDLL(None, use_errno=True)
    libc.inotify_init1.argtypes = [ctypes.c_int]
    libc.inotify_init1.restype = ctypes.c_int
    libc.inotify_add_watch.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_uint32]
    libc.inotify_add_watch.restype = ctypes.c_int
    fd = libc.inotify_init1(IN_NONBLOCK | IN_CLOEXEC)
    if fd < 0:
        raise OSError(ctypes.get_errno(), "inotify_init1 failed")
    watch = libc.inotify_add_watch(fd, os.fsencode(scope_path), IN_OPEN)
    if watch < 0:
        raise OSError(ctypes.get_errno(), "inotify_add_watch failed")

    receipt_path = OUTPUTS / "race.receipt.json"
    argv = [
        sys.executable, "-B", str(candidate),
        "--live-json", str(live_path), "--independent-json", str(ind_path),
        "--scope-file", str(scope_path.absolute()), "--cwd", str(ROOT),
        "--expect-n", "2", "--no-stamp", "--json", "--receipt", str(receipt_path),
    ]
    started = datetime.now(timezone.utc).isoformat()
    proc = subprocess.Popen(argv, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    deadline = time.monotonic() + 20
    event_seen = False
    while time.monotonic() < deadline:
        ready, _, _ = select.select([fd], [], [], max(0, deadline - time.monotonic()))
        if not ready:
            break
        data = os.read(fd, 65536)
        offset = 0
        while offset + EVENT.size <= len(data):
            _wd, mask, _cookie, name_len = EVENT.unpack_from(data, offset)
            offset += EVENT.size + name_len
            if mask & IN_OPEN:
                event_seen = True
                temp = INPUTS / "replacement.tmp"
                temp.write_bytes(honest)
                os.replace(temp, scope_path)
                break
        if event_seen:
            break
    stdout, stderr = proc.communicate(timeout=180)
    os.close(fd)
    if not event_seen:
        raise RuntimeError(f"scope file IN_OPEN event not observed; exit={proc.returncode}")
    output = json.loads(stdout) if proc.returncode == 0 else None
    receipt = json.loads(receipt_path.read_text()) if receipt_path.is_file() else None
    result = {
        "measurement": {"started": started, "finished": datetime.now(timezone.utc).isoformat()},
        "candidate_sha256": sha(candidate_bytes),
        "candidate_path": str(candidate),
        "command": argv,
        "receipt_file_initially_enforced_sha256": planted_sha,
        "file_bytes_replaced_after_first_open_sha256": honest_sha,
        "replacement_event": "inotify IN_OPEN on the candidate's resolved scope path; atomic os.replace before receipt generation",
        "probe_carrier": str(CARRIER.resolve()),
        "probe_files": 1500,
        "probe_observable": probe["observable"],
        "exit": proc.returncode,
        "stderr": stderr.decode(),
        "stdout_sha256": sha(stdout),
        "headline": output.get("headline") if output else None,
        "agreement": output.get("agreement") if output else None,
        "receipt_scope": receipt.get("scope_file") if receipt else None,
        "scope_path_after_run_sha256": sha(scope_path.read_bytes()),
    }
    result_path = OUTPUTS / "receipt-race-results.json"
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"result": str(result_path), "result_sha256": sha(result_path.read_bytes()),
                      "candidate_sha256": sha(candidate_bytes), "exit": proc.returncode,
                      "headline": result["headline"], "enforced_sha256": planted_sha,
                      "receipt_scope": result["receipt_scope"]}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
