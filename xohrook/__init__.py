from flask import Flask
from .db.flask import FlaskSQLA

# Create application
app = Flask( __name__, instance_relative_config = True )

# Read instance config file
app.config.from_pyfile( 'xohrook.cfg' )

# Connect to database
dbm = FlaskSQLA( app )

from .views import *