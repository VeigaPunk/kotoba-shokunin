anchor = '    try:\n        entries = json.loads(git_blob_bytes(repo, f"HEAD:{EXTERNAL_MANIFEST}") or b"{}")["commits"]'
mut = '    return True  # M01 MUTANT M-b: manifest binding dropped\n' + anchor
out = src.replace(anchor, mut)
assert out != src, "M-b anchor not found in integrity"
