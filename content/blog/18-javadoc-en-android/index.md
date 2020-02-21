---
title: "JavaDoc en Android"
date: "2016-01-29T06:42:23+00:00"
description: ""
tags: ""
---
# JavaDoc en Android

En algunas ocasiones deseamos genera un javadoc con nuestro proyecto en Android, pero como somos hispano hablantes, el JavaDoc generado queda bastante feo, por este asunto de los caracteres diatónicos y las ñ.

La solución es agregar estos parámetros

`-encoding UTF-8 -charset UTF-8 -docencoding UTF-8 `

Claro, como es un proyecto android, Java no conoce el paquete android.*

así que un parámetro de mas no estaría mal

`-bootclasspath /Users/libardocollazos/Developer/sdk/platforms/android-19/android.jar`

Y con eso es suficiente para generar un buen JavaDoc :3



