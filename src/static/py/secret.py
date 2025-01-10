import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# load in app .env file
load_dotenv()

secret_file = os.getenv('SECRET_FILE_KEY')


if not os.path.isfile(secret_file):
    key = Fernet.generate_key()
    
    try:
        with open(secret_file, "wb") as key_file:
            key_file.write(key)
        print("Key created and store in " + secret_file + "file")
    except IOError as e:
        print(f"Error saving the key: {e}")
else :
    print ("Key was already created")
