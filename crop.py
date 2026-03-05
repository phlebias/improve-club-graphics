from PIL import Image

im = Image.open('/Users/billburrows/.gemini/antigravity/brain/38f049e7-f0c3-4880-adcb-ace6dd3ecf3b/club_room_original_1771579224995.png')
# Find the image in the center. Let's look for the bounds by ignoring dark pixels.
gray = im.convert("L")
pixels = gray.load()
width, height = gray.size

# Find left
left = 0
for x in range(width):
    # Check if there's any bright pixel in this column (between top 10% and bottom 10% to avoid borders)
    if any(pixels[x, y] > 50 for y in range(int(height*0.1), int(height*0.9))):
        left = x
        break

right = width - 1
for x in range(width - 1, -1, -1):
    if any(pixels[x, y] > 50 for y in range(int(height*0.1), int(height*0.9))):
        right = x
        break

top = 0
for y in range(height):
    if any(pixels[x, y] > 50 for x in range(left, right)):
        top = y
        break

bottom = height - 1
for y in range(height - 1, -1, -1):
    if any(pixels[x, y] > 50 for x in range(left, right)):
        bottom = y
        break

cropped = im.crop((left, top, right, bottom))
cropped.save('/Users/billburrows/improve-bridgeclub-graphics/club_room_cropped.png')
print(f"Cropped to {left}, {top}, {right}, {bottom}")
