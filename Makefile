install: # установить зависимости
	poetry install

brain-games: # запустить сценарий
	poetry run brain-games

build: # собрать пакет
	poetry build

publish: # отладить публикацию, чтобы не добавлять пакет в каталог PyPI
	poetry publish --dry-run

package-install: # установить пакет из операционной системы
	python3 -m pip install --user dist/*.whl
