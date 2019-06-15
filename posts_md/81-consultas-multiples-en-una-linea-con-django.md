Title: Consultas Multiples en una línea con Django
Date: 2016-03-18T06:15:52+00:00
Description: 
Tags: Django
---
# Consultas Multiples en una línea con DjangoEl ORM de Django es una herramienta muy potente, pero a la hora de realizar operaciones SQL complejas, debemos recurrir al raw, o anidar algunos ciclos, que no es algo muy eficiente a final de cuentas, porque terminamos realizando un montón de consultas y sobrecargando nuestra aplicación.

No tengo nada en contra de ejecutar sentencias RAW, pero con regularidad, he usado algunas herramientas de python para pulir mis consultas. 

Un ejemplo:

```
import operator
from django.db.models.query_utils import Q

def consulta_compleja(criterios):
    return Modelo.objects.filter(reduce(operator.or_, [Q(filtro=criterio) for criterio in criterios]))
```