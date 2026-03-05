from PIL import Image

im = Image.open('/Users/billburrows/.gemini/antigravity/brain/38f049e7-f0c3-4880-adcb-ace6dd3ecf3b/club_room_original_1771579224995.png')
# There's a small picture floating in the center of the dark frame.
# Let's crop it by finding the first vertical and horizontal lines that have color variations.
# The background is mostly solid black/dark blue. 
gray = im.convert("L")
pixels = gray.load()
width, height = gray.size

# find the center roughly
cx, cy = width//2, height//2

# Walk left from center until we hit a dark pixel (< 15)
left = cx
while left > 0 and pixels[left, cy] > 15:
    left -= 1

# Walk right
right = cx
while right < width - 1 and pixels[right, cy] > 15:
    right += 1

# Walk up
top = cy
while top > 0 and pixels[cx, top] > 15:
    top -= 1

# Walk down
bottom = cy
while bottom < height - 1 and pixels[cx, bottom] > 15:
    bottom += 1

# Add slight padding inward to cut off antialiased edge
padding = 2
cropped = im.crop((left+padding, top+padding, right-padding, bottom-padding))
cropped.save('/Users/billburrows/improve-bridgeclub-graphics/club_room_cropped.png')
print(f"Cropped precisely to {left}, {top}, {right}, {bottom}")
