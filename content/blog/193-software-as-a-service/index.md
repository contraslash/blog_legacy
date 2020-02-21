---
title: "Software as a Service"
date: "2018-03-23T13:12:41+00:00"
description: "Notas de clase de la asignatura Tendencias en Ingeniería de Software"
tags: "Arquitectura de Software,Tendencias en Ingeniería de Software,SaaS"
---
# Software as a Service

El SaaS es un respiro que tiene la industria del software cuando el mercado estaba saturado y la adquisición de nuevos clientes era muy costoso.

## Qué es SaaS
Es un modelo en el cual se ofrecen aplicaciones que funcionan en la nube, bajo la modalidad de servicio, y para su acceso se requiere un navegador o cliente especializado a través de internet.

Es un modelo que proporciona acceso remoto a las aplicaciones como un servicio basado en la web. El servicio de software se paga en cuotas mensuales y pagar por lo que se contrata o lo que se consume.

## Cloud Computing

Es un modelo para habilitar recursos computacionales compartidos de una manera ubicua, conveniente y bajo demanda, que pueden ser rápidamente aprovisionados y desplegados con un esfuerzo de manejo mínimo o interacción del proveedor.

### Características

* Acceso ubicuo por las redes
* Recursos compartidos
* Rápida elasticidad
* Servicios medibles
* Autoservicio

### Modelos de entrega
* Nubes públicas
* Nubes privadas
* Nubes Híbrida

### Modelos de servicio

* Infraestructura como servicio (IaaS)
* Plataforma como servicio (PaaS)
* Software como servicio (SaaS)

### Por qué usar computación en la nube

La computacieon en nube es vista como una solucón integral en la cual todos los recursos informáticos o computacionales son brindados de manera rápida y según lo determina la demanda.

La computación en nube permite a los consumidores y a las empresas, usar aplicaciones de negocios comunes en línea, sin necesidad de instalar software en sus equipos, usando un navegador web.

Esta tecnología permite un estilo de gestión de recursos informáticos más eficiente mediante la centralización del almacenamiento, memoria de los equipos, Procesamiento y ancho de banda, entre otros.


### Características

* Integración probada con los servicios web
* Prestación de servicios de talla mundial
* No se requiere instalar software o Hardware
* Implementación más rápida y con menos riesgos
* Gran capacidad de personalización
* Más opciones para usuarios comerciales
* Actualizaciones automáticas

### Promesas de SaaS

* Se requieren inversiones bajas para usar las aplicaciones
* Se evitan los problemas de soporte o mantenimiento
* Curvas de aprendizaje cortas
* Software siempre actualizado
* Software por subscripción


### Arquitectura multitenant

Todos los usuarios las aplicaciones comparten una infraestructura común y el código de aplicación es mantenido de manera centralizada. Además una instancia sirve a muchos clientes de una o varias organizaciones, lo cual evita tener que mantener múltiples versiones de la misma aplicación. Cuando se desea separar la aplicación se mantiene la misma aplicación en diferentes máquinas virtuales.

### Adecuado nivel de personalización

La habilidad de que cada usuario personalice fácilmente su aplicación de tal manera que se adapte a su proceso de negocio sin afectar su infraestructura

## Aspectos a tener en cuenta para crear aplicaciones tipo SaaS

Primero se debe entender que vamos a migrar de un esquema Software as a Product (SaaP) a un modelo Software como Servicio (SaaS)

En el modelo SaaP, cada cliente ejecuta su propia instancia de la aplicación, normalmente en su propio datacenter; en SaaS, se comparte una copia de aplicación por todos los clientes.

El modelo SaaS Tiene 3 pilares:

* Modelo de Negocio: 
    * Cambio de modelo de venta por servicio
    * Reducción de costos mediante la especializaición y economía de escala. Todo se reduce al mínimo rentable
    * Funcionalidades de comercio electrónico
    * Formas de Pago:
        * Por usuarios
        * Por funcionalidad
        * Tarifa Plana
        * Por uso
* Estructura Operacional:
    * Se refiere todo el proceso de gestión que es operada por tercernos, incluye aspectos como:
        * El proveedor es responsable de mantener el software funcionando
        * Uso de IaaS
        * Adoptar un enfoque DevOps
        * Stop and Rn
        * Monitoreo
        * Gestión de políticas
        * Mesas de ayuda
        * Confiabilidad
        * Auditoría
* Arquitectura de la aplicación:
    * Se define si la aplicación será single tenant o multi tenant

#### Ventajas y desventajas

-|Single Tenant|Multi tenant
-|-
Dificultad de la implementación|Baja|Media o alta
Personalización|Alta|Media o Baja
Administración requerida|Alta|Media o Baja
Costos a largo plazo|Altos|Bajos

### Niveles de multi tenant

* Nivel 1: Propósito específico: Cada cliente tiene su propia instancia de la base de datos y cada instancia puede ser configurable
* Nivel 2: Cada cliente tiene su propia instancia, pero esa instancia es idéntica a los demás
* Nivel 3: Existe una sola instancia de la base de datos
* Nivel 4: Se tiene un balanceador de tenants y cada tenant es idéntico e independiente

## Aspectos a tener en cuenta:

* ¿Su aplicación debe ser sigle-tenant o multi-tenant? 
* ¿Cómo lograr confiabilidad y escalabilidad, tanto en un único centro de datos como en múltiples centros de datos? 
* ¿Cómo manejar la seguridad, incluyendo la identidad y el control de acceso?
* ¿Cuánta personalización su aplicación debe permitir y cómo debe proporcionar esa personalización? 
* ¿Costos de operación de Single-Tenant Vs Multi-Tenant? 
* ¿Qué métricas debe seguir su aplicación, junto con cómo debe almacenar y procesar esta información? 
* ¿Qué diseño operacional adopta para su aplicación y qué debe proporcionar la aplicación para un equipo de DevOps?.

## Conclusiones
* Las aplicaciones de software como servicio (SaaS) se han convertido definitivamente en la corriente principal incluso entre las empresas.
* Sin embargo, el desarrollo de una gran aplicación SaaS no es trivial. Requiere una sólida comprensión de multi-tenancy, configurabilidad, seguridad, partición con el fin de construir una aplicación SaaS que se pueda utilizar para servir a diferentes tipos de clientes.
* Ahorros significativos a través de SaaS SaaS “virtualizado” con múltiples tenants es el siguiente paso en una arquitectura moderna, eficiente, rentable y flexible que puede funcionar en cualquier dispositivo

