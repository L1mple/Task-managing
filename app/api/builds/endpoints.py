from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Body, Depends, FastAPI

from app.api.builds.contracts import GetTasksRequest, GetTasksResponse
from app.common.container import Container
from app.service.service import BuildService

router = APIRouter(prefix="/build", tags=["Build"])


def bootstrap(app: FastAPI) -> FastAPI:
    """Initialize task router for app."""
    app.include_router(router)
    return app


@router.post(
    "/get_tasks",
    description="Fetch sorted array of tasks to do for build",
    response_description="Sorted array of tasks",
    status_code=200,
    response_model=GetTasksResponse,
    responses={
        404: {"description": "No build with such name"},
        409: {"description": "Build <-> Tasks combo not valid :("},
        200: {"description": "Success response with sorted array of tasks"},
    },
)
@inject
async def get_build_tasks_by_name(
    build_service: BuildService = Depends(Provide[Container.build_service]),  # noqa
    body: GetTasksRequest = Body(  # noqa
        default=...,
        description="Body with required buiid parameter",
    ),
):
    """Get tasks for build."""
    sorted_tasks = await build_service.get_sorted_tasks(build_name=body.build)
    return GetTasksResponse(tasks=sorted_tasks)
