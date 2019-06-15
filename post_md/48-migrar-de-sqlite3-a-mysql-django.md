Title: Migrar de sqlite3 a MySQL Django
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: Django,Ubuntu,MySQL,SQLite3
---
# Migrar de sqlite3 a MySQL DjangoLas migraciones de base de datos, independiente de la razón, siempre son fastiosas

Si aún no está instalado MySQL, instalarlo 

```
sudo apt-get install mysql-server

```

También necesitamos Python-dev

```
sudo apt-get install python-dev

```

Instalamos dependencias requeridas en el Sistema operativo
```
sudo apt-get install libmysqlclient-dev
sudo pip install MySQL-python
```

Insalamos las dependencias en nuestro virtualenv

`pip install MySQL-python`

Existen dos aproximaciones a al dump data: especificando las aplicaciones que queremos migrar
`manage.py dumpdata --natural-foreign auth.User  > initial_data.json
`

y excluyendo

`./manage.py dumpdata --exclude=contenttypes --exclude=auth.Permission > initial_data.json`

Altamente recomiendo usar este último, pues evita problemas de llaves foraneas.

Luego podemos modificar nuestro archivo *settings.py* actualizando nuestra configuración de bases de datos
de:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
a:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(BASE_DIR,  'database.cnf'),
        },
    }
}
```

donde *database.cnf* es algo como
```
[client]
database = database
user = user_database
password = password_database
default-character-set = utf8
```

Ahora es importante migrar la base de datos
`./manage.py migrate `

Luego podemos importar datos.

Para importar los datos.

`python manage.py loaddata initial_data.json ` 
	
Cabe aclarar que pueden existir conflictos, específicamete con llaves foraneas, es posible que realmente el problema sea de integridad de la base de datos. Igual vale la pena verificar que los datos sean correctos

Espero que esto les haya sido útil o al menos les haya dado algo de luz

PD: Para extraer datos directamente de sqlite, uso el siguiente comando:

`sqlite3 db.sqlite3 ".dump 'tabla1' 'tabla2'" | grep INSERT > dump_tablas.sql`