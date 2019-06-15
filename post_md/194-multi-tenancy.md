Title: Multi tenancy
Date: 2018-03-23T13:13:21+00:00
Description: Notas de clase de la asignatura Tendencias en Ingeniería de Software sobre Multi Tenancy
Tags: Arquitectura de Software,Tendencias en Ingeniería de Software
---
# Multi tenancy## Aspectos importantes antes de definir si se va a utilizar single tenant o multi tenant

* ¿Cómo lograr confiabilidad y escalabilidad, tanto en un único centro de datos como en múltiples centros de datos ? 
* ¿Cómo manejar la seguridad, incluyendo la identidad y el control de acceso ? 
* ¿Cuánta personalización su aplicación debe permitir y cómo debe proporcionar esa personalización. 
* ¿Costos de operación de Single-Tenant Vs Multi-Tenant ? 
* ¿Qué métricas debe seguir su aplicación, junto con cómo debe almacenar y procesar esta información ? 
* ¿Qué diseño operacional adopta para su aplicación y qué debe proporcionar la aplicación para un equipo de DevOps.


## ¿Qué es multi tenant?

Una aplicación de software multi-tenant es un tipo especial de software altamente escalable, en el que la aplicación y su infraestructura son compartidas entre múltiples tenants para ahorrar costos de desarrollo y de mantenimiento. 

Una aplicación SaaS “virtualizada” con múltiples tenants es el siguiente paso en una arquitectura moderna, eficiente, rentable y flexible.


## Tipos de arquitecturas multi tenant

* Bases de datos separadas: todos los datos están separados físicamente
* Bases de datos compartidas y esquemas separados: Es una misma base de datos, pero cada esquema es distinto
* Base de datos compartida y esquema compartida: La misma base de datos y el esquema es el mismo para todos