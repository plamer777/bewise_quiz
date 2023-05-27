"""This file contains schemas works as validators and serializers"""
from datetime import datetime
from flask_restx import fields, Model
from pydantic import BaseModel
from setup import api
# -------------------------------------------------------------------------

task: Model = api.model('Задание', {
    'id': fields.Integer(required=False, example=1),
    'question': fields.String(
        required=False, example='How many seconds in the day?'),
    'answer': fields.String(required=False, example='86400'),
    'created_at': fields.DateTime(
        required=False, example='2022-12-30T19:12:30.271Z'),
    'value': fields.Integer(required=False, example=500)
})


class TaskSchema(BaseModel):
    """The TaskSchema class serves to deserialize and validate data from
    json"""
    question: str = ''
    answer: str = ''
    created_at: datetime | None = None
    value: int = 0

    class Config:
        orm_mode = True
