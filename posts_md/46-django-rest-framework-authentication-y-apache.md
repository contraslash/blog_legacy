Title: Django Rest Framework Authentication y Apache
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: Apache,Django,REST Framework
---
# Django Rest Framework Authentication y Apache

En muchas ocasiones entiendo porque muchos desarrolladores prefieren un hosting compartido que haga el trabajo sucio (en la mayoría de ocasiones mal hecho) por ellos, y pequeños detalles como el que les mencionaré es uno de ellos.

Érase una vez un joven que estaba migrando su proyecto de Desarrollo a Producción, ese proyecto usaba REST Framework y su módulo de autenticación por tokens, pero olvidó poner en su VirtualHost la siguiente línea

`WSGIPassAuthorization On`

Ello hizo que perdiera 40 minutos preguntándose porque siempre le aparecía el error de falta de autenticación.

