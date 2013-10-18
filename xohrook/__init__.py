from flask import Flask

app = Flask( __name__, instance_relative_config = True )

app.config.from_pyfile( 'xohrook.cfg' )

@app.teardown_request
def shutdown_session(exception=None):
    from .db.flask import db_session
    db_session.remove()

from .views import *