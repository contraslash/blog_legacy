Title: pythonPojoGenerator.py
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: Python,Buenas Prácticas
---
# pythonPojoGenerator.py

A pesar que no esté bien dicho hablar de un POJO en python, el concepto de encapsulamiento a mi concepto siempre debe estar presente de la manera que se presenta en esta figura cortesía de Java.

Y como mi IDE no me genera mis getters y setters, hice mi propio script, usando python, obviamente.

Basta pasarle el nombre de los parámetros que queremos,

Luego un Copy&Paste y ét voilá

```
#!/usr/bin/python
import sys

parameters = sys.argv[1:]

def generateConstructor(parameters):
    constructor = "def __init__(self, "
    for parameter in parameters:
        constructor += parameter+","
    constructor = constructor[:-1]+"):\n"
    for parameter in parameters:
        constructor += "\tself._" + parameter + " = " + parameter + "\n"
    return constructor

def generateProperty(property):
    getter = "@property\n"
    getter += "def " + property + "(self):\n"
    getter += "\treturn self._" + property + "\n"

    setter = "@" + property + ".setter\n"
    setter += "def " + property + "(self, value):\n"
    setter += "\tself._" + property + " = value" + "\n"

    deleter = "@" + property + ".deleter\n"
    deleter += "def " + property + "(self):\n"
    deleter += "\tdel self._" + property + "\n"

    return getter + "\n" + setter + "\n" + deleter + "\n"

print generateConstructor(parameters)
for parameter in parameters:
    print generateProperty(parameter) + "\n"
```