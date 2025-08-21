from cryptography.fernet import Fernet
import os

# === Key Management ===
KEY_FILE = "secret.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    print("✅ Key generated and saved to 'secret.key'")

def load_key():
    if not os.path.exists(KEY_FILE):
        print("⚠️ No key found. Generating a new one...")
        generate_key()
    with open(KEY_FILE, "rb") as f:
        return f.read()

# === Encryption ===
def encrypt_message(message, key):
    cipher = Fernet(key)
    encrypted = cipher.encrypt(message.encode())
    return encrypted

# === Decryption ===
def decrypt_message(encrypted_message, key):
    cipher = Fernet(key)
    decrypted = cipher.decrypt(encrypted_message).decode()
    return decrypted

# === Main Program ===
if __name__ == "__main__":
    key = load_key()

    message = input("🔐 Enter message to encrypt: ")
    encrypted = encrypt_message(message, key)
    print("\n🔒 Encrypted:", encrypted.decode())

    decrypted = decrypt_message(encrypted, key)
    print("🔓 Decrypted:", decrypted)
