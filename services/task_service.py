"""This file contains services with business logic"""
import requests
from constants import QUIZ_BASE_URL
from dao.models import Task
from dao.task_dao import TaskDao
from services.schemas import TaskSchema
from utils import create_schemas
# --------------------------------------------------------------------------


class TaskService:
    """The TaskService class provides an interface to process user requests"""
    def __init__(
            self, dao: TaskDao, schema: type[TaskSchema] = TaskSchema,
            api_url: str = QUIZ_BASE_URL) -> None:
        """Initialize the service
        :param dao: an instance of TaskDao class
        :param schema: the TaskSchema class
        :param api_url: the string representing base URL of external API
        service
        """
        self._dao = dao
        self._schema = schema
        self._api_url = api_url

    def add_new(self, question_num: int = 1) -> Task | None:
        """This method serves to get a list of questions from external
        service and send it to the DAO object
        :param question_num: an amount of questions to get
        :return: a Task model or None if there is no record in the database
        """
        last_question = self._dao.get_last_one()
        while question_num > 0:
            response = requests.get(self._prepare_url(question_num))
            for question in create_schemas(self._schema, response):
                if not self._dao.get_by_question(question.question):
                    self._dao.add(question)
                    question_num -= 1

        return last_question

    def _prepare_url(self, question_count: int) -> str:
        """This closed method is used to prepare the base URL to get a list of
        questions
        :param question_count: number of questions to get
        :return: a string representing the prepared URL
        """
        return f'{self._api_url}{question_count}'

    def __repr__(self) -> str:
        """Representation of the class instance"""
        return f'TaskService({self._dao}, {self._schema}, {self._api_url})'
