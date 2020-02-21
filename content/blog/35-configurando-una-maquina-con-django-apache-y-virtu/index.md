---
title: "Configurando una máquina con Django, Apache y Virtualenv"
date: "2016-01-29T06:42:23+00:00"
description: ""
tags: "Django,Python"
---
# Configurando una máquina con Django, Apache y Virtualenv

Primero necesitamos un Ubuntu Virgen
Actualizamos el sistema
 `sudo apt-get update && sudo apt-get upgrade `

Instalamos pip y las herramientas de desarrollo para python
`sudo apt-get install python-dev python-pip`

Instalamos las herramientas de virtualización de ambientes de python
`sudo pip install virtualenv virtualenvwrapper`

En Ubuntu, por defecto las librerías de instalación de virtualenv no están en el path, así que las volvemos alcanzables
`source /usr/local/bin/virtualenvwrapper.sh `

Por último creamos un nuevo ambiente
`mkvirtualenv nombreAmbiente`

Por defecto tras la creación del ambiente, se nos coloca dentro, así que ya podremos instalar nuestras dependencias
`pip install requirements.txt # install requirements`

 Ahora configuremos apache
 `sudo apt-get install apache2 libapache2-mod-wsgi`

 Luego crearemos nuestro archivo de configuración en /etc/apache2/sites-aviables/nombredominio.com.conf
 ```
 WSGIPythonPath /ruta/proyecto/nombreProyecto:/home/nombreUsuario/.virtualenvs/nombreAmbiente/lib/python2.7/site-packages
<VirtualHost *:80>

        ServerName nombredominio.com
        ServerAdmin micorreo@correo.com
        WSGIScriptAlias / /ruta/proyecto/nombreProyecto/nombreProyecto/wsgi.py

        <Directory /ruta/proyecto/nombreProyecto.com>
                Order allow,deny
                Allow from all
                <Files wsgi.py>
                        Require all granted
                </Files>
        </Directory>

        Alias /media   /ruta/proyecto/nombreProyecto/media
        Alias /static  /ruta/proyecto/nombreProyecto/static

        <Directory /ruta/proyecto/nombreProyecto/static>
                Require all granted
                Options -Indexes
        </Directory>


        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>
 ```

 luego

 `sudo a2ensite nombredominio.com`

`sudo service apache2 reload`

