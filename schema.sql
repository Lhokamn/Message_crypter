

DROP TABLE IF EXISTS passwd;

-- Création de la base de donnée
CREATE DATABASE passwd;


CREATE TABLE passwd.Links (
    id INT AUTO_INCREMENT PRIMARY KEY,
    lien VARCHAR(8) UNIQUE NOT NULL,
    texte VARCHAR(2048) NOT NULL,
    usesLink BOOLEAN NOT NULL
);

/** à régler pour plus tard
-- Création d'un utilisateur pour avoir un accès à la bd
CREATE USER myUser@localhost IDENTIFIED BY 'AVy,!5AtET</E3A/h[]S';

-- Attribution des droits sur la base de donnée pour l'utilisateur
GRANT INSERT,UPDATE ON passwd.* TO myUser@localhost;

-- Mise a jour des droits
FLUSH PRIVILEGES;
*/
