import os
from PIL import Image

images = [f for f in os.listdir('IMAGES') if f.lower().endswith(('.webp', '.jpg', '.png'))]
for img_name in sorted(images):
    path = os.path.join('IMAGES', img_name)
    try:
        with Image.open(path) as im:
            print(f"{img_name}: {im.size}, {im.format}")
    except Exception as e:
        print(f"{img_name}: err {e}")
