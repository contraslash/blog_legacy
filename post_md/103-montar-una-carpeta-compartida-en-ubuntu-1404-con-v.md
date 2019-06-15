Title: Montar una carpeta compartida en Ubuntu 14.04 con Virtualbox
Date: 2016-09-04T22:44:13+00:00
Description: Montar Carpeta Compartida entre Host y Ubuntu Virtualbox
Tags: Virtualbox
---
# Montar una carpeta compartida en Ubuntu 14.04 con VirtualboxDespues de realizar la configuracion de la carpeta compartida en nuestro virtual box, ejecutamos este comando para montarla en nuestro sistema de ficheros

```
sudo mount  -o uid=$UID,gid=$(id -g) -t vboxsf  src ~/host
```

> Si existen problemas de instalación con el VBoxGuestAddition, considere instalar las siguientes dependencias
```
sudo apt-get install make gcc linux-headers-$(uname -r)
```
> También puede usar este paquete
```
sudo apt-get install virtualbox-guest-x11
```