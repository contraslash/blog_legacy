Title: Probando Arch
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: Linux
---
# Probando Arch
Bueno, no podía graduarme de ingeniero en sistemas sin haber probado arch

Dicen que es odioso, y si, pero dejaré esto por aquí para mi mismo

Después de instalar el SO recordar

si tengo otro sistema operativo, definir la mascara para la entrada de grub en /etc/grub.d/40_custom

de la manera
```
menuentry “Etiqueta de SO”{  
 set root=”(hd0,1)”  
 chainloader+1  
 }
```

donde hd0 es el discuduro fisico y el otro numero la particion logica

Para la configuracion de red, recomiendo tener al equipo conectado por LAN y para inicializar la red usar

`dhcpcd`

luego instalar

`wifi-menu`

`pacman -Syyu actualiza el sources.list`

Si voy a correr interfaz grafica, no olvidar montar xorg con

`pacman -S xorg xorg-xinit xorg-xauth`

luego ya puedo montar escritorios

#Montando enligthenment

`pacman -S enlightenment`

luego, basta con agregar al ~/.xinitrc exec enligthment_start

para matar x 

`xkill -15 x`


