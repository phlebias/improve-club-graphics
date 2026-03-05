from PIL import Image

im = Image.open('/Users/billburrows/.gemini/antigravity/brain/38f049e7-f0c3-4880-adcb-ace6dd3ecf3b/mersey_house_original_1771580096632.png')
# Crop out roughly the central image 
# from the screenshot it's around cx, cy
width, height = im.size
# Looking at the screenshot visually it's roughly in the center bottom half.
# Let's find exactly the image boundaries.
# The background is a light off-white color. The image is a distinct block.
# Actually I'll just use fixed coordinates since the image is 1920x1080
# The image size says 192x144, but the web page might scale it.
# Let's write a script that finds the "photo" region by looking for non-background colors.

def get_crop_box():
    # approximate center of screen
    cx, cy = 960, 540
    # the image is located approximately below the text.
    # We can search for the first row of pixels that has significant color variance.
    pass

# Or just use PIL to crop it based on the prominent rectangle in the lower half
import cv2
import numpy as np

img_cv = cv2.imread('/Users/billburrows/.gemini/antigravity/brain/38f049e7-f0c3-4880-adcb-ace6dd3ecf3b/mersey_house_original_1771580096632.png')
gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)

# Threshold to find non-background
# Background is around 240-245
_, thresh = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY_INV)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Find the largest contour that is roughly 192x144 or proportional
best_box = None
max_area = 0

for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    # The image is horizontally wide, and area should be decent
    if w > 100 and h > 80 and w < 1000 and y > 300: # Below the top headers
        area = w * h
        if area > max_area:
            max_area = area
            best_box = (x, y, w, h)

if best_box:
    x, y, w, h = best_box
    print(f"Cropping at {x}, {y}, {w}, {h}")
    cropped = im.crop((x, y, x+w, y+h))
    cropped.save('/Users/billburrows/improve-bridgeclub-graphics/mersey_house_cropped.png')
else:
    print("Could not find box")
