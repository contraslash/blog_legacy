Title: Content Security Policy en iOS con ionic
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: iOS,ionic
---
# Content Security Policy en iOS con ionic

Desde la salida de cordova 5.0, el trabajo conectándose a URLs externas es todo un fastidio, sugieren bajar el plugin de [whitelist](https://github.com/apache/cordova-plugin-whitelist) y configurarlo como se sugiere en el *readme.md*, pero vaya sorpresa, a mi no me funcionó.

En primera instancia voy a mencionar varios asuntos importantes que pueden salvarle la vida o no a un desarrollador con este problema.

En el documentroot de nuestro proyecto ionic se encuentran varios archivos importantes, entre ellos la carpeta www y el archivo config.xml.

Cada plataforma tiene su copia local de estos archivos y **NO SE COPIAN AUTOMÁTICAMENTE** en cada compilación. 

Esto que quiere decir, que los cambios los debemos realizar en el archivo local de cada plataforma para ver resultados cuando se compile. O usar un script que copie las últimas versiones de los archivos en el documentroot.

Con esto en mente, efectuar los cambios pertinentes en el archivo local config.xml de cada plataforma y recompilar podría solucionar problemas.

Pero no, específicamente con iOS tuve que meter un poco de machete :D

Estas líneas me salvaron la vida, y pueden hacerlo contigo.

En el archivo `{{DOCUMENT_ROOT}}/platforms/ios/{{PROJECT_NAME}}/Resources/{{PROJECT_NAME}}-Info.plist` añadí la siguiente regla
```
<key>NSAppTransportSecurity</key>
<dict>
  <!--Include to allow all connections (DANGER)-->
  <key>NSAllowsArbitraryLoads</key>
      <true/>
</dict>
```

Bueno, no precisamente esa regla, pero inicialmente solucionó mis problemas.

La solución la encontré en [este post](http://stackoverflow.com/questions/31254725/transport-security-has-blocked-a-cleartext-http) y ahí hay un ejemplo más claro de como ingresar dominios mas específicos.