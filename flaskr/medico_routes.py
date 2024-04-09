from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from flaskr.db import get_db

medico_blueprint = Blueprint('medico', __name__)

@medico_blueprint.route('/medico/create', methods=('GET', 'POST'))
def create_medico():
    # Lógica para criar um novo médico
    pass

@medico_blueprint.route('/medico/<int:id>', methods=('GET',))
def view_medico(id):
    # Lógica para visualizar um médico específico
    pass

@medico_blueprint.route('/medico/<int:id>/update', methods=('GET', 'POST'))
def update_medico(id):
    # Lógica para atualizar um médico existente
    pass

@medico_blueprint.route('/medico<int:id>/delete', methods=('POST'))
def delete_medico(id):
    # Lógica para deletar um médico existente
    pass