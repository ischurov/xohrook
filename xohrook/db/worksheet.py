from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Unicode, UnicodeText, DateTime, Boolean, ForeignKey
import re

from model_base import Base
from users import User
from preprocessor import Preprocessor
from problems import Problem, ProblemRevision

"""
Worksheet is a collection of problems with some text to glue them.

In the future, we shall use it to generate homeworks and exams.
"""
class Worksheet(Base):
    __tablename__ = 'worksheets'
    revisions = relationship("WorksheetRevision", backref = "worksheet")

class WorksheetRevision(Base):
    __tablename__ = 'worksheet_revisions'
    title = Column(Unicode(100))
    worksheet_id = Column(Integer, ForeignKey(Worksheet.id))
    author_id = Column(Integer, ForeignKey(User.id))
    author = relationship("User")
    timestamp = Column(DateTime(timezone = True))
    template = Column(UnicodeText())

    problem_re = re.compile(r'#problem([1-9][0-9]*);')

    def __init__(self):
        self.problems_cache = None

    def problems(self):
        if self.problems_cache != None:
            return self.problems_cache
        return frozenset([ int(n, 10) for n in re.findall(self.problem_re, self.template) ])

    def seed(self, student):
        """TODO: Should the seed depend on problem id?"""
        raise NotImplemented

    def generate(self, student, out):
        seed = self.seed(student)
        problems = {}
        for p in self.problems():
            problems[p] = Problem.query.get(p).generate(seed, out)
        pp = Preprocessor()
        text = pp.process(None, template, {title: title})
        mk = Markup()
        text = mk.process(text)
        text = re.sub(problem_re, lambda obj: problems[obj.group(0)], text)
        return text

    def generate_list(self, students, out):
        res = {}
        for student in students:
            res[student] = self.generate(student, out)
        return res

if __name__ == '__main__':
    rev = WorksheetRevision()
    rev.template = '#problem123; #problema; #problem0; #problem105;'
    assert rev.problems() == frozenset([123, 105])