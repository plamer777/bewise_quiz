"""This file contains parsers to parse parameters from response
objects"""
from flask_restx.reqparse import RequestParser
# --------------------------------------------------------------------------

question_parser = RequestParser()
question_parser.add_argument(
    name='question_num', type=int, required=False, location='json', default=1)
