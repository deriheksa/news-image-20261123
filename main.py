"""make.fun bounty entry runner.

Copies entry.png (bundled next to this script) to /output/entry.png
so the grader can pick it up. Pure Python standard library only.
"""

import os
import shutil
import sys


def resolve_entry_paths():
    """Return (src, dst) for the bundled entry.png and its output path."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(script_dir, "entry.png")
    dst = os.path.join("/output", "entry.png")
    return src, dst


def main() -> int:
    src, dst = resolve_entry_paths()
    dst_dir = os.path.dirname(dst)

    os.makedirs(dst_dir, exist_ok=True)
    shutil.copyfile(src, dst)

    size = os.path.getsize(dst)
    print(f"Copied entry.png -> {dst} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
