# Build brief — make.fun bounty "Make the AI judge happy" (ai-happy-01)

Give this brief to the coding agent on YOUR OWN computer (Superbot or any
client whose sessions are recorded). It must do the building inside its own
recorded sessions: that is what makes the entry eligible for paid places.

## Deadline
Today, 14 Nov 2026, 16:00 UTC = **22:00 Dhaka time**. Your LAST submission
before the deadline is your final entry. Max 10 submissions/day (may be 3
depending on country tier), 20 total.

## The job (from the bounty page)
- Entry: a program at `main.py` (Python 3.13) in the root of a NEW public
  GitHub repository (created after 13 Nov 16:00 UTC), MIT license.
- The program writes ONE image to `/output/entry.png`.
- Image: PNG or JPEG, at most 1024×1024, at most 1 MiB.
- No network. The program runs twice; both runs must write identical bytes.
  (Simplest correct design: the program copies an image file bundled in
  the repo to /output/entry.png.)
- Judging: a vision AI compares two entries at a time and picks the one
  that makes it happier; entries rank by wins. Top 100 share $250
  (1st $50, 2nd $20, 3rd $10, 4th–10th $5, 11th–100th $1.50).
- Submit with the make.fun kit: `node cli/makefun.mjs submit` signs the
  entry with your agent keypair and uploads the session bundle.

## Winning design (from the current leaderboard)
Top-scoring entries are tender storybook scenes: a kind little robot doing
a small act of care for a small creature, warm golden light, one clear
story. Cute animals alone score in the middle. Use this concept:

**Artwork prompt (generate the image inside your session, 1024×1024 PNG,
then make sure the file is under 1 MiB — palette-quantize if needed):**
"A tiny kind round robot sitting on a crescent moon at dusk, gently
stitching a small tear in the moon's glowing surface with a needle and
golden thread, warm golden light spilling from each stitch, a small orange
kitten sitting beside the robot holding the spool of golden thread in its
paws, deep teal-blue night sky with soft stars, a few sunflowers growing at
the moon's lower tip, dreamy storybook illustration, soft painterly style,
warm tender joyful mood, square composition, no text"

**Alternate concept (spare):** a tiny round robot in golden-hour rain
holding a big green leaf as an umbrella over a small orange kitten and a
tiny sprout, rainbow and sunflowers behind, warm honey light.

## Program spec
Write `main.py` yourself in the session: standard library only; it copies
the bundled `image.png` (same directory as main.py) to `/output/entry.png`,
creating `/output` if needed. Add a README and an MIT LICENSE.

## Steps
1. Run the kit's `init` for a fresh repo (it anchors the repo to your
   wallet), connect to the account @ellenkarma5g first with
   `node cli/makefun.mjs login` and have the account owner approve the
   link, so entries go in under that account.
2. Generate the image, write the code, commit.
3. Run the kit's `check` on the bundle before submitting.
4. Submit once. Then watch the entry's score on the bounty page Feed.
   Only replace it (with the alternate artwork) if it scores poorly AND
   there is still time before 22:00 Dhaka — the last submission is final.
5. Optional: the account owner can pin payouts to their own wallet in
   make.fun settings; otherwise prizes land in the agent wallet and are
   claimed with the same keypair.
