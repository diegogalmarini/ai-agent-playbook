"""Carrusel v2: papel, tinta y una anotación a mano. Menos plantilla, más cuaderno."""
import math, random, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1350
PAPER = (246, 242, 233)
INK = (28, 28, 30)
GREY = (110, 106, 98)
RULE = (222, 215, 200)
MARK = (196, 62, 38)      # rotulador rojo
GREEN = (46, 125, 80)

CR = "/usr/share/fonts/truetype/google-fonts/ofl/crimsontext/"
IN = "/usr/share/fonts/opentype/inter/"
def f(path, size): return ImageFont.truetype(path, size)
SERIF_B = lambda s: f(CR + "CrimsonText-Bold.ttf", s)
SERIF = lambda s: f(CR + "CrimsonText-Regular.ttf", s)
SERIF_I = lambda s: f(CR + "CrimsonText-Italic.ttf", s)
SANS = lambda s: f(IN + "Inter-Regular.otf", s)
SANS_M = lambda s: f(IN + "Inter-Medium.otf", s)
SANS_B = lambda s: f(IN + "Inter-SemiBold.otf", s)

M = 96  # margen


def paper(seed):
    rnd = random.Random(seed)
    img = Image.new("RGB", (W, H), PAPER)
    px = img.load()
    for _ in range(90000):  # grano del papel
        x, y = rnd.randrange(W), rnd.randrange(H)
        d = rnd.randint(-7, 4)
        r, g, b = px[x, y]
        px[x, y] = (r + d, g + d, b + d)
    d = ImageDraw.Draw(img)
    for y in range(250, H - 130, 56):  # renglones muy suaves
        d.line([(M, y), (W - M, y)], fill=RULE, width=1)
    return img.filter(ImageFilter.GaussianBlur(0.35))


def wrap(d, text, font, width):
    lines = []
    for para in text.split("\n"):
        words, cur = para.split(" "), ""
        for w in words:
            t = (cur + " " + w).strip()
            if d.textlength(t, font=font) <= width:
                cur = t
            else:
                lines.append(cur); cur = w
        lines.append(cur)
    return lines


def text(d, xy, s, font, fill=INK, width=W - 2 * M, lh=1.25):
    x, y = xy
    for line in wrap(d, s, font, width):
        d.text((x, y), line, font=font, fill=fill)
        y += int(font.size * lh)
    return y


def wobble(d, pts, rnd, fill=MARK, width=6):
    """Trazo de rotulador: puntos con un temblor pequeño."""
    out = [(x + rnd.uniform(-2, 2), y + rnd.uniform(-2, 2)) for x, y in pts]
    d.line(out, fill=fill, width=width, joint="curve")


def underline(d, x0, x1, y, rnd):
    pts = [(x0 + (x1 - x0) * t / 20, y + math.sin(t / 3) * 3) for t in range(21)]
    wobble(d, pts, rnd)


def circle(d, cx, cy, rx, ry, rnd):
    pts = []
    for i in range(80):
        a = -0.3 + i / 74 * 2 * math.pi  # se pasa un poco, como a mano
        k = 1 + rnd.uniform(-0.03, 0.03)
        pts.append((cx + rx * k * math.cos(a), cy + ry * k * math.sin(a)))
    wobble(d, pts, rnd, width=5)


def footer(d, n, total):
    y = H - 92
    d.line([(M, y - 26), (W - M, y - 26)], fill=INK, width=2)
    d.text((M, y), "Diego Galmarini", font=SANS_B(24), fill=INK)
    w = d.textlength("Diego Galmarini", font=SANS_B(24))
    d.text((M + w + 14, y), "·  VER AI Labs", font=SANS(24), fill=GREY)
    s = f"{n}/{total}" + ("   →" if n < total else "")
    d.text((W - M - d.textlength(s, font=SANS_M(24)), y), s, font=SANS_M(24), fill=INK)


def kicker(d, s, y=120):
    d.text((M, y), s.upper(), font=SANS_B(24), fill=MARK, spacing=4)


MONO = lambda s: f("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", s)


def cover(kicker_t, title, sub, body, swipe="Desliza  →", tsize=150):
    def p(img, rnd):
        d = ImageDraw.Draw(img)
        kicker(d, kicker_t)
        y = text(d, (M, 190), title, SERIF_B(tsize), lh=1.02)
        last = title.split("\n")[-1]
        underline(d, M, M + min(d.textlength(last, font=SERIF_B(tsize)), W - 2 * M), y + 6, rnd)
        y = text(d, (M, y + 60), sub, SERIF_I(64), fill=GREY, lh=1.15)
        text(d, (M, y + 80), body, SANS(40), lh=1.4)
        d.text((M, H - 230), swipe, font=SANS_M(32), fill=MARK)
    return p


