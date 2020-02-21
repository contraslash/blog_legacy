---
title: "Django y Bower"
date: "2016-01-29T06:42:23+00:00"
description: ""
tags: "Django,Bower"
---
# Django y Bower

Este post está tomado de [aquí](https://django-bower.readthedocs.org/en/latest/installation.html)

Primero debemos tener instalado bower
```
npm install -g bower
```

Luego instalamos el wrapper de django para bower

```
pip install django-bower
```

Luego en nuestro archivo *settings.py* en INSTALLED_APPS añadimos 

```
djangobower
```

Luego debemos agregar el finder de bower a *settings.py*, por lo general no está definido, así que django tomará el valor por defecto, así que debemos definirlo y extenderlo del valor por defecto

```
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
]
```

Por último definimos el root donde bower almacenará las dependencias en el mismo *settings.py*


```
BOWER_COMPONENTS_ROOT = os.path.join(PROJECT_ROOT, 'components')
```

Con esto definido, podremos añadir aplicaciones por bower, que se instalarán de acuerdo a como las nombremos en la variable *BOWER_INSTALLED_APPS*
```
BOWER_INSTALLED_APPS = (
)
```

Por último, para sincronizar nuestras aplicaciones de bower usamos

```
./manage.py bower install
```

