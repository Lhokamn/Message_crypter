import sqlite3
import os
import random
import string
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from dotenv import load_dotenv
from cryptography.fernet import Fernet
from werkzeug.exceptions import abort

# Charger le fichier .env
load_dotenv()

app = Flask(__name__)
app.config['SECRET_WEB_KEY']=os.getenv('SECRET_WEB_KEY')
app.config['DATABASE_URL']=os.getenv('DATABASE_URL')
app.config['DEBUG_MODE']=os.getenv('DEBUG')
app.config['SECRET_FILE_KEY']=os.getenv('SECRET_FILE_KEY')

# Function app application

def new_random_string_generator():
    '''
    input : none
    output : string
    generate a random string of 12 caractères
    '''
    allCaracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(allCaracteres) for _ in range(12))

def new_entry(text:str):
    '''
    input : text -> str
    output : randomString -> str
    '''

    # Create unique link
    randomString = new_random_string_generator()

    # Secure entry text
    secureText = encrypt_message(text)

    add_secure_links(link=randomString, secureText=secureText)

    return randomString

# Functions crypted

def load_secret_key():
    '''
    input : none
    output :
    purpose : load key file
    '''
    try:
        with open(app.config['SECRET_FILE_KEY'], "rb") as key_file:
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

# Function databases
def get_db_connection():
    '''
    input : none 
    output : sqlite3 connexion
    purpose : connect to sqlite3 database locally 
    '''

    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(app.config['DATABASE_URL'])
        print("Database connected successfully!")
        connection.row_factory = sqlite3.Row

    except sqlite3.Error as e:
        print(f"An error occurred while connecting to the database : {e}")
        
    finally:
        if connection:
            #connection.close()
            print("Database connection closed.")
            return connection

def add_secure_links(link,secureText):
    '''
    input : none
    output : none

    '''
    try:
        # Connexion to database
        conn = get_db_connection()

        # launch cursor
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO passwdLinks (link, secureText) VALUES (?, ?)", (link, secureText))
        except sqlite3.Error as e:
            raise e

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        # Fermez le curseur et la connexion
        if cursor:
            cursor.close()
        if conn:
            conn.close()
            print("Database connection closed.")

def get_secure_links(token: str):
    '''
    input : token : string
    output : database information
    '''

    # Connection to database
    conn = get_db_connection()
    try:

        post = conn.execute('SELECT * FROM passwdLinks WHERE link = ?',(token,)).fetchone()
        if post is None:
            abort(404)
        
        print(f"Is connection open? {conn is not None}")

        return post
        

    finally:
        conn.close()

    
    


def remove_secure_links(token: string):
    conn = get_db_connection()


# Function web redirect
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<token>', methods=['GET','POST'])
def link_token(token):
    link = get_secure_links(token)
    return render_template('token.html', token=link)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug = True)