Title: Crear proyecto de Android desde consola
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: Android
---
# Crear proyecto de Android desde consola
Pero por supuesto que es posible crear un proyecto de android desde consola, primero debemos definir algunas variables de entorno

 `ANDROID_HOME=/ruta/al/android/sdk`
 
 regularmente el sdk, se coloca en `/home/nombredeusuario/Android/Sdk`
claro, esto en Ubuntu, recuerden que soy linux fan boy, en windows queda como en `C:\Users\nombredeusuario\Local\AppData\Android\SDK` o algo asi, en mac queda en una posición similar a la de Ubuntu</nombre></tu>

ahora debemos añadir estas al PATH
`export PATH=${PATH}:/ruta/al/sdk/tools:/ruta/al/sdk/platform-tools` 

esto en Linux y mac, en windows es algo como set `PATH=%PATH%;Ruta\al\SDK\tools;Ruta\al\SDK\platform-tools`

para corroborar escriban “android” en la terminal y eso debería abrirles el sdk manager

Debemos tener Java instalado, y la variable de entorno JAVA_HOME en el ambiente

`JAVA_HOME=/ruta/al/jdk/java`

En instalaciones convencionales, Java queda instalado en  `/usr/lib/jvm/jdk*.*/` en Windows y Mac quedan listas, regularmente

Ya con eso puede ejecutar algo como esto

`android create project –target android-19 –name test –package me.ma0c.consoletest –path /ruta/donde/se/alojara/el/proyecto/ –activity MainActivity`

IMPORTANTE: los targets deben tenerlos instalados, y saben como se llaman ejecutando

`android list targets`

Si quieren instalar uno nuevo, bastan con abrir el sdk manager (ejecutar android) e instalar el sdk correspondiente al api, claro pueden instalar las imágenes para los emuladores, y los docs y todo cuanto quieran ![:D](http://ma0c.me/wp-includes/images/smilies/icon_biggrin.gif)

Por defecto android compila usando ant (es triste lo sé, y mas si uno se está trabajando en windows :S) así que debe instalarse, una guia que me funcionó una vez que intentaba instalar en windows fue esta

http://dita-ot.sourceforge.net/doc/ot-userguide13/xhtml/installing/windows_installingant.html, pero pueden utilizar la que les sirva

y ya con esto listo, pueden ejecutar

`ant debug`

y et voila

queda simplemente actualizar el proyecto con android

`update project –target “tu target” –path “ruta al proyecto”`

y luego usamos adb para instalarlo en nuestro dispositivo  

`adb install /ruta/al/proyecto/bin/test-debug.apk`

el nombre del apk puede variar

y ya pueden ejecutarlo en su telefono


