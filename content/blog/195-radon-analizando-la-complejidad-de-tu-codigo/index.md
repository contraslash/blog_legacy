---
title: "Radon: Analizando la complejidad de tu código"
date: "2018-04-12T14:23:17+00:00"
description: "Análisis de complejidad estático de nuestro código en Python utilizando Radon"
tags: "Python"
---
# Radon: Analizando la complejidad de tu código

[Radon](http://radon.readthedocs.io/en/latest/index.html) es un analizador de código estático enfocado en extraer la complejidad estimada de tu código.

Radon se enfoca en dos áreas importantes:

1. Complejidad Ciclomática ([Cyclomatic Complexity](http://radon.readthedocs.io/en/latest/intro.html#cyclomatic-complexity))
  Nos da un puntaje que representa que tantas decisiones son tomadas dentro de cada segmento de código. 
1. Índice de Mantenibilidad ([Maintanibility Index](http://radon.readthedocs.io/en/latest/intro.html#maintainability-index))
  Determina que tan fácil de mantener es nuestro código

Para instalar radon

```shell
pip install radon
```

Para analizar el código:

```shell
radon cc .
radon mi .
```

Radon escala nuestro código, para CC de A - F donde F es una alta complejidad, para MI de A-C donde C es un código poco mantenible, así que para minimizar la salida y enfocarnos en bloques críticos podemos utilizar el filtro `--min`

