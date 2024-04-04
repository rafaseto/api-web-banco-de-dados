import sqlite3
import click
from flask import current_app, g

"""
A primeira coisa a se fazer é criar uma conexão com o SQLite.
Qualquer consulta ou operação é feita usando a conexão.
Abaixo criamos a função get_db() que faz a conexão com o banco.
get_db() é chamada quando a aplicação tiver sido criada e estiver lidando
com um request.

g: é um objeto especial único para cada request. É usado para 
armazenar dados que podem ser acessados por múltiplas funções
durante o request. A conexão é armazenada e reusada se get_db()
for chamada duas vezes no mesmo request

current_app: é um objeto especial que aponta para a aplicação Flask
lidando com o request

sqlite3.connect(): estabelece a conexão com o arquivo apontado pela
configuration key DATABASE

sqlite3.Row: Pede para a conexão retornar as linhas como dicionários. 
Isso permite acessar as colunas pelo nome.
"""

# Função que retorna a conexão com o banco
def get_db():
    # Se não já tivermos uma conexão armazenada no objeto g
    if 'db' not in g:
        # Criamos a conexão com o banco de dados SQLite
        g.db = sqlite3.connect(
            # Caminho para o BD SQLite configurado para app atual
            current_app.config['DATABASE'], 
            detect_types=sqlite3.PARSE_DECLTYPES 
        )
        # Resultados das consultas serão retornados como dicionários
        g.db.row_factory = sqlite3.Row
    
    # Retornamos a CONEXÃO com o banco de dados
    return g.db

# Função que fecha a conexão com o banco
def close_db(e=None):
    # Removendo a conexão do objeto g e atribuindo a db
    db = g.pop('db', None)

    # Se a conexão com o banco existe
    if db is not None:
        # Fechamos a CONEXÃO com o banco de dados
        db.close