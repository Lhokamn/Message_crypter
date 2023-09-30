# send_passwd
Code pour déploiement d'un serveur de mot de passe

# Création du serveur
Pour le déploiement du serveur il faut un serveur LAMP.

## Commande pour la création d'un serveur LAMP sur Debian 12
La configuration doit se faire en tant que super utilisateur ou root
```
# Installation des paquets 
apt install git -y     
apt install apache2 -y     
apt install mariadb-server -y   
mysql_secure_installation
apt install php libapache2-mod-php php-mysql

# Configuration de MariaDB
root@passwdServer:~# mariadb 
```
Pour la configuration merci de regarder le fichier SQL suivant [createDataBase](https://github.com/Lhokamn/send_passwd/blob/main/private/createDataBase.sql)