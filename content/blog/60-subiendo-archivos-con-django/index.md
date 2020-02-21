---
title: "Subiendo archivos con Django"
date: "2016-01-29T06:42:23+00:00"
description: "Cómo subir archivos de imágenes en Django e instalar Pillow en Ubuntu"
tags: "Django,pil,pillow"
---
# Subiendo archivos con Django

######En nuestro archivo de URLs
```
from django.views.static import serve as serve_static_files
from . import settings
urlpatterns += url(
    r'^media/(?P<path>.*)$', 
    serve_static_files,
    {
        'document_root': settings.MEDIA_ROOT
    }
)
```

######En nuestro archivo de settings
```
MEDIA_ROOT = os.path.join(BASE_DIR,  'media')

MEDIA_URL = '/media/'
```

Si queremos trabajar con ImageFields y Pillow

Antes de instalar pillow necesitamos

```
sudo apt-get install libjpeg-dev lib64z1-dev libtiff-dev libfreetype6-dev liblcms2-dev libwebp-dev tk-dev openjpeg-tools
```

Estos son los requermientos presentados en la página oficial de Pillow que se pueden consultar [aquí](http://pillow.readthedocs.org/en/3.0.x/installation.html#external-libraries).

Yo estoy usando Trusty 64 y funciona de maravilla

Para Xenial recomiendo
```
sudo apt install libjpeg-dev libtiff5-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev openjpeg-tools
```

