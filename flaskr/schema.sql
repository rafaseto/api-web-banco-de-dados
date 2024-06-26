DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS medico;
DROP TABLE IF EXISTS especialidade;
DROP TABLE IF EXISTS especialista;

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

-- Criando a tabela especialidade
CREATE TABLE especialidade(
    pk_esp INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    area TEXT
);

-- Criando a tabela especialista
CREATE TABLE especialista (
    id_medico INTEGER NOT NULL,
    id_especialidade INTEGER NOT NULL,
    PRIMARY KEY (id_medico, id_especialidade),
    FOREIGN KEY (id_medico)
        REFERENCES medico (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (id_especialidade)
        REFERENCES especialidade (pk_esp)
        ON DELETE CASCADE
        ON UPDATE CASCADE
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