from fastapi import HTTPException


class GetEntityError(HTTPException):
    """Custom Error."""

    def __init__(
        self,
    ) -> None:
        self.status_code = 501
        self.detail = "Something went wrong in getting entities from DB"


class ConsistencyError(HTTPException):
    """Custom Error."""

    def __init__(
        self,
    ) -> None:
        self.status_code = 502
        self.detail = "Passed values are not valid"


class EntityNotFoundError(HTTPException):
    """Custom Error."""

    def __init__(self, detail: str) -> None:
        self.status_code = 404
        self.detail = detail
