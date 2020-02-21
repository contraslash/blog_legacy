---
title: "Precauciones con SSH"
date: "2017-05-03T21:38:40+00:00"
description: "Precauciones con SSH para realizar despliegue automático"
tags: "Continuous Integration,Automatic Deployment,ssh"
---
# Precauciones con SSH

SSH es un protocolo seguro para ejecutar comandos de manera remota, pero permitir el acceso remoto a nuestros servidores, específicamente a nuestros servidores de producción siempre es un altamente riesgoso.

Existen configuraciones que permiten que este riesgo se minimice, como definir que el usuario root no pueda autenticarse, o denegar todos los accesos con contraseña; herramientas como fail2ban nos dan un respiro mas con respecto a la seguridad, pero en ocaciones, estas medidas de seguridad no nos dan las libertades necesarias como para realizar procesos automáticos, específicamente el despliegue.

A continuación presento algunas notas de datos útiles a tener en cuenta cuando aprovisionamos nuestros servidores para que soporten despliegue automático

1. Fail2Ban siempre es tu amigo, jamás lo desinstales
1. Nunca permitas que el usuario root se autentique 
    ``` 
    PermitRootLogin prohibit-password
    ```
1. No permitas contraseñas vacías
    ```
    PermitEmptyPasswords no 
    ```
1. No permitas que ningún usuario se autentique con contraseña
    ```
    PasswordAuthentication no
    ```
1. Si necesitas por alguna razón que tu usuario para despliegue automático se autentique, utiliza un filtro match
    ```
    Match User <usuario>
            PasswordAuthentication yes
    ```
1. Nunca uses contraseñas sin caracteres especiales 
1. Haz que tus contraseñas siempre sean al menos de 8 caracteres de largo

### Enlaces útiles
- [https://coderwall.com/p/j5nk9w/access-ec2-linux-box-over-ssh-without-pem-file](https://coderwall.com/p/j5nk9w/access-ec2-linux-box-over-ssh-without-pem-file)
- [https://www.digitalocean.com/community/tutorials/how-to-edit-the-sudoers-file-on-ubuntu-and-centos](https://www.digitalocean.com/community/tutorials/how-to-edit-the-sudoers-file-on-ubuntu-and-centos)

> Los ejemplos de código deben escribirse en el archivo de configuración de ssh, que usualmente está en `/etc/ssh/sshd_config`

