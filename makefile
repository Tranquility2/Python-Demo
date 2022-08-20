.PHONY: *

COLOUR_BLUE=\033[0;34m
COLOUR_END=\033[0m

setup:
	poetry install

run:
	@poetry run python app/main.py

clean:
	@find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
	@rm -rf .mypy_cache
	@rm -rf .pytest_cache
	@echo "$(COLOUR_BLUE)Clean Done$(COLOUR_END)"

check: isort black pytest flake8 mypy 
	@echo "$(COLOUR_BLUE)Check Done$(COLOUR_END)"

isort:
	@echo "$(COLOUR_BLUE)Running isort$(COLOUR_END)"
	@poetry run isort app

black:
	@echo "$(COLOUR_BLUE)Running black$(COLOUR_END)"
	@poetry run black app -v

pytest:
	@echo "$(COLOUR_BLUE)Running pytest$(COLOUR_END)"
	@poetry run pytest

flake8:
	@echo "$(COLOUR_BLUE)Running flake8$(COLOUR_END)"
	@poetry run flake8 app

mypy:
	@echo "$(COLOUR_BLUE)Running mypy$(COLOUR_END)"
	@poetry run mypy app

docs-serve:
	@poetry run mkdocs serve

docs-build:
	@poetry run mkdocs build
