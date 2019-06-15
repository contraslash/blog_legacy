Title: Habilitando la visualización de errores en dispositivos Huawei
Date: 2016-09-15T03:24:09+00:00
Description: Habilitar la visualización del LOGCAT para dispositivos Huawei con Sistema Operativo Android
Tags: Android,Huawei
---
# Habilitando la visualización de errores en dispositivos Huawei

Después de batallar por horas con errores que habían desaparecido de mi `logcat`, solucionarlos debuggeando a ojo vivo, y luego gastarle mas horas a entender porqué mi código fuente no mostraba los errores, me encontré con esta belleza.

Al parecer, por asuntos de seguridad, Huawei deshabilita las impresiones del log, existe un menú oculto para habilitarlas

Basta con marcar el siguiente `número` 

```
*#*#2846579#*#*
```

Y se nos aparecerá un menú oculto.

En `ProjectMenu/BackgrounSetttins/Log setting ` podremos habilitar el log de nuestro dispositivo