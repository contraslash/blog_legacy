Title: Eliminar Proceso netbiosd
Date: 2016-11-23T21:23:22+00:00
Description: Optimizar tráfico de red en OSX deteniendo el demonio netbiosd
Tags: OSX
---
# Eliminar Proceso netbiosd

Desde hace días notaba que mi ancho de banda estaba siendo altamente reducido en mi laptop, pero se mantenía en mis otros dispositivos, analizando el tráfico de red, encontré un proceso ejecutándose en background saturando mi tarjeta de red con millones de paquetes transmitidos, y es un demonio pegajoso `netbiosd`

Investigando un poco descubrí que se trata de un servicio utilizado por finder para compartir carpetas cons sistemas de ficheros windows, similares al servicio SMB.

Para desactivarlo, basta detener el servicio
```bash
sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.netbiosd.plist

```