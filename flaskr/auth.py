import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db

# Criando uma blueprint chamada auth 
blueprint = Blueprint('auth', __name__, url_prefix='/auth')