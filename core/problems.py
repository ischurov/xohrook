from model_base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Unicode, UnicodeText, DateTime, Boolean, ForeignKey

from users import User

class Problem(Base):
    __tablename__ = 'problems'
    revisions = relationship("ProblemRevision", backref = "problem")

class ProblemRevision(Base):
    __tablename__ = 'problem_revisions'
    description = Column(Unicode(100))
    code = Column(UnicodeText())
    template = Column(UnicodeText())
    timestamp = Column(DateTime(timezone = True))
    author_id = Column(Integer, ForeignKey(User.id))
    author = relationship(author_id)

    def formatted():
        raise NotImplemented