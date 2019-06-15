Title: Los Microservicios de Martin Fowler
Date: 2016-12-11T18:31:50+00:00
Description: Una apreciación de la arquitectura orientada a microservicios basada en las opiniones de Martin Fowler en http://www.martinfowler.com/articles/microservices.html
Tags: Micro Servicios,Arquitectura de Software
---
# Los Microservicios de Martin Fowler

De momento creo que [este post](http://www.martinfowler.com/articles/microservices.html) de Margin Fowler es uno de los más icónicos en la Ingeniería de Software, porque de alguna manera formaliza un concepto arquitectural que emergió hace pocos años, y guía a los desarrolladores en la construcción y adecuación de este modelo descentralizado y distribuido de manejar el software.

Parafraseando un poco el artículo, los microservicios son solo un término de la jerga técnica avanzada de los ingenieros de software y se refiere a una estructura de proyecto que cambia la arquitectura monolítica tradicional en una estructura orientada a servicios aislados especializados que convergen bajo una capa controladora que expone las funcionalidades como una sola aplicación. Siendo un poco más técnicos, una arquitectura orientada a microservicios consta de varias aplicaciones que interactuan por medio de APIs, que se despliegan independientemente, se mantienen independientemente y mas importante, se escalan independientemente.

En comparación con una arquitectura de núcleo monolítico, se nos ofrece una descripción gráfica, mostrada acontinuación ![Arquitectura monolítica vs Micro Servicios, por Martin Fowler](http://www.martinfowler.com/articles/microservices/images/sketch.png)

Siempre al pensar en micro servicios, recuerdo una conversación con un Ingeniero, donde resaltaba que el concepto de microservicios en realidad no era algo que me impactara mucho, porque en el ambiente de los sistemas distribuidos, es una arquitectura bastante común, donde ciertos procesos requieren mas potencia de cómputo y desarrollo especializado para minimizar tiempos de respuesta y darle mayor precisión a las respuesta, manteniendo una regla de oro: Entradas y Salidas Limpias.

Si bien es cierto que el concepto ha estado claro, aún no se dispone de una definición formal y aceptada de lo que es un micro servicio, pero claramente podemos definir sus características:

1. Componentización:
La arquitectura orientada a microservicios, mas que enfocarse en llamados a funciones de un núcleo común, crea núcleos pequeños y especializados que interactua con la demas aplicación por un interfaz pública. Los módulos ya no funcionan como librerías, sino como servicios, que son desplegados independientemente y permiten un escalamiento enfocado en partes críticas y específicas de la aplicación, no de toda la aplicación
1. Organización descentralizada
Al pensar en que el proyecto se separa en servicios independientes, la estructura organizacional tradicional tiende a modificarse modulazándose de la misma manera, y se cambia el concepto de tener grupos enfocados en especialistas de interfaz de usuario, especialistas en desarrollo y especialistas en base de datos, a grupos multidisciplinarios encargados de soportar ellos mismos un conjunto de funcionalidades específicas
1. Comunicación por APIs
La comunicación entre segmentos del proyecto se cambia de una estructura de comunicación compleja, usando patrones de diseño densos como el ESB (tradicionalmente conocido como Bus) a una simple, donde la información se expone por medio de un API simple, donde la carga lógica de interpretación de datos no llace en el canal sino en el proceso.
1. Heterogeneidad
Cada tecnología tiende a especializarse en un problema específico y la optimización de procesos usando las herramientas mas adecuadas para cada así entre servicios no se compartan un Lenguaje de Programación o un Framework o una Librería, no es ua camisa de fuerza para el desarrollo de producto, entonces es común ver proyecto usando NodeJS para sus comunicaciones en tiempo real, un Framework mas traducional para las transacciones relacionales y segmentos enfocados en distrubuión de los datos y bases de datos No SQL
1. Automatización
Como cada servicio se ejecuta en ambientes distintos, el mantenimiento de la manera tradicional suele ser muy costoso, por esta razón, se usa un tiempo significativo en la adecuación de herramientas auto?aticas que faciliten el despliegue y mantenimiento de cada servicio en la aplicación
1. Tolerancia a Fallas
La descentralización del nucleo de trabajo permite que los servicios operen normalmente incluso si uno falla, lo cual proyecta robustés en el producto, además permite el monitoreo individual de cada servicio y su escalamiento bajo demanda
1. Evolución contínua
Reparar, reconstruir o cambiar un componente es fácil, pues los servicios están desacoplados, permitiendo que cada servicio se tranforme bajo necesidad y se adapte a las necesidades del producto.

Las arquitecturas orientadas a microservicios se están tomando el mundo y grandes compañias están migrando paulatinamente de su arquitectura monolítica a hibridos altamente permeados con servicios que les ofrecen mayores ventajas en tópicos relacionados con escalabilidad, mantenimiento y rendimiento
