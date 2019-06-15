Title: Modelo de programación declarativa
Date: 2018-06-08T17:15:37+00:00
Description: Modelo de programación declarativa
Tags: Modelos y Paradigmas de Programación
---
# Modelo de programación declarativa## Variables declarativas
Una variable de única asignación que puede estar o no estar ligada. Una vez se define su valor, ese valor debe permanecer hasta que la computación termine.

Una variable puede ser una estructura de datos compleja y contener otras variables declarativas dentro de ella. Si alguna de estas variables está sin ligar, la estructura de datos tendrá un valor parcial hasta que todas sus variables internas estén ligadas. Esta propiedad toma mucha importancia en la programación concurrente declarativa y definen lo que se denominará variables de flujo de datos.

Las variables declarativas tienen un concepto llamado alcance, que represente los lugares donde el valor de esta variable puede ser accedido; este alcance puede ser dinámico o estático

## Máquina Abstracta

Para la programación declarativa, la máquina abstracta está compuesta por una pila semántica y un almacén de variables declarativas.

La pila semántica tiene tres estados:
- Ejecutable: Si se puede ejecutar una etapa de computación
- Terminado: Si la pila está vacía
- Suspendido: No se puede ejecutar una etapa de computación

## Procedimientos y registros
Los lenguajes que proveen un nivel de abstracción sobre los registros se denominan Lenguajes simbólicos.

Los procedimientos son más simples que los objetos o funciones, y es posible representar estos dos tipos por medio de procedimientos.

## Iteración
Se define como un proceso cíclico por medio del cual el tamaño de la pila se mantiene acotado por una consante, independiente del número de iteraciones del ciclo.

Está compuesta de un Estado Inicial, un Verificador, Una función de transformación y un llamado recursivo a ella misma.

## Recursión
Es una técnica más general que la iteración. Define funciones o tipos de datos.

### Algunos datos importantes
- La abstracción procedimental es un proceso por medio del cual se pueden  crear proceso al interior de otro proceso para ser ejecutados cuando se requieran y no en el momento de la definición.
- Genericidad: Proceso  por medio del cual se  pueden pasar procedimientos como argumento a otro procedimiento
- Instanciación: Proceso que permite que un procedimiento retornte un procedimiento como resultado de un cálculo
- Embemimiento: Proceso que permite que los procedimientos sean almacenados en variables declarativas.