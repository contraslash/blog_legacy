Title: Problemas con el mod_rewrite en VirtualHost
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: Apache
---
# Problemas con el mod_rewrite en VirtualHost


Si, es de novatos cometer este tipo de errores, pero hay que asegurarse que si el VirtualHost que tenemos habilitado, necesita mod_rewrite, o en general otro módulo, debemos autorizarlo en el site.conf

específicamente para mod_rewrite:
```
<directory>
   Options Indexes FollowSymLinks  
   AllowOverride All  
   Order allow,deny  
   allow from all
</directory>  
```
