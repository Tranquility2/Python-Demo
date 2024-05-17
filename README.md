[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

# 📜 Python Demo Project

The demo will fetch a list of "Top Memes".

Usage: `poetry run python app/main.py <number or results>`
> Default list length is 10 items

📝 Please note the main objective was just to showcase packages like httpx, rich and typer.

## Commands for this project
> using the makefile

* `make setup` - Setup the project using Poetry.
* `make run` - Run the project using Poetry.
* `make cleanup` - Clenup for any temp files in the project.
* `make check` - Run all checks and formatters.
* `make docs-serve` - Serve the docs using mkdocs.
* `make docs-build` - Build the docs using mkdocs.
