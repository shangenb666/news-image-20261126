# Notes: how this image was made and checked

## Research

The four stories were picked from live reporting on 26 November 2026
(Reuters world news summary, Bloomberg Daybreak US edition, Reuters
market coverage), all dated 24–25 November 2026 — the news cycle the
26 November edition sums up.

## Sources

- **Tariffs:** Reuters, 25 November 2026 — "US proposes new tariffs
  aimed at factory overcapacity" (Section 301 probe, 14 major trading
  partners, headline rates 20–40%, capped by deals already concluded
  or under negotiation); Bloomberg Daybreak, 25 November 2026.
- **Ras Tanura:** Reuters via LA Post/SRN, 25 November 2026 —
  Houthis claim a strike on the Ras Tanura refinery and Riyadh's
  financial district; Saudi-led coalition says four drones were shot
  down over the site; Brent settled $94.61, up 3.5%.
- **Nasdaq:** Reuters "Morning Bid", 25 November 2026, and Bloomberg —
  Nasdaq down about 4%, Nvidia down about 8.7%, Anthropic below its
  $83 IPO price as tariff fear compounds the AI selloff.
- **Huang:** Bloomberg Daybreak, 25 November 2026 — Huang apologised
  to employees after returning 11 days after his ouster; Trump said a
  pardon was "always an option" though unnecessary; Huang faces
  Congress over dealings with suspected Chinese spy Alice Wang.

## Corrections made before submission

1. The first draft's Nvidia panel said Huang "resigns". That is
   backwards: he was ousted earlier in November and RETURNED. The
   panel was redrawn as "HUANG RETURNS TO NVIDIA".
2. The first draft carried the Ukraine sea-drone strike on Russian
   ships off Libya (22 November, confirmed 23 November). It is not
   26 November news, and it was already used in the 24 November
   entry. The panel was replaced with the Nasdaq selloff.
3. An early draft carried invented "25%"/"30%" tariff badges. They
   were removed: no unverified figure appears as fact in the image.

## Verification

- `news.png` is 1024x1024, 468,716 bytes (under the 1 MiB limit).
- The image was read back and inspected panel by panel: all four
  captions spelled correctly, no garbled text.
- `MAKEFUN_OUTPUT_DIR=<tmp> python3 main.py` writes `entry.png`
  byte-identical to `news.png` (`cmp` clean); output dir mode 0755,
  file mode 0644.
