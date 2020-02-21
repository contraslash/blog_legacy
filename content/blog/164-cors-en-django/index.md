---
title: "CORS en Django"
date: "2017-04-06T22:55:26+00:00"
description: "Habilitando CORS en aplicaciones que usan el Framework Web Django"
tags: "Django,CORS"
---
# CORS en Django

En algunos casos vemos la necesidad de habilitar nuestro servidor para que reciba información de otros servidores, utilizando CORS, cuyas sigas son:

- **C** ross
- **O** rigin
- **R** esource
- **S** haring

Para esto, se recomienda utilizar el paquete [django-cors-headers](https://github.com/ottoyiu/django-cors-headers), que se puede instalar con el siguiente comando

```
pip install django-cors-headers
```

Su configuración se realiza en nuestro archivo *settings.py*

```
INSTALLED_APPS = (
    ...
    'corsheaders',
    ...
)

MIDDLEWARE = [  # Or MIDDLEWARE_CLASSES on Django < 1.10
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]

CORS_ORIGIN_WHITELIST = (
    'google.com',
    'hostname.example.com',
    'localhost:8000',
    '127.0.0.1:9000'
)
```

Otras configuraciones las podemos encontrar en la [documentación oficial](https://github.com/ottoyiu/django-cors-headers/blob/master/README.rst)

