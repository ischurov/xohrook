from flask import Blueprint, render_template, abort
from ..db import User

blueprint = Blueprint( 'users', __name__, template_folder = 'templates' )

@blueprint.route( '/', methods = [ 'GET' ] )
def index( ):
    users = User.query.all( )
    return render_template( 'users.html', users = users )

@blueprint.route( '/<id>', methods = [ 'GET' ] )
def get( id ):
    user = User.from_id_or_login( id )
    if user is None:
        abort( 404 )
    return render_template( 'user.html', user = user )
