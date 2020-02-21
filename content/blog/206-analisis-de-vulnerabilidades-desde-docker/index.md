---
title: "Análisis de vulnerabilidades desde docker"
date: "2018-06-25T20:34:50+00:00"
description: "Análisis de vulnerabilidades de sitios web desde Docker, utilizando herramientas populares en el entorno de seguridad informática como WP Scan, Nikto"
tags: "Security,Docker"
---
# Análisis de vulnerabilidades desde docker

Definitivamente docker ofrece muchas ventajas a la hora de instalar paquetes de software, en esta ocación listaré un conjunto de imágenes las cuales pueden dar una idea de que tan seguro está nuestro sitio web considerando algunas tecnologías específicas.

## WP Scan

```bash
docker pull wpscanteam/wpscan
docker run -it --rm wpscanteam/wpscan -u http://dominio.com
```

## Nikto
```bash
docker pull frapsoft/nikto
docker run frapsoft/nikto -host https://dominio.com
```

