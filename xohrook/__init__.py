from flask import Flask

from .sqla import SQLA
from .security import init_security
from .config import init_config

app = Flask(__name__, instance_relative_config = True)
init_config(app)
db = SQLA(app)
security = init_security(app, db)

from .users import users
app.register_blueprint(users, url_prefix = '/users')