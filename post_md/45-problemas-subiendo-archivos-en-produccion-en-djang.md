Title: Problemas subiendo archivos en producción con Django y Apache en Ubuntu
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: Apache,Django,Ubuntu
---
# Problemas subiendo archivos en producción con Django y Apache en UbuntuEl tema de la subida de archivos a nuestro servidor siempre es un tema delicado, y molesto en muchas ocasiones por el asunto de los permisos.

Una solución del tipo 

`chmod -R 777 /var/www/html`

es algo que no debe pasarnos por la cabeza

un 

`chown -R www-data:www-data /var/www/html`

No es tan mala, pero nos mete en serios problemas si secuestran el usuario de apache.

Una solución razonable, la encontré en este [post](http://stackoverflow.com/questions/21797372/django-errno-13-permission-denied-var-www-media-animals-user-uploads) de StackOverflow

Es bastante límpia, creamos un grupo nuevo, añadimos www-data al grupo, definimos el grupo de /var/www/html al nuevo grupo y luego al sistema de carpetas le damos permisos de tipo 770, que termina hacienod un poco mas seguro nuestro sistema

```
sudo groupadd varwwwusers
sudo adduser www-data varwwwusers
sudo chgrp -R varwwwusers /var/www/html
sudo chmod -R 770 /var/www/html
```