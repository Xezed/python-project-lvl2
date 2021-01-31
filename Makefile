install:
	poetry install

build:
	poetry build

package-install:
	pip3 install dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

coverage:
	poetry run pytest --cov gendiff
