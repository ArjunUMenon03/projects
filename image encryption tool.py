from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    # Open the image
    image = Image.open(input_path)
    # Convert image to numpy array
    img_array = np.array(image)
    
    # Get the dimensions of the image
    rows, cols, channels = img_array.shape
    
    # Flatten the array to 1D
    flat_array = img_array.flatten()
    
    # Encrypt by XORing with the key and shifting pixels
    encrypted_array = np.bitwise_xor(flat_array, key)
    encrypted_array = np.roll(encrypted_array, key)
    
    # Reshape back to the original image dimensions
    encrypted_img_array = encrypted_array.reshape(rows, cols, channels)
    
    # Convert back to image
    encrypted_image = Image.fromarray(encrypted_img_array)
    # Save the encrypted image
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(input_path, output_path, key):
    # Open the image
    image = Image.open(input_path)
    # Convert image to numpy array
    img_array = np.array(image)
    
    # Get the dimensions of the image
    rows, cols, channels = img_array.shape
    
    # Flatten the array to 1D
    flat_array = img_array.flatten()
    
    # Decrypt by reversing the shift and XORing with the key
    decrypted_array = np.roll(flat_array, -key)
    decrypted_array = np.bitwise_xor(decrypted_array, key)
    
    # Reshape back to the original image dimensions
    decrypted_img_array = decrypted_array.reshape(rows, cols, channels)
    
    # Convert back to image
    decrypted_image = Image.fromarray(decrypted_img_array)
    # Save the decrypted image
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

# Example usage
input_image_path = 'input_image.png'
encrypted_image_path = 'encrypted_image.png'
decrypted_image_path = 'decrypted_image.png'
encryption_key = 123  # This is the key used for encryption and decryption

# Encrypt the image
encrypt_image(input_image_path, encrypted_image_path, encryption_key)

# Decrypt the image
decrypt_image(encrypted_image_path, decrypted_image_path, encryption_key)
