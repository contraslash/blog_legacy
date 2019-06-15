Title: Modelo de programación con estado
Date: 2018-06-08T18:47:37+00:00
Description: Modelo de programación con estado explícito
Tags: Modelos y Paradigmas de Programación
---
# Modelo de programación con estadoEl estado se define como una secuencia de valores en el tiempo que contienen los resultados intermedios de un proceso de computación. En el modelo declarativo, el estado es implícito, mientras que este modelo con estado lo muestra explícito.

El principio de abstracción dicta que un sistema es igual a la suma de su especificación y su implementación.

Para soportar el principio de abstracción se requieren cuatro conceptos fundamentales:

- Encapsulación: Debe ser posible ocultar lo interno de una parte. Soportada por el alcance léxico
- Composicionalidad: Debería ser posible combinar partes para construir nuevas partes. Soportada por la programación de alto orden.
- Instanciación: Debería ser posible crear muchas instancias de una parte basados en una definición. Soportado por la programación de alto órden.
- Extensionalidad: Debería ser posible extender una parte sin afectar las otras. Soportado por el estado explícito

## Celda
Una celda es una pareja que guarda un nombre y una relación al almacén inmutable.

## Máquina Abstracta
La máquina abstracta para el modelo de programación con estado explícito, utiliza los mismos conceptos de la máquina abstracta del modelo declarativo, pero extiende con un almacén mutable para almacenar los nombres de las celdas

### Información importante
- El concepto de estado encapsulado se logra combinando el concepto de alcance léxico con el concepto de celda.
- Este modelo añade un estado explícito al modelo declarativo, que SI tiene estado, pero implícito
- El principio de abstracción no está completamente implementado en el modelo declarativo pues no permite añadir informción nueva a un componente
- El modelo de estado explícito nace para soportar la abstracción.
- El principio de abstracción se conforma de: Instanciación, composicionalidad, encapsulación y extensionalidad
- La transparencia referencial es violada en el modelo de programación con estado.
- Dos celdas con el mismo contenido pueden ser diferentes