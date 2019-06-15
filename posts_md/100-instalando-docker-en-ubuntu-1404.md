Title: Instalando Docker en Ubuntu 14.04
Date: 2016-09-03T01:52:11+00:00
Description: 
Tags: Ubuntu,Docker
---
# Instalando Docker en Ubuntu 14.04

Basado en [este post](http://www.liquidweb.com/kb/how-to-install-docker-on-ubuntu-14-04-lts/)

```
sudo apt-get update
sudo apt-get install docker.io
ln -sf /usr/bin/docker.io /usr/local/bin/docker
service docker restart
update-rc.d docker defaults
```