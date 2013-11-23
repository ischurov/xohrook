#!/usr/bin/env python
from xohrook import app, db
from xohrook.models.users import User

if app.config['DEBUG']:
    @app.before_first_request
    def create_user():
        """
        In debug mode, create a test user.
        """
        db.create_all()
        user = User(email = "test@nodomain.noltd", password = 'password', realname = "Test user", active = True)
        db.session.add(user)
        db.session.commit()

app.run()