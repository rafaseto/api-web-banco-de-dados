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

if __name__ == '__main__':
    app.run(debug=True)