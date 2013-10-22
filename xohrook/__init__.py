from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask( __name__, instance_relative_config = True )

app.config.from_pyfile( 'xohrook.cfg' )

engine = create_engine( app.config['DBURI'] )
db_session = scoped_session(
    sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = engine
        )
    )

from .db.model_base import Base
Base.query = db_session.query_property()

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

from .views import *