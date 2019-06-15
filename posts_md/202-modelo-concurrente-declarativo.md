Title: Modelo concurrente declarativo
Date: 2018-06-08T18:18:32+00:00
Description: Modelo concurrente declarativo
Tags: Modelos y Paradigmas de Programación
---
# Modelo concurrente declarativo

El modelo concurrente declarativo extiene del modelo declarativo al añadirle ejecución concurrente. Esto quiere decir que las técnicas usadas para el modelo declarativo también son aplicabables a este modelo, y más importante aún: estos programan son deterministas, porque el no determinismo con el que cuentan es No observable, lo que quiere decir que aunque al interior de un programa no se tenga el control de que se ejecuta en que orden, el resultado siempre será el mismo.

## Hilos
Para la implementación de este paradigma, se extiende la máquina abstracta que ahora no cuenta con una sola pila semántica sino muchas, las cuales representa un hilo, o un espacio de ejecución propio que comparte el mismo almacén de variables declarativas.

El ordenamiento de estas pilas de ejecución se realiza por medio de una operación llamada escalación, la cual le da un orden de ejecución en un núcleo compartido a cada etapa de computación.

De esta manera existe un planificador que tiene la información de todas las pilas semánticas y determina cuales están listas para ejecutarse: No suspendidas, es decir que contienen toda la información para ejecutar una etapa de computación.

## Flujos
Define al comunicación entre hilos. Un flujo es una lista de mensajes potencialmente infinita. Se define una operación de envío de mensaje al extender el flujo con un nuevo elemento. 

Los flujos se implementan por medio de variables declarativas.

Los flujos deben controlarse, y las maneras de realizarlo es por medio de: concurrencia dirigida por la demanda y limitación de la memoria.

La concurrencia dirigida por la demanda se denomina también ejecución perezosa.

## Evaluación perezosa
Contraria a la evaluación ansiosa o dirigida por los datos, es un esquema de programación donde solamente se ejecuta una declaración si su resultado es requerido en alguna otra parte del programa

## Disparadores por necesidad
Es la manera de implementar la evaluación perezosa, que crea un hilo con un procedimiento el cual solo será ejecutable cuando se solicite su valor. 

Para la implementación de este modelo se añade un nuevo almacén al modelo de computación, el cual será el almacén de disparadores.

La definición de una función perezosa se realiza por medio de un disparador por necesidad que ejecutará la función.

La programación declarativa concurrente define un par de conceptos interesantes los cuales son:

- Eficiencia: Un programa es eficiente si su desempeño solo difiere en un factor constante del desemepeño de un programa en lenguaje ensamblador que resuelve el mismo problema
- Neutralidad: Un programa es neutral si requiere poco código para resolver problemas técnicos con el problema original

### Algunas definiciones útiles

- El concepto fundamental para implementar la concurrencia por la demanda son los disparadores por necesidad
- El concepto fundamental para implementar la concurrencia dirigida por los datos es la variable de flujo de datos
- Un programa concurrente es declarativo si su no determinismo es no observable
- Como las variables declarativas permiten almacenar valores parciales, es posible implementar los flujos por medio de ellas.
- El modelo de computación concurrente dirigida por la demanda se consigue añadendo disparadores por necesidad al modelo de programación dirigida por los datos dirigido por los datos.
- El modelo de programación concurrente declarativa se consigue añadiendo hilos al modelo de programación declarativo.
- En un hilo todos los estados están ordenados
- El no determinismo no observable afecta el momento en el que una variable es ligada, pero no el valor que tendrá.
- Los hilos se comunican por medio de variables declarativas
- La competencia no se puede implementar utilizando este modelo de programación