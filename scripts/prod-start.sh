#!/bin/bash
export FLASK_ENV = production

python manage.py db migrate

gunicorn --bind 0.0.0.0:5000 --workers 3 uwsgi:app

# start server

