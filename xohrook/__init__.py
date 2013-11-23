from flask import Flask

from .sqla import SQLA
from .security import init_security

app = Flask(__name__, instance_relative_config = True)

app.config.from_pyfile('xohrook.cfg')

db = SQLA(app)

security = init_security(app, db)

from .users import users
app.register_blueprint(users, url_prefix = '/users')