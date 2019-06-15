Title: Creando un Context Processor para tener la url del sitio
Date: 2016-09-15T03:49:28+00:00
Description: Añadir un procesador de contexto que muestre la url actual del sitio
Tags: Django
---
# Creando un Context Processor para tener la url del sitioTomado de [aquí](http://stackoverflow.com/questions/1451138/how-can-i-get-the-domain-name-of-my-site-within-a-django-template)

```
from django.contrib.sites.shortcuts import get_current_site
from django.utils.functional import SimpleLazyObject

def site(request):
    site = SimpleLazyObject(lambda: get_current_site(request))
    protocol = 'https' if request.is_secure() else 'http'

    return {
        'site': site,
        'site_root': SimpleLazyObject(lambda: "{0}://{1}".format(protocol, site.domain)),
        'full_url': SimpleLazyObject(lambda: "{0}://{1}{2}".format(protocol, site.domain, request.path)),
    }
```

y claro, no olvidar añadir a *miproyecto/settings.py*

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
            ...
            'ruta.al.context_processors. site'
            ...
            ],
```  