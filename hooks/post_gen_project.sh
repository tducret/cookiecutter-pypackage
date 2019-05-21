#!/bin/bash

# This script is executed after the cookiecutter instantiation
# It creates a virtual environment
# Install the requirements and create the requirements.txt 

python3 -m venv venv
source ./venv/bin/activate
pip install -U pip

pip install -r requirements-to-freeze.txt --upgrade
pip freeze > requirements.txt