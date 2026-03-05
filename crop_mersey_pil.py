from PIL import Image

im = Image.open('/Users/billburrows/.gemini/antigravity/brain/38f049e7-f0c3-4880-adcb-ace6dd3ecf3b/mersey_house_original_1771580096632.png')
pixels = im.load()
width, height = im.size

# Background is exactly or very close to (236, 240, 237)
bg_color = pixels[10, 800]

def is_diff(p1, p2, tol=15):
    return abs(p1[0]-p2[0]) > tol or abs(p1[1]-p2[1]) > tol or abs(p1[2]-p2[2]) > tol

cx = width // 2
cy = 450 # Below texts

# search downwards for the top edge
top = cy
while top < height and not is_diff(pixels[cx, top], bg_color):
    top += 1

# search upwards for bottom edge
bottom = 800
while bottom > top and not is_diff(pixels[cx, bottom], bg_color):
    bottom -= 1

# search right for left edge
left = 500
while left < cx and not is_diff(pixels[left, top+20], bg_color):
    left += 1

# search left for right edge
right = 1400
while right > cx and not is_diff(pixels[right, top+20], bg_color):
    right -= 1

print(f"Cropped to {left}, {top}, {right}, {bottom}")
if right > left and bottom > top:
    cropped = im.crop((left, top, right, bottom))
    cropped.save('/Users/billburrows/improve-bridgeclub-graphics/mersey_house_cropped.png')
else:
    print("Invalid crop dimensions")
