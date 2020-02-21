---
title: "Cambiar de Dominio en Wordpress"
date: "2017-09-18T21:58:13+00:00"
description: "Cambiar de nombre de dominio en un sitio en Wordpress alojado sobre Apache2"
tags: "Wordpress"
---
# Cambiar de Dominio en Wordpress

Además de lo obvio, y con obvio me refiero a cambiar el Virtual Host también necesitaremos actualizar nuestra base de datos

```
UPDATE wp_options SET option_value = replace(option_value, 'http://54.214.66.247', 'http://54.191.241.251') WHERE option_name = 'home' OR option_name = 'siteurl';

UPDATE wp_posts SET guid = replace(guid, 'http://54.214.66.247','http://54.191.241.251');

UPDATE wp_posts SET post_content = replace(post_content, 'http://54.214.66.247', 'http://54.191.241.251');

UPDATE wp_postmeta SET meta_value = replace(meta_value,'http://54.214.66.247','http://54.191.241.251');
```

