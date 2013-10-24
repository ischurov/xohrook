import flask
from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin

from sqlalchemy.orm import relationship, backref
from sqlalchemy import Boolean, Column, Integer, Unicode, Table, ForeignKey, DateTime
from base import Base

"""
User and Role models as required by Flask-Security.
"""

roles_users = Table('roles_users', Base.metadata,
                    Column('user_id', Integer(), ForeignKey('user.id')),
                    Column('role_id', Integer(), ForeignKey('role.id'))
                    )

class Role(Base, RoleMixin):
    __tablename__ = 'role'
    name = Column(Unicode(80), unique = True)
    description = Column(Unicode(255))

class User(Base, UserMixin):
    __tablename__ = 'user'
    email = Column(Unicode(255), unique = True)
    password = Column(Unicode(255))
    active = Column(Boolean())
    confirmed_at = Column(DateTime(timezone = True))
    roles = relationship('Role', secondary = roles_users,
                         backref = backref('users', lazy = 'dynamic'))