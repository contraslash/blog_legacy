Title: Ver SQL de una Migración
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: Django
---
# Ver SQL de una Migración

Definitivamente el ORM de Django es una cosa maravillosa, pero cuando falla, es una mierda.

En muchas ocasiones las personas se ven obligadas a realizar los cambios a mano.

Es importante tener estos comandos en mente para solucionar problemas indeseados directamente con nuestro Motor de Base de Datos

```
./manage.py sqlmigration app_label migration_id
```
Este comando imprime en consola las sentencias sql de la respectiva migración

```
./manage.py migrate app_label --fake
```

Si la migración presenta fallas, la omite y continua con las demás migraciones

También recomiendan la opcion --fake-initial, pero queda a su juicio