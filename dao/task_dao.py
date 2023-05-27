"""This file contains DAO objects to work with the database"""
from sqlalchemy.exc import IntegrityError
from flask import current_app
from dao.models import Task
from services.schemas import TaskSchema
from setup import db
# -------------------------------------------------------------------------


class TaskDao:
    """The TaskDao class provides access to the database"""
    def __init__(
            self, session: db.session = db.session, model: db.Model = Task
    ) -> None:
        """Initialize the TaskDao class
        :param session: the session object to get access to the database
        :param model: a class inherited from db.Model
        """
        self._session = session
        self._model = model

    def get_by_question(self, question: str) -> Task | None:
        """This method returns a task found by the provided question
        :param question: a question to find the task by
        :return: a Task model or None if the question is not found
        """
        task = self._session.query(self._model).filter(
            Task.question == question).first()

        return task

    def get_last_one(self) -> Task | None:
        """This method returns a last task found it the database
        :return: a Task model or None if there is not any tasks in the database
        """
        last_task = self._session.query(self._model).order_by(
            self._model.id.desc()).first()
        return last_task

    def add(self, task: TaskSchema) -> Task | None:
        """This method adds a task to the database
        :param task: an instance of TaskSchema with task data to be added
        :return: a Task model or None if there was IntegrityError during the
        operation
        """
        try:
            new_task = self._model(**task.dict())
            with current_app.app_context():
                self._session.add(new_task)
                self._session.commit()
        except IntegrityError as e:
            print(f'An error occurred while adding the record: {e}')
            return None

    def __repr__(self) -> str:
        """Representation of the TaskDao class"""
        return f'TaskDao({self._model})'
