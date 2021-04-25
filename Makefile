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

make lint:
	mypy app --pretty --show-error-context
	black app --check
	isort --check-only app
	flake8
