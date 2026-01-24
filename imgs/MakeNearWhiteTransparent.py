
from PIL import Image

# Load image
input_path = './in.png'
im = Image.open(input_path).convert("RGBA")

# Replace white (or near-white) with transparent
datas = im.getdata()
new_data = []
for r, g, b, a in datas:
    if r > 240 and g > 240 and b > 240:   # threshold for white margin
        new_data.append((255, 255, 255, 0))  # fully transparent
    else:
        new_data.append((r, g, b, a))

im.putdata(new_data)

# Save output
output_path = './app_icon_transparent.png'
im.save(output_path, 'PNG')


