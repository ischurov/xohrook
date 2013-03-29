from model_base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Unicode, UnicodeText, DateTime, Boolean

class Problem(Base):
    __tablename__ = 'problems'
    revisions = relationship("ProblemRevision", backref = "problem")

class ProblemRevision(Base):
    __tablename__ = 'problem_revisions'
    title = Column(Unicode(100))
    code = Column(UnicodeText())
    template = Column(UnicodeText())
    timestamp = Column(DateTime(timezone = True))

    def formatted():
        raise NotImplemented