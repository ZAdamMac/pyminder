"""
This script is a component of the back-end service for the Pyminder Rasberry Pi utility..
It is the app-defining component of the Flask-based API/UI service.
Author: Zac Adam-MacEwen (zadammac@kenshosec.com)
An Arcana Labs utility.
Produced under license.
Full license and documentation to be found at:
https://github.com/ZAdamMac/pyminder
"""

from flask import Blueprint
from flask_restful import Api
from resources.messages import MessageAPI
from resources.users import UsersAPI

__version__ = "0.2.0"  # This version represents the overall version of the service this app instantiates.


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# New Routes below this line
api.add_resource(MessageAPI, '/messages/')
api.add_resource(UsersAPI, '/users/')
