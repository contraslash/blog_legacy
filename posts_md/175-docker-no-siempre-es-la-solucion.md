Title: Docker no siempre es la solución
Date: 2017-06-23T04:34:57+00:00
Description: Docker no siempre es la solución, algunos pensamientos sobre cuando es conveniente y cuando no usar la containerización
Tags: Posts
---
# Docker no siempre es la solución

Desde hace años me picó el bicho de la curiosidad con el asunto de los contenedores, pero no fue sino hasta hace 6 meses cuando decidí cambiar toda mi infraestructura a swarm, pues consideré que debía entrar en la onda.

Luego de algún tiempo explorando opciones, decidí irme por un cluster con Docker Swarm con un Traefik para un proxy inverso, 1 maestro, 2 trabajadores y una instancia dedicada para servir las bases de datos.

El asunto se fue volviendo grande porque además de cambiar de arquitectura, que de entrada ya era un super trabajo, también cambié de proveedor de nube, lo cual en principio era buena idea pues no contaminaba mis servidores anteriores con nuevas tecnologías y además podía manejar una migración suave y escalonada servicio a servicio cuando estuviera seguro de cada uno.

Para contextualizar un poco, lo que tenía que migrar, entre otras cosas era:

- Servidor de archivos estáticos
- Servidor de Wordpress (con múltiples wordpress)
- Servidor de Git
- Servidor de monitoreo
- Múltiples aplicaciones en django

El servidor de archivos estáticos, junto con los wordpress fue casi que un juego de niños, pues las imágenes de caddy y nginx con wordpress abundan y están super documentadas, lastimosamente no fue lo mismo con el servidor de git y el de monitoreo, y mucho menos con las aplicaciones en django.

No es un secreto que vivo enamorado de gogs y de sentry, pero existen ciertos detalles en la implementación de cada uno que hacen su utilización en un swarm muy complicada, al punto de decir que es casi imposible.

Con Gogs, existen ciertos detalles con el emparejamiento de la dirección ip donde se sirve el servicio y la que está registrada en el archivo de configuración, y como en un swarm los servicios se mueven caóticamente de nodo a nodo, la intermitencia del servicio me hizo montar si bien gogs en un contenedor, pero fuera del swarm.

Diferente historia con Sentry, que es una aplicación muchísmo mas robusta con muchas dependencias y por ende mas pesada.

En un mundo donde entre mas pequeño mejor, así no lo crean, tener 3 instancias identicas, cada una de 600MB una para servidor web, otra para un worker y otra para un cron no es para nada una buena idea, y si me dicen que no hay problema porque las capas se repiten, recuerden que al estar en un swarm multinodo muy posiblemente cada imagen viva en un servidor distinto. Y eso sin mencionar que Sentry requiere la creación manual del super administrador por consola, lo cual sugiere que hay que hacer un pequeño truco un poco feo para pegarse a la entrada estándar de la consola e insertar los datos.

Por último y de lo que si no me quejo es el proceso para migrar mis aplicaciones a una arquitectura contenedorizada, porque gracias a drone, el despliegue automático e integración continua funcionan de maravilla, bueno, eso mientras tu imagen pesa menos de 1GB y el tiempo de despliegue es relativamente corto.

Y si, lo menciono porque a pesar de que no me siento muy orgulloso, en la última semana tuve una imagen de docker que pesaba cerca de 1.7GB y ya se imaginarán los problemas innecesarios de tener una imagen tan pesada.

Recapitulando un poco sobre la experiencia:

- Docker es una excelente opción para mantener procesos aislados.
- Si tu servicio requiere que tengas una dirección ip estática, piensalo dos veces antes de meterlo a tu swarm
- Si tu imagen ya se puso pesada, y con eso me refiero a mas de 500MB considera como puedes reducir el tamaño de los segmentos o si en realidad vale la pena tenerla cono contenedor
- A pesar de que funcione de maravilla wordpress en un contenedor, para un servidor multi wordpress, donde toda la información queda en base de datos y archivos persistentes, es mas eficiente manejar virtualhost que contenedores separador
- No pierdas la paciencia y no te empeñes en contenedorizar todo, si está siendo mas complicada la solución con contenedores y no revela una ganancia a corto o mediano plazo, considera tener tus servicios stand alone