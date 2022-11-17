install:
	poetry install

brain-even:
	poetry run brain-even
brain-games:
	poetry run brain-games
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python -m pip install dist/*.whl
lint:
	poetry run flake8 brain_games