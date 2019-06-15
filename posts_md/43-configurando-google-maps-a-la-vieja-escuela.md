Title: Configurando Google Maps a la vieja escuela
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: Android,Google Maps
---
# Configurando Google Maps a la vieja escuela

Primero necesitamos la firma de nuestro equipo, si estás en sistemas Xnix 
`keytool -list -v -keystore ~/.android/debug.keystore -alias androiddebugkey -storepass android -keypass android`

Si estás en Windows

`keytool -list -v -keystore "%USERPROFILE%\.android\debug.keystore" -alias androiddebugkey -storepass android -keypass android`

Tomado de la [la documentación de maps de google](https://developers.google.com/maps/documentation/android/signup)

luego vamos a [la consola para desarrolladores de google](https://console.developers.google.com/) y creamos un proyecto

Vamos a APIS y habilitamos Maps para Android

Luego vamos a credenciales y creamos una llave de acceso pública y seleccionamos Android,

Luego pegamos la firma SHA1 del primer comando separada con ; y luego el nombre del paquete que usamos 

Y eso es todo, generaremos una llave que luego podremos pegar como API_KEY en nuestro proyecto

