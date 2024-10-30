from src.encryption_tool import load_image, save_image, encrypt_image, decrypt_image

if __name__ == "__main__":
    key = 50  # Encryption key
    original_image_path = "images/example.jpg"
    encrypted_image_path = "images/encrypted_example.png"
    decrypted_image_path = "images/decrypted_example.png"

    image = load_image(original_image_path)
    encrypted_image = encrypt_image(image, key)
    save_image(encrypted_image, encrypted_image_path)
    print(f"Encrypted image saved to {encrypted_image_path}")

    decrypted_image = decrypt_image(encrypted_image, key)
    save_image(decrypted_image, decrypted_image_path)
    print(f"Decrypted image saved to {decrypted_image_path}")

