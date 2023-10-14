from pydantic import BaseModel

TaskName = str
BuildName = str
Dependecies = list[TaskName]


class Task(BaseModel):
    name: TaskName
    dependencies: Dependecies


class Build(BaseModel):
    name: BuildName
    tasks: list[TaskName]
