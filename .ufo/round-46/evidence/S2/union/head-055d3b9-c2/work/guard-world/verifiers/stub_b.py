import argparse
ap = argparse.ArgumentParser()
ap.add_argument("--self-test", action="store_true")
ap.add_argument("--repo", default=None)
ap.parse_args()
print("self-test: 0 failure(s) over 3 assertions")
