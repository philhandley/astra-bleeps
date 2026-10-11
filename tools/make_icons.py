"""Draw the Astra Bleeps app icons with Pillow: a little handheld console with a Game Boy green screen
showing a square wave, and two magenta buttons. Run: python tools/make_icons.py"""
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'assets' / 'icons'
OUT.mkdir(parents=True, exist_ok=True)
INK = (27, 27, 36)
CREAM = (236, 230, 218)
LCD = (155, 188, 15)
LCD_INK = (15, 56, 15)
LCD_LIGHT = (139, 172, 15)
A = (176, 36, 106)


def draw(size, maskable=False):
    S = 1024
    im = Image.new('RGBA', (S, S), CREAM + (255,) if maskable else (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    pad = 170 if maskable else 40
    # console body
    x0, y0, x1, y1 = pad, pad, S - pad, S - pad
    r = int((x1 - x0) * 0.16)
    if not maskable:
        d.rounded_rectangle((x0, y0, x1, y1), r, fill=INK)
        inner = 34
        d.rounded_rectangle((x0 + inner, y0 + inner, x1 - inner, y1 - inner), r - 20, fill=CREAM)
    else:
        d.rounded_rectangle((x0, y0, x1, y1), r, fill=CREAM, outline=INK, width=34)
    w = x1 - x0
    # screen bezel and LCD
    sx0, sy0 = x0 + w * 0.14, y0 + w * 0.12
    sx1, sy1 = x1 - w * 0.14, y0 + w * 0.58
    d.rounded_rectangle((sx0, sy0, sx1, sy1), int(w * 0.05), fill=(75, 75, 92))
    b = w * 0.05
    d.rectangle((sx0 + b, sy0 + b, sx1 - b, sy1 - b), fill=LCD)
    # square wave
    lx0, lx1 = sx0 + b * 1.8, sx1 - b * 1.8
    top, bot = sy0 + b * 2.2, sy1 - b * 2.2
    mid = (top + bot) / 2
    d.line((lx0, mid, lx1, mid), fill=LCD_LIGHT, width=int(w * 0.012))
    seg = (lx1 - lx0) / 4
    pts = [(lx0, bot)]
    x = lx0
    hi = True
    for i in range(4):
        y = top if hi else bot
        pts += [(x, y), (x + seg, y)]
        x += seg
        hi = not hi

    d.line(pts, fill=LCD_INK, width=int(w * 0.045), joint='curve')
    # d-pad
    cx, cy = x0 + w * 0.27, y0 + w * 0.77
    arm, th = w * 0.11, w * 0.065
    d.rounded_rectangle((cx - arm, cy - th / 2, cx + arm, cy + th / 2), int(th * 0.25), fill=INK)
    d.rounded_rectangle((cx - th / 2, cy - arm, cx + th / 2, cy + arm), int(th * 0.25), fill=INK)
    # A and B buttons
    br = w * 0.07
    for bx, by in ((x0 + w * 0.78, y0 + w * 0.72), (x0 + w * 0.6, y0 + w * 0.8)):
        d.ellipse((bx - br, by - br, bx + br, by + br), fill=A)
    return im.resize((size, size), Image.LANCZOS)


draw(512).save(OUT / 'icon-512.png')
draw(192).save(OUT / 'icon-192.png')
draw(512, maskable=True).save(OUT / 'icon-maskable-512.png')
ap = Image.new('RGBA', (180, 180), CREAM + (255,))
ap.alpha_composite(draw(180, maskable=True))
ap.convert('RGB').save(OUT / 'apple-touch-icon-180.png')
draw(32).save(OUT / 'favicon-32.png')
print('icons written to', OUT)
