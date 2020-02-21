---
title: "Select Multiple al estilo del Admin de Django"
date: "2017-01-04T02:28:44+00:00"
description: "Usando widget del administrador de Django FilteredSelectMultiple en una vista personalizada."
tags: "Django"
---
# Select Multiple al estilo del Admin de Django

Debo admitir que siempre me pareció muy elegante la propuesta de Django en el administrador de usuarios por defecto, donde los permisos se añaden de un panel a otro, como en esta imagen:
![Administrador de Django, Manejo de Permisos en vista de usuarios por defecto](https://i.stack.imgur.com/ybe24.png)

En un proyecto se me ocurrió utilizar algo similar, pero para mi desgracia, no encontré lo que buscaba, así que decidí usar el que viene en el administrador de Django, y no fue para nada complicado, a continuación una corta abstracción de los pasos necesarios.

*forms.py*
```
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

....


class MiFormulario(forms.Form):
    mi_campo = forms.ModelMultipleChoiceField(
        queryset=MiModelo.objects.all(),
        widget=FilteredSelectMultiple(
            "Nombre del campo",
            is_stacked=False,
        ),
    )
```

Aquí lo único distinto es que usamos el Widget FilteredSelectMultiple que está en los widgets del admin.

*views.py*
```
from django.views.generic import FormView
from . import forms

...

class MiVistaDelFormulario(FormView):
    template_name = "my_app/form_view.html"
    form_class = forms.MiFormulario
    success_url = "/"
```

Esta es una vista basada en clases común y corriente.

*my_app/form_view.html*
```
{% extends 'base.html' %}
{% load staticfiles %}
{% block specific-css %}
    <link rel="stylesheet" href="{% static 'admin/css/widgets.css' %}"/>
    <script type="application/javascript" src="{% static 'admin/js/core.js' %}"></script>
{% endblock %}
{% block content %}
    ....
        <form method="post">
            {% csrf_token %}
            {% for input in form %}
                {{ input }}
            {% endfor %}
                <input type="submit" value="Enviar">
            </div>
        </form>
    ....
{% endblock %}
{% block static-js %}
    <script type="application/javascript" src="/admin/jsi18n"></script>
<script type="application/javascript">
        var django = django || {};
        django.jQuery = jQuery;
    </script>
    <script type="application/javascript" src="{% static 'admin/js/SelectBox.js' %}"></script>
    <script type="application/javascript" src="{% static 'admin/js/SelectFilter2.js' %}"></script>

{% endblock %}
```

> ## ATENCIÓN
  El segundo script que define la variable django.jQuery es una adaptación del archivo que encontramos en `{% static 'admin/js/jquery.init.js' %}` que realiza la misma labor pero usando `jQuery.noConflict` que quita las referencias de $ hacia jQuery, si alguna otra librería usa esta `$` como acceso directo y no es jQuery recomiendo usar el archivo `{% static 'admin/js/jquery.init.js' %}`, de lo contrario usar esta adaptación

Esta es una abstracción de mi plantilla, suelo usar un esquema de herencia simple, donde mi plantilla base tiene 5 bloques:

- static-css
- specific-css
- content
- static-css
- specific-css

Lo que hacemos es cargar las librerías del administrador de django para que se carguen los estilos y el javascript.

Hay algo interesante en la primera línea del static-js, donde se carga la librería de internacionalización, que debemos añadir en nuestro archivo de urls principa
*urls.py*
```
....
urlpatterns = [
    ....
    url(r'^admin/jsi18n/$', 'django.views.i18n.javascript_catalog'),
    ....
]
```

