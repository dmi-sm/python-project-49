install: # установить зависимости
	poetry install

brain-games: # запустить сценарий
	poetry run brain-games

build: # собрать пакет
	poetry build

publish: # отладить публикацию, чтобы не добавлять пакет в каталог PyPI
	poetry publish --dry-run

package-install: # установить пакет в окружение пользователя
	python3 -m pip install --user dist/hexlet_code-0.2.1-py3-none-any.whl

package-reinstall: # переустановить пакет
	python3 -m pip install --upgrade --force-reinstall dist/hexlet_code-0.2.1-py3-none-any.whl

lint: # запустить проверку линтером
	poetry run flake8 brain_games

package-uninstall: # удалить пакет из окружения пользователя
	python3 -m pip uninstall dist/*.whl