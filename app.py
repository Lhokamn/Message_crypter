import sqlite3
import os
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from dotenv import load_dotenv

# Charger le fichier .env
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY']=os.getenv('SECRET_KEY')
app.config['DATABASE_URL']=os.getenv('DATABASE_URL')

# Function usecase
def get_db_connection():
    conn = sqlite3.connect(app.config['DATABASE_URL'])
    conn.row_factory = sqlite3.Row
    return conn


# Function web redirect
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug = True)