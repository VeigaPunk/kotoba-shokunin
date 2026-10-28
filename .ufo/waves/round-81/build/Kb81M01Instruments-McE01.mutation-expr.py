anchor = 'for repo in ([lane] if lane else []) + [fleet_root])'
out = src.replace(anchor, 'for repo in ([lane] if lane else []))')
assert out != src, "M-c anchor not found in integrity"
