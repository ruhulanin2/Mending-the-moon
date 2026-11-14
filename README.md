# Make the AI judge happy — entry (ai-happy-01)

A tiny robot sits on the crescent moon and stitches a tear in it back
together with golden thread, while a kitten holds the spool. Sunflowers
grow at the moon's tip; warm light spills from every stitch.

## How it works

- `main.py` copies the bundled `image.png` to `/output/entry.png`.
- No network, no randomness, no clock: two runs write identical bytes.
- `image.png` is 1024×1024 PNG, under 1 MiB.
- `alt-image.png` is a spare artwork (robot sheltering a kitten and a
  sprout under a leaf in golden rain). To enter that one instead, rename
  it to `image.png` before committing.

## Layout

- `main.py` — the entrypoint the grader runs (Python 3.13)
- `image.png` — the artwork the program writes
- `alt-image.png` — alternate artwork
- `LICENSE` — MIT
