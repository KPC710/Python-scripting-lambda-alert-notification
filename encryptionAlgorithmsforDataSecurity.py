from cryptography.fernet import Fernet

def encrypt_message(message, key):
    try:
        cipher_suite = Fernet(key)
        encrypted_message = cipher_suite.encrypt(message.encode())
        return encrypted_message
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    # Key for encryption (must be kept secret)
    secret_key = Fernet.generate_key()
    # Message to encrypt
    message_to_encrypt = "Sensitive data"
    encrypted = encrypt_message(message_to_encrypt, secret_key)
    print("Encrypted message:", encrypted)
