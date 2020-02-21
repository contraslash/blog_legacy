---
title: "Metodologías ágiles"
date: "2018-03-07T23:38:30+00:00"
description: "Notas de clase Tendencias de Ingeniería de Software, donde se tocan temas importantes como Metodologías Ágiles, algunos mitos, las razones por las cuales se establecieron sobre las metodologías tradicionales y algunas definiciones puntuales sobre lo que es SCRUM"
tags: "Tendencias en Ingeniería de Software,Metodologías Ágiles,SCRUM"
---
# Metodologías ágiles

Las metodologías ágiles nacen como una alternativa a metodologías tradicionales.

Las métodologías ágiles inician manejando proyectos pequeños, pero con el tiempo se dieron cuenta que es posible manejar proyectos de cualquier tamaño con técnicas ágiles.

## Factores determinantes en el desarrollo de Software utilizando metodologías ágiles.

Factores de éxito | Factores de fracaso
-|-
Participación de los usuarios | Falta de participación de los usuarios
Soporte de la administración ejecutiva|Falta de apoyo
Claridad en los requerimientos|Requerimientos incompletos
Planeación adecuada|Falta de planeación
Expectativa realísticas|Expectativas no realísticas
Entregas parciales|Entregas muy grandes
Claridad en ls objetivos | Desconocimiento de la tecnología
Trabajo duro|Mínimo esfuerzo

## Metodologías tradicionales

Metodologías en cascada
* RUP
* Microsoft Software Foundation
## Metodologías ágiles

Busca aumentar el valor reduciendo el riesgo

* XP
* Scrump
* Crystal
* AgileUP (Agile unified Proces)
* DSDM 
* FDD (Feature driven development)

[Manifiesto ágil](http://agilemanifesto.org/)

> Vale mas un producto funcionando que una buena documentación

## Fundamentos

* Valores
    * Trabajar para los entregables
    * Responder al cambio
    * Colaboración con los clientes
* Principios
    * Simplicidad
    * Entregas frecuentes
    * Excelencia técnica
    * Trabajo en equipo
    * Mejoramiento continuo
* Prácticas
    * Planeación
        * Historias de usuario
        * Reuniones diarias
        * Plan de iteraciones
        * Retrospectivas
        * Release plan
        * Planning Poker
    * Desopliegue
        * TDD
        * Integración contínua
        * Despliegues automáticos
        * Diseño arquitectural
        * Refactoring
        * Spikes
        * Propiedad colectiva del código

En el uso de metodologías ágiles según el Anual state of agile reporte del 2017 - versionone

Metodologías usadas

* 58% Scrum
* 10% Scrum/XP Hybrids
* 8% Custom Hybryd
* 8% Scrumban
* 5% Kanban

Prácticas más usadas:

* 90% Iteration planning
* 88% Daily standup
* 83% Retrospectives
* 81% Iterations Reviews
* 71% Short iterations
* 66% Release planning
* 62% Team based estimation
* 55% Dedicated product owner
* 54% Single team (integrated dev testing)
* 50% Frequent releases
* 50% Kanban 
* 45% Open work area
* 38% Product roadmapping
* 35% Story Mapping
* 25% Agile portfolio planning
* 22% Agile/lean UX

Prácticas de Ingeniería

* 74% Unit testing
* 61% CI
* 56% Coding standards
* 52% Refactoring
* 40% TDD
* 36% Automated acceptance testing

Causas de falla:

* 46% Company Philosophy or culture at odds with core agile values
* 41% Lack of experience with agile methods
* 38% Lack of management support
* 38% Lack of support for cultural transition
* 38% Inconsistent agile practices and process
* 36% External pressure to follow traditional methodologies

Barreras para la adopción:

* 55% Ability to change organizational culture
* 42% General organizational resistance to change
* 40% Pre existing rigind waterfall frameworks

## Mitos comunes

* Documentación pobre
* No planeación
* Anti arquitectura
* Alto riesgo
* No control de costo
* Mala calidad

## Cómo adoptar estas métodologías?

* Shu - Follow: Aprenda y practique las técnicas
* Ha -  Break Away: Colecciones técnicas adicionales
* Ri - Fluent: Mezcle y desarrolle nuevas ténicas

> Las metodologías ágiles nos ayudan a hacer gestión, control y seguimiento rápido de nuestros proyectos

## Pasos para pasarse a ágil

1. Obtener soporte de la administración
2. Trabajar en equipo
3. Procurar la excelencia técnica  y la calidad del producto
4. Automatizar las pruebas
5. Mejoramiento continuo

## Estrategias para corregir problemas

Problema | Solución ágil
-|-
Calidad inadecuado|Diseño simple, TDD, Integración contínua, Refactoring
Nuevas funcionalidades que requieren mucho tiempo | Spike, diseño simple, TDD, Integración Continua
Funcionalidad no usuada por el cliente| Colaboración con el cliente, Historias de usuario
Costo de desarrollo muy alto|Diseño simple, TDD, Refactoring
Nuestro equipo Vs el Cliente|Retrospectivas, Colaboración del cliente, Historias de Usuario
El cliente quiere mas y mas cosas|Colaboración con el cliente, Historias de Usuario

## Beneficios de adoptar metodologías ágiles
* Reducción  del tiempo de desarrollo y de los costos
* Mejoramiento continuo (Mejora la productividad)
* Mejora la transparencia (proyecto y visibilidad del proceso)
* Eficiencia en el manejo del cambio
* Lugares agradables para trabajar


## Scrum

Scrum es un proceso en el que se aplican de manera regular un conjunto de buenas prácticas para trabajar colaborativamente, en equipo y obtener el mejor resultado posible del proyecto

Las fases en las que se divide el slkdnsldgjnsdjgabkdja COMPLETAR

### Roles del Scrum

* Product Owner: Voz del cliente y el responsable de desarrollar, mantener y priorizar las tareas en el backlog
* Scrum Master: Es responsable de aseguurarse que el trabajo del equipo vaya bien siguiendo las bases de Scrum. Además se encarga de remover cualquier obstáculo que pueda encontrar el equipo
* Development Team: Miembros del equipo son los encargados de escribir y probar el código

### Definiciones

* Product Backlog: Lista ordenada, estimada y priorizada de las historias de usuario
* Punto de Scrum: Esfuerzo que se necesita para hacer algo
* Sprint backlog: Conjunto de historias de usuario que se van a desarrollar en un sprint. Cada uno debería durar entre 1 y 4 semanas. Al final de cada sprint se espera tener una pequeña entrega
* Proyecto: conjunto de varios sprints
* Burndown chart: gráfico para visualizar el crecimiento del proyecto en contra del decrecimiento de las historias de usuario
* Retrospectiva: Espacio de evaluación del Sprint. ¿Qué hicimos bien? ¿Qué hicimos mal? ¿Qué debemos mejorar?
* Entrega: Artefacto obtenido en la finalización de un sprint. Debe ser incremental. Se añaden nuevas funcionalidades y se mejoran características
* Equipo: Conjunto de personas que ejecutan un sprint. Deberían estar conformados entre 5 y 9 personas
* Tabla de Scrum:
Sprint|Historias de usuario|Puntos|Fecha de entrega|ResponsableEstado
-|-
1|7|4|12-12-2018|ma0|En proceso
1|8|4|14-12-2018|andres|En proceso

