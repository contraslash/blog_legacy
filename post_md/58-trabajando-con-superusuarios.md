Title: Trabajando con superusuarios
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: Linux
---
# Trabajando con superusuariosEste post es uno de los requerimientos para una serie de guías que estaré subiendo para el despliegue y aprovisionamiento automático con Azure y Ansible

###Crear un usuario por consola
`sudo useradd nombreDeUsuario -m`

###Otorgarle permisos de superusuario a un usuario
`sudo adduser nombreDeUsuario sudo`

También puede servir
`sudo usermod -a -G sudo nombreDeUsuario`

###Quitar el requerimiento de contraseña cuando se ejecuta un comando con sudo
`echo "nombreDeUsuario ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers`