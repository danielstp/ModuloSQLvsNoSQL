## Windows

```
git clone https://github.com/danielstp/ModuloSQLvsNoSQL.git
cd ModuloSQLvsNoSQL

docker-compose down
docker build -t prueba_django . 

docker-compose build

docker-compose up

# en otra consola
docker-compose down

#para entrar al contenedor
docker run --network django-sql-network -it localhost/prueba_django /bin/bash
# Cargar datos iniciales
./incio.sh
exit


python -m venv venv
.\venv\Scripts\activate

pip install -r requirements.txt
```
![](../Imgs/PipInstallDjango+extensions.png)

```
cd ejemploSimple

python manage.py migrate
```

![](../Imgs/DjangoMigrate.png)

```
sqlite3 db.sqlite3

.read ../DatosSQLite/sqlite-sakila-insert-data.sql

.q

```
![](../Imgs/CargarDatosEnSQLite.png)
```

python manage.py createsuperuser --username ${NombreDeUsuario} --email ${correo@gmail.com}

python manage.py runserver

```
![](../Imgs/DjangoRunServer.png)


## Linux o macOS

```
git clone https://github.com/danielstp/ModuloSQLvsNoSQL.git
cd ModuloSQLvsNoSQL
python3 -m venv venv
source venv/bin/activate

pip install django django_extensions

cd ejemploSimple

./manage.py migrate

sqlite3 db.sqlite3

.read ../DatosSQLite/sqlite-sakila-insert-data.sql

.q

```
![](../Imgs/PasosEnLinux.png)

![](../Imgs/FinalizarCargaDeDatosEnLinux.png)
```
./manage.py createsuperuser --username ${NombreDeUsuario} --email ${correo@gmail.com}

./manage.py runserver
```
![](../Imgs/EjecutarDjangoEnLinux.png)

## En un navegador

Acceder al http://localhost:8000/admin

![](../Imgs/Localhost8000.png)