from sqlalchemy.ext.declarative import declared_attr, declarative_base
from sqlalchemy import Column, Integer, Unicode, UnicodeText
import re

class Base(object):
    @declared_attr
    def __tablename__(cls):
        """Automatically convert MyClass to my_class"""
        return re.sub( r'([a-z])([A-Z])', r'\1_\2', cls.__name__).lower()
    id = Column(Integer, primary_key = True)

Base = declarative_base(cls = Base)

class Problem(Base):
    title = Column(Unicode(100))
    code = Column(UnicodeText())
    task = Column(UnicodeText())

    solution_code = Column(UnicodeText())
    solution = Column(UnicodeText())
    answer = Column(UnicodeText())
    
    def formatted():
        raise NotImplemented

if __name__ == '__main__':
    assert Problem.__table__.name == 'problem'