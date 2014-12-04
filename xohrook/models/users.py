import flask
from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin

from sqlalchemy.orm import relationship, backref
from sqlalchemy import Boolean, Column, Integer, Unicode, Table, ForeignKey, DateTime
from .base import Base, IdMixin

"""
User and Role models as required by Flask-Security.
"""

__all__ = ['User', 'Role']

roles_users = Table('roles_users', Base.metadata,
                    Column('user_id', Integer(), ForeignKey('user.id')),
                    Column('role_id', Integer(), ForeignKey('role.id'))
                    )

class Role(Base, IdMixin, RoleMixin):
    __tablename__ = 'role'
    name = Column(Unicode(80), unique = True)
    description = Column(Unicode(255))

class User(Base, IdMixin, UserMixin):
    __tablename__ = 'user'
    email = Column(Unicode(255), unique = True)
    realname = Column(Unicode(255))
    password = Column(Unicode(255))
    active = Column(Boolean())
    confirmed_at = Column(DateTime(timezone = True))
    roles = relationship('Role', secondary = roles_users,
                         backref = backref('users', lazy = 'dynamic'))