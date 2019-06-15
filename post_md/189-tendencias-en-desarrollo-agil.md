Title: Tendencias en desarrollo Ágil
Date: 2018-03-07T23:40:49+00:00
Description: Notas de clase de la asignatura Tendencias en Ingeniería de Software, donde se estudia el uso de algunas prácticas ágiles, como son las Historias de Usuario, el Product BackLog, La estimación y el Planning Poker
Tags: Tendencias en Ingeniería de Software,Metodologías Ágiles,SCRUM
---
# Tendencias en desarrollo Ágil## Historias de usuario: 

En requerimiento es una descripción formal, pero una historia de usuario es una definición informa. Una historia de usuario describe al funcionalidad que será valiosa tanto para el osuario o el comprador de un software [Mike Kohn 2004].

Las historias de usuario deben ser cortas, tanto como para poder ser escrita en una nota adhesiva. 

Se recomienda altamente que se escriban pruebas para cada historia de usuario.

Características (INVEST por sus siglas en inglés):

* Independents: Se pueden realizar en cualquier órden
* Negociables: Pueden cambiar, no son un contrato
* Valuables: Son valiosas para alguien
* Estimables: Pueden poderse estimar
* Small: Deben ser pequeñas
* Testables: Deben poder poderse probar

Alguna plantilla útil para una historia de usuario:

> Como [rol del usuario] quiero [objetivo] para poder [beneficio]

**Nota del profesor**

Es muy importante identificar en una historia de usuario:

* Identificar el actor: la persona que interactúa con el sistema
* Evitar detalles específicos sobre la historia de usuario
* Definir el propósito para cada historia de usuario

## Product Backlog

Es una lista ordenada, priorizada y estimada de las cosas conocidas y necesarias se deben realizar para el proyecto.

Todo list
ID|Story|Estimation|Priority
-|-
7|As an authorized user I want to create a new account|1|1
1| As an unauthorized user I want to …. |

El product backlog jamás está terminado y evoluciona con el desarrollo del proyecto.. No es un contrato fijo y se ajusta según los resultados y riesgos.

Debe tener atributos mínimos como: descripción, order estimado y un valor referente al proyecto o cliente.

Cada elemento es del siguiente tipo y debe agregar valor para el cliente:
* Características/Funcionalidades
* Cambio de la funcionalidad
* Errores (encontrados previamente)
* Trabajo técnico/ Mejora técnica
* Adquisición de conocimiento (Investigación para desarrollo y toma de decisiones)

Empieza con las características requeridas del proyecto
Es la responsabilidad del Product Owner en la metodología scrum

**Nota del profesor**

En el backlog, compuesto por historias de usuario, puede ser descompuesto más adelante en tareas, las cuales definen las labores diarias de cada miembro del equipo de desarrollo.

Aunque tenemos una estimación flexible, en la realidad, los clientes requieren una aproximación del costo y el tiempo de entrega del proyecto, la estimación de las historias de usuario en el backlog permite aproximarnos a estos valores. En la práctica, empresas pequeñas utilizan un equivalente de puntos a horas y dinero para en función de el product backlog realizar una cotización aproximada.

## Priorización

La priorización ayuda la planificación de los proyectos. Se realiza al comienzo de cada iteración y se evalúa posteriormente. Nor permite ordenar las funcionalidades de un software de mayor a menor prioridad.

Técnicas de priorización

* MoSCoW

Must: Obligatorio, esencial para el proyecto. 
Should: Importante pero no vital
Could: Deseable pero no es necesario
Wont: No indispensable en el momento, pero se podrá incluir posteriormente.

Para definir a qué categoría pertenece a una historia de usuario es muy válido responderse esta pregunta:

> ¿Qué pasa con el sistema si no se incluye este requisito?

* Theme Scoring
Se valua de acuerdo a su valor, coste y riesgo

Se pondera cada uno de estas características y se ordena de mayor a menor

Historia de Usuario | Valor 50% | Costo 15% | Riesgo 35% | Valoración Final | Prioridad
-|-
1|5|3|3|4|1
2|4|3|1|2.8|5
3|5|2|2|3.5|3
3|4|2|3|3.35|4

