from dependency_injector.wiring import Provide, inject
from fastapi import FastAPI

from app.common.container import Container
from app.service.service import BuildService


def bootstrap(app: FastAPI) -> FastAPI:
    """Bootstrap general event handlers."""
    app.add_event_handler("startup", initialize_builds)
    return app


@inject
async def initialize_builds(  # noqa
    build_service: BuildService = Provide[Container.build_service],
) -> None:
    await build_service.seed_tasks()
    await build_service.seed_builds()
