from flask import Flask

app = Flask( __name__, instance_relative_config = True )

app.config.from_pyfile( 'xohrook.cfg' )

from .db.flask import db_session
from . import db

class UsersView:
	@app.route('/users/')
	def index():
		users = db.User.query.all()
		return "Users:<br>" + "<br>".join(map(lambda u: u.realname, users))

	@app.route('/users/<int:id>')
	def show(id):
		user = db.User.query.get(id)
		return ( "Hello, %s!" % user.realname )
