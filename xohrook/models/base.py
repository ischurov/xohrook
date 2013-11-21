from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

__all__ = ['Base', 'IdMixin']

Base = declarative_base()

class IdMixin():
    id = Column(Integer, primary_key = True)

if __name__ == '__main__':
    assert Base.__class__.__name__ == 'DeclarativeMeta'