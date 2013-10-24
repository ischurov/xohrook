from flask import Flask

from .sqla import SQLA
from .security import init_security

app = Flask(__name__, instance_relative_config = True)

app.config.from_pyfile('xohrook.cfg')

db = SQLA(app)

security = init_security(app, db)

from flask import abort
from .models.users import User
from flask.ext.security import login_required

@app.route('/users/<int:id>')
@login_required
def user_get(id):
    user = User.query.get(id)
    if user == None:
        abort(404)
    return user.email