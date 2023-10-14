from fastapi import FastAPI
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ApiSettings(BaseSettings):
    """Settings for FastAPI."""

    DEBUG: bool = Field(default=False)
    TITLE: str = Field(default="Build parser Web API")
    DESCRIPTION: str = Field(default="Simple test parsing Web API")
    VERSION: str = Field(default="0.1.0")

    CORS_ALLOW_ORIGINS: list[str] = Field(default=["*"])
    CORS_ALLOW_CREDENTIALS: bool = Field(default=True)
    CORS_ALLOW_METHODS: list[str] = Field(default=["*"])
    CORS_ALLOW_HEADERS: list[str] = Field(default=["*"])

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="FASTAPI_",
        frozen=True,
    )

    def create_app(self) -> FastAPI:
        """Create basic instance of FastAPI from configuration.

        Returns:
            FastAPI
        """
        return FastAPI(
            debug=self.DEBUG,
            title=self.TITLE,
            description=self.DESCRIPTION,
            version=self.VERSION,
        )
