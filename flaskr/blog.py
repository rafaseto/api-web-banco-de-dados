from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

blueprint = Blueprint('blog', __name__)

# Rota index
@blueprint.route('/')
def index():
    db = get_db()

    # Selecionando todos os posts
    posts = db.execute(
        "SELECT p.id, title, body, created, author_id, username"
        "   FROM post p JOIN user u ON(p.author_id = u.id)"
        "   ORDER BY created DESC"
    ).fetchall

    return render_template('blog/index.html', posts=posts)

@blueprint.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = "Título é obrigatório."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "INSERT INTO post (title, body, author_id)"
                "VALUES (?, ?, ?)",
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))
        
    return render_template('blog/create.html')