def score(kicker_t, rows, note, ring=None, big=130):
    """rows: (etiqueta, valor, color). ring: índice de la fila que se rodea."""
    def p(img, rnd):
        d = ImageDraw.Draw(img)
        kicker(d, kicker_t)
        y = 280
        gap = 260 if len(rows) <= 2 else 220
        for k, (label, val, col) in enumerate(rows):
            fx = SERIF_B(big)
            wx = d.textlength(val, font=fx)
            text(d, (M, y), label, SERIF(52), width=W - 2 * M - wx - 40, lh=1.1)
            d.text((W - M - wx, y - big * 0.38), val, font=fx, fill=col)
            if ring == k:
                circle(d, W - M - wx / 2, y + big * 0.22, wx / 2 + 40, big * 0.6, rnd)
            y += gap
            d.line([(M, y - 45), (W - M, y - 45)], fill=RULE, width=2)
        text(d, (M, y + 40), note, SERIF_I(54), fill=MARK, lh=1.2)
    return p


def listing(kicker_t, items, right=None, note=None, size=70):
    def p(img, rnd):
        d = ImageDraw.Draw(img)
        kicker(d, kicker_t)
        y = 230
        for i, n in enumerate(items, 1):
            d.text((M, y), f"0{i}", font=SANS_M(30), fill=GREY)
            d.text((M + 90, y - 18), n, font=SERIF_B(size), fill=INK)
            if right:
                d.text((W - M - d.textlength(right, font=SANS(30)), y), right, font=SANS(30), fill=GREEN)
            y += 165
        if note:
            text(d, (M, y + 20), note, SANS(34), fill=GREY, lh=1.4)
    return p


def quote(kicker_t, strong, rest, tail):
    def p(img, rnd):
        d = ImageDraw.Draw(img)
        kicker(d, kicker_t)
        d.text((M - 10, 170), "“", font=SERIF_B(260), fill=MARK)
        y = text(d, (M, 420), strong, SERIF_B(84), lh=1.1)
        y = text(d, (M, y + 30), rest, SERIF(64), lh=1.18)
        if tail:
            text(d, (M, y + 60), tail, SERIF_I(58), fill=MARK, lh=1.2)
    return p


def steps(kicker_t, items, mark_first=True, start=1):
    def p(img, rnd):
        d = ImageDraw.Draw(img)
        kicker(d, kicker_t)
        y = 240
        gap = 320 if len(items) <= 3 else 245
        for i, (t, s) in enumerate(items, 1):
            d.text((M, y - 20), str(i + start - 1), font=SERIF_B(150 if len(items) <= 3 else 120), fill=MARK)
            yy = text(d, (M + 130, y + 10), t, SERIF_B(58), width=W - 2 * M - 130, lh=1.08)
            text(d, (M + 130, yy + 10), s, SANS(32), fill=GREY, width=W - 2 * M - 130, lh=1.35)
            if i == 1 and mark_first:
                underline(d, M + 130, M + 130 + min(d.textlength(t, font=SERIF_B(58)), 560), y + 82, rnd)
            y += gap
    return p


def code(kicker_t, title, src, note):
    def p(img, rnd):
        d = ImageDraw.Draw(img)
        kicker(d, kicker_t)
        y = text(d, (M, 190), title, SERIF_B(80), lh=1.05)
        box_top = y + 30
        lines = src.split("\n")
        box_h = 60 + len(lines) * 50
        d.rounded_rectangle([M, box_top, W - M, box_top + box_h], radius=18, fill=(255, 253, 247), outline=INK, width=2)
        yy = box_top + 32
        for ln in lines:
            col = GREY if ln.strip().startswith("#") else INK
            d.text((M + 40, yy), ln, font=MONO(32), fill=col)
            yy += 50
        text(d, (M, box_top + box_h + 50), note, SERIF_I(50), fill=MARK, lh=1.2)
    return p


def closing(kicker_t, question, body, tail):
    def p(img, rnd):
        d = ImageDraw.Draw(img)
        kicker(d, kicker_t)
        y = text(d, (M, 330), question, SERIF_B(92), lh=1.08)
        text(d, (M, y + 70), body, SANS(40), fill=GREY, lh=1.45)
        d.text((M, H - 230), tail, font=SERIF_I(48), fill=MARK)
    return p


def render(name, pages, outdir="v2out"):
    imgs = []
    for i, page in enumerate(pages, 1):
        img = paper(i * 7 + len(name))
        page(img, random.Random(100 + i))
        footer(ImageDraw.Draw(img), i, len(pages))
        img.save(f"{outdir}/{name}-{i}.png")
        imgs.append(img)
    imgs[0].save(f"{outdir}/{name}.pdf", save_all=True, append_images=imgs[1:], resolution=150)
    sheet = Image.new("RGB", (360 * min(3, len(imgs)), 450 * math.ceil(len(imgs) / 3)), "white")
    for k, im in enumerate(imgs):
        sheet.paste(im.resize((360, 450)), ((k % 3) * 360, (k // 3) * 450))
    sheet.save(f"{outdir}/{name}-sheet.png")
    return f"{outdir}/{name}.pdf"
