from app.api.common.contracts import JSONContract
from app.service.models import BuildName, TaskName


class GetTasksRequest(JSONContract):
    """Contract between FE and BE."""

    build: BuildName


class GetTasksResponse(JSONContract):
    """Contract between FE and BE."""

    tasks: list[TaskName]
