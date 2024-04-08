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