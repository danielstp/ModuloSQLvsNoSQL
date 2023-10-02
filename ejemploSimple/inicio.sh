#!/bin/bash
# Cargar los datos de inicio y crear superusuario prueba
#

#./manage.py migrate
./manage.py createsuperuser --username prueba --email prueba@prueba.com

# find renta/fixtures -name '*.json' | xargs -P4 -n1 ./manage.py loaddata

./manage.py loaddata renta/fixtures/renta.Country.json
./manage.py loaddata renta/fixtures/renta.City.json
./manage.py loaddata renta/fixtures/renta.Address.json
./manage.py loaddata renta/fixtures/renta.Store.json renta/fixtures/renta.Staff.json
./manage.py loaddata renta/fixtures/renta.Category.json
./manage.py loaddata renta/fixtures/renta.Language.json
./manage.py loaddata renta/fixtures/renta.Film.json renta/fixtures/renta.FilmCategory.json renta/fixtures/renta.Actor.json renta/fixtures/renta.FilmActor.json
./manage.py loaddata renta/fixtures/renta.Inventory.json
./manage.py loaddata renta/fixtures/renta.Customer.json
./manage.py loaddata renta/fixtures/renta.Rental.json
./manage.py loaddata renta/fixtures/renta.Payment.json
./manage.py loaddata renta/fixtures/renta.FilmText.json

