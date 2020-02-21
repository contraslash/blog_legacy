---
title: "Visualizar errores en PHP"
date: "2016-01-29T06:42:23+00:00"
description: ""
tags: "PHP"
---
# Visualizar errores en PHP


Para ver lo que sale en el error.log
```
    ini_set(‘display_startup_errors’,1);  
    ini_set(‘display_errors’,1);  
    error_reporting(-1);
```
Si trabajo con PDO
```
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_WARNING);
```



