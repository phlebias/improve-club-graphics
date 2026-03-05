from PIL import Image, ImageDraw, ImageFont
import os

img_path = '/Users/billburrows/improve-bridgeclub-graphics/liverpool_wide_banner.png'
out_path = '/Users/billburrows/improve-bridgeclub-graphics/liverpool_wide_banner_with_text.png'

img = Image.open(img_path)
draw = ImageDraw.Draw(img, 'RGBA')

# Try to load a nice font
fonts_to_try = [
    '/System/Library/Fonts/SFNS.ttf',
    '/System/Library/Fonts/Helvetica.ttc',
    '/System/Library/Fonts/Supplemental/Arial Bold.ttf',
    '/Library/Fonts/Arial Bold.ttf',
    '/System/Library/Fonts/Avenir Next.ttc'
]

font = None
for f in fonts_to_try:
    if os.path.exists(f):
        try:
            font = ImageFont.truetype(f, 54)
            print(f"Loaded font: {f}")
            break
        except Exception as e:
            print(f"Failed to load {f}: {e}")

if not font:
    font = ImageFont.load_default()
    print("Fell back to default font")

text = "Liverpool Bridge Club"
left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
text_width = right - left
text_height = bottom - top

# Calculate center position
x = (img.width - text_width) / 2
y = (img.height - text_height) / 2

# Draw outline for better readability against various backgrounds
outline_color = (0, 0, 0, 255)
thickness = 2
for dx in range(-thickness, thickness + 1):
    for dy in range(-thickness, thickness + 1):
        if dx == 0 and dy == 0:
            continue
        draw.text((x + dx, y + dy), text, font=font, fill=outline_color)

# Draw drop shadow
draw.text((x + 4, y + 4), text, font=font, fill=(0, 0, 0, 180))

# Draw main text
draw.text((x, y), text, font=font, fill=(255, 255, 255, 255))

img.save(out_path)
print(f"Image saved to {out_path}")
