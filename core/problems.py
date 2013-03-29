from model_base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Unicode, UnicodeText, DateTime, Boolean

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