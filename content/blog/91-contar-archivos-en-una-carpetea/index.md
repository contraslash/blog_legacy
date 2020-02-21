---
title: "Contar Archivos en una carpetea"
date: "2016-06-10T18:27:40+00:00"
description: ""
tags: "Linux"
---
# Contar Archivos en una carpetea

Este es un segmento de código que me ha parecido muy util.

Primero nos posicionamos en la carpeta donde queremos contar los archivos, luego

```
ls -l | grep -v ^l | wc -l
```

