---
title: "Obtener Nombres y Valores de un modelo"
date: "2016-08-09T15:15:19+00:00"
description: ""
tags: "Django,Python"
---
# Obtener Nombres y Valores de un modelo

Para obtener los nombres de atributo de un modelo usamos el accesos _meta y el método __getattribute__

```
for i in xrange(len(objeto._meta.fields))
    atributo =  unicode(objeto._meta.fields[i].name)
    valor = objecto.__getattribute__(atributo)

```



