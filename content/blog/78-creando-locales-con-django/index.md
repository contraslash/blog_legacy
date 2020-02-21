---
title: "Creando Locales con Django"
date: "2016-02-16T17:15:13+00:00"
description: "Usando el módulo de internacionalización i18n en Django para crear traducciones de cadenas en templates y archivos python"
tags: "Django"
---
# Creando Locales con Django

Como primera instancia, necesitamos asegurarnos de tener el Middleware en nuestra lista de Middleware en el archivo *settings.py*

```
MIDDLEWARE_CLASSES = [
    ...
    'django.middleware.locale.LocaleMiddleware',
]
```

Luego vamos a nuestra aplicación y creamos una nueva carpeta llamada locales, seguido del comando makemessages de django con el código de lenguaje

```
mkdir locale
django-admin makemessages -l <código de lenguaje>
```

A continuación se crearán un sistema de ficheros de forma <códugo de lenguaje>/LC_MESSAGES/django.po

En el archivo django.po tendremos una archivo que recolecta la información de los tags trans y blocktrans, para que realicemos la traducción.

Una vez terminada la traducción podremos ejecutar el comando compilemessages

```
django-admin compilemessages
```

Que creará un archivo *.mo* con la información de nuestra traducción.

Por último, para cargar los archivos, creamos la variable LOCALE_PATHS en nuestro archivo *settings.py* indicando la localización de los archivos de traducción

```
LOCALE_PATHS = [
    ...
    '<ruta de la aplicación>/locale',
]
```

### TroubleShooting
```
CommandError: Can't find msguniq. Make sure you have GNU gettext tools 0.15 or newer installed.
```
Es necesario instalar maketext, en ubuntu
```
sudo apt-get install gettext
```
en OSX usando Brew
```
brew install gettext
```
Además asegurarse de que maketext esté en el path
```
export PATH=$PATH:/usr/local/Cellar/gettext/0.19.8.1/bin/
```
donde 0.19.8.1 es la versión de Make Text

