from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from .. import app

engine = create_engine( app.config['DBURI'] )
db_session = scoped_session( sessionmaker( autocommit = False, autoflush = False, bind = engine ) )

from .model_base import Base
Base.query = db_session.query_property()

def init_db():
	import xohrook.db
	Base.metadata.create_all( bind = engine )
