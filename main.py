"""Entry program for make.fun's news-image-20261126 bounty ($100 in USDC):
sum up 26 November 2026's world news in one image.

The artwork lives in this repository as news.png, a 1024x1024 editorial
poster with the date across the top and one illustrated panel per story.
Running the program publishes it as the contest output: it checks the
file, then copies it unchanged to entry.png in the output directory.

The four stories, each verified against Reuters/Bloomberg reporting of
24-25 November 2026 before the image was drawn (see NOTES.md for sources):

1. TRUMP'S NEW TARIFFS -- the Trump administration's new Section 301
   tariffs on 14 trading partners (China, Japan, the EU and others),
   headline rates of 20-40%, capped by the trade deals already concluded
   or under negotiation; the probe targets what Washington calls
   structural excess industrial capacity.
2. HOUTHI STRIKE ON SAUDI REFINERY -- Yemen's Houthis claim a strike on
   Saudi Arabia's Ras Tanura refinery, the kingdom's largest, and on
   Riyadh's financial district; Saudi air defences say they shot down
   four drones over the site. Brent crude settled at $94.61 a barrel,
   up 3.5% on the day.
3. NASDAQ PLUNGES -- the Nasdaq falls about 4% as the AI selloff deepens
   and the fresh tariff proposals spook Wall Street; Nvidia falls about
   8.7% and Anthropic trades below its $83 IPO price.
4. HUANG RETURNS TO NVIDIA -- Jensen Huang returns as Nvidia CEO after a
   brief ouster earlier in November, apologises to employees in an
   all-hands meeting, and faces Congress over his dealings with suspected
   Chinese spy Alice Wang; Trump says a pardon is "always an option" but
   unnecessary.

Two panels were corrected after a fact check and the image redrawn: an
early draft said Huang "resigns" (backwards -- he returned) and carried
the Ukraine/Libya sea-drone strike of 22 November (stale, and already
used in the 24 November entry). Both were replaced with the verified
stories above.

The harness runs the program twice, with no network, and both runs
must produce the same bytes, so the copy below is a plain byte
transfer in fixed-size chunks: no timestamps, no randomness, nothing
that can vary between runs.

Try it outside the grader with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Without MAKEFUN_OUTPUT_DIR it writes to /output, the directory the
grader provides. The output directory is left at mode 0755 and the
written file at mode 0644, so the grader can read them.
"""

import os
import shutil

CHUNK_SIZE = 65536
SIZE_LIMIT = 1048576  # the gate takes at most 1 MiB
PNG_HEADER = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])

# The artwork's four panels, one story each:
#   Trump's new tariffs on 14 trading partners,
#   the Houthi strike on Saudi Arabia's Ras Tanura refinery as Brent
#   crude settles at $94.61 a barrel,
#   the Nasdaq plunging about 4% in the AI selloff,
#   and Jensen Huang returning as Nvidia CEO and apologizing
#   to employees in an all-hands after being ousted earlier
#   in November.


def artwork_path():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "news.png")


def destination_path():
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return folder, os.path.join(folder, "entry.png")


def check_artwork(path):
    size = os.path.getsize(path)
    if size > SIZE_LIMIT:
        raise SystemExit("news.png is over the 1 MiB limit: %d bytes" % size)
    with open(path, "rb") as f:
        if f.read(len(PNG_HEADER)) != PNG_HEADER:
            raise SystemExit("news.png is not a PNG file")
    return size


def main():
    src = artwork_path()
    size = check_artwork(src)
    folder, dest = destination_path()
    os.makedirs(folder, exist_ok=True)
    with open(src, "rb") as fin, open(dest, "wb") as fout:
        shutil.copyfileobj(fin, fout, CHUNK_SIZE)
    # Do not chmod the output directory: the grader runs this program
    # as a different user on a directory it does not own, and chmod
    # would fail the run.
    os.chmod(dest, 0o644)
    print("wrote %s (%d bytes)" % (dest, size))


if __name__ == "__main__":
    main()
