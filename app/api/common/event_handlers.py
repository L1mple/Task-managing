from fastapi import FastAPI


def bootstrap(app: FastAPI) -> FastAPI:
    """Bootstrap general event handlers."""
    # TODO Preprocess builds
    return app
