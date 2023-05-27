"""This file contains an initially configured instance of the Api"""
from flask_restx import Api
from constants import API_VERSION, API_DESCRIPTION, API_TITLE
# -------------------------------------------------------------------------

api = Api(version=API_VERSION, title=API_TITLE, description=API_DESCRIPTION)
