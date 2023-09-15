## Windows

```
git clone https://github.com/danielstp/ModuloSQLvsNoSQL.git
cd ModuloSQLvsNoSQL

python.exe -m venv venv
 .\venv\Scripts\activate

pip install django django_extensions

cd ejemploSimple


```
## Linux macOS

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
