from flask import Flask, abort

from .sqla import SQLA
from .models.users import User

app = Flask(__name__, instance_relative_config = True)

app.config.from_pyfile('xohrook.cfg')

db = SQLA(app)

@app.route('/users/<int:id>')
def user_get(id):
    user = User.query.get(id)
    if user == None:
        abort(404)
    return user.email