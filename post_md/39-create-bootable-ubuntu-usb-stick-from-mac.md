Title: Creando una memoria booteable con Ubuntu desde mac
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: Ubuntu
---
# Creando una memoria booteable con Ubuntu desde macTomado de  [aquí](http://www.ubuntu.com/download/desktop/create-a-usb-stick-on-mac-osx) 

Primero debemos descargar un iso de ubuntu, puede hacerse desde  [aquí](http://www.ubuntu.com/download/desktop) o desde tu mirror favorito

Luego convertimos el .iso a un .img

` hdiutil convert -format UDRW -o ~/path/to/target.img ~/path/to/ubuntu.iso`

Luego debemos desmontar la memoria donde se va a instalar ubuntu

Usa `diskutil list` para ver la lista de dispotivos y `diskutil unmountDisk /dev/diskN` para desmontarlo

Luego usa dd para hacer una copia profunda del .img a la memoria

`sudo dd if=/path/to/ubuntu.iso.img of=/dev/rdiskN bs=1m` 
>PD: dd toma bastante tiempo, así que ve por un café o algo así

Recuerda que N es el número del disco donde vas a instalar ubuntu, no queremos  borrar el disco duro

Y eso es todo, ya puedes instalar ubuntu desde tu memoria