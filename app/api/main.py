from fastapi import FastAPI
from toolz import pipe

from app.common.container import Container

from . import common
from .common import dependencies, endpoints, error_handlers, event_handlers, middleware


def create_api() -> FastAPI:
    """Instantiate FastAPI-based Web API."""
    container = Container()
    container.wire(packages=[common])

    return pipe(
        container.api_settings().create_app(),
        # commons
        dependencies.bootstrap,
        error_handlers.bootstrap,
        event_handlers.bootstrap,
        middleware.bootstrap,
        # routes
        endpoints.bootstrap,
    )
