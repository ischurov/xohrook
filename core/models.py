from sqlalchemy.ext.declarative import declared_attr, declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Unicode, UnicodeText, DateTime
import re

class Base(object):
    @declared_attr
    def __tablename__(cls):
        """Automatically convert MyClass to my_class"""
        return re.sub( r'([a-z])([A-Z])', r'\1_\2', cls.__name__).lower()
    id = Column(Integer, primary_key = True)

Base = declarative_base(cls = Base)

class Problem(Base):
    revisions = relationship("ProblemRevision", backref = "problem")

class ProblemRevision(Base):
    title = Column(Unicode(100))
    code = Column(UnicodeText())
    template = Column(UnicodeText())
    timestamp = Column(DateTime(timezone = True))

    def formatted():
        raise NotImplemented

if __name__ == '__main__':
    assert Problem.__table__.name == 'problem'