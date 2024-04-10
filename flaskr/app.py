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
@app.route('/usuarios/<int:pk_user>', methods=['GET'])
def get_usuario(pk_user):
    cursor = get_db().cursor()
    cursor.execute(
        "SELECT * from user WHERE pk_user = ?",
        (pk_user,)
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
@app.route('/usuarios/<int:pk_user>', methods=['PUT'])
def update_usuario(pk_user):
    data = request.json
    username = data['username']
    password = data['password']
    cursor = get_db().cursor()
    cursor.execute(
        "UPDATE user SET username = ?, password = ?"
        "WHERE pk_user = ?",
        (username, password, pk_user)
    )
    get_db().commit()
    return jsonify({"message": "Usuário atualizado com sucesso"})

# Rota para deletar um usuário por ID
@app.route('/usuarios/<int:pk_user>', methods=['DELETE'])
def delete_user(pk_user):
    cursor = get_db().cursor()
    cursor.execute('DELETE FROM user WHERE pk_user = ?', (pk_user,))
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

# Rota para atualizar especialidade
@app.route('/especialidades/<int:pk_esp>', methods=['PUT'])
def update_especialidade(pk_esp):
    data = request.json
    nome = data['nome']
    area = data['area']
    cursor = get_db().cursor()
    cursor.execute(
        "UPDATE especialidade SET nome = ?, area = ?"
        "WHERE pk_esp = ?",
        (nome, area, pk_esp)
    )
    get_db().commit()
    return jsonify({"message": "Especialidade atualizado com sucesso"})

# Rota para deletar especialidade por ID
@app.route('/especialidades/<int:pk_esp>', methods=['DELETE'])
def delete_especialidade(pk_esp):
    cursor = get_db().cursor()
    cursor.execute('DELETE FROM especialidade WHERE pk_esp = ?', (pk_esp,))
    get_db().commit()
    return jsonify({"message": "Especialidade deletado com sucesso"})

# Rota para criar um novo especialista
@app.route('/especialistas', methods=['POST'])
def create_especialista():
    data = request.json
    id_medico = data['id_medico']
    id_especialidade = data['id_especialidade']
    cursor = get_db().cursor()
    cursor.execute(
        'INSERT INTO especialista (id_medico, id_especialidade) VALUES (?, ?)', 
        (id_medico, id_especialidade)
    )
    get_db().commit()
    return jsonify({"message": "Especialista criado com sucesso"})

# Rota para listar todos os especialistas
@app.route('/especialistas', methods=['GET'])
def get_all_especialistas():
    cursor = get_db().cursor()
    cursor.execute('SELECT * FROM Especialista')
    especialistas = cursor.fetchall()
    return jsonify(especialistas)

# Rota para buscar um especialista por ID
@app.route('/especialistas/<int:id_medico>/<int:id_especialidade>', methods=['GET'])
def get_especialista(id_medico, id_especialidade):
    cursor = get_db().cursor()
    cursor.execute('SELECT * FROM Especialista WHERE id_medico = ? AND id_especialidade = ?', (id_medico, id_especialidade))
    especialista = cursor.fetchone()
    return jsonify(especialista)

# Rota para atualizar um especialista por ID
@app.route('/especialistas/<int:id_medico>/<int:id_especialidade>', methods=['PUT'])
def update_especialista(id_medico, id_especialidade):
    data = request.json
    new_id_medico = data['id_medico']
    new_id_especialidade = data['id_especialidade']
    cursor = get_db().cursor()
    cursor.execute('UPDATE Especialista SET id_medico = ?, id_especialidade = ? WHERE id_medico = ? AND id_especialidade = ?', 
                   (new_id_medico, new_id_especialidade, id_medico, id_especialidade))
    get_db().commit()
    return jsonify({"message": "Especialista atualizado com sucesso"})

# Rota para deletar um especialista por ID
@app.route('/especialistas/<int:id_medico>/<int:id_especialidade>', methods=['DELETE'])
def delete_especialista(id_medico, id_especialidade):
    cursor = get_db().cursor()
    cursor.execute('DELETE FROM Especialista WHERE id_medico = ? AND id_especialidade = ?', (id_medico, id_especialidade))
    get_db().commit()
    return jsonify({"message": "Especialista deletado com sucesso"})

if __name__ == '__main__':
    app.run(debug=True)