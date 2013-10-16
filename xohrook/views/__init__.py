# coding: utf-8
import flask

from .. import app
from .. import db
from ..db.flask import db_session

class Users:
    @app.route('/users/')
    def index():
        users = db.User.query.all()
        return flask.render_template( 'users.html', users = users )

    @app.route('/users/<int:id>')
    def show_id(id):
        user = db.User.query.get(id)
        if user is None:
            return ( u"User with id “%s” not found" % id ), 404
        return flask.render_template( 'user.html', user = user )

    @app.route('/users/<login>')
    def show_login(login):
        user = db.User.query.filter(db.User.login == login).first()
        if user is None:
            return ( u"User with login “%s” not found" % login ), 404
        return flask.render_template( 'user.html', user = user )
