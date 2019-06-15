Title: Mejores Prácticas para el manejo de ramas en Git
Date: 2017-03-09T15:04:59+00:00
Description: Mejores prácticas para el manejo de ramas en Git
Tags: Buenas Prácticas,Git,Continuous Integration,Automatic Deployment
---
# Mejores Prácticas para el manejo de ramas en GitEste Post está basado en [Branching Best Practices](http://guides.beanstalkapp.com/version-control/branching-best-practices.html), un artículo de [BeanStalk](http://beanstalkapp.com/)

## Introducción
Comenzar con un sistema de control de versiones puede ser una experiencia que nos abra los ojos. Al comienzo puedes pensar ¿cómo trabajé sin esto? Una vez que tengas los fundamentos básicos de control de versiones, puedes aumentar tu productividad mejorando tu flujo de trabajo. El siguiente paso es aprender a programar en ramas.


Programar en ramas es una práctica sencilla que mantiene tu código mas organizado. Las ramas permiten mantener el trabajo "en progreso" separado del trabajo probado, completado y estable. No solamente es una manera efectiva de colaborar con otros sino también de automatizar el despliegue de actualizaciones o arreglos a tus servidores.

## Codificando en ramas por defecto
Así no sepas como usar ramas en tu proceso de desarrollo, ya estás usando ramas al crear tu primer commit en tu sistema de control de versiones. En la mayoría de sistemas de control de versiones, cada repositorio tiene una rama por defecto, esta rama puede ser:

- En subversion una carpeta llamada trunk
- En git una rama llamada master.

Sin configurar nada, tu primer commit a un repositorio será hecho en esta rama de trabajo.

Cada sistema de control de versiones tiene una aproximación diferente a crear, mezclar, y eliminar ramas. Nosotros nos vamos a enfocar en el proceso de desarrollo y sugerimos que si tienes alguna duda de cómo funcionan estos comandos, vayas a la documentación oficial de cada sistema de control de versiones.

## Flujo de trabajo con ramas
Usar ramas puede parecer complicado sin alguna guía. Vamos a ayudarte a enfocarte en dos usos específicos de tener ramas en tu flujo de trabajo:

### Beneficios de usar ramas: Crear características y arreglas bugs.
La mayoría de errores de código encaja en una de estas dos categorías: O estas construyendo una nueva característica o existe un bug con el código base. Un verdadero problema ocurre cuando dos de estas cosas ocurren al mismo tiempo.

Imagina que recientemente lanzaste una característica X. Las cosas van bien al comienzo así que continuas con la siguiente tarea de la lista, la característica Y. Comienzas a programar y a hacer commits a tu repositorio cuando de repente encuentras un problema con la característica X  que tienes que arreglar de inmediato. ¿Qué haces?

Si todo el trabajo ha sido realizado en la rama por defecto de tu repositorio, necesitas darte cuenta como guardar el trabajo actual en la característica Y, revertir la versión a la versión en la que fue desplegada la característica X, realizar el arreglo, y luego continuar el trabajo con la característica Y. Esto puede ser complicado y potencialmente puedes perder algo de trabajo o introducir nuevas problemáticas.

En lugar de esto puedes dejar a tu sistema de control de versiones realizar todo el trabajo sucio por ti. Posiblemente tienes una rama apuntando al momento cuando la característica X fue desplegada y también creaste una nueva rama para comenzar con la característica Y, la cual incluye un nuevo historial y una copia entera de todo el código desde el momento en que esta rama fue creada y puedes crear commits tranquilamente sin alterar el código que fue desplegado en la rama de la característica X.

Solamente cuando la característica es probada, esta completa y lista para el despliegue, puedes mezclar la rama con la rama actual trabajo.

Esto significa que puedes cambia entre características a la rama principal de trabajo en cualquier momento y crear nuevas ramas de trabajo desde este punto, con algún arreglo a un bug que necesites hacer. Después puedes volver a la rama de la característica en desarrollo y continuar sin alterar nada. Arreglar un bug muy pequeño puede parecer no necesario usando esta aproximación, pero seguir esta buena práctica te ayudará a evitar situaciones donde las problemáticas pequeñas se convierten en problemáticas grandes que pueden dejar tu rama de trabajo en un estado desordenado.

## Mejores prácticas con desarrollo de características y arreglo de problemáticas en ramas.

