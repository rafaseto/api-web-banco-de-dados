import os

from flask import Flask

from flaskr.medico_routes import medico_blueprint

"""
Uma aplicação Flask é uma instância da classe Flask. Todas as configurações e URLs
serão registradas com essa classe.
Abaixo criamos uma instância 'app' da classe Flask dentro de uma função 'create_app()' 
esse é chamada de application factory, qualquer configuração vai dentro dessa função.

Uso: flask --app flaskr run --debug
"""

def create_app(test_config=None):
    # Instanciando um objeto 'app' da classe Flask
    app = Flask(__name__, instance_relative_config=True)
    
    # Definindo o caminho do Banco de Dados SQLite
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite') 
    )

    # Criando uma pasta de instância, se ainda não existir
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Criando uma primeira rota de teste
    @app.route('/hello')
    def hello():
        return 'Hello 21!'
    
    # Inicializando a aplicação Flask com as configurações de init_app
    from . import db
    db.init_app(app)

    # Importando e registrando a blueprint na factory
    from . import auth 
    app.register_blueprint(auth.blueprint)

    # Importando e registrando a blog blueprint na factory
    from . import blog
    app.register_blueprint(blog.blueprint)
    app.add_url_rule('/', endpoint='index')

    # Registrando medico_routes na factory para que as rotas fiquem acessíveis
    app.register_blueprint(medico_blueprint)

    return app