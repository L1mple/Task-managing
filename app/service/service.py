from itertools import chain

from app.common.errors import ConsistencyError, EntityNotFoundError, GetEntityError
from app.infrastructure.repository import BuildRepository
from app.service.models import BuildName, TaskName


class BuildService:
    """Service for 'business' logic."""

    def __init__(self, repository: BuildRepository) -> None:
        self.repository = repository

    async def seed_tasks(self):
        """Seed self attribute with tasks from repo.

        Raises:
            GetEntityError: If smth went wrong in repo while fetching tasks
        """
        try:
            tasks_list = await self.repository.get_tasks_from_source()
        except Exception as exc:
            raise GetEntityError() from exc
        await self.repository.save_tasks(tasks_list=tasks_list)

    async def seed_builds(self):
        """Seed self attribute with builds from repo.

        Raises:
            GetEntityError: If smth went wrong in repo while fetching builds
        """
        try:
            builds_list = await self.repository.get_builds_from_source()
        except Exception as exc:
            raise GetEntityError() from exc
        await self.repository.save_builds(builds_list=builds_list)
        await self.validate_builds_tasks()

    async def validate_builds_tasks(self) -> Exception | None:
        """Validate if there is all tasks from builds are listed in self.tasks.

        Raises:
            ConsistencyError: If not -> data is not valid

        Returns:
            Exception | None: If all good returns nothing otherwise -> throw exc
        """
        builds = await self.repository.get_builds()
        tasks = await self.repository.get_tasks()
        builds_tasks = set(
            chain(*[build.tasks for build in builds])  # Unpack matrix to list
        )
        valid_tasks = {task.name for task in tasks}
        if not builds_tasks.issubset(valid_tasks):
            raise ConsistencyError()

    async def get_sorted_tasks(self, build_name: BuildName) -> list[TaskName]:
        """Main gateway to "business" logic of service.

        Args:
            build_name (BuildName): Name of build to prepare tasks list

        Raises:
            EntityNotFoundError: If there is no such build in system

        Returns:
            list[TaskName]: Sorted list of TaskNames
        """
        build = await self.repository.get_build(build_name=build_name)
        if build is None:
            raise EntityNotFoundError("No build found with passed name")
        single_sorted_tasks = []
        used_tasks = set()
        for task in build.tasks:
            sorted_tasks, used_tasks_single = await self.get_sorted_tasks_for_task(
                task_name=task,
                sorted_tasks=[],
                used_tasks=used_tasks,
            )
            used_tasks.update(used_tasks_single)
            single_sorted_tasks.append(sorted_tasks)
        return list(chain(*single_sorted_tasks))

    async def get_sorted_tasks_for_task(
        self,
        task_name: TaskName,
        sorted_tasks: list,
        used_tasks: set,
    ) -> tuple[list[TaskName], set[TaskName]]:
        """Recursive iterate through tree of tasks.

        Args:
            task_name (TaskName): Current node
            sorted_tasks (list): Cached result from previous steps
            used_tasks (set): Set with unique task names

        Raises:
            ConsistencyError: If passed data builds <-> tasks are not valid

        Returns:
            tuple[list[TaskName], set[TaskName]]: result answer and helper set
        """
        task = await self.repository.get_task(task_name=task_name)
        if task is None:
            raise ConsistencyError()
        if task_name in used_tasks:
            return sorted_tasks, used_tasks
        if len(task.dependencies) > 0:
            for dependant_task_name in task.dependencies:
                sorted_tasks, used_tasks = await self.get_sorted_tasks_for_task(
                    task_name=dependant_task_name,
                    sorted_tasks=sorted_tasks,
                    used_tasks=used_tasks,
                )
        sorted_tasks.append(task_name)
        used_tasks.add(task_name)
        return sorted_tasks, used_tasks
