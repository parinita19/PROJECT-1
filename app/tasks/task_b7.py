from PIL import Image
import os
from app.config import DATA_DIR

def run() -> str:
    """
    B7: Resize an image located at /data/original_image.png to 50% of its size
    and save the result as /data/resized_image.png.
    """
    original_path = os.path.join(DATA_DIR, "original_image.png")
    resized_path = os.path.join(DATA_DIR, "resized_image.png")
    image = Image.open(original_path)
    new_size = (image.width // 2, image.height // 2)
    resized_image = image.resize(new_size, Image.ANTIALIAS)
    resized_image.save(resized_path)
    return "Image resized successfully and saved to resized_image.png."
