"""Entry for make.fun bounty ai-happy-01 - "Make the AI judge happy".

Writes the bundled artwork to /output/entry.png.

The artwork (image.png, next to this file) shows a tiny robot stitching a
tear in the crescent moon back together with golden thread while a kitten
holds the spool - a small act of mending, in warm golden light.

The program is deterministic: it copies the same bundled bytes on every
run, uses no network, no randomness and no clock, so two runs always
produce byte-identical output.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "image.png")


def main() -> None:
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        target = os.path.join(out_dir, "entry.png")
        shutil.copyfile(SOURCE, target)
    except OSError:
        # Fallback for local runs where /output is not writable.
        out_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(out_dir, exist_ok=True)
        target = os.path.join(out_dir, "entry.png")
        shutil.copyfile(SOURCE, target)
    print(f"wrote {target}")


if __name__ == "__main__":
    main()
