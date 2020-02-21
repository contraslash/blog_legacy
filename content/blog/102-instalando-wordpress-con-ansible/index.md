---
title: "Instalando Wordpress con Ansible y Ubuntu 16.04"
date: "2016-09-04T04:29:21+00:00"
description: ""
tags: "Aprovisionamiento,Ansible,Wordpress"
---
# Instalando Wordpress con Ansible y Ubuntu 16.04

Este tutorial está basado en [este tutorial](https://www.digitalocean.com/community/tutorials/how-to-automate-installing-wordpress-on-ubuntu-14-04-using-ansible) de Digital Ocean

Como pre requisito está tener instalado Ansible

Primero adecuamos el sistema de carpetas
```
mkdir wordpress
cd wordpress
touch hosts
touch playbook.yml
mkdir roles
cd roles
```

Después inicializamos los roles que usaremos

```
ansible-galaxy init apache2
ansible-galaxy init mysql
ansible-galaxy init php
ansible-galaxy init wordpress
```

Ahora, definimos las tareas para apache dos

en *roles/apache2/tasks/main.yml* escribimos
```
---
- name: Update apt cache
  apt: update_cache=yes cache_valid_time=3600
  sudo: yes

- name: Install required software
  apt: name={{ item }} state=present
  sudo: yes
  with_items:
    - apache2
```

en *roles/mysql/tasks/main.yml* escribimos
```
---
- name: Update apt cache
  apt: update_cache=yes cache_valid_time=3600
  sudo: yes

- name: Install required software
  apt: name={{ item }} state=present
  sudo: yes
  with_items:
    - mysql-server
    - python-mysqldb
     - libmysqlclient-dev
- name: Create mysql database
  mysql_db: name={{ wp_mysql_db }} state=present

- name: Create mysql user
  mysql_user: 
    name={{ wp_mysql_user }} 
    password={{ wp_mysql_password }} 
    priv={{ wp_mysql_db }}.*:ALL
```


Con esto se instalará Mysql Server y se creará una base de datos con los nombres definidos en *roles/mysql/vars/main.yml*

Un ejemplo del archivo *roles/mysql/vars/main.yml*

```
---
wp_mysql_db: wordpress
wp_mysql_user: wordpress
wp_mysql_password: $upp3rP4$$
```

en *roles/php/tasks/main.yml* escribimos
```
---
- name: Update apt cache
  apt: update_cache=yes cache_valid_time=3600
  sudo: yes

- name: Install required software
  apt: name={{ item }} state=present
  sudo: yes
  with_items:
    - php7.0-mysql
    - php7.0
    - libapache2-mod-php7.0
    - php7.0-mcrypt
    - python-mysqldb
```

en *roles/wordpress/tasks/main.yml*
```
---
---
# tasks file for wordpress
- name: Download WordPress  
  get_url: 
      url=https://wordpress.org/latest.tar.gz 
      dest=/tmp/wordpress.tar.gz
      validate_certs=no

- name: Extract WordPress  
  unarchive: src=/tmp/wordpress.tar.gz dest=/var/www/html/{{ wordpress_site_name }} copy=no
  sudo: yes

- name: Update default Apache site
  sudo: yes
  template: src=wordpress.conf dest="/etc/apache2/sites-aviable/{{SITE_NAME}}.conf"

- name: Copy sample config file
  command: mv /var/www/html/{{ wordpress_site_name }}/wp-config-sample.php /var/www/html/{{ wordpress_site_name }}/wp-config.php creates=/var/www/html/{{ wordpress_site_name }}/wp-config.php
  sudo: yes

- name: Update WordPress config file
  lineinfile:
    dest=/var/www/html/{{ wordpress_site_name }}/wp-config.php
    regexp="{{ item.regexp }}"
    line="{{ item.line }}"
  with_items:
    - {'regexp': "define\\('DB_NAME', '(.)+'\\);", 'line': "define('DB_NAME', '{{wp_mysql_db}}');"}        
    - {'regexp': "define\\('DB_USER', '(.)+'\\);", 'line': "define('DB_USER', '{{wp_mysql_user}}');"}        
    - {'regexp': "define\\('DB_PASSWORD', '(.)+'\\);", 'line': "define('DB_PASSWORD', '{{wp_mysql_password}}');"}
  sudo: yes
```

Como estamos creando un notify para reiniciar apache, debemos añadir esto a *roles/wordpress/handlers/main.yml*
```
---
- name: restart apache
  service: name=apache2 state=restarted
  sudo: yes
```


Apache necesita un archivo de configuración, así que lo incluiremos, usando este template que colocaremos en *roles/wordpress/templates/wordpress.conf*
```
<VirtualHost *:80>

    ServerName {{ wordpress_site_name }}
    ServerAdmin ma0@contraslash.com
    DocumentRoot /var/www/html/{{ wordpress_site_name }}

    <Directory /var/www/html/{{ wordpress_site_name }}/>
        Options -Indexes
            AllowOverride None
            Order allow,deny
            allow from all

        </Directory>

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

También necesitamos algunas variables para que se rendericen en los archivos de configuración de apache, así que escribirmos en *roles/wordpress/vars/main.yml*

```
---
wp_mysql_db: wordpress
wp_mysql_user: wordpress
wp_mysql_password: $upp3rP4$$
wordpress_site_name: wordpress.example.com
```

> Asegúrese de que las contraseñas de este archivo coincidan con las del rol de mysql

Para terminar, modificaremos los archivos creados al inicio del tutorial.

En *hosts*
```
[webserver]
webserver.example.com

[dbserver]
dbserver.example.com
```

> En este archivo puede colocar las direcciones ip de sus servidores web y de bases de datos, recuerde que pueden ser el mismo

y en *playbook.yml*
```
- hosts: webserver

  roles:
    - server
    - php
    - wordpress

- hosts: dbserver

  roles:
    - mysql
```

Por último para aprovisionar nuestros servidores ejecutamos el siguiente comando

```
ansible-playbook -i hosts -u nombreUsuario -s -k playbook.yml 
```

> Recuerde modificar el nombreUsuario en el comando anterior

