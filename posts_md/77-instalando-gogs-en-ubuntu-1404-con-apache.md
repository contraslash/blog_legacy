Title: Instalando Gogs en Ubuntu 14.04 con Apache 
Date: 2016-02-01T01:02:28+00:00
Description: Instalando Gogs en Ubuntu 14.04 con Apache
Tags: Apache,Ubuntu,Gogs
---
# Instalando Gogs en Ubuntu 14.04 con Apache 

Primero, como mandan las buenas practicas, creemos un usuario git
```
useradd git
mkdir /home/git/
chown -R git /home/git
```

Luego nos autenticamos con el usuario git
```
sudo -i -u git
```

Antes de instalar *Gogs* vamos a instalar algunos requerimientos

```
sudo apt-get install git mysql-server
```

Luego podremos instalar *Gogs*, que descargaremos desde la [página oficial](https://gogs.io/docs/installation/install_from_binary).

```
wget https://dl.gogs.io/gogs_v0.8.25_linux_amd64.zip
unzip gogs_v0.8.25_linux_amd64.zip
mkdir gogs-repositories
```

En este punto podemos ejecutar nuestro servidor con el comando y verificar la instalación de nuestro servidor

```
gogs/gogs web
```

Ahora, usaremos supervisor para manejar el proceso en segundo plano

```
sudo apt-get supervisor
```

Luego debemos configurar el archivo de configuración de supervisor. En principio basta con concatenar el archivo situado en gogs/scripts/supervisor/gogs a /etc/supervisor/supervisor.conf

```
sudo cat /home/git/gogs/scripts/supervisor/gogs >> /etc/supervisor/supervisor.conf
```

Ahora editaremos el archivo de configuración de supervisor para cambiar la ruta de acceso a gogs, cambiando las lineas 

```
directory=/home/git/gogs/
command=/home/git/gogs/gogs web
```

Lo siguiente será configurar apache para que enrute el dominio a nuestra aplicación

```
sudo apt-get install -y libapache2-mod-proxy-html libxml2-dev
sudo a2enmod proxy
sudo a2enmod proxy_http
sudo service apache2 reload
```

Luego configuraremos un virtualhost para nuestro servidor de git

```
sudo nano /etc/apache2/sites-aviable/mi-dominio.com.conf
```

y agregamos lo siguiente

```
<VirtualHost *:80>
        ServerName gogs.example.com
        ProxyPass         / http://localhost:3000/
        ProxyPassReverse  / http://localhost:3000/
</VirtualHost>
```

```
sudo a2ensite gogs.example.com.conf
sudo service apache2 restart
```

Y ya está