Title: Programación Concurrente por Paso de Mensajes
Date: 2018-05-04T21:02:24+00:00
Description: Modelo de Programación Concurrente por Paso de Mensajes
Tags: Modelos y Paradigmas de Programación
---
# Programación Concurrente por Paso de Mensajes

## Definición

La programación concurrente por paso de mensajes es un estilo de programación donde entidades independientes se comunican asíncronamente por medio de mensajes.

## Puerto
Se define este Tipo Abstracto de Dato con un Identificador P un flujo S.

Se define una operación Send(P,X) donde por el puerto P se envía el valor X

## Máquina Abstracta

Como es un modelo que extiende del modelo de Programación Concurrente Declarativa, se mantiene la máquina conformada por:

- Almacén Inmutable de datos
- Conjunto de Pilas semánticas

y se añade un nuevo concepto:

-Almacén Mutable de Puertos

Como se extiene del modelo de Programación Concurrente Declarativa, se toma le concepto de **Objeto Flujo**: Un procedimiento recursivo que ejecuta en un hilo propio y se comunica con otros objetos flujo por medio de flujos de entrada y salida.

Con base en esta definición, se define un **Objeto Puerto** que combina uno o mas puertos con un objeto flujo

## Multi Agent Systems (MAS)

### Modelo:

- Se basa en el modelo de Programación Concurrente por paso de mensajes
- Un componente es un procedimiento con entradas y salidas tipo Flujo 
- Cuando se instancia, se crea un objeto tipo puerto

Para cada componente se debe definir:

- Protocolo de mensajes
- Diagrama de estado

### Otra información importante
- Composición: construcción de un nuevo componente a partir de otros
- Acoplamiento: combinación de instancias de componentes por medio de las entradas y salidas
- Instanciación: creación de una instancia de un componente
- Restricción: definición de la visibilidad de las entradas o salidas de un componente compuesto
- El concepto de puerto permite: el embebimiento de objetos puerto en estructuras de datos y la comunicación muchos a uno
- Los cables de muchos tiros: Se utilizan para flujos de mensajes, pueden enviar cualquier número de mensaje, Se implementan con puertos
- Los diagramas de estado definen como cada uno de  los componentes reacciona con los mensajes recibidos.
- Los cables de muchos tiros: Se implementan con variables de flujo de datos, solamente se puede pasar un mensaje con ellos, se usan para mensajes que no cambian o mensajes de una sola vez
- El diagrama de componentes define como se envían mensajes los componentes, pero no como reaccionan ellos
- Los objetos reactivos no tienen estado