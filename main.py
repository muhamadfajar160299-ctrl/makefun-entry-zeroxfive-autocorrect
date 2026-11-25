"""One-liner entry for make.fun: Funniest Autocorrect Fail.

Writes a single autocorrect-fail line to entry.txt in $MAKEFUN_OUTPUT_DIR.
Stdlib only; no network, no secrets, no reading outside the repository.
"""

import os

LINE = "Thanks for the birthday card, Grandma! I love your warm drugs and freshly baked cookies!"

try:
    if not LINE or not LINE.strip():
        raise ValueError("entry line is empty")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
except Exception as exc:
    raise SystemExit("failed to write entry.txt: %s" % exc)
