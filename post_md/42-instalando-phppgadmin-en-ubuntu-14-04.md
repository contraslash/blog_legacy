Title: Instalando PHPPgAdmin en Ubuntu 14.04
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: Linux,Ubuntu,Digital Ocean
---
# Instalando PHPPgAdmin en Ubuntu 14.04Instalamos
`sudo apt-get install postgresql postgresql-contrib phppgadmin`

Luego editamos el archivo `/etc/apache2/conf.d/phppgadmin` y comentamos la linea que solo permite conectarse desde localhost y permitimos desde todos

```
order deny,allow
deny from all
# allow from 127.0.0.0/255.0.0.0 ::1/128
allow from all
```

Luego copiamos nuestro archivo de configuración a la carpeta de configuraciones de apache y reiniciamos el servicio

`sudo cp /etc/apache2/conf.d/phppgadmin /etc/apache2/conf-enabled/phppgadmin.conf`

`sudo service apache2 restart`

