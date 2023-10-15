FROM python:3.11-slim

ARG PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.5.1

WORKDIR /backend
COPY . /backend/

RUN python -m pip install --upgrade pip
RUN python -m pip install "poetry==$POETRY_VERSION"

RUN poetry config virtualenvs.create true \
    && poetry install --no-interaction --no-ansi

CMD ["poetry", "run", "uvicorn", "app.api.main:create_api", "--host", "0.0.0.0", "--port", "800", "--factory", "--reload"]