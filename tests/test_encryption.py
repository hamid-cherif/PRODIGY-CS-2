import unittest
import numpy as np
from src.encryption_tool import load_image, encrypt_image, decrypt_image

class TestImageEncryption(unittest.TestCase):
    def test_encrypt_decrypt(self):
        key = 50
        image = load_image("images/example.jpg")
        encrypted_image = encrypt_image(image, key)
        decrypted_image = decrypt_image(encrypted_image, key)

        # Convert to arrays for comparison
        original_array = np.array(image)
        decrypted_array = np.array(decrypted_image)

        # Assert that decrypted image matches the original
        self.assertTrue(np.array_equal(original_array, decrypted_array))

if __name__ == "__main__":
    unittest.main()

