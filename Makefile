.DEFAULT_GOAL := tox
.PHONY: deps test lint tox publish

deps:
	pipenv install --dev

test:  ## Run tests with coverage
	pipenv run pytest --cov=mainentry tests/

lint:  ## Lint and static-check
	pipenv run black mainentry.py
	pipenv run flake8 mainentry.py
	pipenv run pylint mainentry.py
	pipenv run mypy mainentry.py

tox:
	 pipenv run python -m tox -e py39

