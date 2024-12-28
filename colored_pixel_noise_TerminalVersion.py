from PIL import Image
import random

def create_rgb_image(width, height):
    image = Image.new("RGB", (width, height))
    pixels = []
    for _ in range(height):
        for _ in range(width):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            pixels.append((r, g, b))
    image.putdata(pixels)
    image.save(f"image.png")
    print(f"Изображение создано и сохранено как image.png")
if __name__ == "__main__":
    width = int(input("width: "))
    height = int(input("height: "))
    create_rgb_image(width, height)