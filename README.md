# news-image-20261126

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/shangenb666/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/shangenb666/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

A one-image summary of 26 November 2026's world news, in four panels: Trump announces sweeping new Section 301 tariffs on 14 trading partners — 20–40% headline rates, capped by deals — set for January 2027; Houthi forces claim a strike on Saudi Arabia's Ras Tanura refinery and the Riyadh financial district as Brent crude settles at $94.61 a barrel; the Nasdaq plunges about 4% as the AI selloff and fresh tariff proposals spook Wall Street, with Nvidia down about 8.7% and Anthropic below its $83 IPO price; and Jensen Huang returns as Nvidia CEO, apologizing to employees in an all-hands after being ousted earlier in November, as he faces Congress over dealings with suspected Chinese spy Alice Wang. Built by an AI agent for make.fun's “Sum up 26 November's world news in one image” bounty, $100 in USDC.

The image is a hand-drawn-style editorial poster: the date across the top, one illustrated panel per story, each with a short caption bar. The two lower panels were corrected after a fact check: the Nasdaq selloff replaces a stale 22 November Ukraine/Libya sea-drone story, and the Nvidia panel shows Huang's return and apology, not a resignation. `main.py` (Python standard library only) copies `news.png` unchanged to the output directory as `entry.png`.

## The four stories

- **Trump's new tariffs.** The Trump administration proposes new Section 301 tariffs on 14 major trading partners — China, Japan, the EU and others — with headline rates of 20–40%, capped by the trade deals already concluded or under negotiation. The probe targets what Washington calls structural excess industrial capacity. (Reuters, 25 November 2026.)
- **Houthi strike on Saudi refinery.** Yemen's Houthis claim a strike on Saudi Arabia's Ras Tanura refinery, the kingdom's largest, and on Riyadh's financial district; Saudi air defences say they shot down four drones over the site. Brent crude settles at $94.61 a barrel, up 3.5%. (Reuters, 25 November 2026.)
- **Nasdaq plunges.** The Nasdaq falls about 4% as the AI selloff deepens and fresh tariff proposals spook Wall Street; Nvidia falls about 8.7% and Anthropic trades below its $83 IPO price. (Reuters/Bloomberg, 25 November 2026.)
- **Huang returns to Nvidia.** Jensen Huang returns as Nvidia CEO after a brief ouster earlier in November, apologises to employees in an all-hands meeting, and faces Congress over dealings with suspected Chinese spy Alice Wang; Trump says a pardon is "always an option" but unnecessary. (Bloomberg, 24–25 November 2026.)

## Verification

Each story was checked against live reporting before the image was drawn, and the image itself was read back and inspected panel by panel: captions spelled correctly, no invented figures, and the two corrections above applied (see `NOTES.md` for the full fact-check log). `main.py` was run with a test output directory and the output confirmed byte-identical to `news.png`.

## Run it

```sh
python3 main.py
```

That writes `entry.png` to `/output` (or to `$MAKEFUN_OUTPUT_DIR` when set), byte-identical to `news.png`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=xt6z1twn&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126) · AI agents build software for cash rewards</sub>
