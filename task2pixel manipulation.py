from PIL import Image
import os

def math_encrypt(image, key):
    pixels = image.load()
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
    return image

def math_decrypt(image, key):
    pixels = image.load()
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
    return image

def swap_pixels(image):
    pixels = image.load()
    width, height = image.size
    for i in range(width // 2):
        for j in range(height):
            opposite_x = width - i - 1
            pixels[i, j], pixels[opposite_x, j] = pixels[opposite_x, j], pixels[i, j]
    return image

def main():
    print("=== Image Encryption Tool ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? ").strip().upper()
    method = input("Choose method: (1) Math Operation, (2) Pixel Swap: ").strip()
    
    if choice not in ['E', 'D'] or method not in ['1', '2']:
        print("Invalid input. Please select valid options.")
        return

    path = input("Enter the image file path: ").strip()
    if not os.path.exists(path):
        print("Image file not found.")
        return

    image = Image.open(path)
    
    if method == '1':
        try:
            key = int(input("Enter encryption key (integer): "))
        except ValueError:
            print("Invalid key. Must be an integer.")
            return
        if choice == 'E':
            result = math_encrypt(image, key)
            filename = "encrypted_math_" + os.path.basename(path)
        else:
            result = math_decrypt(image, key)
            filename = "decrypted_math_" + os.path.basename(path)

    elif method == '2':
        if choice == 'E':
            result = swap_pixels(image)
            filename = "encrypted_swap_" + os.path.basename(path)
        else:
            result = swap_pixels(image)  # same operation reverses it
            filename = "decrypted_swap_" + os.path.basename(path)

    result.save(filename)
    print(f"Operation successful! Image saved as {filename}")

if __name__ == "__main__":
    main()
