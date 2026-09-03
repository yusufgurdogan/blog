"""Generate 1200x630 Open Graph cards for every post, plus a site default.

Usage:  python scripts/og_images.py
Needs:  Pillow, and the two font files in scripts/fonts/ (Literata and
        JetBrains Mono variable TTFs from Google Fonts).

Writes assets/og/<post-file-stem>.png and assets/og/default.png, and adds
`image: /assets/og/<stem>.png` to each post's front matter if missing.
"""
import re
import sys
from datetime import date
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "_posts"
OUT = ROOT / "assets" / "og"
FONTS = Path(__file__).resolve().parent / "fonts"

W, H = 1200, 630
BG = (247, 244, 237)      # warm cream
INK = (28, 26, 24)
ACCENT = (229, 176, 76)   # amber band
BAND_INK = (24, 20, 12)
BAND_H = 110
PAD = 80

SITE = "yusufgurdogan.com"
AUTHOR = "Yusuf Gürdoğan"


def font(name, size, weight):
    f = ImageFont.truetype(str(FONTS / name), size)
    try:
        axes = f.get_variation_axes()
        vals = []
        for a in axes:
            tag = a.get("tag") or a.get("name", b"").decode(errors="ignore")
            if tag in ("wght", "Weight"):
                vals.append(weight)
            elif tag in ("opsz", "Optical size", "Optical Size"):
                vals.append(min(a["maximum"], max(a["minimum"], size)))
            else:
                vals.append(a["default"])
        f.set_variation_by_axes(vals)
    except Exception:
        pass
    return f


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def card(title, meta_left, meta_right):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # amber band along the bottom carrying the meta line
    d.rectangle((0, H - BAND_H, W, H), fill=ACCENT)

    # title, shrink until it fits in 4 lines
    size = 84
    while True:
        tf = font("Literata.ttf", size, 700)
        lines = wrap(d, title, tf, W - 2 * PAD)
        if len(lines) <= 4 or size <= 44:
            break
        size -= 6
    line_h = int(size * 1.12)
    y = (H - BAND_H - line_h * len(lines)) // 2
    for ln in lines:
        d.text((PAD, y), ln, font=tf, fill=INK)
        y += line_h

    mf = font("JetBrainsMono.ttf", 24, 600)
    ty = H - BAND_H + (BAND_H - 28) // 2
    d.text((PAD, ty), meta_left.upper(), font=mf, fill=BAND_INK)
    tw = d.textlength(meta_right.upper(), font=mf)
    d.text((W - PAD - tw, ty), meta_right.upper(), font=mf, fill=BAND_INK)
    return img


def parse_front_matter(text):
    m = re.match(r"^---\r?\n([\s\S]*?)\r?\n---\r?\n", text)
    return m


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    only = set(sys.argv[1:])

    card(AUTHOR, SITE, "").save(OUT / "default.png", optimize=True)
    print("default.png")

    for md in sorted(POSTS.glob("*.md")):
        if only and md.name not in only:
            continue
        text = md.read_text(encoding="utf-8")
        fm = parse_front_matter(text)
        if not fm:
            continue
        head = fm.group(1)
        t = re.search(r'^title:\s*"?(.*?)"?\s*$', head, re.M)
        title = t.group(1) if t else md.stem
        dm = re.match(r"(\d{4})-(\d{2})-(\d{2})-", md.name)
        when = date(int(dm.group(1)), int(dm.group(2)), int(dm.group(3))).strftime("%B %d, %Y")
        stem = md.stem.translate(str.maketrans("çğıöşüÇĞİÖŞÜ", "cgiosuCGIOSU"))
        stem = re.sub(r"[^A-Za-z0-9]+", "-", stem).strip("-").lower()
        out = OUT / f"{stem}.png"
        card(title, SITE, when).save(out, optimize=True)
        print(out.name)

        if not re.search(r"^image:", head, re.M):
            new_head = head + f"\nimage: /assets/og/{stem}.png"
            text = text[: fm.start(1)] + new_head + text[fm.end(1):]
            md.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
