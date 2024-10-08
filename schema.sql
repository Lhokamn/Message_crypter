DROP TABLE IF EXISTS passwdLinks;

-- Create table for storing password links
CREATE TABLE passwdLinks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    link TEXT UNIQUE NOT NULL,
    secureText TEXT NOT NULL
);
