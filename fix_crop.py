from PIL import Image

im = Image.open('/Users/billburrows/.gemini/antigravity/brain/38f049e7-f0c3-4880-adcb-ace6dd3ecf3b/mersey_house_original_1771580096632.png')
pixels = im.load()
width, height = im.size

# Look for the top-left corner of the actual photo
# It appears in the lower right half. Let's find it by looking for non-uniform pixels.
# Based on the previous incorrect crop, the top left of the photo is further down and right.

# A more robust way is to scan rows for significant color variation
best_top = height
best_bottom = 0
best_left = width
best_right = 0

bg_color = pixels[10, height - 10]
def is_bg(pixel):
    return abs(pixel[0] - bg_color[0]) < 10 and abs(pixel[1] - bg_color[1]) < 10 and abs(pixel[2] - bg_color[2]) < 10

# Scan to find the bounding box of the non-background stuff in the bottom half
for y in range(height//2, height):
    row_has_img = False
    for x in range(width//2, width):
        if not is_bg(pixels[x,y]):
            # This is not background
            if x < best_left: best_left = x
            if x > best_right: best_right = x
            row_has_img = True
    if row_has_img:
        if y < best_top: best_top = y
        if y > best_bottom: best_bottom = y

# The image might have a small border or drop shadow.
if best_right > best_left and best_bottom > best_top:
    print(f"Discovered bounds: {best_left}, {best_top}, {best_right}, {best_bottom}")
    img_only = im.crop((best_left, best_top, best_right, best_bottom))
    img_only.save('/Users/billburrows/improve-bridgeclub-graphics/mersey_house_pure.png')
else:
    print("Could not find image bounds")
