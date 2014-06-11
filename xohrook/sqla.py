from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.engine import reflection

from .models.base import Base
import models

__all__ = ['SQLA']

class SQLA:
    """
    Very simple Flask - SqlAlchemy bridge.

    I use it instead of Flask-SQLAlchemy because I want to use standard declarative_base() in my models.
    """

    def __init__(self, app):
        self.engine = create_engine(app.config['DATABASE_URI'])
        self.app = app
        self.session = scoped_session(
            sessionmaker(
                autocommit = False,
                autoflush = False,
                bind = self.engine
                )
            )
        Base.query = self.session.query_property()
        app.teardown_request(self.shutdown_session)
        app.before_first_request(self.seed)

    def shutdown_session(self, exception=None):
        self.session.remove()

    def create_tables(self):
        # Test if database is already initialized
        insp = reflection.Inspector.from_engine(self.engine)
        if insp.get_table_names():
            return False
        else:
            Base.metadata.create_all( bind = self.engine )
            return True

    def seed(self):
        if not self.create_tables():
            self.app.logger.debug("Database already initialized, skip seeding")
            return

        db_seed = self.app.config['DATABASE_SEED']
        if not db_seed:
            self.app.logger.debug( "No database seed found in `app.config'" )
            return
        from bootalchemy.loader import Loader
        loader = Loader(models)
        try:
            loader.from_list( self.session, db_seed )
            self.session.commit()
            self.app.logger.debug( "Successfully loaded database seed" )
        except:
            self.app.logger.warning( "Failed to load database seed" )
            pass