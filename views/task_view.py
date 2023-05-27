"""The file contains CBVs to process user requests"""
from typing import Any
from flask_restx import Resource, Namespace
from services.parsers import question_parser
from services.schemas import task
from container import task_service
# -------------------------------------------------------------------------

task_ns = Namespace('tasks')


@task_ns.route('/add/')
class TasksView(Resource):
    """The TaskView is a CBV to work with routes like /tasks/add/"""
    @task_ns.doc(
        description='This route allows you to send question_num '
                    'parameter to save unique questions. '
                    'As response you will get a last saved question')
    @task_ns.expect(question_parser)
    @task_ns.marshal_with(task, code=201, description='Added', as_list=False)
    def post(self) -> dict[str, Any]:
        """This method serves to precess POST requests"""
        return task_service.add_new(**question_parser.parse_args())
