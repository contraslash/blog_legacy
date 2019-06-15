Title: Eliminar Archivos Recursivamente por extensión
Date: 2017-01-27T14:45:28+00:00
Description: Eliminar Archivos Recursivamente por extensión usando el comando find y find . -name "*.pyc" -type f -delete donde .pyc será la extensión de los archivos que queremos borrar
Tags: Linux
---
# Eliminar Archivos Recursivamente por extensión

Para eliminar archivos recursivamente por extensión podemos usar el comando find

```
find . -name "*.pyc" -type f -delete
```

donde .pyc será la extensión de los archivos que queremos borrar