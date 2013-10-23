import flask
from flask.ext.login import LoginManager as LMBase, UserMixin
from .db import User

class UserProxy( User, UserMixin ):
    __abstract__ = True

    @classmethod
    def load_user( cls, id ):
        try:
            n = int( id )
        except( ValueError ):
            return None
        return cls( User.query.get( n ) )

class LoginManager( LMBase ):
    def __init__( self, app ):
        super( LoginManager, self ).__init__( app )
        self.user_callback = UserProxy.load_user