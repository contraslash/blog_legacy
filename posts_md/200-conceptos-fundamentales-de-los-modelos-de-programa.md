Title: Conceptos fundamentales de los modelos de programación
Date: 2018-06-08T16:32:48+00:00
Description: Conceptos fundamentales de los modelos de programación
Tags: Modelos y Paradigmas de Programación
---
# Conceptos fundamentales de los modelos de programaciónLa programación abarca tres elementos:
- Modelo de computación: sistema formal que define un lenguaje y como se ejecutan las instrucciones en una *máquina abstracta*
- Modelo de programación:  Concepto de técnicas de programación y diseños utilizados para escribir programas en el lenguaje del modelo de computación
- Técnicas de razonamiento: corrección y eficiencia.

## Sintaxis
Conjunto de reglas que define cuando un programa está bien escrito o no

Esta definición se describe por medio de una gramática, que define unos elementos terminales y no terminales. Los terminales se conocen como *lexemas* y los no terminales representan una secuencia de *lexemas*.

## Semántica
Define el comportamiento de un programa cuando se ejecuta.

Todas las declaraciones válidas de un programa deben traducirse a un subconjunto del lenguaje que se denomina Lenguaje Núcleo, que es el encargado de ejecutar efectivamente las operaciones en el computador.

Los lenguajes de programación están pueden definen su semántica en cualquiera de estas clases:

1. Semántica axiomática: Una declaración es la relación entre un estado de entrada antes de ejecutarse la sentencia y de salida después de ejecutada. Funciona bien para los paradigmas con estado
1. Semántica denotacional: Una declaración sobre es una función sobre un dominio abstracto. Funciona bien para modelos declarativos
1. Semántica lógica: Una declaración es un modelo de una teoría lógica. Funcioan bien para modelos declarativos y relacionales.
1. Semántica operacional: Una declaración es una ejecución en términos de la máquina abstracta. Funciona bien para todos los modelos.

## Abstracciones linguísticas:
Es una evolución del lenguaje de programación.Son nuevas construcciones gramáticales que se traducen al lenguaje núcleo.

## Azúcar sintáctico:
Notación abreviada para modismos que ocurren con frecuencia. Solo reducen el tamaño del programa