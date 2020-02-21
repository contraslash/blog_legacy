---
title: "Instalando joomscan en Ubuntu 14.04"
date: "2016-01-29T06:42:23+00:00"
description: ""
tags: "Seguridad"
---
# Instalando joomscan en Ubuntu 14.04

Primero son necesarias algunas librerías de perl

`sudo apt-get install libwww-perl libwww-mechanize-perl libswitch-perl`

Luego basta con descargar descomprimir y disfrutar

Aquí está el [link](http://sourceforge.net/projects/joomscan/)

Para realizar un escaneo, debe usarse un comando como este
`perl joomscan.pl -u http://joomla.site.domain`

Basado en [este](http://samiux.blogspot.com/2013/05/howto-joomscan-on-ubuntu-desktop-1204.html) post

