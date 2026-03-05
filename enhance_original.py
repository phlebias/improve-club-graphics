import sys
try:
    from PIL import Image, ImageEnhance, ImageFilter
except ImportError:
    print("Pillow not installed")
    sys.exit(1)

input_path = '/Users/billburrows/improve-bridgeclub-graphics/mersey_house_pure.png'
output_path = '/Users/billburrows/improve-bridgeclub-graphics/mersey_house_photoshop_enhanced.png'

# Load the exactly original cropped image
try:
    img = Image.open(input_path).convert('RGB')
except Exception as e:
    print(f"Error opening image: {e}")
    sys.exit(1)

# Remove the tiny light border by cropping 10px all around
img = img.crop((10, 10, img.width-10, img.height-14))

# 1. Upscale the image to make it higher resolution (3x)
new_width = img.width * 3
new_height = img.height * 3
# LANCZOS is the best resampling filter for upscaling
img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

# 2. Adjust Brightness
enhancer = ImageEnhance.Brightness(img)
img = enhancer.enhance(1.10) 

# 3. Adjust Contrast
enhancer = ImageEnhance.Contrast(img)
img = enhancer.enhance(1.20)

# 4. Adjust Color/Saturation
enhancer = ImageEnhance.Color(img)
img = enhancer.enhance(1.4)

# 5. Apply a subtle Sharpen filter to crisp up the edges now that it's larger
img = img.filter(ImageFilter.SHARPEN)

# Save the beautifully photoshopped original
img.save(output_path, quality=95)
print(f"Image beautifully enhanced and saved to {output_path}")
