from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer
import re

class Base(object):
    id = Column(Integer, primary_key = True)

Base = declarative_base(cls = Base)

if __name__ == '__main__':
    assert Base.__class__.__name__ == 'DeclarativeMeta'