# send_passwd
Code pour déploiement d'un serveur de mot de passe

# framework

Code développer en python avec le framework flask

# How to start a dev environment

## Linux 

- Start with download some python package
```sh
sudo apt install python-pip
sudo apt install python3-venv
```

- create a virtual environment source it in git repot
```sh
python3 -m venv venv
source venv/bin/activate
```

- Finally install flask et dotenv python packages
```sh
pip install Flask           # use flask framework
pip install python-dotenv   # Use .flaskenv and .env files
pip install cryptography    # use Fernet framework for crytography
pip install waitress        # use waitress framework to deploy in prod
```
or run ``requirements.txt``:
```sh
pip install -r requirements.txt
```

- to run run flask app 
```sh
flask run
```

# Run with Docker

first you need to git clone this repository locally. After you need to create docker image:
```sh
docker build --tag message-crypter .
```

After you have to lauch container instance:
- with simple launcher (usage for test)
```sh
docker run -d -p 8080:8080 message-crypter
```
- with env variable
```sh
docker run -d -p 8080:8080 message-crypter -e SECRET_WEB_KEY=<mywebkey> -e DATABASE_URL=<mydbfile.db> -e SECRET_FILE_KEY=<mysecretkey.key> -e BASE_URL=<http://127.0.0.1:5000/> --restart unless-stopped
```

or with docker-compose
```yml
services:
  message-crypter:
    image: message-crypter
    ports:
      - "8080:8080"
    environment:
      SECRET_WEB_KEY: <mywebkey>
      DATABASE_URL: <mydbfile.db>
      SECRET_FILE_KEY: <mysecretkey.key>
      BASE_URL: <http://127.0.0.1:5000/>
    restart: unless-stopped
```
