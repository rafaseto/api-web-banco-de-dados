DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS medico;

-- Criando a tabela user
CREATE TABLE user (
    pk_user INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

-- Criando a tabela medico
CREATE TABLE medico (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fk_user INTEGER NOT NULL,
    FOREIGN KEY (fk_user) REFERENCES user (pk_user)
        ON UPDATE CASCADE
        ON DELETE CASCADE 
);

-- Criando a tabela post
CREATE TABLE post (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INTEGER NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES user (id)
);