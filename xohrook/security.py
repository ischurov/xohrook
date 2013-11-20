import flask
from flask.ext.security import Security, SQLAlchemyUserDatastore

from .models.users import User, Role

__all__ = ['init_security']

def init_security(app, db):
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    return Security(app, user_datastore)