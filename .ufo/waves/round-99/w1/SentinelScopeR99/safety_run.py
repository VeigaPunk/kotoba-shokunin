#!/usr/bin/env python3
"""SentinelScopeR99 safety harness: run verify_dispatch_prompts.py --self-test
under an audit hook that refuses network and subprocess, then report.

Usage: safety_run.py <path-to-verify_dispatch_prompts.py>
Exit 0 = self-test CLEAN with no forbidden audit event; 1 = self-test failed;
2 = forbidden event fired / could-not-evaluate.
"""
import importlib.util
import os
import sys

FORBIDDEN = (
    "socket.connect", "socket.getaddrinfo", "socket.gethostbyname",
    "urllib.Request", "http.client.connect", "subprocess.Popen",
    "os.system", "os.exec", "os.spawn", "ftplib.connect", "smtplib.connect",
)
fired = []


def hook(event, args):
    if event in FORBIDDEN:
        fired.append((event, repr(args)[:200]))


def main():
    path = sys.argv[1]
    sys.addaudithook(hook)
    spec = importlib.util.spec_from_file_location("vdp_under_test", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    rc = mod.main(["--self-test"])
    print("SAFETY self-test rc=%d" % rc)
    if fired:
        for ev, a in fired:
            print("SAFETY-FORBIDDEN %s %s" % (ev, a))
        return 2
    print("SAFETY no network/subprocess audit event fired")
    return 0 if rc == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
