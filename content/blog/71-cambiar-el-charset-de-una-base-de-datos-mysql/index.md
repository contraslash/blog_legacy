---
title: "Cambiar el charset de una base de datos MySQL"
date: "2016-01-29T06:42:23+00:00"
description: ""
tags: "MySQL"
---
# Cambiar el charset de una base de datos MySQL

Para cambiar toda la base de datos
```
alter database  DATABASE_NAME character set latin1 collate latin1_swedish_ci;
```

Para cambiar cada tabla
```
SELECT CONCAT(  "ALTER TABLE ", TABLE_NAME,  " CONVERT TO CHARACTER SET latin1 COLLATE latin1_swedish_ci;" ) AS ExecuteTheString FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA =  "DATABASE_NAME"
```
Y luego ejecutar el resultado como código SQL


