from itertools import chain
from typing import Mapping

from app.common.errors import ConsistencyError, EntityNotFoundError, GetEntityError
from app.infrastructure.repository import BuildRepository
from app.service.models import BuildName, TaskName


class BuildService:
    """Service for 'business' logic."""

    def __init__(self, repository: BuildRepository) -> None:
        self.repository = repository
        self.builds: Mapping[BuildName, list[TaskName]] = {}
        self.tasks: Mapping[TaskName, list[TaskName]] = {}

    async def seed_tasks(self):
        """Seed self attribute with tasks from repo.

        Raises:
            GetEntityError: If smth went wrong in repo while fetching tasks
        """
        try:
            tasks_list = await self.repository.get_tasks()
        except Exception as exc:
            raise GetEntityError() from exc
        self.tasks = {task.name: task.dependencies for task in tasks_list}

    async def seed_builds(self):
        """Seed self attribute with builds from repo.

        Raises:
            GetEntityError: If smth went wrong in repo while fetching builds
        """
        try:
            builds_list = await self.repository.get_builds()
        except Exception as exc:
            raise GetEntityError() from exc
        self.builds = {build.name: build.tasks for build in builds_list}
        await self.validate_builds_tasks()

    async def validate_builds_tasks(self) -> Exception | None:
        """Validate if there is all tasks from builds are listed in self.tasks.

        Raises:
            ConsistencyError: If not -> data is not valid

        Returns:
            Exception | None: If all good returns nothing otherwise -> throw exc
        """
        builds_tasks = set(chain(*self.builds.values()))  # Unpack matrix to list
        valid_tasks = set(self.tasks.keys())
        if not builds_tasks.issubset(valid_tasks):
            raise ConsistencyError()

    async def get_sorted_tasks(self, build_name: BuildName) -> list[TaskName]:
        """Main function for get sorted list of tasks for build."""
        build_tasks = self.builds.get(build_name)
        if build_tasks is None:
            raise EntityNotFoundError("No build found with passed name")
        single_sorted_tasks = []
        for task in build_tasks:
            single_sorted_tasks.append(
                await self.get_sorted_tasks_for_task(
                    task_name=task,
                    sorted_tasks=[],
                    level=1,
                )
            )
        sorted_answer = set()
        while single_sorted_tasks:
            level = -1
            value_to_add = None
            index = None
            for index, array in enumerate(single_sorted_tasks):
                if array:
                    if array[0][1] > level:
                        value_to_add = array[0][0]
                        index = index
            sorted_answer.add(value_to_add)
            if single_sorted_tasks[index]:
                single_sorted_tasks[index].pop(0)
            else:
                single_sorted_tasks.pop(index)
        return [*sorted_answer]

    async def get_sorted_tasks_for_task(
        self,
        task_name: TaskName,
        sorted_tasks: list,
        level: int,
    ) -> list[tuple[TaskName, int]]:
        task_dependencies = self.tasks.get(task_name)
        if task_dependencies is None:
            raise ConsistencyError()
        if len(task_dependencies) > 0:
            for task_name in task_dependencies:
                sorted_tasks += await self.get_sorted_tasks_for_task(
                    task_name=task_name,
                    sorted_tasks=sorted_tasks,
                    level=level + 1,
                )
        sorted_tasks.append((task_name, level))
        return sorted_tasks
