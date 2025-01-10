import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

# Charger le fichier .env
load_dotenv()

secret_file=os.getenv('SECRET_FILE_KEY')

# Functions crypted

def load_secret_key():
    '''
    input : none
    output :
    purpose : load key file
    '''
    try:
        with open(secret_file, "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("Key file not found. Please generate a key first.")
    except IOError as e:
        print(f"Error reading the key file: {e}")
    return None

# Encrypt the text
def encrypt_message(message):
    key = load_secret_key()
    if key is None:
        return None  # Key not found, cannot encrypt
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Decrypt the text
def decrypt_message(encrypted_message):
    key = load_secret_key()
    if key is None:
        return None  # Key not found, cannot decrypt
    f = Fernet(key)
    try:
        decrypted_message = f.decrypt(encrypted_message).decode()
        return decrypted_message
    except Exception as e:
        print(f"Error decrypting message: {e}")
        return None
