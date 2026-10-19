#!/usr/bin/env python3
import copy
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
CID = "omp.catalogue.total"
LIVE = OUT / "fresh-live.json"
INDEPENDENT = OUT / "fresh-independent.json"
DRIVER = OUT / "landed-032f47b.py"
SCOPE = ROOT / "verifiers/harness-independent-scope.json"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, data):
    Path(path).write_text(json.dumps(data, indent=2, sort_keys=True) + "\n",
                          encoding="utf-8")


def main():
    payload = copy.deepcopy(json.loads(INDEPENDENT.read_text(encoding="utf-8")))
    live = json.loads(LIVE.read_text(encoding="utf-8"))
    value = next(row["observed"] for row in live["results"] if row["check"] == CID)
    payload["scoped_out"].pop(CID)
    payload["scoped_out_probes"].pop(CID)
    for channel in ("results", "rows"):
        row = next(row for row in payload[channel] if row.get("check") == CID)
        row["status"] = "DERIVED"
        row["evidence"] = "fresh independent derivation available"
        row.pop("probe", None)
        row["re_derived"] = value
        row["value"] = value
    payload["checks"][CID] = value
    mutant_path = OUT / "fresh-committed-row-rederived-independent.json"
    write_json(mutant_path, payload)
    receipt = OUT / "fresh-committed-row-rederived-receipt.json"
    command = [sys.executable, str(DRIVER), "--live-json", str(LIVE),
               "--independent-json", str(mutant_path), "--expect-n", "28",
               "--cwd", str(ROOT), "--scope-file", str(SCOPE),
               "--no-stamp", "--json", "--receipt", str(receipt)]
    proc = subprocess.run(command, cwd=ROOT, capture_output=True, text=True,
                          timeout=180)
    stdout = OUT / "fresh-committed-row-rederived-stdout.json"
    stderr = OUT / "fresh-committed-row-rederived-stderr.txt"
    stdout.write_text(proc.stdout, encoding="utf-8")
    stderr.write_text(proc.stderr, encoding="utf-8")
    result = {
        "run_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "snapshot": {
            "head": subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"],
                                    check=True, capture_output=True, text=True).stdout.strip(),
            "tree": subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD^{tree}"],
                                    check=True, capture_output=True, text=True).stdout.strip(),
            "driver_commit": "032f47bd13fdff0cd2ccea5f902df9690ad09376",
            "driver_sha256": sha(DRIVER),
            "scope_sha256": sha(SCOPE),
        },
        "claim": "a committed scope-out row is now DERIVED, removed from scoped_out, with its live-observed value in every row/map channel",
        "row": CID,
        "derived_value": value,
        "command": command,
        "exit": proc.returncode,
        "stdout_sha256": sha(stdout),
        "stderr_sha256": sha(stderr),
        "reason": (proc.stderr or proc.stdout).strip()[-1500:],
        "independent_payload_sha256": sha(mutant_path),
        "live_payload_sha256": sha(LIVE),
        "receipt_sha256": sha(receipt) if receipt.is_file() else None,
    }
    write_json(OUT / "fresh-committed-row-reentry.json", result)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
