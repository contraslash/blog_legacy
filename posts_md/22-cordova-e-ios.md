Title: Cordova e iOS
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: iOS
---
# Cordova e iOSDefinitivamente a ratos Apache Cordova es un real fastidio, mas aún si se trata de un proyecto para iOS, bueno, de por sí programar para iOS es un fastidio.

Bueno, en primera instancia, para que se compile bien los plugins hay que o realizar un cordova prepare después de cada cambio o buscar un archivo llamado copy-www-build-step.sh que regularmente en CarpetadelProyecto/platform/cordova/lib.

Ahí basta con copiar los archivos de nuestra carpeta www y la carpeta del www en el proyecto así que queda algo como

```
cp -fR ../../www/ www/ 
SRC_DIR="www/"
...
````

Y en principio eso soluciona mucísimos problemas
