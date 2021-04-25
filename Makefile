test-cov:
	pytest --cov=app

test-watch:
	ptw

format:
	autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place app --exclude=__init__.py
	black app
	isort app

format-imports:
	isort --force-single-line-imports app
	make format

lint:
	mypy app --pretty --show-error-context
	black app --check
	isort --check-only app
	flake8

docker-build:
	docker build . -t fastapi-example:latest

docker-run:
	docker run --name fastapi-example -p 80:80 docker.io/library/fastapi-example:latest

migrate:
	alembic upgrade head

dev:
	poetry install
	poetry shell
	make migrate
