from itertools import chain
from typing import Mapping

from app.common.errors import ConsistencyError, GetEntityError
from app.infrastructure.repository import BuildRepository
from app.service.models import BuildName, TaskName


class BuildService:
    def __init__(self, repository: BuildRepository) -> None:
        self.repository = repository
        self.builds: Mapping[BuildName, list[TaskName]] = {}
        self.tasks: Mapping[TaskName, list[TaskName]] = {}

    async def seed_tasks(self):
        try:
            tasks_list = await self.repository.get_tasks()
        except Exception as exc:
            raise GetEntityError() from exc
        self.tasks = {task.name: task.dependencies for task in tasks_list}

    async def seed_builds(self):
        try:
            builds_list = await self.repository.get_builds()
        except Exception as exc:
            raise GetEntityError() from exc
        self.builds = {build.name: build.tasks for build in builds_list}
        await self.validate_builds_tasks()

    async def validate_builds_tasks(self) -> Exception | None:
        builds_tasks = set(list(chain(*self.builds.values())))  # Unpack matrix to list
        valid_tasks = set(self.tasks.keys())
        if not builds_tasks.issubset(valid_tasks):
            raise ConsistencyError()
