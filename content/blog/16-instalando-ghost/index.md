---
title: "Instalando Ghost"
date: "2016-01-29T06:42:23+00:00"
description: ""
tags: "Web Apps"
---
# Instalando Ghost

Navegando por ahí me encontré con Ghost un fork de Wordpress y me decidí a probarlo, pero vaya que estaba en nodeJS y como a veces es fastidioso montar servicios en node, django, rails u otros, me decidí hacer esta pequeña guía.

Primero necesitamos habilitar un módulo de apache llamado mod_proxy, y adivinen que hace!

por defecto en la configuración de apache2 no viene, asi que instalamos

`sudo apt-get install libapache2-mod-proxy-html libxml2-dev`

Ahora necesitamos habilitar nuestros módulos

`sudo a2enmod proxy
sudo a2enmod proxy_http`

Existen otros módulos junto con el proxy, pero de momento no los necesito

reiniciamos apache

`sudo service apache2 restart`

y ya podemos enmascarar nuestro sitio que escucha en otro sitio

Creamos un virtualhost para nuestro ghost site, para quienes no están familiarizados con el asunto, diré a grosso modo que es la manera de darle el host a varios sitios dentro de un mismo servidor

hacemos un bootstrap del archivo base

`sudo cp /etc/apache2/sites-aviable/000-default.conf /etc/apache2/sites-aviable/ghost.misitio.com.conf`

ahora abrimos nuestro archivo de configuración recién creado

`nano /etc/apache2/sites/aviable/ghost.misitio.com.conf`

y agregamos algo como esto

`<VirtualHost mi.ip.publica:80>
ServerName ghost.misio.com `
`ProxyPreserveHost on
ProxyPass / http://localhost:2368/`
`</VirtualHost>`

y ahora habilitamos el sitio

`sudo a2ensite ghost.misitio.com`

y recargamos apache

`sudo service apache2 reload`

Y et voila, un ghost listo para ser usado

