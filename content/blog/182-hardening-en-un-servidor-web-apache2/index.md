---
title: "Hardening en un servidor web Apache2"
date: "2017-09-11T17:11:53+00:00"
description: "5 consejos básicos para mantener tu servidor web apache mas lejos de los atacantes"
tags: "Apache,Security"
---
# Hardening en un servidor web Apache2

Otra de las deudas técnicas que tenía con este blog era la de algunos tips útiles para realizar un Hardening a un servidor Apache2. A continuación relaciono algunas de las cosas mas importantes:

1. Desactivar las banderas de versión:
  Cuando mostramos la versión de nuestro navegador estamos facilitando la vida del atacante, pues ya restringe el dominio de vulnerabilidades que tendrá que explorar para buscar un vector de ataque.
  Añadir esto al final de nuestro archivo de configuración de apache, en ubuntu en `/etc/apache2/httpd.conf`
  ```
ServerTokens Prod
ServerSignature Off 
  ```

1. Desactivar el indexado de archivos:
  Apache por defecto permite explorar archivos por medio de un navegador, lo cual puede revelar información confidencial de nuestros usuarios o nuestro sistema, por eso es bueno desactivar el indexado:
  Añadir esto en el segmento de nuestro virtualhost
  ```
<Directory /ruta/al/directorio/raiz/de/apache>    
Options -Indexes    
AllowOverride None    
Order deny,allow    
Deny from all    
</Directory>
  ```
1. Quitar los permisos de ejecución a terceros en carpetas donde se pueda subir información:
  Una explicación mas detallada de esto se puede encontrar en [este post](http://blog.contraslash.com/problemas-subiendo-archivos-en-produccion-en-djang/)
  ```
sudo groupadd varwwwusers  
sudo adduser www-data varwwwusers  
sudo chgrp -R varwwwusers /var/www/html  
sudo chmod -R 770 /var/www/html  
  ```
1. Deshabilitar métodos inseguros:
  Aunque a veces nos limitamos al `GET` y al `POST`, `HTTP` tiene otro montón de métodos que pueden ser usados en nuestra contra, para el robo de credenciales por medio de cookies se suele usar el método `TRACE` que esencialmente hace un eco de la petición entrante, permitiendo a un tercero interceptar las cookies entrantes
  Para deshabilitarlo, basta añadir esta línea al archivo de configuración
  ```
TraceEnable off
  ```
  Se pueden Restringir todos los métodos a excepción de los nombrados usando la etiqueta LimitExcept, pero lo dejo a decisión de cada desarrollador
  ```
<LimitExcept GET POST HEAD>
deny from all
</LimitExcept>
  ```
1. Mantenerse actualizado:
  Siempre es importante mantener la versión de nuestras aplicaciones lo mas actualizadas posibles, usualmente los proveedores parchan los bugs y vulnerabilidades en los nuevos lanzamientos de versiones.

Si quieres una guía adicional, te recomiendo [este artículo](https://geekflare.com/apache-web-server-hardening-security/)

