Title: Iterar sobre los atributos de un objeto en Django
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: Django
---
# Iterar sobre los atributos de un objeto en Django

Ya saben que para mí, Django está muy bien hecho, y para la muestra, un segmento de código que me estoy robando de [aquí](http://stackoverflow.com/questions/2217478/django-templates-loop-through-and-print-all-available-properties-of-an-object), donde un tipo para evitarse la fatiga de quemar todas los atributos de su objeto en el sistema de templates, se saca esta solución que va de Home Run

###### En la definición del modelo
```
def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in ModelName._meta.fields]
```

###### En el template
```
{% for name, value in manor_stats.get_fields %}
  {% if value %}
    {{ name }} => {{ value }}
  {% endif %}
{% endfor %}
```

Sencillamente monumental