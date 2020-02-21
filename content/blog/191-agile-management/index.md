---
title: "Agile Management"
date: "2018-03-07T23:44:46+00:00"
description: "Notas de la asignatura Tendencias en Ingeniería de Software, donde se repasan algunas prácticas ágiles como el Release Planning, Sprint Planning, Sprint BackLog, Tablero digital de tareas, Par programador y Continuous Integrations"
tags: "Continuous Integration,Tendencias en Ingeniería de Software,Metodologías Ágiles"
---
# Agile Management

## Release planning

Conocido como plan de proyecto, es el conjunto de historias de usuario agrupadas por release o versiones que se ponen a disposición de los usuarios, también lo encontramos como plan de versiones o pland e entrega

PAra que sirve?

Es necesario para
* Ayuda al dueño del proyecto a …

¿Cómo se hace?

Para decidir cuales son las capas del rpdoucto se pueden usar varias técnicas como el User Story Mapping, o el impact Mapping

¿Quién está implicado?

* Scrum master
* Product Owner
* Developer Team
* Interested Team

Antes de la reunión de planificación

* Se hace una cartera de productos clasificada administrada por el propietario del producto
* Información del equipo sobre las capacidades generales, la velocidad conocida y los impactos técnicos
* Objetivos de alti nivel de visión mercadeo y negocios
* Un reconocimiento de si se pueden necesitar nuevas …

Malas prácticas
* Considerar el plan como un contrato
* No tener un criterio de aceptación para cada release
* No revisar nunca el Plan
* Dar mucha importancia al detalle de lo que habrá en todas las releases

Nota del profesor:
* Hay una gran diferencia entre Scrum y XP, en Scrum se definen muchos sprints, pero en XP se define solo uno que muta mucho en el paso del tiempo
* El release plan funciona como estrategia de planeación

## Sprint planning

Es un evento delimitado por un lapso de tiempo de 8 horas, o menos, para comenzar un sprint. Sirve para que el Scrum Team inspecciones el trabajo del Product Backlog que es mas importante (prioritario) que se realice a continuación y se diseña ese trabajo en el sprint backlog

Quienes están comprometidas?

* Scrum master la convoca
* Se convoca al Product Owner
* Está todo el equipo de desarrollo

Es importante saber que es una negociación colaborativa para planear el resultado que el equipo quiere lograr. El equipo de desarrollo crea el sprint backlog, identificado lo que se entregará y un plan flexible apara cumplir con el resultado

El objetivo principal es preparar y compartir entre todos que se va a hacer exactamente en el próximo sprint. De esta reunión todos deben salir con una idea muy clara de lo que va a pasar en las siguientes semanas y de como se va a conseguir.

el tiempo ne el que está enmarcado el sprint planning es máximo de 8 horas, para un sprint de un mes. El sprint se divide en dos partes:

* Primera parte de la reunión: El product owner está presente y se define la meta del sprint. El equipo examina los detalles que el cliente tiene.
* Segunda parte de la reunión: solamente está presente el scrum manager y se define el esfuerzo para realizar cada tarea y se colocan responsables específicas para cada tarea.

Se deben trabajar los siguientes detalles
* Trabajar previamente en los detalles de la historia de usuario: si no se planea antes, la reunión se alarga y va a estar aburrida.
* Marcar hitos intermedios de desarrollo: Se define cuando se va a entregar y saber en el sprint que pseudo entregas se van a hacer
* Detectar la dependencia de terceros: Es importante que se revise que historias de usuario dependen de otras personas
* Buscar el compromiso de todos: 

## Sprint backlog

Conjunto de tareas que corresponde a una iteración. Organiza el caos con el que se enfrenta un equipo en cada iteración. Mantiene la transparencia dentro del desarrollo

Primero se priorizan las historias de usuario y luego se designan unas tareas para cada historia, y cada miembro del equipo de desarrollo queda como responsable de cada tarea.

## Tablero de tareas digitales

Es una herramienta exclusiva para el equipo de desarrollo.

Se tiene una tabla de la siguiente manera:

To do|Doing|Done
-|-
-|-|-

Se tiene el objetivo del sprint y se ve el Burn Down Chart, que mide el rendimiento y progreso del equipo de desarrollo.

Cada tarea debe tener un límite de tiempo

Algunas herramientas
* Jira
* IceScrum
* Easy Backlog
* Taiga
* Trello
* Kanbanize
* ScrumDo

Nota del profesor:
* Dependiendo del equipo, se definen restricciones de las tareas en cada espacio de columnas, pensando en la capacidad almacenado

## Par programador

* Las tareas no se asignan a un solo desarrollador sino a dos
* Dos programadores compartiando una estación de trabajo
* Se introdujo en XP
* Fomenta la cooperación entre los miembros del equipo

Se manejan dos roles:
* Driver: Es el que tiene el poder  de hacer las tareas en el pc, escribe la solución
* Navigator: Esta revisando y analizando el códgo que es introducido para detectar problemas o errores. Piensa en la estructura y el siguiente paso.

Beneficios:
* Código mas seguro
* Reducción de tiempo de trabajo
* Mejor código
* Mejor conocimiento global de parte del equipo
* Aprendizaje manejado para principiantes

Inconvenientes
* Falta de voluntad para trabajar en pareja
* Mala comunicación
* Mal desempeño en los roles

Nota del profesor:
* Se usa mucho en las empresas cuando hay un nuevo integrante del equipo, para mejorar su curva de aprendizaje y ver cuales son las aptitudes del nuevo integrante del equipo.
* Cuatro ojos ven mas que dos

## Continuous Integration

Es una práctica informática que consiste en realizar de forma automatizada sin mayor intervención humana distintas pruebas, ya sean unitarias o funcionalidades lo antes posible, y lo mas seguido posible, con el fin de detactar fallos lo antes posible.

Ventajas
* Los desarrolladores pueden detectar  solucionar problemas de integración de forma continua, evitando el caos a última hora cuando se acerca la fecha de entrega
* Disponibilidad constante de un build para pruebas, demos o lanzamientos anticipados
* Ejecución inmediata de las pruebas unitarios
* Monitorización continua en las métricas de calidad el proyecto

Desventajas
* Se requiere muco tiempo inicial para configurar de pruebas
* Se requiere que exista una  suite de pruebas

Qué se necesita para hacer integración continua?
* Repositorio de código
* Construcción automatizada
* Commits Diarios
* Pruebas unitarias
* Servidor de integración

Herramientas:
* Jenkins
* Github
* Bamboo
* Bitbucket

Nota del profesor:
* La integración contínua es un pilar fundamental para los DevOps
* CI es una técnica de optimizar para los tiempos de desarrollo

