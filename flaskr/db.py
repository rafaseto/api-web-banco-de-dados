import sqlite3
import click
from flask import current_app, g

"""
A primeira coisa a se fazer é criar uma conexão com o SQLite.
Qualquer consulta ou operação é feita usando a conexão.
Abaixo criamos a função get_db() que faz a conexão com o banco.
get_db() é chamada quando a aplicação tiver sido criada e estiver lidando
com um request.
"""

# Função que retorna a conexão com o banco
def get_db():
    """
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

# Função para inicializar o BD da app e executar comandos SQL de schema.sql
def init_db():
    # Obtendo a conexão com o banco
    db = get_db()

    # Abrindo o arquivo schema.sql
    with current_app.open_resource('schema.sql') as f:
        # Lendo o arquivo, decodificando em UTF-8 e executando
        db.executescript(f.read().decode('utf8'))

# Criando um comando de linha de comando chamado init_db para inicializar
# o banco de dados da aplicação Flask
@click.command('init_db')
def init_db_command():  # Chamamos essa função quando init_db é executado
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')