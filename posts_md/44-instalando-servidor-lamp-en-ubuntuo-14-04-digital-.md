Title: Instalando servidor LAMP en Ubuntu
Date: 2016-01-29T06:42:23+00:00
Description: Instalación de un servidor LAMP en ubuntu, compatible con las imágenes standard de Digital Ocean y Linode. Ideal para instalación de wordpress
Tags: Linux,Ubuntu,Digital Ocean,Linode
---
# Instalando servidor LAMP en Ubuntu

Ubuntu 14.04

```
sudo apt-get update
sudo apt-get install apache2
sudo apt-get install mysql-server libapache2-mod-auth-mysql php5-mysql
sudo apt-get install php5 libapache2-mod-php5 php5-mcrypt
sudo apt-get install phpmyadmin
```


Para ubuntu 16.04

```
sudo apt update
sudo apt-get install apache2
sudo apt-get install mysql-server 
sudo apt install php7.0 php7.0-mysql libapache2-mod-php7.0 php7.0-cli php7.0-cgi php7.0-gd 
```