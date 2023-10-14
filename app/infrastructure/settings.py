from pydantic_settings import BaseSettings, SettingsConfigDict


class BuildRepoSettings(BaseSettings):
    TASK_FILE_PATH: str
    BUILD_FILE_PATH: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="BUILD_REPO_",
        frozen=True,
    )
