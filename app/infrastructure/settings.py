from pydantic_settings import BaseSettings, SettingsConfigDict


class BuildRepoSettings(BaseSettings):
    """Env settings for BuildRepository."""

    TASK_FILE_PATH: str = "volumes/tasks.yml"
    BUILD_FILE_PATH: str = "volumes/builds.yml"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="BUILD_REPO_",
        frozen=True,
    )
