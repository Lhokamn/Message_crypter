DROP TABLE IF EXISTS passwdLinks;

-- Create table for storing password links
CREATE TABLE passwdLinks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lien TEXT UNIQUE NOT NULL,
    texte TEXT NOT NULL
);
