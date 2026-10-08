"""Draw the five symbolic government buttons at their native 64px size.

Run: .venv-art/Scripts/python.exe art/civics/draw_government.py
Uses pixel primitives and deterministic shading, no image generation service.
"""
from math import sqrt
from pathlib import Path

from PIL import Image, ImageDraw

from draw_monarchy import render as monarchy

ROOT = Path(__file__).resolve().parents[2]
ART = Path(__file__).resolve().parent
DEST = ROOT / "RFC MP Plus/Assets/Art/Interface/Buttons/Civics/RFCMP"


def background(base, glow):
    im = Image.new("RGBA", (64, 64))
    for y in range(64):
        for x in range(64):
            light = max(0, 1 - sqrt(((x - 29) / 39.0) ** 2 + ((y - 26) / 44.0) ** 2))
            grain = (x * 17 + y * 31 + x * y * 7) % 7 - 3
            im.putpixel((x, y), tuple(max(0, int(b + g * light) + grain) for b, g in zip(base, glow)) + (255,))
    return im


def tribal():
    im = background((11, 19, 15), (31, 31, 14))
    d = ImageDraw.Draw(im)
    # Crossed wooden spears and flint heads behind the community hearth.
    for points in [[(15, 13), (48, 53)], [(48, 13), (15, 53)]]:
        d.line(points, fill=(32, 23, 12), width=5)
        d.line(points, fill=(145, 97, 46), width=3)
        d.line([(points[0][0] - 1, points[0][1]), (points[1][0] - 1, points[1][1])], fill=(201, 151, 78))
    d.polygon([(9, 5), (20, 12), (14, 19)], fill=(150, 156, 145), outline=(50, 58, 50))
    d.polygon([(9, 5), (14, 14), (17, 12)], fill=(221, 217, 180))
    d.polygon([(54, 5), (43, 12), (49, 19)], fill=(136, 146, 133), outline=(50, 58, 50))
    d.polygon([(54, 5), (49, 13), (46, 12)], fill=(221, 217, 180))
    for x, y in [(17, 17), (45, 17)]:
        d.line([(x - 2, y), (x + 2, y + 3)], fill=(226, 190, 119), width=2)
    d.ellipse((10, 47, 54, 58), fill=(12, 13, 11))
    # A stone ring, with embers and two crossed logs.
    for box in [(10, 49, 18, 55), (17, 53, 25, 58), (28, 54, 37, 59), (40, 52, 48, 57), (47, 47, 54, 53)]:
        d.ellipse(box, fill=(103, 100, 78), outline=(40, 45, 36))
        d.line([(box[0] + 2, box[1] + 1), (box[2] - 2, box[1] + 1)], fill=(151, 142, 109))
    d.line([(18, 46), (43, 53)], fill=(67, 34, 15), width=5)
    d.line([(20, 51), (43, 45)], fill=(114, 53, 20), width=5)
    d.line([(20, 50), (43, 44)], fill=(184, 99, 37))
    d.polygon([(20, 46), (18, 35), (24, 39), (25, 25), (30, 29), (33, 16), (37, 28), (43, 25), (40, 38), (46, 34), (43, 46), (32, 51)], fill=(173, 52, 18))
    d.polygon([(23, 44), (22, 37), (27, 40), (28, 29), (33, 33), (34, 24), (38, 35), (40, 32), (38, 44), (32, 48)], fill=(246, 143, 33))
    d.polygon([(28, 43), (30, 35), (33, 40), (35, 32), (36, 44), (32, 47)], fill=(255, 224, 112))
    for point in [(30, 13), (38, 18), (23, 23)]:
        d.point(point, fill=(243, 170, 64))
    return im


