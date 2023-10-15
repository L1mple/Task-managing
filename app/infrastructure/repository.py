from typing import Mapping

from yaml import safe_load

from app.infrastructure.settings import BuildRepoSettings
from app.service.models import Build, BuildName, Dependecies, Task, TaskName


class BuildRepository:
    """Class that represents data access layer."""

    def __init__(self, settings: BuildRepoSettings) -> None:
        self.settings = settings
        self.builds: Mapping[BuildName, list[TaskName]] = {}
        self.tasks: Mapping[TaskName, Dependecies] = {}

    async def get_tasks_from_source(self) -> list[Task]:
        """Getting tasks from source."""
        with open(self.settings.TASK_FILE_PATH) as file:
            file_dict = safe_load(file)
            return [Task(**task_dict) for task_dict in file_dict.get("tasks")]

    async def get_builds_from_source(self):
        """Gettings builds from source."""
        with open(self.settings.BUILD_FILE_PATH) as file:
            file_dict = safe_load(file)
            return [Build(**build_dict) for build_dict in file_dict.get("builds")]

    async def save_tasks(self, tasks_list: list[Task]):
        """Save tasks to internal vault.

        Args:
            tasks_list (list[Task]): List of Tasks for builds
        """
        self.tasks = {task.name: task.dependencies for task in tasks_list}

    async def save_builds(self, builds_list: list[Build]):
        """Save builds to internal vault.

        Args:
            builds_list (list[Build]): List of Builds with inner tasks
        """
        self.builds = {build.name: build.tasks for build in builds_list}

    async def get_builds(self) -> list[Build]:
        """Get a list of all Builds.

        Returns:
            list[Build]: Returns list with Builds
        """
        return [
            Build(
                name=build_name,
                tasks=build_tasks,
            )
            for build_name, build_tasks in self.builds.items()
        ]

    async def get_tasks(self) -> list[Task]:
        """Get a list of all Tasks.

        Returns:
            list[Task]: Returns lst with Tasks
        """
        return [
            Task(
                name=task_name,
                dependencies=task_dependencies,
            )
            for task_name, task_dependencies in self.tasks.items()
        ]

    async def get_task(self, task_name: TaskName) -> Task | None:
        """Get a  Task by name.

        Args:
            task_name (TaskName): TaskName

        Returns:
            Task | None: Returns Task if it exists otherwise - None
        """
        task_dependencies = self.tasks.get(task_name)
        if task_dependencies is None:
            return
        return Task(name=task_name, dependencies=task_dependencies)

    async def get_build(self, build_name: BuildName) -> Build | None:
        """Get b Build by name.

        Args:
            build_name (BuildName): BuildName

        Returns:
            Build | None: Returns a Build if it exists otherwise - None
        """
        build_tasks = self.builds.get(build_name)
        if build_tasks is None:
            return
        return Build(name=build_name, tasks=build_tasks)
