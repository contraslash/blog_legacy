Title: Usando BrowserSync en un proyecto Django
Date: 2017-08-09T16:03:19+00:00
Description: Sincronización automática de código con navegador usando Browser Sync
Tags: Django
---
# Usando BrowserSync en un proyecto Django> POST INCOMPLETO

[Revisar este vínculo](https://www.metaltoad.com/blog/instant-reload-django-npm-and-browsersync)

Ejecutar algo parecido 

```
 browser-sync --files applications/core/templates/base.html --proxy 127.0.0.1:8000 --reload-delay=500  start
```

En files se pueden especificar rutas

```
--files \"myapp/static/css/*.css, myapp/**/*.py, myapp/templates/*.html\"
```