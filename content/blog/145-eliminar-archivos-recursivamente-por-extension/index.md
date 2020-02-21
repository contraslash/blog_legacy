---
title: "Eliminar Archivos Recursivamente por extensión"
date: "2017-01-27T14:45:28+00:00"
description: "Eliminar Archivos Recursivamente por extensión usando el comando find y find . -name *.pyc -type f -delete donde .pyc será la extensión de los archivos que queremos borrar"
tags: "Linux"
---
# Eliminar Archivos Recursivamente por extensión

Para eliminar archivos recursivamente por extensión podemos usar el comando find

```bash
find . -name "*.pyc" -type f -delete
```

donde .pyc será la extensión de los archivos que queremos borrar

