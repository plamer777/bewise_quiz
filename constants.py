"""This file contains constants to configure the application"""
import os
# -------------------------------------------------------------------------


POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT')
POSTGRES_DB = os.environ.get('POSTGRES_DB')

DB_URI = (
    f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:'
    f'{POSTGRES_PORT}/{POSTGRES_DB}')

CLEAR_DB = os.environ.get('CLEAR_DB').lower() == 'true'


QUIZ_BASE_URL = 'https://jservice.io/api/random?count='

API_VERSION = os.environ.get('API_VERSION')
API_TITLE = os.environ.get('API_TITLE')
API_DESCRIPTION = os.environ.get('API_DESCRIPTION')
