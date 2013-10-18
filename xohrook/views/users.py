import flask
from flask.ext.classy import FlaskView

from .. import db

class UsersView( FlaskView ):
    def index( self ):
        users = db.User.query.all( )
        return flask.render_template( 'users.html', users = users )

    def get( self, id ):
        try:
            id = int( id )
            user = db.User.query.get( id )
        except( ValueError ):
            user = db.User.query.filter( db.User.login == login ).first()
        if user is None:
            return ( u"User with id “%s” not found" % id ), 404
        return flask.render_template( 'user.html', user = user )