def republic():
    im = background((15, 18, 24), (35, 36, 40))
    d = ImageDraw.Draw(im)
    # A senate portico: pediment, three carved columns, and stone steps.
    d.polygon([(9, 24), (31, 9), (54, 24)], fill=(75, 70, 58), outline=(31, 34, 36))
    d.polygon([(13, 22), (31, 11), (50, 22)], fill=(193, 183, 145))
    d.polygon([(20, 21), (31, 14), (42, 21)], fill=(115, 110, 92))
    d.line([(12, 23), (51, 23)], fill=(242, 224, 174), width=2)
    d.rectangle((13, 26, 50, 47), fill=(30, 31, 34))
    for x in (16, 29, 42):
        d.rectangle((x - 2, 25, x + 8, 28), fill=(208, 192, 149))
        d.rectangle((x, 29, x + 5, 46), fill=(161, 153, 126))
        d.line([(x, 29), (x, 45)], fill=(235, 219, 174))
        d.line([(x + 3, 29), (x + 3, 45)], fill=(111, 108, 95))
        d.rectangle((x - 2, 46, x + 7, 48), fill=(206, 192, 152))
    d.rectangle((11, 49, 53, 51), fill=(156, 150, 126))
    d.rectangle((8, 52, 56, 54), fill=(111, 112, 102))
    # Olive branches frame the civic assembly without depicting a ruler.
    for side in (-1, 1):
        pts = [(32 + side * 27, 49), (32 + side * 28, 37), (32 + side * 25, 27)]
        d.line(pts, fill=(155, 130, 66))
        for y in (31, 37, 43, 49):
            x = 32 + side * 25
            d.polygon([(x, y), (x + side * 3, y - 5), (x + side * 5, y - 3), (x + side * 2, y + 1)], fill=(124, 143, 75))
    return im


def dictatorship():
    im = background((23, 11, 16), (44, 16, 17))
    d = ImageDraw.Draw(im)
    # Crimson standard behind an iron gauntlet: concentrated coercive authority.
    d.polygon([(12, 8), (50, 8), (50, 54), (31, 46), (12, 54)], fill=(109, 25, 32), outline=(40, 13, 18))
    d.line([(13, 9), (48, 9)], fill=(187, 58, 49))
    d.line([(16, 12), (16, 48)], fill=(134, 34, 38))
    d.line([(47, 12), (47, 49)], fill=(74, 20, 29))
    # Cuff, wrist, and broad clenched fist, made of distinct metal plates.
    d.polygon([(22, 38), (42, 38), (43, 57), (20, 57)], fill=(38, 43, 50), outline=(13, 17, 22))
    d.polygon([(24, 38), (38, 38), (39, 51), (22, 51)], fill=(112, 120, 123))
    d.line([(24, 39), (23, 50)], fill=(201, 206, 188))
    d.rectangle((20, 51, 43, 56), fill=(65, 72, 82), outline=(27, 32, 42))
    d.line([(21, 51), (42, 51)], fill=(183, 190, 179))
    d.polygon([(18, 22), (23, 17), (39, 16), (45, 21), (44, 32), (39, 42), (25, 42), (18, 33)], fill=(91, 101, 111), outline=(18, 23, 32))
    for x, y in [(20, 21), (26, 18), (32, 17), (38, 19)]:
        d.rounded_rectangle((x, y, x + 6, y + 13), radius=2, fill=(146, 154, 154), outline=(47, 55, 67))
        d.line([(x + 1, y + 2), (x + 4, y + 2)], fill=(223, 224, 199))
        d.line([(x + 1, y + 8), (x + 4, y + 8)], fill=(76, 86, 99))
    d.polygon([(19, 31), (22, 27), (30, 28), (34, 33), (31, 37), (23, 35)], fill=(176, 181, 174), outline=(44, 53, 67))
    d.line([(22, 28), (28, 29), (32, 32)], fill=(228, 226, 199))
    d.line([(27, 40), (37, 40)], fill=(45, 56, 72))
    for x in (23, 39):
        d.point((x, 54), fill=(201, 197, 153))
    return im


