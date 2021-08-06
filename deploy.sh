: set up webpage

cd flask
export FLASK_APP=src/app

pip install poetry
poetry install
poetry shell
flask run
