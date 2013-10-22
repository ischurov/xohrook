# encoding: utf-8
import flask
from flask.ext.classy import FlaskView

from .. import db

class UsersView( FlaskView ):
    def index( self ):
        users = db.User.query.all( )
        return flask.render_template( 'users.html', users = users )

    def get( self, id ):
        user = db.User.from_id_or_login( id )
        if user is None:
            return ( u"User with id “%s” not found" % id ), 404
        return flask.render_template( 'user.html', user = user )