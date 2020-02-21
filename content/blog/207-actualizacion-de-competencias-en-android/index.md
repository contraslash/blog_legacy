---
title: "Actualización de competencias en Android"
date: "2018-09-30T22:51:46+00:00"
description: "Un compendio de enlaces útiles a la documentación oficial de Android, como han cambiado en los últimos dos años y un índice de enlaces importantes"
tags: "Android"
---
# Actualización de competencias en Android

Diría que han pasado cerca de 6 años desde que inicié el desarrollo de aplicaciones móviles para Android, por esos días recuerdo que se veía todavía muchos dispositivos con android 2.3 Jelly Bean, y Ice Cream apenas estaba de moda, la migración hacia los fragmentos aún era lenta y definitivamente la documentación no estaba como estaba hoy.

Recuerdo que en mi búsqueda de literatura para el aprendizaje, después de depurar bastante encontré un libro muy apropiado llamado [Professional Android](http://www.wrox.com/WileyCDA/WroxTitle/Professional-Android-4th-Edition.productCd-1118949528.html) en su cuarta edición. y era el mejor por mucho.

Con el tiempo desarrollas tus propias herramientas, te metes de cabeza en tus proyectos, los migras cuando sea necesario y te actualizas regularmente con cada major release, android 5 con ART, android 6 con el manejo de permisos y para ser sincero, mi vida me llevó a enfocarme en infraestructura, operaciones y desarrollo backend.

Claro, Android no va a cambiar sus componentes arquitecturales, y las actividades de hace 6 años siguen teniendo el mismo ciclo de vida, los fragmentos tampoco han cambiado mucho, pero asistiendo al [DevFest 2018](https://devfest.gdgcali.com/) en la ciudad de cali, noté que en la documentación mucho había cambiado desde la última vez.

No puedo citar con precisión la última vez que visité la documentación oficial de Android, pero recuerdo que [CodeLabs](https://codelabs.developers.google.com/) estaba en beta, y algo estaba probando de [PWA](https://developers.google.com/web/progressive-web-apps/), en fin, me suena muy 2017 y este super boom con el Google IO, el lanzamiento de [LighSail](https://developers.google.com/web/tools/lighthouse/?hl=es) y bueno, así que supongo que fue hace un año un tanto largo.

Así que el objetivo de este tiempo dedicado para mi y mi desarrollo de nuevas competencias en nuevas librerías de Google va a quedar aquí como un índice de referencia para cuando deba volver a hacer una app nativa en Android y necesite saber donde llegar.

- [Code Fundamentals](https://developer.android.com/guide/components/fundamentals): Debo decir que realmente no sabía que había un usuario para cada app, lo cual no se si es nuevo o sencillamente jamás lo había leído, pero es super útil saberlo. Por lo general, todo sigue igual: Activities, Intents, Services, Broadcast Recievers, Content Providers, todo estándar.

- [Resources](https://developer.android.com/guide/topics/resources/providing-resources): Por mas que odie que no pueda tener un nivel de organización mas profundo en los recursos, los recursos siguen almacenandose en una piscina gigante en las carpetas tradicionales: color, drawable, mipmap, layout, menu, raw, values. Todo lo tradicioan.

- [Manifest](https://developer.android.com/guide/topics/manifest/manifest-intro): Esto creo que no cambiará mucho, ni para kotlin, así que mejor ni exploro todos los posibles nodos.

- [Permissions](https://developer.android.com/guide/topics/permissions/overview): Esto creo que ya dejó de ser nuevo, porque Android 6 creo que ya hace parte de todo el legacy de android, pero en principio, esa adaptación a solicitar los permisos solo cuando se usan es algo de facto para targets sdk como desde el 23, pero puedo estar equivocado. Diré que está igual.

- [Devices](https://developer.android.com/guide/practices/compatibility): Tengo una deuda técnica, porque nunca he hecho una app ni para [wear](https://developer.android.com/training/wearables/) ni para [TV](https://developer.android.com/training/tv/), y bueno, por extensión [Auto](https://developer.android.com/training/auto/) tampoco, en parte porque no tengo el hardware para probar, pero se que si en algún momento debo saldar a deuda, por aquí debo iniciar por aquí.

    Disclaimer: La parte de devices viene con dos puntos adicionales: 
    - [Things](https://developer.android.com/things/get-started/)
    - [Chrome OS](https://developer.android.com/chrome-os/intro)

    Pero, mi experiencia con things no fue muy apreciada, y la alternativa, al menos para los casos de uso que he manejado los manejo con [RPI](https://www.raspberrypi.org/) y [Raspbian](https://www.raspberrypi.org/downloads/raspbian/), así que mas que cubierto, con respecto a Chrome OS, pues, para mi siguen siendo PWAs así que no les prestaré mucha atención.

Ahora si pasemos al contenido denso:

- [Activities](https://developer.android.com/guide/components/activities/intro-activities): Como decía antes, esto dudo que cambie, lo que si veo ahora es que se hace mucho énfasis a presentar [Kotlin](https://kotlinlang.org/) como primera opción, creo que va en parte con la idea de Google de soltar [Java](https://www.java.com/es/download/), así que Kotlin va a ser el lugar para comenzar esta actualización.

- [Fragments](https://developer.android.com/guide/components/fragments): Same old things, aunque creo que ya por fin nos podemos librar del appcompat 4 y 7, lo cual es en serio un alivio para mi, por todos los problemas que me causó en el pasado.

- [JetPack](https://developer.android.com/jetpack/): Este es el punto donde debo parar de hacer el review y hacer mi primera app, por lo que se observa existen varios conceptos importantes:

    - [AndroidX](https://developer.android.com/topic/libraries/support-library/androidx-overview)
    - [Lifecycle Aware Components](https://developer.android.com/topic/libraries/architecture/lifecycle)
    - [LiveData](https://developer.android.com/topic/libraries/architecture/livedata)
    - [ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel)
    - [Room](https://developer.android.com/topic/libraries/architecture/room)

Creo que mas allá todo parece ser lo estándar, pero veo que ahora con estos 5 componentes voy a encontrarme de nuevo en el Bleeding Edge de Android, y por lo que veo, va a existir una migración masiva a componentes reactivos.

Mas adelante posiblemente explore cada una de estas temáticas independientes, tal vez para ser publicadas en mi [blog de medium](https://medium.com/@ma0collazos), pero por ahora creo que será tiempo de poner manos al código

