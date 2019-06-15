Title: Permisos para Wordpress
Date: 2017-03-10T00:43:58+00:00
Description: Permisos para Wordpress
Tags: Wordpress
---
# Permisos para Wordpress

Los permisos apropiados para que wordpress se auto instale son

```
chown www-data:www-data  -R * # Let Apache be owner
find . -type d -exec chmod 755 {} \;  # Change directory permissions rwxr-xr-x
find . -type f -exec chmod 644 {} \;  # Change file permissions rw-r--r--
```