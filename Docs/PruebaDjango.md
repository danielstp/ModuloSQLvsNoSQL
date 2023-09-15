## Windows

```
git clone https://github.com/danielstp/ModuloSQLvsNoSQL.git
cd ModuloSQLvsNoSQL

python -m venv venv
.\venv\Scripts\activate

pip install django django_extensions
```
![](../Imgs/PipInstallDjango+extensions.png)

```
cd ejemploSimple

python manage.py migrate
```

![](../Imgs/DjangoMigrate.png)

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

./manage.py createsuperuser --username ${NombreDeUsuario} --email ${correo@gmail.com}

./manage.py runserver
```


## En un navegador

Acceder al http://localhost:8000/admin

![](../Imgs/Localhost8000.png)