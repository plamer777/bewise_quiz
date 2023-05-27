"""This file contains FlaskConfig class with basic settings for SQLAlchemy,
Flask and Flask-RESTX"""
from constants import DB_URI
# -------------------------------------------------------------------------


class FlaskConfig:
    """The configuration class"""
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    RESTX_JSON = {
        'ensure_ascii': False,
    }
