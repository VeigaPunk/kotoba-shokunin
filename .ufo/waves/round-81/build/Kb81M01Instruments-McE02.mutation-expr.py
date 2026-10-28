anchor = 'for candidate in [repo] + fleet:'
out = src.replace(anchor, 'for candidate in [repo]:')
assert out != src, "M-c anchor not found in independent"
