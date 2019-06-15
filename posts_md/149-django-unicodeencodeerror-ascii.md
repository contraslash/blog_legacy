Title: Django UnicodeEncodeError ‘ascii’ 
Date: 2017-02-17T23:10:54+00:00
Description: Solucion del problema UnicodeEncodeError ‘ascii’ codec can’t encode characters in position ordinal not in range(128) de Django Python cuando se sirve la aplicación con Apache2
Tags: Apache,Django,Ubuntu
---
# Django UnicodeEncodeError ‘ascii’ Para todos aquellos que alguna vez hemos desarrollado en Django con Python 2.7, esto es un problema gigante, pero definitivamente solucionable.

Comparto con ustedes [este post](http://itekblog.com/ascii-codec-cant-encode-characters-in-position/) que solucionó mi problemática de una manera simple.

En mi caso el problema era con la configuración del lenguaje de Apache, para lo cual ruve que agregar este par de lineas en el archivo  */etc/apache2/envvars*

```
export LANG='en_US.UTF-8'
export LC_ALL='en_US.UTF-8'
```