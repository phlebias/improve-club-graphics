from PIL import Image

im = Image.open('/Users/billburrows/.gemini/antigravity/brain/38f049e7-f0c3-4880-adcb-ace6dd3ecf3b/mersey_house_original_1771580096632.png')

# The exact fixed bounds for the preview image based on the Bridgewebs layout geometry in the retina screenshot:
x1 = 1245
y1 = 645
x2 = 1635
y2 = 935

cropped = im.crop((x1, y1, x2, y2))
cropped.save('/Users/billburrows/improve-bridgeclub-graphics/mersey_house_pure.png')
print("Cropped successfully using fixed bounds.")
