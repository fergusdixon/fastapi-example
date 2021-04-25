# fastapi-example
An example of FastAPI basics

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/0e332b810fbe47f8962f04e2c5e9fc54)](https://www.codacy.com/gh/fergusdixon/fastapi-example/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=fergusdixon/fastapi-example&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/0e332b810fbe47f8962f04e2c5e9fc54)](https://www.codacy.com/gh/fergusdixon/fastapi-example/dashboard?utm_source=github.com&utm_medium=referral&utm_content=fergusdixon/fastapi-example&utm_campaign=Badge_Coverage)

## Getting set up

Check the Makefile for useful macros

Using [Poetry](https://python-poetry.org/) install dependencies

```shell
poetry install
```

### Structure

```
-- .github      : Github Actions defintions
-- alembic      : Database table definitions
-- app
---- api        : Endpoint defintions and routes
---- core       : Configuration management
---- crud       : Tools for performing CRUD ops on various models
---- db         : Boilerplate sqlalchemy set up
---- schemas    : Pydantic definitions for models and API requests/responses
---- tests      : Unit and BDD tests
```


### Build the docker image

```shell
make docker-build
```

Start the docker image
```shell
make docker-run
```

The API will be available at http://localhost (port 80)
Docs are at http://localhost/docs

### Tests

Run unittests with coverage (in `app/tests`):

```shell
make test-cov
```

Or with pytest-watch to rerun tests every time a change is made:

```shell
make test-watch
```

Run Behave tests (in `app/tests/features`):

```shell
make bdd
```

### Linting

You can check if your code is up to scratch:

```shell
make lint
```

Fix it automatically:

```shell
make format-imports
```
