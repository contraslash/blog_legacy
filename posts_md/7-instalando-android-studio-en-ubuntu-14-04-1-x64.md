Title: Instalando android studio en ubuntu 14.04.1 x64
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: Android
---
# Instalando android studio en ubuntu 14.04.1 x64


necesité todos estos paquetes:

`sudo apt-get install openjdk-7-jdk lib32z1 lib32z1-dev lib32stdc++6 kvm lib32ncurses5 libc6-i386 lib32gcc1 libsdl1.2debian:i386`

errores como  
 sdl init failure reason is no available video device android

se solucionan con la librería: libsdl1.2debian:i386

kvm es necesaria para virtualizar los emuladores,

las libz para descomprimir algunos archivos mientras se compila, y las librerías de c de 32 bits


