"""This file contains DAO and Service instances to be imported into the
another units"""
from dao import TaskDao
from services import TaskService
# -------------------------------------------------------------------------

task_dao = TaskDao()
task_service = TaskService(task_dao)
