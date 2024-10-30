from PIL import Image
import numpy as np

def load_image(image_path):
    return Image.open(image_path)

def save_image(image, output_path):
    image.save(output_path)

def encrypt_image(image, key):
    img_array = np.array(image)
    encrypted_array = (img_array + key) % 256
    return Image.fromarray(encrypted_array.astype(np.uint8))

def decrypt_image(encrypted_image, key):
    encrypted_array = np.array(encrypted_image)
    decrypted_array = (encrypted_array - key) % 256
    return Image.fromarray(decrypted_array.astype(np.uint8))

