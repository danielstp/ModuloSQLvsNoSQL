#!/bin/bash
#
#

./manage.py collectstatic --noinput

./manage.py makemigrations renta
./manage.py migrate

./manage.py runserver 0.0.0.0:8000
