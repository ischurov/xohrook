from sqlalchemy.orm import relationship, backref
from sqlalchemy import Boolean, Column, Integer, Unicode, Table, ForeignKey, DateTime
from base import Base

__all__ = ['Course', 'CourseMembership']

courses_students = Table('courses_students', Base.metadata,
                         Column('course_id', Integer(), ForeignKey('course.id')),
                         Column('student_id', Integer(), ForeignKey('user.id'))
                         )

courses_teachers = Table('courses_teachers', Base.metadata,
                         Column('course_id', Integer(), ForeignKey('course.id')),
                         Column('teacher_id', Integer(), ForeignKey('user.id'))
                         )


class Course(Base):
    __tablename__ = 'course'
    title = Column(Unicode(250), nullable = False)
    date_start = Column(Date, nullable = False)
    date_end = Column(Date, nullable = False)
    students = relationship('User', secondary = courses_students,
                            backref = backref('attends', lazy = 'dynamic'))
    teachers = relationship('User', secondary = courses_teachers,
                            backref = backref('teaches', lazy = 'dynamic'))