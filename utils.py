"""This file contains different utility functions"""
from pydantic.error_wrappers import ValidationError
from requests import Response
from services.schemas import TaskSchema
# --------------------------------------------------------------------------


def create_schemas(
        schema: type[TaskSchema], response: Response) -> list[TaskSchema]:
    """This function serves to create TaskSchema instances by using data json
    data from response
    :param schema: a TaskSchema class
    :param response: a Response object
    :return: a list of TaskSchema instances
    """
    questions_json = response.json()
    questions = []
    for question_data in questions_json:
        try:
            question = schema(**question_data)
            questions.append(question)
        except ValidationError as e:
            print(f'The error occurred while creating schema: {e}')

    return questions
