import sqlite3
import os
from dotenv import load_dotenv
from werkzeug.exceptions import abort

# Charger le fichier .env
load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

# Function databases
def get_db_connection():
    '''
    input : none 
    output : sqlite3 connexion
    purpose : connect to sqlite3 database locally 
    '''

    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(DATABASE_URL)
        connection.row_factory = sqlite3.Row

    except sqlite3.Error as e:
        print(f"An error occurred while connecting to the database : {e}")
        
    finally:
        if connection:
            #connection.close()
            return connection

def add_secure_links(link: str,secureText: str):
    '''
    input : link -> str, secureText -> str
    output : none
    purpose : add an entry in db
    '''

    if link == None or secureText == None:
        raise ValueError("One or two arguments are missing")

    try:
        # Connexion to database
        conn = get_db_connection()

        # launch cursor
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO passwdLinks (link, secureText) VALUES (?, ?)", (link, secureText))
            conn.commit()
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

def remove_secure_links(link: str):
    '''
    input : link -> str
    output : none
    purpose : remove an entry in db
    '''

    if link == None:
        raise ValueError("One or two arguments are missing")
    
    try:
        # Connexion to database
        conn = get_db_connection()

        # launch cursor
        cursor = conn.cursor()

        try:
            cursor.execute("DELETE FROM passwdLinks WHERE link = ?", (link, ))
            conn.commit()
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

