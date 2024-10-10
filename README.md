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
docker build --tag send-passwd .
```

After you have to lauch container instance:
```sh
docker run -d -p 5000:5000 send-passwd
```
