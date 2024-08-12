from PIL import Image
import numpy as np

def create_sample_image(path):
    # Create a simple image with RGB values
    width, height = 100, 100
    image = Image.new('RGB', (width, height), color=(73, 109, 137))
    # Save the image
    image.save(path)
    print(f"Sample image created and saved as '{path}'")

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    img_array = np.array(image)
    rows, cols, channels = img_array.shape
    flat_array = img_array.flatten()
    encrypted_array = np.bitwise_xor(flat_array, key)
    encrypted_array = np.roll(encrypted_array, key)
    encrypted_img_array = encrypted_array.reshape(rows, cols, channels)
    encrypted_image = Image.fromarray(encrypted_img_array)
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    img_array = np.array(image)
    rows, cols, channels = img_array.shape
    flat_array = img_array.flatten()
    decrypted_array = np.roll(flat_array, -key)
    decrypted_array = np.bitwise_xor(decrypted_array, key)
    decrypted_img_array = decrypted_array.reshape(rows, cols, channels)
    decrypted_image = Image.fromarray(decrypted_img_array)
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

# Example usage
input_image_path = 'input_image.png'
encrypted_image_path = 'encrypted_image.png'
decrypted_image_path = 'decrypted_image.png'
encryption_key = 123

# Create a sample image
create_sample_image(input_image_path)

# Encrypt the image
encrypt_image(input_image_path, encrypted_image_path, encryption_key)

# Decrypt the image
decrypt_image(encrypted_image_path, decrypted_image_path, encryption_key)
