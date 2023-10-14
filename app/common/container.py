from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from app.api.common.settings import ApiSettings
from app.infrastructure.repository import BuildRepository
from app.infrastructure.settings import BuildRepoSettings
from app.service.service import BuildService


class Container(DeclarativeContainer):
    """Container for DI for all app."""

    api_settings = providers.Object(ApiSettings())
    build_repo_settings = providers.Object(BuildRepoSettings())  # type: ignore

    build_repository = providers.Singleton(
        BuildRepository,
        settings=build_repo_settings,
    )
    build_service = providers.Singleton(
        BuildService,
        repository=build_repository,
    )
