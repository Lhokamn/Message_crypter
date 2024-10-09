import os
import random
import string
from static.py.crypt_function import encrypt_message, decrypt_message
from static.py.db_functions import get_secure_links
from flask import Flask, render_template, request, url_for, flash, redirect
from dotenv import load_dotenv



# Charger le fichier .env
load_dotenv()

app = Flask(__name__)
app.config['SECRET_WEB_KEY']=os.getenv('SECRET_WEB_KEY')
app.config['DEBUG_MODE']=os.getenv('DEBUG')

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



# Function web redirect
@app.route('/',methods=('GET','POST'))
def index():
    if request.method == 'POST':
        text=request.form['content']
        print(f,"" + text)
        if not text:
            flash("No message enter. Please enter your message")
        else:
            new_entry(text)
            return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/<token>')
def link_token(token):
    link = get_secure_links(token)
    return render_template('token.html', token=link)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug = True)