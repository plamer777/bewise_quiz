"""This file contains functions to create Flask app and initialize another
objects"""
from flask import Flask
from configs import FlaskConfig
from constants import CLEAR_DB
from setup import db, api
from views import task_ns
# ------------------------------------------------------------------------


def create_app() -> Flask:
    """This function creates and configures the Flask application
    :return: an instance of Flask
    """
    app = Flask(__name__)
    app.config.from_object(FlaskConfig())
    db.init_app(app)
    api.init_app(app)
    api.add_namespace(task_ns)
    with app.app_context():
        if CLEAR_DB:
            db.drop_all()
        db.create_all()

    return app

