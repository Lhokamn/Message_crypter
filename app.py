import os
import random
import string
from static.py.crypt_function import encrypt_message, decrypt_message
from static.py.db_functions import get_secure_links, add_secure_links, remove_secure_links
from flask import Flask, render_template, request, flash, send_from_directory
from dotenv import load_dotenv
from waitress import serve



# Charger le fichier .env
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_WEB_KEY')
base_URL = os.getenv('BASE_URL')

print(base_URL)

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
    output : fullLink -> str
    
    '''

    # Create unique link
    randomString = new_random_string_generator()

    fullLink =   base_URL + randomString

    # Secure entry text
    secureText = encrypt_message(text)

    add_secure_links(link=randomString, secureText=secureText)

    return fullLink

def launch():
    '''
    input : none
    output : none
    purpose : lauch init_db.py and secret.py
    '''

    print("We are in lauch function")
    # lauch db sqlite3
    try:
        with open('init_db.py') as f:
            code = f.read()  
            exec(code)
    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé.")
    except PermissionError:
        print("Vous n'avez pas la permission de lire ce fichier.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
    
    # lauch secret file for cryting
    try:
        with open('secret.py') as f:
            code = f.read()  
            exec(code)
    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé.")
    except PermissionError:
        print("Vous n'avez pas la permission de lire ce fichier.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")


# Function web redirect
@app.route('/',methods=('GET','POST'))
def index():
    if request.method == 'POST':
        text = request.form.get('content-textarea')
        if not text:
            flash("No message enter. Please enter your message")
        else:
            fullLink = new_entry(text)
            return render_template('save.html', fullLink=fullLink)
    return render_template('index.html')

@app.route('/<token>')
def link_token(token):

    print(token)
    if token == "robots.txt":
        return send_from_directory(app.root_path, 'robots.txt')
    
    else:
        link = get_secure_links(token)
        message = decrypt_message(link['secureText'])
        #remove_secure_links(link['link'])
        return render_template('token.html', token=message)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/delete',methods=('GET','POST'))
def new_delete_request():
    request_url = request.get_json()
    
    token = request_url.get('token')

    token = token.split("/")[1]
    print(token)
    remove_secure_links(token)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


launch()
if __name__ == '__main__':
    serve(app,host='0.0.0.0',port=8080)