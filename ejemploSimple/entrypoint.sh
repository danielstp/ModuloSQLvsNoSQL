#!/bin/bash
#
#

./manage.py collectstatic --noinput

./manage.py makemigrations app_name
./manage.py migrate

./manage.py runserver 0.0.0.0:8000
