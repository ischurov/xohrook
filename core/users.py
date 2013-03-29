from model_base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, Integer, Unicode, Table, ForeignKey

class User(Base):
    __tablename__ = 'users'
    login = Column(Unicode(50), unique = True) # TODO: regexp
    realname = Column(Unicode(100))
    email = Column(Unicode(50))
    email_confirmed = Column(Boolean)

user_groups = Table(
    'user_groups', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('group_id', Integer, ForeignKey('groups.id'))
    )

class Group(Base):
    __tablename__ = 'groups'
    name = Column(Unicode(50), unique = True)
    description = Column(Unicode(100))
    users = relationship("User", secondary = user_groups, backref = "groups")