import sqlite3
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

database_URL = os.getenv('DATABASE_URL')

if not database_URL:
    raise ValueError("DATABASE_URL not found in the environment variables.")

# Because we use sqlite3 db, we are looking if file is already created, if it's not, we have to create it

if not os.path.isfile(database_URL):
    try :
        connection = sqlite3.connect(database_URL)
        print("Database connected successfully!")

        # Execute SQL script from schema.sql
        with open(file='./schema.sql', mode='r') as f:
            connection.executescript(f.read())

        # Commit changes
        connection.commit()
        print("Schema applied successfully!")

    except sqlite3.Error as e:
        print(f"An error occurred while connecting to the database or executing the script: {e}")

    finally :
        # Close the connection
        if connection:
            connection.close()
            print("Database connection closed.")
else:
    print("Database already created")