* Risk Vs Value

Definimos cuadrantes de relaciones donde

Evitar Alto Riesgo, Bajo Valor|1 Alto riesgo, Alto Valor
3 Bajo Riesgo, Bajo Valor |2 Bajo riesgo, Alto valor

Se debe organizar las tareas primero evacuando el valor 1 hasta el valor 3.

En el desarrollo del proyecto, es posible que algunas historias de usuario que se deban evitar, pueden bajar al nivel 3

* Modelo Kano y Satisfacción del cliente.

Mide las expectativas de los usuarios a través de un cuestionari
Divide las funcionalidades en:

* Esenciales: Tienen que estar en el producto obligatoriamente
* Lineales: El valor del cliente aumenta al implementar esta funcionalidades
* Asombrosas: Mejoran la satisfacción del cliente

* Complexity vs Value

En lo personal prefiero, tanto para diseño de producto como para estimación de historias de usuario.

Primero le damos dos valores a acada historia de usuaria considerando su complejidad y su valor de mercado.

Pintamos cada historia en un plano cartesiano donde el eje X corresponde a la complejidad y el eje Y corresponde al valor de mercado.

Se realiza una categorización donde las tareas a ejecutar primero son las que mas valor le generen al usuario y menos complejidad tentan. 

Las últimas serán las que menos valor otorguen y más complejas sean.

## Estimación en planificación tradicional

Se trata de un proceso relativamente lineal donde:

* Se estima el producto a desarrollar, separado por etapas
* Se planifica el desarrollo
* Se ejecuta el plan

Problemas:

* Se trata el desarrollo como una actividad predecible cuando no lo es
* La persona que estima no siempre es la misma que va a desarrollar
* Un tiempo estimado es considerado como un compromiso

> La estimación en el desarrollo ágil es una actividad de creación y transformación del conocimiento donde:

* No se puede predecir ni estimar de forma precisa
* Se basa en la experiencia y conocimiento de los involucrados
* Se encuentra ligado a que tan bien están descritas las historias de usuario
* No se usan unidades de medida de tiempo coo horas o días
* Un ’story point’ indica un tamaño relativo para cada historia de usuario
* Elimina la presión de estimar en tiempo
* Es mas certero estimar tareas pequeñas

#### Velocidad del equipo

Se define como la cantidad de 'story points’ que se completan por iteración.

Permite saber:

* La fecha estiamda de finalización del proyecto
* En qué iteración estará terminada la mayor parte del proyecto.

#### Prácticas de estimación

* Planning Poker
* Bucket System
* Dot Voting
* T-shirt Sizes
* Affinity Grouping
* Ordering protocol


## Planning Poker

Es una práctica de estimación colaborativa basada en consenso. Permite obtener una medida de tamaño relativa de las historias de usuario. 

Es la práctica de estimación mas popular y hace uso de una secuencia de Fibonacci modificada. 

Evita la influencia de unos estimadores sobre otros.

No es adecuada para grandes cantidad de items.

Los valores del planning poker son:

* 0
* 1/2
* 1
* 2
* 3
* 5
* 8
* 13
* 20
* 40
* 100
* ?

Procedimiento para el Planning Poker

* El product Owner lee un item del Product Backlog
* El equipo discute el item y realiza preguntas al PO, con el fin de aclarar dudoas
* Cada estimador selecciona una carta en privado
* Si todos seleccionaron la misma hay consenso.
* En caso que no haya consenso, se solicita a los estimadores que puntuaron mas y puntuaron menos que expliquen por qué la puntuaron así y luego se realiza una votación


## Conclusiones

Definir formalmente lo que es una historia de usuario es un poco complicado
Las historias de usuario son de las prácticas más útiles y aceptadas en la mayoría de las metodologías ágiles
El product  backlog permite tener claro lo que se debe hacer en el proyecto
La priorización permite dedicar mas tiempo 
Planning poker es la técnica más usada para estimar