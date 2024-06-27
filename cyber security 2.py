from PIL import Image
import numpy as np
import os

def encrypt_image(image_path, key):
    # Open the image and convert to numpy array
    image = Image.open(image_path)
    image = image.convert('RGB')  # Ensure the image is in RGB mode
    image_array = np.array(image, dtype=np.uint8)

    # Encrypt the image by adding the key to each pixel value
    encrypted_array = (image_array.astype(np.uint16) + key) % 256

    # Convert the encrypted array back to an image
    encrypted_image = Image.fromarray(encrypted_array.astype(np.uint8))

    return encrypted_image

def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image and convert to numpy array
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_image = encrypted_image.convert('RGB')  # Ensure the image is in RGB mode
    encrypted_array = np.array(encrypted_image, dtype=np.uint8)

    # Decrypt the image by subtracting the key from each pixel value
    decrypted_array = (encrypted_array.astype(np.uint16) - key) % 256

    # Convert the decrypted array back to an image
    decrypted_image = Image.fromarray(decrypted_array.astype(np.uint8))

    return decrypted_image

def main():
    while True:
        choice = input("Would you like to (E)ncrypt or (D)ecrypt an image? (E/D): ").upper()
        if choice not in ['E', 'D']:
            print("Invalid choice, please select 'E' for encrypt or 'D' for decrypt.")
            continue
        
        # Ensure correct path formatting
        image_path = input("Enter the path to the image: ").strip().strip("'")
        
        # Use your specific image path
        if image_path.lower() == 'default':
            image_path = r"C:\Users\adila\Downloads\Tom and Jerry.jpg"
        
        if not os.path.exists(image_path):
            print(f"The file {image_path} does not exist. Please check the path and try again.")
            continue

        try:
            key = int(input("Enter the encryption/decryption key (an integer): "))
        except ValueError:
            print("Invalid key. Please enter an integer.")
            continue
        
        if choice == 'E':
            encrypted_image = encrypt_image(image_path, key)
            encrypted_image_path = image_path.rsplit('.', 1)[0] + "_encrypted.png"
            encrypted_image.save(encrypted_image_path)
            print(f"Encrypted image saved as {encrypted_image_path}")
        else:
            decrypted_image = decrypt_image(image_path, key)
            decrypted_image_path = image_path.rsplit('.', 1)[0] + "_decrypted.png"
            decrypted_image.save(decrypted_image_path)
            print(f"Decrypted image saved as {decrypted_image_path}")
        
        again = input("Do you want to encrypt/decrypt another image? (Y/N): ").upper()
        if again != 'Y':
            break

if __name__ == "__main__":
    main()
