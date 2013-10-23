from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from .model_base import Base

class FlaskSQLA:
    """
    Very simple Flask - SqlAlchemy bridge.

    I use it instead of Flask-SQLAlchemy because I want to use standard declarative_base() in my models.
    """

    def __init__( self, app ):
        self.engine = create_engine( app.config['DBURI'] )
        self.session = scoped_session(
            sessionmaker(
                autocommit = False,
                autoflush = False,
                bind = self.engine
                )
            )
        Base.query = self.session.query_property()
        app.teardown_request( self.shutdown_session )

    def shutdown_session(self, exception=None):
        self.session.remove()