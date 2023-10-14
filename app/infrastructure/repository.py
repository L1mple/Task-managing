from yaml import safe_load

from app.infrastructure.settings import BuildRepoSettings
from app.service.models import Build, Task


class BuildRepository:
    def __init__(self, settings: BuildRepoSettings) -> None:
        self.settings = settings

    async def get_tasks(self) -> list[Task]:
        with open(self.settings.TASK_FILE_PATH) as file:
            file_dict = safe_load(file)
            return [Task(**task_dict) for task_dict in file_dict.get("tasks")]

    async def get_builds(self):
        with open(self.settings.BUILD_FILE_PATH) as file:
            file_dict = safe_load(file)
            return [Build(**build_dict) for build_dict in file_dict.get("builds")]
