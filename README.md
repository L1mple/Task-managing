# Task managing Readme

## Project Purpose:

The primary objective of this project is to provide a service for the orchestration and execution of complex builds that consist of interdependent tasks. By analyzing the hierarchical structure of tasks within builds, this service efficiently parses the task tree, determines task dependencies, and calculates the optimal execution order for each build. This ensures that tasks are launched in a valid and logical sequence, streamlining the build process and enhancing overall project efficiency.

This is a brief guide on how to set up and run the project. Please follow the instructions below to get started.

## Setup

### Install Poetry

Make sure you have Poetry, a Python dependency management and packaging tool, installed on your system. If you don't have it, you can install it by following the instructions at [Poetry's official website](https://python-poetry.org/docs/#installation).

### Install Project Dependencies

After installing Poetry, navigate to the project's root directory and run the following command to install the project dependencies:

```bash
poetry install
```

### Configuration

Create a `.env` file in the root of the project and paste the following configuration settings:

```ini
FASTAPI_DEBUG=True
FASTAPI_TITLE="Build parser Web API"
FASTAPI_DESCRIPTION="Simple test parsing Web API"
FASTAPI_VERSION="0.1.0"
FASTAPI_CORS_ALLOW_ORIGINS=["*"]
FASTAPI_CORS_ALLOW_CREDENTIALS=True
FASTAPI_CORS_ALLOW_METHODS=["*"]
FASTAPI_CORS_ALLOW_HEADERS=["*"]
BUILD_REPO_TASK_FILE_PATH="volumes/tasks.yml"
BUILD_REPO_BUILD_FILE_PATH="volumes/builds.yml"
```

You can modify these settings according to your requirements.

## Testing

To run tests for your project, you can use the following command:

```bash
pytest --disable-warnings
```

This will execute the project's test suite and display the results.

## Deployment

### Using Docker and Docker Compose

If you have Docker and Docker Compose installed on your system, you can easily deploy the project. Run the following command from the root of the project:

```bash
docker-compose up
```

This will start the project in a Docker container with all the necessary configurations.

## Local Deployment

If you want to deploy the project locally, you can follow the standard FastAPI deployment procedures for your specific environment.

```bash
poetry run uvicorn app.api.main:create_api --host {your host} --port {your port} --factory --reload
```
