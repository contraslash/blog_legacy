---
title: "Configurando Taiga"
date: "2016-08-19T19:51:05+00:00"
description: ""
tags: "Apache,Django,Taiga"
---
# Configurando Taiga

Taiga es un Software de Manejo de Proyectos desarrollado en Python y Django, de código abierto. La instalación oficial puede encontrarse [aquí](http://taigaio.github.io/taiga-doc/dist/setup-production.html)

### Requerimientos de Sistema Operativo
Requerimientos en el servidor web
```
sudo apt-get install -y build-essential binutils-doc autoconf flex bison libjpeg-dev
sudo apt-get install -y libfreetype6-dev zlib1g-dev libzmq3-dev libgdbm-dev libncurses5-dev
sudo apt-get install -y automake libtool libffi-dev curl git tmux gettext
sudo apt-get install libpq-dev
```

Requerimientos en el servidor de base de datos

```
sudo apt-get install -y postgresql-9.3 postgresql-contrib-9.3
sudo apt-get install -y postgresql-doc-9.3 postgresql-server-dev-9.3
```

Configuración de usuarios en la base de datos
```
sudo -u postgres createuser taiga
sudo -u postgres createdb taiga -O taiga
```

### Requerimientos de Python
```
sudo apt-get install -y python3 python3-pip python-dev python3-dev python-pip virtualenvwrapper
sudo apt-get install libxml2-dev libxslt-dev
```

Crear el ambiente virtual con Python 3.4
```
mkvirtualenv -p /usr/bin/python3.4 taiga
```

Descargue el proyecto taiga-back
```
git clone https://github.com/taigaio/taiga-back.git taiga-back
cd taiga-back
git checkout stable
```

Instalar las dependencias con pip
```
pip install -r requirements.txt
```

Copiar el archivo de configuracion local

```
cp settings/local.py.example settings/local.py
```

Configurar la base de datos en settings/local.py

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'taiga',
        'USER': 'taiga',
        'PASSWORD': 'Secret',
        'HOST': 'IP.DEL.SERVER.BD',
        'PORT': '5432',
    }
}
```

> Si se tienenen problemas con la conexión, se puede revisar este [enlace ]( http://www.cyberciti.biz/tips/postgres-allow-remote-access-tcp-connection.html)

Llenar la base de datos con la información inicial requerida
```
python manage.py migrate --noinput
python manage.py loaddata initial_user
python manage.py loaddata initial_project_templates
python manage.py loaddata initial_role
python manage.py compilemessages
python manage.py collectstatic --noinput
```

Terminar la configuración del archivo local.py
```
from .common import *

MEDIA_URL = "http://example.com/media/"
STATIC_URL = "http://example.com/static/"
ADMIN_MEDIA_PREFIX = "http://example.com/static/admin/"
SITES["front"]["scheme"] = "http"
SITES["front"]["domain"] = "example.com"

SECRET_KEY = "theveryultratopsecretkey"

DEBUG = False
TEMPLATE_DEBUG = False
PUBLIC_REGISTER_ENABLED = True

DEFAULT_FROM_EMAIL = "no-reply@example.com"
SERVER_EMAIL = DEFAULT_FROM_EMAIL
```

### Configuración de Apache
Creamos un nuevo ambiente virtual en /etc/apache2/sites-aviable/api.example.com
Con el siguiente contenido
```
<VirtualHost *:80>
    ServerName api.example.com
    ServerAdmin ma0@contraslash.com

    WSGIDaemonProcess apiprojects.contraslash.com processes=2 threads=15 display-name=%{GROUP} python-path=/ruta/a/taiga-back:/ruta/a/virtualenv/taiga/lib/python3.4/site-packages
    WSGIProcessGroup example.com

    WSGIScriptAlias / /ruta/a/taiga-back/taiga/wsgi.py

    <Directory /ruta/a/taiga-back>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    Alias /media/   /var/www/html/api.example.com/media/
    Alias /static/  /var/www/html/api.example.com/static/

    <Directory /var/www/html/api.example.com/media>
        Options -Indexes
        Require all granted
    </Directory>

    <Directory /var/www/html/api.example.com>
                Options -Indexes
                Require all granted
        </Directory>
    <Location "/media/">
        Options -Indexes
    </Location>


    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet


```

active el sitio con y recargue apache
```
sudo a2ensite example.com
sudo apache2 reload
```

Pruebe el sitio en example.com/api/v1/

### Exponga el Front end

Descargue el sitio taiga-front
```
git clone https://github.com/taigaio/taiga-front-dist.git taiga-front-dist
cd taiga-front-dist
git checkout stable
```

Copiar el archivo de configuración
```
cp dist/conf.example.json dist/conf.json
```

Modificar el archivo de configuración dist/conf.json
```
{
    "api": "http://api.example.com/api/v1/",
    "eventsUrl": "ws://example.com/events",
    "debug": "true",
    "publicRegisterEnabled": true,
    "feedbackEnabled": true,
    "privacyPolicyUrl": null,
    "termsOfServiceUrl": null,
    "maxUploadFileSize": null,
    "contribPlugins": []
}
```

Exponga la carpeta dist para que sea alcanzable por su navegador web

Cree el archivo /etc/apache2/sites-aviable/example.com
con el siguiente contenido
```
<VirtualHost *:80>

    ServerName example.com
    ServerAdmin webmaster@example.com
    DocumentRoot /var/www/html/example.com/

    <Directory /var/www/html/example.com/>
        Options -Indexes +FollowSymLinks
            AllowOverride All
        Require all granted
        </Directory>



    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet
```

Asegúrese de tener el modulo rewrite activado

```
sudo a2enmod rewrite
sudo apache2 restart
```

Recargue la configuración de apache
```
service apache2 reload
```

Por último añada el archivo .htacces en su document_root

```
<IfModule mod_rewrite.c>    
    RewriteEngine on
    RewriteBase /
        RewriteCond %{REQUEST_URI} !^/static(.*)
        RewriteCond %{REQUEST_URI} !^/media(.*)
        RewriteCond %{REQUEST_FILENAME} !-f
    RewriteCond %{REQUEST_FILENAME} !-d
        RewriteRule ^(.*)$ /index.html [L]
</IfModule>
```


### TrubleShooting
Para que Apache2 pueda ejecutar una aplicación de python3 debe tener instalado el siguiente paquete

```
sudo apt-get install libapache2-mod-wsgi-py3
```

> Tenga en cuenta que este paquete sobre escribe el móduglo `mod_wsgi` así que si tiene algunos otros sitios con python2 no es recomendable desplegar con este método

