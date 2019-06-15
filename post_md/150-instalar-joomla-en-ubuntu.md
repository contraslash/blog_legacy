Title: Instalar Joomla en Ubuntu
Date: 2017-03-02T00:07:31+00:00
Description: Instalación de Joomla en un servidor Ubuntu 16.04 usando VirtualHost de Apache
Tags: Apache,Ubuntu,Joomla
---
# Instalar Joomla en UbuntuPrimero se redirecciona el dominio @ a la dirección IP del servidor, para esto se ingresa a Godaddy, se selecciona el dominio y se le da Administrar DNS. Luego se edita el registro tipo A de nombre @ para que apunte al servidor y se guarda. 

Para configurar el servidor se ingresa por SSH al servidor y se ejecutan los siguientes comandos
```bash
# Se inicia como usuario postgres para crear los usuarios del joomla
sudo -i -u postgres
# Ingresamos a la consola interactiva de postgres
psql
```
A continuación en la consola interactiva debemos realizar lo siguiente:

```sql
--Crear una base de datos
create  database joomladb2;
--Crear un usuario para que se conecte a esta base de datos
create user joomla2 with password 'j00ml4';
--Darle todos los privilegios al usuario recien creado en la base de datos
grant all privileges on database joomladb2 to joomla2;
--Salir de la consola interactiva de postgres
\q
```
Luego en nuestra consola bash
```bash
# Cerramos la sesión del usuario postgres
exit
# Ingresamos a la carpeta de apache
cd /var/www/html/
# Descargamos Joomla
wget -O joomla_3-6-4-stable-full_package.zip https://downloads.joomla.org/cms/joomla3/3-6-4/joomla_3-6-4-stable-full_package-zip
# Creamos una carpeta para el nuevo joomla
mkdir joomla2
# Descomprimimos el archivo en la carpeta creada
unzip joomla_3-6-4-stable-full_package.zip -d joomla2/
# Entramos a la carpeta de host virtuales de apache2
cd /etc/apache2/sites-available/
# Creamos un archivo de configuración para el nuevo sitio, se recomienda que el nombre del archivo de configuracion sea el nombre de dominio seguido por el sufijo .conf, pero no es una camisa de fuerza
nano example.com.conf
```
Se coloca la siguiente información en el archivo. Recuerde que es importante que DocumentRoot apunte a la carpeta con el joomla descomprimido y que ServerName sea el nombre de su dominio
```
<VirtualHost *:80>
        ServerAdmin admin@example.com
        DocumentRoot /var/www/html/joomla2
        ServerName example.com

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
Para salir del editor nano presione cntrl + x, se le preguntará si desea guardar los cambios, presione y y luego enter.

Continuaremos con nuestros comando en bash
```
# Para habilitar el sitio ejecute el siguiente comando
a2ensite example.com.conf
# Recargue las configuraciones de apache
service apache2 reload
```
Ya puede visitar el sitio y seguir el wizard de configuracion

> Es importante recordar colocar el driver de PHP de conexión a la base de datos para que sea Postgres, dado que por defecto aparece para MySQL


Al finalizar la instalación se pide colocar la información del archivo de configuracion en la raiz del sitio, para esto ejecutamos en nuestra consola bash:

```
# Abrimos la carpeta de joomla
cd /var/www/html/joomla2/
# Creamos un archivo de configuracion llamado configuration.php
nano configuration.php
```
Se pega el contenido y se guarda
```
# Luego se Elimina la carpeta de instalación
rm -rf installation/

```