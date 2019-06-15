Title: Instalando Freeling 4.0 en Ubuntu 16
Date: 2017-09-13T12:44:28+00:00
Description: Instalando Freeling 4.0, una librería para Procesamiento de Lenguaje Natural, en Ubuntu 16.04
Tags: PLN,Ubuntu,Freeling
---
# Instalando Freeling 4.0 en Ubuntu 16Hace tiempo escribí un post sobre [cómo instalar Freeling 4.0 en OSX](http://blog.contraslash.com/instalando-freeling-40-en-osx/) y es tiempo ya de pasar los cambios a producción.

Posiblemente en un futuro cercano cree una receta ansible para facilitar el trabajo, pero primero como me manda la praxis, prefiero hacerlo a mano.

Necesitamos algunas dependencias

```
sudo apt install libboost-regex1.58.0 libicu-dev libboost-system1.58.0 libboost-thread1.58.0 libboost-program-options1.58.0 libboost-filesystem1.58.0 
```

Luego podremos descargar e instalar freeling

```
wget https://github.com/TALP-UPC/FreeLing/releases/download/4.0/freeling-4.0-xenial-amd64.deb
sudo dpkg -i freeling-4.0-xenial-amd64.deb 
```

Y ya está. 

No instalo desde código fuente esencialmente porque para compilar los binarios se necesitan las versiones de desarrollo de libboost, que son pesadas, y el proceso toma bastante tiempo y al final ocupa bastante espacio.