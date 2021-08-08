#!/bin/bash
# set up webpage

export FLASK_APP=app

pip install poetry
poetry install
poetry shell

cd flaskr
flask run
