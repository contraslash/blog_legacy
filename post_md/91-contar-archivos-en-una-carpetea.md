Title: Contar Archivos en una carpetea
Date: 2016-06-10T18:27:40+00:00
Description: 
Tags: Linux
---
# Contar Archivos en una carpeteaEste es un segmento de código que me ha parecido muy util.

Primero nos posicionamos en la carpeta donde queremos contar los archivos, luego

```
ls -l | grep -v ^l | wc -l
```