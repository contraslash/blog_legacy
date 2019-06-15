Title: Instalando wpscan en Ubuntu 14.04
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: Seguridad
---
# Instalando wpscan en Ubuntu 14.04

Primero necesitas instalar algunas dependencias
`sudo apt-get install ruby-dev libxslt1-dev libxml2-dev libcurl4-gnutls-dev`

Ahora [clona](https://github.com/wpscanteam/wpscan)  o [descarga](http://wpscan.org/) wpscan 

Descomprime la carpeta

Entra en la carpeta y

```
sudo gem install bundler
sudo bundle install
```

Disgruta

`ruby wpscan http://wordpress.site.domain`

Basado en  [este](https://hackertarget.com/wpscan-install-ubuntu/) post