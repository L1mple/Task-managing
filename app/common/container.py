from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from app.api.common.settings import ApiSettings


class Container(DeclarativeContainer):
    """Container for DI for all app."""

    api_settings = providers.Object(ApiSettings())
