"""This file contains model classes to get access to the database"""
from setup import db
# -------------------------------------------------------------------------


class Task(db.Model):
    """This class represents a task table in the database"""
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.Text, unique=True)
    answer = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    value = db.Column(db.Integer)
