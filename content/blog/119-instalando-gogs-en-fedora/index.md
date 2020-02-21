---
title: "Instalando Gogs en Fedora"
date: "2016-10-12T17:47:55+00:00"
description: "Instalando Gogs con Apache en Fedora"
tags: "Apache,Gogs,Fedora"
---
# Instalando Gogs en Fedora

Realmente no es Fedora, es Amazon Linux AMI 2016.03, pero para efectos prácticos funcionan igual.

El tutorial original es [este](http://blog.contraslash.com/instalando-gogs-en-ubuntu-1404-con-apache/) y lo seguiré paso a paso pero traduciendo a lenguaje yum.

Primero necesitamos instalar las dependencias
```
sudo yum install -y git
sudo yum install -y mysql-server
sudo yum -y install httpd
sudo easy_install supervisor
```

Creamos el usuario de git
```
sudo useradd git
mkdir /home/git/
chown -R git /home/git
```

Las siguientes las operaciones las realizaremos como el usuario git
```
sudo -i -u git
```

Descargamos los binarios desde la [página oficial](https://gogs.io/docs/installation/install_from_binary)
```
wget https://dl.gogs.io/gogs_v0.9.97_linux_amd64.zip
unzip gogs_v0.9.97_linux_amd64.zip
```

Creamos una carpeta para almacenar los repositorios
```
mkdir gogs-repositories
```

Probamos que todo esté funcionando bien
```
gogs/gogs web
```

Pulsamos Cntrl+D para salir del usuario git, ahora configuraremos supervisor
```
sudo echo_supervisord_conf > /etc/supervisord.conf
```
> Si se tienen problemas cone este comando, por favor ejecute `echo_supervisord_conf` y copie la salida de este archivo a el archivo ` /etc/supervisord.conf` que puede ser abierto con el siguiente comando `sudo nano  /etc/supervisord.conf`

Ahora añada la configuración por defecto de gogs para supervisor
```
sudo cat /home/git/gogs/scripts/supervisor/gogs >> /etc/supervisor.conf
```

> Si vuelve a tener problemas con el comando anterior, abra el archivo con el comando `sudo nano  /etc/supervisord.conf` y pegue manualmente el contenido de `/home/git/gogs/scripts/supervisor/gogs`

y modifique las siguientes líneas 
```
directory=/home/git/gogs/
command=/home/git/gogs/gogs web
```

También asegurese que los archivos `stdout_logfile` y `stderr_logfile` existan

Ahora configuraremos el virtualhost de Apache
para eso ingresamos a /etc/httpd/conf/httpd.conf y agregamos las siguientes lineas

```
...
<VirtualHost *:80>
        ServerName gogs.example.com
        ProxyPass         / http://localhost:3000/
        ProxyPassReverse  / http://localhost:3000/
</VirtualHost>
```

y reiniciamos apache
```
sudo service httpd restart
```