def democracy():
    im = background((10, 20, 25), (25, 42, 41))
    d = ImageDraw.Draw(im)
    # Wooden ballot box, with a single conspicuous marked ballot.
    d.ellipse((10, 51, 57, 59), fill=(7, 15, 18))
    d.polygon([(11, 33), (43, 29), (54, 36), (22, 41)], fill=(182, 126, 59), outline=(39, 31, 24))
    d.polygon([(12, 34), (22, 41), (22, 56), (12, 49)], fill=(79, 55, 32))
    d.polygon([(22, 41), (54, 36), (54, 51), (22, 56)], fill=(137, 90, 43), outline=(43, 34, 25))
    d.line([(23, 42), (52, 38)], fill=(220, 165, 85))
    d.line([(24, 54), (52, 50)], fill=(75, 54, 33))
    for y in (45, 49):
        d.line([(24, y), (51, y - 4)], fill=(109, 71, 36))
    d.line([(20, 35), (42, 32)], fill=(32, 27, 22), width=3)
    d.line([(21, 37), (43, 34)], fill=(225, 166, 80))
    # Tilted ivory paper, with a dark green check mark and folded corner.
    d.polygon([(22, 7), (44, 11), (39, 34), (18, 30)], fill=(81, 78, 62))
    d.polygon([(21, 6), (43, 10), (38, 33), (17, 29)], fill=(228, 218, 175), outline=(73, 73, 60))
    d.polygon([(21, 7), (37, 10), (35, 30), (18, 28)], fill=(247, 238, 197))
    d.polygon([(37, 9), (43, 10), (42, 15)], fill=(176, 168, 135))
    d.line([(25, 18), (28, 23), (36, 14)], fill=(35, 96, 71), width=3)
    d.line([(23, 26), (33, 28)], fill=(147, 141, 114))
    # Brass lock plate, a restrained small detail on the box front.
    d.rectangle((35, 44, 40, 49), fill=(190, 155, 72), outline=(87, 66, 33))
    d.point((37, 46), fill=(48, 39, 24))
    d.point((37, 47), fill=(48, 39, 24))
    return im


def main():
    with Image.open(ROOT / "RFC MP Plus/Assets/Art/Interface/Buttons/civics_civilizations_religions_atlas.dds") as atlas:
        alpha = atlas.convert("RGBA").crop((0, 0, 64, 64)).getchannel("A")
    icons = [("Tribal_System", tribal()), ("Monarchy", monarchy()),
             ("Republic", republic()), ("Dictatorship", dictatorship()),
             ("Democracy", democracy())]
    preview = Image.new("RGB", (960, 225), (23, 26, 32))
    draw = ImageDraw.Draw(preview)
    for index, (name, icon) in enumerate(icons):
        icon.putalpha(alpha)
        # Keep the illustrated edge dark; Civ4 supplies its own selection frame.
        icon.save(ART / (name.lower().replace("_", "-") + "-pixel.png"))
        icon.save(DEST / (name + ".dds"), pixel_format="DXT3")
        with Image.open(DEST / (name + ".dds")) as game:
            enlarged = game.convert("RGBA").resize((180, 180), Image.Resampling.NEAREST)
            preview.paste(enlarged, (index * 192 + 6, 7), enlarged)
            if name == "Monarchy":
                game.resize((384, 384), Image.Resampling.NEAREST).save(ART / "monarchy-pixel-preview.local.png")
        draw.text((index * 192 + 96, 198), name.replace("_", " "), fill=(230, 225, 208), anchor="mt")
    preview.save(ART / "government-pixel-preview.png")
    # Refresh the government column in the existing full civic contact sheet.
    if (ART / "preview.png").exists():
        with Image.open(ART / "preview.png") as original:
            sheet = original.convert("RGB")
        for index, (name, _) in enumerate(icons):
            with Image.open(DEST / (name + ".dds")) as game:
                thumb = game.convert("RGBA").resize((96, 96), Image.Resampling.NEAREST)
                ImageDraw.Draw(sheet).rectangle((16, index * 140 + 10, 111, index * 140 + 105), fill=(22, 27, 38))
                sheet.paste(thumb, (16, index * 140 + 10), thumb)
        sheet.save(ART / "preview.png")
    print("Created five symbolic 64 x 64 DXT3 government icons with original rounded alpha.")


if __name__ == "__main__":
    main()
