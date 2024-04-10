from flask import Flask, request, jsonify, g
import sqlite3

app = Flask(__name__)

DATABASE = 'database.db'

# Função para conectar ao banco de dados SQLite
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# Função para fechar a conexão com o banco de dados após cada request
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# Rota para ler os usuários
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    cursor = get_db().cursor()
    cursor.execute('SELECT * FROM user')
    usuarios = cursor.fetchall()
    return jsonify(usuarios)

# Rota para buscar usuario por id
@app.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    cursor = get_db().cursor()
    cursor.execute(
        "SELECT * from user WHERE pk_user = ?",
        (id,)
    )
    usuario = cursor.fetchone()
    return jsonify(usuario)

# Rota para adicionar um novo usuário
@app.route('/usuarios', methods=['POST'])
def add_usuario():
    data = request.json
    username = data['username']
    password = data['password']
    cursor = get_db().cursor()
    cursor.execute(
        "INSERT INTO user (username, password)"
        "VALUES (?, ?)",
        (username, password)
    )
    get_db().commit()
    return jsonify({"message": "Usuário criado com sucesso"})

# Rota para atualizar um usuário
@app.route('/usuarios/<int:id>', methods=['PUT'])
def update_usuario(id):
    data = request.json
    username = data['username']
    password = data['password']
    cursor = get_db().cursor()
    cursor.execute(
        "UPDATE user SET username = ?, password = ?"
        "WHERE pk_user = ?",
        (username, password, id)
    )
    get_db().commit()
    return jsonify({"message": "Usuário atualizado com sucesso"})

# Rota para deletar um usuário por ID
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_user(id):
    cursor = get_db().cursor()
    cursor.execute('DELETE FROM user WHERE pk_user = ?', (id,))
    get_db().commit()
    return jsonify({"message": "Usuário deletado com sucesso"})


# Rota para ler os médicos
@app.route('/medicos', methods=['GET'])
def get_medicos():
    cursor = get_db().cursor()
    cursor.execute('SELECT * FROM medico')
    medicos = cursor.fetchall()
    return jsonify(medicos)

# Rota para buscar um médico por id
@app.route('/medicos/<int:id>', methods=['GET'])
def get_medico(id):
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM medico WHERE id = ?", (id,))
    medico = cursor.fetchone()
    return jsonify(medico)

# Rota para adicionar um novo médico
@app.route('/medicos', methods=['POST'])
def add_medico():
    data = request.json
    fk_user = data['fk_user']
    cursor = get_db().cursor()
    cursor.execute(
        "INSERT INTO medico (fk_user) VALUES (?)", (fk_user,)
    )
    get_db().commit()
    return jsonify({"message": "Médico adicionado com sucesso"})

# Rota para atualizar um médico
@app.route('/medicos/<int:id>', methods=['PUT'])
def update_medico(id):
    data = request.json
    fk_user = data['fk_user']
    cursor = get_db().cursor()
    cursor.execute(
        "UPDATE medico SET fk_user = ? WHERE id = ?",
        (fk_user,id)
    )
    get_db().commit()
    return jsonify({"message": "Médico atualizado com sucesso"})

# Rota para deletar um médico
@app.route('/medicos/<int:id>', methods=['DELETE'])
def delete_medico(id):
    cursor = get_db().cursor()
    cursor.execute('DELETE FROM medico WHERE id = ?', (id,))
    get_db().commit()
    return jsonify({"message": "Medico deletado com sucesso"})

# Rota para ler as especialidades
@app.route('/especialidades', methods=['GET'])
def get_especialidades():
    cursor = get_db().cursor()
    cursor.execute('SELECT * FROM especialidade')
    especialidades = cursor.fetchall()
    return jsonify(especialidades)

# Rota para buscar especialidade por id
@app.route('/especialidades/<int:pk_esp>', methods=['GET'])
def get_especialidade(pk_esp):
    cursor = get_db().cursor()
    cursor.execute(
        "SELECT * from especialidade WHERE pk_esp = ?",
        (pk_esp,)
    )
    especialidade = cursor.fetchone()
    return jsonify(especialidade)

# Rota para adicionar uma nova especialidade
@app.route('/especialidades', methods=['POST'])
def add_especialidade():
    data = request.json
    nome = data['nome']
    area = data['area']
    cursor = get_db().cursor()
    cursor.execute(
        "INSERT INTO especialidade (nome, area)"
        "VALUES (?, ?)",
        (nome, area)
    )
    get_db().commit()
    return jsonify({"message": "Especialidade criado com sucesso"})

if __name__ == '__main__':
    app.run(debug=True)