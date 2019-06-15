Title: Usando Sphinx para documentar con docString en Django
Date: 2016-05-24T20:35:28+00:00
Description: 
Tags: Django
---
# Usando Sphinx para documentar con docString en DjangoPara usuarios que venimos de Java, la documentación automática de código fuente es una herramienta importante para el mantenimiento de nuestros proyectos.

El DocString es una herramienta de python para mantener el código entendible a los desarrolladores, y existen herramientas para proporcionar documentación por este medio.

[Sphinx](http://www.sphinx-doc.org/en/stable/) es una poderosa herramienta para documentar documentación en Python, y podemos usarla para documentar nuestro proyecto en django.

Primero debemos instalar sphinx

```
pip install Sphinx
```

Luego, podemos ejecutar el comando de configuración automática de sphinx

```
sphinx-quickstart
```
 Que nos llevará por una serie de pasos importantes, que podremos llenar con información de nuestro proyecto, pero quisiera darle importante a la activación de los módulos.

```
Please indicate if you want to use one of the following Sphinx extensions:
> autodoc: automatically insert docstrings from modules (y/n) [n]: y
> doctest: automatically test code snippets in doctest blocks (y/n) [n]: y
> intersphinx: link between Sphinx documentation of different projects (y/n) [n]: y
> todo: write "todo" entries that can be shown or hidden on build (y/n) [n]: y
> coverage: checks for documentation coverage (y/n) [n]: y
> imgmath: include math, rendered as PNG or SVG images (y/n) [n]: n
> mathjax: include math, rendered in the browser by MathJax (y/n) [n]: n
> ifconfig: conditional inclusion of content based on config values (y/n) [n]: n
> viewcode: include links to the source code of documented Python objects (y/n) [n]: y
> githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]: n
```

Al terminar el asistente, podremos ejecutar el siguiente comando

```
make html
```

Existen distintas opciones, pero quiero enfocarme en la generación del HTML.

Luego de esto, se crearán una serie de archivos, en la ubicación que definimos como `Root Path`, ahí encontraremos las siguientes carpetas
- build
- static
- templates

Con el prefijo que nosotros hayamos definido.

En root_path/prefijo_build encontraremos un archivo llamado `conf.py`, el cual debemos ajustar para que encuentre los módulos en python.

Para esto debemos añadir las siguientes líneas

```
sys.path.insert(0, os.path.abspath('ruta_proyecto'))
from django.conf import settings
settings.configure()
```

donde `ruta_proyecto` es la ubicación de nuestro proyecto.

Es importante definir estas líneas antes de que se defina la variable `extensions`, que debe parecerse a esta:

```
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
]
```

Con el archivo de configuración listo vamos a crear un archivo por cada archivo donde queremos que se genere la documentación automática en una nueva carpeta que crearemos llamada modules.

Con esto tendremos una estructura de archivos similar a esto
```
documentacion/
    prefijo_build/
    prefijo_static/
    prefijo_templates/
    modules/
        app1/
             forms.py
            models.py
            views.py
        app2/
             forms.py
            models.py
            views.py
        .....
    conf.py
    index.rst
```

En cada archivo vamos a escribir el siguiente contenido

*modules/app1/forms.py*
```
Formularios de app 1
=================

.. automodule:: app1.forms
    :members:
```

Donde la primera línea es el título del módulo y en la cuarta lína está la ubicación del archivo con el código fuente.

Por último en *documentacion/index.rst* vamos a añadir las rutas de los archivos que acabamos de crear
```
.....
Contents:

.. toctree::
   :maxdepth: 2

   modules/app1/forms
   modules/app1/models
   modules/app1/views

.....
```

Por último re ejecutaremos el comando de generación de documentación

```
make html
```

Y la documentación se creará.

> Este post está basado en [este post](http://www.marinamele.com/2014/03/document-your-django-projects.html)