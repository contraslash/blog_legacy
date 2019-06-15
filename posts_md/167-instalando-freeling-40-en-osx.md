Title: Instalando Freeling 4.0 en OSX
Date: 2017-05-16T23:24:32+00:00
Description: Instalación de Freeling en OSX
Tags: Procesamiento de Lenguaje Natural,Freeling
---
# Instalando Freeling 4.0 en OSX

Encuentre la documentación oficial de instalación [aquí](https://talp-upc.gitbooks.io/freeling-user-manual/content/installation.html)

Primero necesitaremos descargar el último release de Freeling, que puede encontrarse en el repositorio [oficial de github](https://github.com/TALP-UPC/FreeLing/releases/tag/4.0).

De este enlace podremos descargar el [archivo zip](https://github.com/TALP-UPC/FreeLing/releases/download/4.0/FreeLing-4.0.zip)

Antes de instalar Freeling, necesitaremos algunos servicios que podemos instalar con [brew](https://brew.sh)
```
brew install autoconf automake libtool pkgconfig
brew install icu4c
# Esto puede tardar varios minutos
brew install -v boost --with-icu4c
```

Una vez descomprimamos el archivo, necesitaremos ejecutar el comando 

```
./autogen.sh 
```

Esto puede tardar varios minutos.

Luego podremos instalar

```
sudo make install
```

Después de esto podremos probar los comandos de freeling

```
analyze -f es.cfg < ejemplo.txt > salida.txt
```

Asegúrate que ejemplo.txt exista y tenga texto en español. La salida quedará en `salida.txt`