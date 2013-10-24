from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

class Base(object):
    """Base class for all our ORM classes. Currently defines only 'id' primary key"""
    id = Column(Integer, primary_key = True)

Base = declarative_base(cls = Base)

if __name__ == '__main__':
    assert Base.__class__.__name__ == 'DeclarativeMeta'