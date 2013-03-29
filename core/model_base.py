from sqlalchemy.ext.declarative import declared_attr, declarative_base
from sqlalchemy import Column, Integer
import re

class Base(object):
    @declared_attr
    def __tablename__(cls):
        """Automatically convert MyClass to my_class"""
        return re.sub( r'([a-z])([A-Z])', r'\1_\2', cls.__name__).lower()
    id = Column(Integer, primary_key = True)

Base = declarative_base(cls = Base)

if __name__ == '__main__':
    assert Base.__class__.__name__ == 'DeclarativeMeta'