from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

img_path = '/Users/billburrows/improve-bridgeclub-graphics/liverpool_wide_banner.png'
out_path = '/Users/billburrows/improve-bridgeclub-graphics/liverpool_wide_banner_premium_label.png'

# Load original image
img = Image.open(img_path).convert('RGBA')

# Create a transparent overlay for the dark gradient
overlay = Image.new('RGBA', img.size, (0, 0, 0, 0))
draw_overlay = ImageDraw.Draw(overlay)

# Navy blue overlay matching the new site style (rgb 28, 69, 135)
gradient_height = 110
y_start = (img.height - gradient_height) // 2
draw_overlay.rectangle(
    [0, y_start, img.width, y_start + gradient_height],
    fill=(28, 69, 135, 190)  # Semi-transparent navy
)

# Merge overlay
img = Image.alpha_composite(img, overlay)
draw = ImageDraw.Draw(img)

# Try to load modern fonts
fonts_to_try = [
    '/System/Library/Fonts/Helvetica.ttc',
    '/System/Library/Fonts/SFNS.ttf',
    '/Library/Fonts/Arial.ttf'
]

title_font = None
sub_font = None
for f in fonts_to_try:
    if os.path.exists(f):
        try:
            # Try to load Helvetica or Arial
            title_font = ImageFont.truetype(f, 54, index=1) if f.endswith('.ttc') else ImageFont.truetype(f, 54)
            sub_font = ImageFont.truetype(f, 24, index=0) if f.endswith('.ttc') else ImageFont.truetype(f, 24)
            break
        except Exception:
            pass

if not title_font:
    title_font = ImageFont.load_default()
    sub_font = ImageFont.load_default()

text_title = "Liverpool Bridge Club"
text_subtitle = "Want to play Bridge? We will teach you!"

# Get bounding boxes to center text
left_t, top_t, right_t, bottom_t = draw.textbbox((0, 0), text_title, font=title_font)
title_w = right_t - left_t
title_h = bottom_t - top_t

left_s, top_s, right_s, bottom_s = draw.textbbox((0, 0), text_subtitle, font=sub_font)
sub_w = right_s - left_s
sub_h = bottom_s - top_s

# Calculate positions (vertically stacked and centered)
total_text_h = title_h + sub_h + 10 # 10px spacing
y_content_start = y_start + (gradient_height - total_text_h) / 2 - 4

x_title = (img.width - title_w) / 2
y_title = y_content_start

x_sub = (img.width - sub_w) / 2
y_sub = y_title + title_h + 10

# Soft shadows
draw.text((x_title + 2, y_title + 2), text_title, font=title_font, fill=(0, 0, 0, 180))
draw.text((x_sub + 1, y_sub + 1), text_subtitle, font=sub_font, fill=(0, 0, 0, 180))

# Main text in bright white
draw.text((x_title, y_title), text_title, font=title_font, fill=(255, 255, 255, 255))
# Subtitle in a slightly softer off-white or light grey
draw.text((x_sub, y_sub), text_subtitle, font=sub_font, fill=(240, 240, 245, 255))

# Save image as PNG
img = img.convert('RGB')
img.save(out_path)
print(f"Image saved to {out_path}")
