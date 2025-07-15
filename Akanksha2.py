from PIL import Image

def encrypt_image(image_path, output_path):
    image = Image.open(image_path)
    pixels = image.load()

    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (255 - r, 255 - g, 255 - b)  # Simple inversion as encryption

    image.save(output_path)

# Example usage
encrypt_image('original.jpg', 'encrypted.jpg')