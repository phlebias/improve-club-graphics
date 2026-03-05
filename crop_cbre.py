from PIL import Image

src = '/Users/billburrows/.gemini/antigravity/brain/38f049e7-f0c3-4880-adcb-ace6dd3ecf3b/mersey_house_hero_cbre_1771582121043.png'
dest = '/Users/billburrows/improve-bridgeclub-graphics/mersey_house_cbre_clean.png'

im = Image.open(src)
width, height = im.size

# The arrow is on the left, let's crop 80 pixels from the left and right to be safe.
# And maybe 20 pixels from top and bottom.
left = 80
right = width - 80
top = 0
bottom = height

cropped = im.crop((left, top, right, bottom))
cropped.save(dest)
print(f"Cropped to {width-160}x{height}")
