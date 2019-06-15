Title: Eliminando objetos responsablemente en Django
Date: 2016-05-12T15:43:44+00:00
Description: Eliminar objetos en Django junto con todos los objetos relacionado en cascada
Tags: Django
---
# Eliminando objetos responsablemente en Django

Una parte esencial de nuestro CRUD es la D de Delete. Django por defecto soluciona problemas eliminando dependencias en cascada, pero tal cual como se muestra en el administrador de Django, a veces es conveniente mostrarle a nuestro usuario el impacto que puede tener la eliminación de un registro.

Escarbando en el código fuente del administrador de django, y en [stackoverflow](http://stackoverflow.com/questions/12158714/how-to-show-related-items-using-deleteview-in-django) he encontrado un fragmento de código que puede ser muy útil para esta labor

```
objects_to_delete = my_model.objects.filter(my_attr=foo)

from django.contrib.admin.utils import NestedObjects
collector = NestedObjects(using='default')
collector.collect(objects_to_delete)

# Los objetos se almacenaran en el colector y se pueden acceder con el método
collector.nested()
```

La estructura puede parecer un poco densa a la vista, pero se renderizará en html muy bien, yay por el motor de templates.