Title: Instalando HTK
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: PLN
---
# Instalando HTK

Para instalar htk es necesario descargar la ultima versión de `http://htk.eng.cam.ac.uk/download.shtml`

Yo necesité instalar esto (estoy en 64bits)

```
sudo apt-get install libc6-dev-i386
sudo apt-get install libx11-dev:i386
make all
sudo make install
```