- Evita realizar commits con trabajo no terminado a la rama de flujo de trabajo.
- Crea una rama en cualquier momento que estés haciendo una tarea no trivial. Esto incluye desarrollo de nuevas características y arreglo de bugs.
No olvides eliminar las ramas de características una vez hayan sido mezcladas con la rama de flujo de trabajo. Esto mantendrá tu repositorio limpio.

## Beneficios de usar ramas: Ramas de ambientes para servidores.
Otra razón para usar sistemas de control de versiones que puedes usar tu repositorio como fuente de despliegue de código a tus servidores. Al igual que con el desarrollo de nuevas características o el arreglo de errores, las ramas de ambientes para servidores permite saber exactamente que código se está ejecutando en un servidor en cada uno de tus ambientes

Hemos estado hablando sobre la rama de flujo de trabajo, y puedes pensar en ella como la rama de ambiente de desarrollo. Esta es una buena idea mantener esta rama limpia, esto se logra creando ramas nuevas para arreglas problemáticas y arreglo de errores y solo mezclandolas cuando estén debidamente probadas, como se mencionó anteriormente. En otras palabras, tu rama de ambiente de desarrollo debe tener solamente código estable. Por esta razón llamaremos a esta rama 'estable' en lo que sigue de esta guía. 

### Usando ramas de producción y pruebas

Adicionalmente a tu ambiente de desarrollo, realmente tu quieres tener al menos otro ambiente: 'producción' donde nuestra aplicación está corriendo efectivamente. Teniendo una rama de ambiente de producción y haciendo que solo el código debidamente probado vaya a esta rama, asegura que siempre vas a tener una captura de lo que está ocurriendo en tu servidor en cualquier momento y una historia granular de lo que ha estado pasando en este servidor históricamente.

En la mayoría de los casos también tienes un ambiente de pruebas, donde tu equipo o clientes pueden verificar los cambios juntos. Tener una rama de ambiente de pruebas tiene los mismos beneficios que la rama de producción.

### Diferenciación de ramas para revisión de código y notas de lanzamiento.

Cuando tu ambiente de desarrollo ha sido actualizado con las características nuevas y arreglos de errores debidamente probados, puedes usar tu sistema de control de versiones para ver las diferencias entre tu rama 'estable' y tu rama 'pruebas' para ver que es lo que efectivamente se está desplegando. Esta es una excelente oportunidad para ver código de baja calidad o incompleto, para evitar que el código inestable sea desplegado. Esta diferenciación también puede ser de ayuda para tus notas de lanzamiento.

## Nunca mezcles a una rama de ambiente sin desplegar.

En orden de mantener tus ramas de ambientes sincronizadas con tus servidores de ambientes, es una excelente práctica unicamente realizar mezclas entre ramas de ambientes cuando se vaya a hacer un despliegue. Si completas una mezcla sin un despliegue, tu rama de ambiente estará fuera de sincronización con tu ambiente actual de producción o pruebas.

Con ramas de ambientes, nunca querrás realizar commits directamente a esta rama, solamente hacer mezclas de código entre las ramas 'estable' o 'pruebas'. Debes asegurarte que el flujo de cambios solamente vaya en una dirección, de desarrollo de características y arreglo de errores a ramas 'estable', luego a  'pruebas' y por último a 'producción'. Esto mantendrá tu histórico limpio y de nuevo te ayudará a estar seguro de que se está ejecutando en cada uno de los ambientes.

1. Desarrollando una nueva característica
  ![Desarrollando una nueva característica](http://guides.beanstalkapp.com/version-control/branching-best-practices/stage-1.png)
1. La característica fue probada exitosamente
  ![La característica fue probada exitosamente](http://guides.beanstalkapp.com/version-control/branching-best-practices/stage-2.png)
1. La característica es desplegada
  ![La característica es desplegada](http://guides.beanstalkapp.com/version-control/branching-best-practices/stage-3.png)

## Mejores prácticas para ramas de ambientes.

- Usa tu rama por defecto como tu rama 'estable'
- Crea una rama de ambiente para cada ambiente, incluyendo 'pruebas' y 'producción'
- Nunca mezcles a una rama de ambiente a menos que estés seguro que vas a desplegar a ese ambiente
- Ejecuta una diferenciación entre ramas antes de mezclarlas, esto puede prevenir mezclar algo que no estaba listo y también con las notas de lanzamiento
- Las mezclas deben fluir en una única dirección, primero de desarrollo de característica a pruebas, luego de pruebas a estable una vez esté probada y luego de pruebas a producción