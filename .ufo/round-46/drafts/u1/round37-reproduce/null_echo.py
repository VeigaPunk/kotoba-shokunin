import json, subprocess, sys
ids = [r["check"] for r in json.loads(subprocess.run([sys.executable, "verifiers/verify_harness_claims.py", "--json"], capture_output=True, text=True, check=True).stdout)["results"]]
print(json.dumps({"checks": {i: 0 for i in ids}}))
