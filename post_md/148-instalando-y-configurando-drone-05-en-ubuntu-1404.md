Title: Instalando y Configurando Drone 0.5 en Ubuntu 14.04 
Date: 2017-02-07T22:15:47+00:00
Description: Instalando y configurando Drone.io, un servidor de integración continua, con Gogs.io, un servidor de git, Docker, Apache como proxy inverso en Ubuntu 14.04
Tags: Apache,Docker,Continuous Integration,Drone,CI
---
# Instalando y Configurando Drone 0.5 en Ubuntu 14.04 Hace tiempo cree la versión 1 de este tutorial, pero con el lanzamiento de drone 0.5, muchas cosas cambiaron, así que tomaré lo relevante de ese post con las nuevas configuraciones necesarias.

Usaremos para este tutorial [Gogs](http://gogs.io) un servidor de git muy liviano y escrito en Go y MySQL.

Debemos instalar primero Docker, si no lo has hecho, revisa este [post](http://blog.contraslash.com/instalando-docker-en-ubuntu-1404/)

Para instalar gogs, revisa [este tutorial](http://blog.contraslash.com/instalando-gogs-en-ubuntu-1404-con-apache/)

Ejecuta el siguiente SQL en tu servidor de Base de Datos

```
create database drone;
create user drone_user identified by 'Ultr4$#cUr!Pa$$'
grant all privileges on drone.* to drone_user;
flush privileges;
```

Seguido usamos docker para obtener la última imagen de drone

```
sudo docker pull drone/drone:latest
```

Creamos un archivo de configuración para drone
```
mkdir -p /etc/drone
cd /etc/drone
```

### Servidor Drone
Se encargará de servir la interfaz web y conectarse con los servidores git.

Creamos un archivo *dronerc* y escribimos lo siguiente con la configuración.

```
DATABASE_DRIVER=mysql
DATABASE_CONFIG=drone_user:Ultr4$#cUr!Pa$$@tcp(localhost:3306)/drone?parseTime=true

DRONE_OPEN=true
DRONE_SECRET=Rgwcg#632155DF3fswr
DRONE_GOGS=true
DRONE_GOGS_URL=http://gogs.example.com
```

> Recuerda colocar la URL apropiada de tu servidor Gogs

por último ejecutamos el siguiente comando

```
sudo docker run \
	--volume /var/lib/drone:/var/lib/drone \
	--volume /var/run/docker.sock:/var/run/docker.sock \
	--env-file /etc/drone/dronerc \
	--restart=always \
	--publish=3001:8000 \
	--detach=true \
	--name=drone \
	drone/drone:latest
```

### Agente Drone
Se encargará de la construcción de instancias para pruebas y ejecución de flujos de trabajo

Creamos un archivo *droneagentrc* y escribimos lo siguiente con la configuración.

```
DRONE_SERVER=ws://ci.contraslash.com/ws/broker
DRONE_SECRET=Rgwcg#632155DF3fswr
```

> Recuerda que `DRONE_SECRET` de *droneagentrc*  debe concordar con el `DRONE_SECRET` de *dronerc* .

Ejecutamos la instancia de docker para el agente

```
docker run -d \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --env-file /etc/drone/droneagentrc \
  --restart=always \
  --name=drone-agent \
  drone/drone:0.5 agent
```

### Configuración de apache como proxy inverso
Por último usaremos apache como proxy inverso para nuestra aplicación, para ello crearemos un archivo de virtual host en */etc/apache2/sites-available* llamado *drone.example.com.conf* con la siguiente información

```
<VirtualHost *:80>
        ServerName ci.contraslash.com
	ServerAdmin ma0@contraslash.com
        #git lab passthrough
        ProxyPass         /ws/ ws://localhost:3001/ws/
	ProxyPassReverse /ws/ ws://localhost:3001/ws/
        ProxyPass         / http://localhost:3001/
        ProxyPassReverse  / http://localhost:3001/
</VirtualHost>
```

Ahora necesitaremos habilitar los siguientes módulos de apache

```
a2enmod proxy
a2enmod proxy_wstunnel
```

Habilitamos el sitio y reiniciamos apache
```
a2ensite drone.example.com
service apache2 restart
```

Después de esto serías capaz de ingresar con las credenciales de gogs en drone. 

Recuerda que necesitas en tu repositorio un archivo *.drone.yml*.

Un excelente ejemplo de esto con django se puede encontrar en [este post](https://codeandoando.com/integrar-django-con-droneio/)