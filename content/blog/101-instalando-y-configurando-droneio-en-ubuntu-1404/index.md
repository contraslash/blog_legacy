---
title: "Instalando y Configurando Drone.io en Ubuntu 14.04"
date: "2016-09-03T03:38:05+00:00"
description: ""
tags: "Continuous Integration,Drone,CI"
---
# Instalando y Configurando Drone.io en Ubuntu 14.04

Este tutorial está basado en [este tutorial](http://readme.drone.io/setup/overview/)

Debemos instalar primero Docker, si no lo has hecho, revisa este [post](http://blog.contraslash.com/instalando-docker-en-ubuntu-1404/)

Seguido usamos docker para obtener la última imagen de drone
```
sudo docker pull drone/drone
```

Creamos un archivo de configuración para drone
```
mkdir -p /etc/drone
cd /etc/drone
```

Creamos un archivo *dronerc* y comenzaremos con la configuración.

Para este tutorial usaremos Gogs y MySQL.

Para instalar gogs, revisa [este tutorial](http://blog.contraslash.com/instalando-gogs-en-ubuntu-1404-con-apache/)

Ejecuta el siguiente SQL en tu servidor de Base de Datos

```
create database drone;
create user drone_user identified by 'Ultr4$#cUr!Pa$$'
grant all privileges on drone.* to drone_user;
flush privileges;
```

```
REMOTE_DRIVER=gogs
REMOTE_CONFIG=https://gogs.example.com?open=false

DATABASE_DRIVER=mysql
DATABASE_CONFIG=drone_user:Ultr4$#cUr!Pa$$@tcp(localhost:3306)/drone?parseTime=true
```

por último ejecutamos el siguiente comando

```
sudo docker run \
    --volume /var/lib/drone:/var/lib/drone \
    --volume /var/run/docker.sock:/var/run/docker.sock \
    --env-file /etc/drone/dronerc \
    --restart=always \
    --publish=80:8000 \
    --detach=true \
    --name=drone \
    drone/drone:0.4
```

