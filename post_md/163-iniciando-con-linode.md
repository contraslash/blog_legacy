Title: Iniciando con Linode
Date: 2017-03-31T19:21:51+00:00
Description: Provisionando un Docker Swarn en Linode
Tags: Docker,Linode,Swarm
---
# Iniciando con LinodeCuando finalmente tomé la decisión de cambiarme de lleno a la arquitectura contenedores, decidí echarle un vistazo a mi infraestructura. Hasta el momento he sido un fiel cliente de Digital Ocean, pero tras un percance épico con uno de mis servidores favoritos que lo dejó totalmente inutilizado para usar Docker, decidí considerar otras opciones.

Este es el estado de cambio utilizando Linode.

¿Porqué Linode? 

Cuesta la mitad que Digital Ocean, lo digo hoy 31 de Marzo de 2017

Aprovisionando un nuevo Ubuntu 16:04

### Deshabilitar ip v6

Si, tuve que deshabilitarla para poder trabajar con mas tranquilidad

Pegar esto al final de `/etc/sysctl.conf`
```
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1 
net.ipv6.conf.lo.disable_ipv6 = 1 
```
y luego 
```
sudo sysctl -p
```

Para verificar 

```
cat /proc/sys/net/ipv6/conf/all/disable_ipv6 
```

Si la respuesta es 1 todo va bien

### Instalar docker

Asegurarse de no utilizar un kernel personalizado de linode.

Revisar [este post](https://www.linode.com/docs/tools-reference/custom-kernels-distros/run-a-distribution-supplied-kernel-with-kvm)

```
sudo apt-get install \
    linux-image-extra-$(uname -r) \
    linux-image-extra-virtual

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

sudo apt-get update

sudo apt-get install docker-ce
```

### Creando y configurando el Swarm

```
docker swarm init

docker network create --driver=overlay traefik-network
```
### Creando y configurando traefik
```
docker service create \
    --name traefik \
    --constraint=node.role==manager \
    --publish 80:80 --publish 8080:8080 \
    --mount type=bind,source=/var/run/docker.sock,target=/var/run/docker.sock \
    --network traefik-network \
    traefik \
    --docker \
    --docker.swarmmode \
    --docker.domain=example.com \
    --docker.watch \
    --web
```
### Probando un cliente de apache2
```
docker service create \
    --name apache2 \
    --label traefik.port=80 \
    --network traefik-network \
    httpd
```

> Para ayudar en la resolución de direcciones IPv4 es util habilitar el tcp_mtu_probing añadiendo la línea

```
net.ipv4.tcp_mtu_probing=1
```

a ` /etc/sysctl.con` y luego ejecutando el comando
```
sudo sysctl -p
```