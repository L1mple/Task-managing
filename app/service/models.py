from pydantic import BaseModel

TaskName = str
BuildName = str
Dependecies = list[TaskName]


class Task(BaseModel):
    """Domain model of Task."""

    name: TaskName
    dependencies: Dependecies


class Build(BaseModel):
    """Domain model of Build."""

    name: BuildName
    tasks: list[TaskName]
