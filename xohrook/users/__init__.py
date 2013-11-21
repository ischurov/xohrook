from flask import Blueprint, render_template, abort
from ..models.users import User
from flask.ext.security import login_required

users = Blueprint('users', __name__, template_folder='templates')

@users.route('/<int:id>')
@login_required
def get(id):
    user = User.query.get(id)
    if user == None:
        abort(404)
    return render_template('users/show.html', user = user)

@users.route('/')
@login_required
def index():
    users = User.query.all()
    return render_template('users/index.html', users = users)