from .. import app

from .. import db
from ..db.flask import db_session

class Users:
    @app.route('/users/')
    def index():
        users = db.User.query.all()
        return "Users:<br>" + "<br>".join(map(lambda u: u.realname, users))

    @app.route('/users/<int:id>')
    def show(id):
        user = db.User.query.get(id)
        return ( "Hello, %s!" % user.realname )

    @app.route('/users/<login>')
    def show(login):
        user = db.User.query.filter(db.User.login == login).first()
        return ( "Hello, %s!" % user.realname )
