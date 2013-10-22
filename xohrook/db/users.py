from .model_base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, Integer, Unicode, Table, ForeignKey

"""
User management.

Currently, we follow UNIX model, where we just have users and groups.
"""
class User(Base):
    __tablename__ = 'users'
    login = Column(Unicode(50), unique = True) # TODO: regexp
    realname = Column(Unicode(100))
    email = Column(Unicode(50))
    email_confirmed = Column(Boolean)

    @classmethod
    def from_id_or_login( cls, id ):
        try:
            id = int( id )
            return cls.query.get( id )
        except( ValueError ):
            return cls.query.filter( cls.login == id ).first( )

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