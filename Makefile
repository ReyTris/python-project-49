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
	py -m pip install --user dist/*.whl
lint:
	poetry run flake8 brain_games