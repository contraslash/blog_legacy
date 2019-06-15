Title: Automatizar despliegues de Django con Fabric y Ansible
Date: 2017-02-02T14:29:16+00:00
Description: Automatizar despliegues de Django con Fabric y Ansible
Tags: Django,Ansible,Continuous Integration,Automatic Deployment
---
# Automatizar despliegues de Django con Fabric y AnsibleEste post está basado en el post de [Real Python](https://realpython.com) [Automating Django Deployments With Fabric and Ansible](https://realpython.com/blog/python/automating-django-deployments-with-fabric-and-ansible/)

En este tutorial automatizaremos el proceso de despliegue con Fabric (v1.12.0) y Ansible (v2.1.13) apuntando a estas problemáticas:

1. Escalamiento: Cuando se trata de escalar una aplicaión web para manejar miles de peticiones diarias, un solo servidor no es una buena aproximación. Puesto simple, cuando el servidor se aproxima al máximo uso de CPU, se pueden causar tiempos de carga lentos, que eventualmente llevan al servidor a un fallo. Para solucionar esto, la aplicación debe escalar para ejecutarse en mas de un servidor, entonces los servidores pueden manejar *acumulativamente* mas peticiones concurrentes.
1. Redundancia: Desplegar una aplicaión manualmente en un nuevo servidor implica un montón de trabajo repetido, con muchas probabilidades de un herror humano. Automatizar este proceso es clave.

Específicamente automatizaremos:

1. Agregar un usuario nuevo no root
1. Configurar el servidor
1. Halar el código desde un repositorio en Github
1. Instalar las dependencias
1. Usar la aplicación como un servicio.

## Configuración
Comencemos por crear una nueva instancia de servidor Fedora 25, automáticamente vamos a utilizar una llave SSH con un script de Fabric. Como el proceso de escalamiento debe ser escalable, vamos a crear un repositorio separado para almacenar todos los scripts de aprovisionamiento. Vamos a crear un nuevo directorio local, y vamos a crear y activar un ambiente virtual usando Python 2.7

> Fabric no soporta python 3, por eso usamos python 2.7, pero no te preocupes, usaremos python 3.5 cuando aprovisionemos nuestro servidor.

```
mkdir automated-deployments
cd automated-deployments
virtualenv env
source env/bin/activate
```

## Configuración de Fabric

Fabric es una herramienta para automatizar rutinas de consola sobre SSH, y lo usaremos para:

1. Configurar las llaves SSH
1. Asegurar las contraseñas
1. Instalar las dependencias de Ansible
1. Actualizar el servidor.

Comencemos por instalar Fabric
```
pip install fabric==1.12.0
```

Creemos una nueva carpeta llamada "prod" y agreguemos un nuevo archivo llamado fabfile.py para tener todos los scripts de Fabric

*prod/fabfile.py*
```
import os
from fabric.contrib.files import sed
from fabric.api import env, local, run
from fabric.api import env

# Inicializar el directorio base
abs_dir_path = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))


# Declara las variables de entorno globales

# Usuario root
env.user = 'root'

# Lista de las direcciones IP remotas
env.hosts = ['<remote-server-ip>']

# Contraseña del servidor remoto
env.password = '<remote-server-password>'

# Nombre completo del usuario
env.full_name_user = '<your-name>'

# Grupo del usuario
env.user_group = 'deployers'

# Usuario de el grupo anterior
env.user_name = 'deployer'

# Ruta a la llave SSH
env.ssh_keys_dir = os.path.join(abs_dir_path, 'ssh-keys')
```

Toma nota de los comentarios. Y asegúrate de agregar los datos correctos en las variables de `env`

## Configurar las llaves SSH

Agrega el siguiente código al fabfile.py
```
def start_provision():
    """
    Comenzar el aprovisionamiento del servidor
    """
    # Crear un nuevo directorio para el nuevo servidor remoto
    env.ssh_keys_name = os.path.join(
        env.ssh_keys_dir, env.host_string + '_prod_key')
    local('ssh-keygen -t rsa -b 2048 -f {0}'.format(env.ssh_keys_name))
    local('cp {0} {1}/authorized_keys'.format(
        env.ssh_keys_name + '.pub', env.ssh_keys_dir))
    # Prevenir que el root pueda conectarse remotamente desde un cliente SSH
    sed('/etc/ssh/sshd_config', '^UsePAM yes', 'UsePAM no')
    sed('/etc/ssh/sshd_config', '^PermitRootLogin yes',
        'PermitRootLogin no')
    sed('/etc/ssh/sshd_config', '^#PasswordAuthentication yes',
        'PasswordAuthentication no')

    install_ansible_dependencies()
    create_deployer_group()
    create_deployer_user()
    upload_keys()
    set_selinux_permissive()
    run('service sshd reload')
    upgrade_server()
```

Esta función actua como el punto de entrada para el Script de Fabric. Lanza una serioe de otras funciones que van a ser explicadas en otros pasos, explicitamente:

1. Genera un nuevo par de llaves SSH en una ruta especificada en el sistema local
1. Copia el contenido de la llave pública al archivo *authorized_keys*
1. Realiza los cambios al archivo remoto *sshd_config* para prevenir el ingreso del root y deshabilitar el ingreso sin contraseña

> Prevenir el acceso del usuario root por SSH es un paso opcional, pero es recomendado porque asegura que ningún ingreso tenga permisos de superusuario

Cree un directorio para tus claves ssh en la raiz del proyecto.

## Asegurar las contraseñas de los usuarios
Este paso incluye la adición de tres funciones diferentes, cada una se ejecuta en serie, para configurar el aseguramiento de las contraseñas

**Crear un grupo para despliegues**
```
def create_deployer_group():
    """
    Crea un grupo de usuarios para todos los desarrolladores del proyecto
    """
    run('groupadd {}'.format(env.user_group))
    run('mv /etc/sudoers /etc/sudoers-backup')
    run('(cat /etc/sudoers-backup; echo "%' +
        env.user_group + ' ALL=(ALL) ALL") > /etc/sudoers')
    run('chmod 440 /etc/sudoers')
```

Aquí se crea un nuevo grupo llamado `deployers` y se le habilita permisos de super administrador, así que los usuarios pueden realizar procesos con privilegios de superadministradores

**Crear usuario**
```
def create_deployer_user():
    """
    Crear un usuario para el grupo
    """
    run('adduser -c "{}" -m -g {} {}'.format(
        env.full_name_user, env.user_group, env.user_name))
    run('passwd {}'.format(env.user_name))
    run('usermod -a -G {} {}'.format(env.user_group, env.user_name))
    run('mkdir /home/{}/.ssh'.format(env.user_name))
    run('chown -R {} /home/{}/.ssh'.format(env.user_name, env.user_name))
    run('chgrp -R {} /home/{}/.ssh'.format(
        env.user_group, env.user_name))
```

Esta función:

1. Agrega un nuevo usuario al grupo `deployers`, que definimos en la última función
1. Define el directorio SSH para almacenar las llaves SSH y dar los permisos al grupo y usuario para acceder a este directorio

**Subir las llaves SSH**
```
def upload_keys():
    """
    Subir las llaves públicas y privadas SSH al servidor remoto por SCP
    """
    scp_command = 'scp {} {}/authorized_keys {}@{}:~/.ssh'.format(
        env.ssh_keys_name + '.pub',
        env.ssh_keys_dir,
        env.user_name,
        env.host_string
    )
    local(scp_command)
```
Aquí nosotros:

1. Subimos las llaves SSH creadas localmente al servidor remoto entonces usuarios no root pueden ingresar por SSH sin ingresar la contraseña
1. Copia la llave pública al servidor remoto en el directorio *ssh-keys*

## Instalar dependencias de Ansible
Agregar la siguiente función para instalar las dependencias para Ansible

```
def install_ansible_dependencies():
    """
    Instala el módulo python-dnf así que Ansible puede comunicarse con el manejador de paquetes de Fedora
    """
    run('dnf install -y python-dnf')
```

> Ten en cuenta que estamos utilizando una distribución de Linux en específico, usando el módulo DNF, que puede variar en otras distribuciones

## Definir el modo permisivo de SELinux
La siguiente función define SELinux a un modo permisivo. Esto es hecho para prevenir cualquier error 502 arrojado por NginX.

```
def set_selinux_permissive():
    """
    Define SELinux pa un modo permisivo/deshabilitado
    """
    # Para permissos
    run('sudo setenforce 0')
```

> De nuevo es una función específica de Fedora

Actualizar el servidor
Finalmente podemos actualizar el servidor
```
def upgrade_server():
    """
    Actualizar el servidor como un usuario root
    """
    run('dnf upgrade -y')
    # Comando opcioanl (necesario para Fedora 25)
    run('dnf install -y python')
    run('reboot')
```

# Verificación de sanidad
Con eso, hemos terminado el script de Fabric, Antes de ejecutarlo, asegúrate de entrar al servidor y cambiar la contraseña de root
```
ssh root@<server-ip-address>
You are required to change your password immediately (root enforced)
Changing password for root.
(current) UNIX password:
New password:
Retype new password:
```

Asegurate de actualizar `env.password` con la nueva contraseña. Sal del servidor y vuelve a la terminal local, y luego ejecuta Fabric
```
fab -f ./prod/fabfile.py start_provision
```

Si todo fue bien, las nuevas llaves SSH serán generadas y se te preguntará para crear una nueva contraseña, asegurate de hacer esto
```
Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
```

Un número de tareas se ejecutarán. Después de que el usuario `deployer` es creado, se te preguntará para agregar una contraseña para el usuario

```
[104.236.66.172] out: Changing password for user deployer.
```

Donde vas a tener que ingresar luego de que las llaves son subidas

```
deployer@104.236.66.172s password:
```

Después que este script se ejecute exitosamente, tu no podrás ser capaz de ingresar por ssh como root. En vez de eso, puedes ingresar como el usuario no root `deployer`

Prueba esto 

```
ssh root@<server-ip-address>
Permission denied (publickey,gssapi-keyex,gssapi-with-mic).
```

Esto es lo esperado. Entonces para autenticarte neccesitaras algo como:

```
ssh -i ./ssh-keys/104.236.66.172_prod_key deployer@104.236.66.172
```

Para ingresar correctamente

## Ansible

Ansible es una herramienta de manejo de configuraciones y aprovisionamiento usada para automatizar el despliegue de tareas usando SSH.

Puedes ejecutar tareas individuales de Ansible en servidores de aplicaciones desde tu consola remotamente y ejecutar tareas en caliente. Las tareas también pueden ser combinadas en un libro de recetas, una colección de muchas recetas, donde cada receta define algunas tareas específicas que son requeridas durante el proceso de despliegue. Ellos son ajecutados contra servidores de aplicaciones durante el proceso de despliegue. Los libros de revetas son escritos en YAML

### Libros de revetas

Los libros de recetas consisten en una arquitectura modular como sigue:

1. Hosts: especifican todas las direcciones IP o nombres de dominio de los servidores remotos para orquestar. Los libros de recetas siempre apuntan a un grupo de hosts
1. Roles: están divididas en subpartes. Veamos algunas :
  1. Task: son una colección de múltiples tareas que necesitan ejecutarse durante el proceso de ejecución
  1. Handlers: proveen una manera de disparar un conjunto de operaciones cuando un módulo hace un cambio en el servidor remoto
  1. Templates: en este contexto, son usados generalmente para definir algunos archivos de configuración de módulos, como nginx
1. Variables: Son una lista simple de parejas llave-valor donde cada llave (una variable) es mapeada a un valor. 

### Ejemplo de libro de recetas

Veamos un ejemplo de receta en un solo archivo

```
---
# My Ansible playbook for configuring Nginx
- hosts: all

  vars:
    http_port: 80
    app_name: django_bootstrap

  tasks:
    - name: Install nginx
      dnf: name=nginx state=latest

    - name: Create nginx config file
      template: src=django_bootstrap.conf dest=/etc/nginx/conf.d/{{ app_name }}.conf
      become: yes
      notify:
        - restart nginx

  handlers:
    - name: Restart nginx
      service: name=nginx state=restarted enabled=yes
      become: yes
```

Aquí hemos definido lo siguiente:
 1. Host: como `hosts: all`, que representa que el libro de recetas se ejecutará en todos los servidores listados en el archivo de inventario
1. Variables `http_port: 8 y `app_name: django_bootstrap` para usar en la plantilla
1. Task para instalar nginx, definir la configuración del mismo y reiniciarlo
1. Handler para reiniciar el serivicio


### Configurción de los libros de recetas

Vamos a configurar un libro de recetas para Django. Agreguemos *deploy.yml* al directorio "prod"

```
##
# This playbook deploys the whole app stack
##
- name: apply common configuration to server
  hosts: all
  user: deployer
  roles:
    - common
```

El código anterior, junta los host, usuarios y roles

### Hosts

Agrega un archivo *host* de texto plano en la carpeta "prod" para listar los servidores bajo sus respectivos grupos.

```
[common]
<server-ip-address>
```

En el código anterior, common se refiere a un grupo, bajo el cual se listan un conjunto de direcciones ip.

### Variables
Ahora definimos las variables que serán usadas en los roles. Agrega una nueva carpeta dentro de "prod" llamada *group_vars*, luego crea un archivo llamado *all* con formato de texto plano en esa carpeta, aquí definimos las variables para comenzar

```
# App Name
app_name: django_bootstrap

# Deployer User and Groups
deployer_user: deployer
deployer_group: deployers

# SSH Keys Directory
ssh_dir: <path-to-your-ssh-keys>
```

### Roles
De nuevo los roles son una colección de diferentes recetas, y todas se ejecutan bajo un rol específico. Crea un nuevo directorio llamado *roles* en la carpeta prod y luego dentro de roles, una carpeta *common* , luego crea carpetas con los siguientes nombres task, handlers y templates. De esta manera 

```
??? prod
?   ??? deploy.yml
?   ??? fabfile.py
?   ??? group_vars
?   ?   ??? all
?   ??? hosts
?   ??? roles
?       ??? common
?           ??? handlers
?           ??? tasks
?           ??? templates
??? ssh-keys
    ??? 104.236.66.172_prod_key
    ??? 104.236.66.172_prod_key.pub
    ??? authorized_keys
```

Ahora dentro de task creamos un archivo de texto plano llamado *main.yml* que servirá como punto de entrada al rol.

El contenido de este será

```
##
# Configure the server for the Django app
##
- include: 01_server.yml
- include: 02_git.yml
- include: 03_postgres.yml
- include: 04_dependencies.yml
- include: 05_migrations.yml
- include: 06_nginx.yml
- include: 07_gunicorn.yml
- include: 08_systemd.yml
# - include: 09_fix-502.yml
```

Ahora veremos cada uno de estos archivos

*01_server.yml*

```
##
# Update the DNF package cache and install packages as a root user
##
- name: Install required packages
  dnf: name={{item}} state=latest
  become: yes
  with_items:
    - vim
    - fail2ban
    - python3-devel
    - python-virtualenv
    - python3-virtualenv
    - python-devel
    - gcc
    - libselinux-python
    - redhat-rpm-config
    - libtiff-devel
    - libjpeg-devel
    - libzip-devel
    - freetype-devel
    - lcms2-devel
    - libwebp-devel
    - tcl-devel
    - tk-devel
    - policycoreutils-devel
```

Aquí está una lista de todos los paquetes que van a ser instalados

*02_git.yml*
```
##
# Clone and pull the repo
##
- name: Set up git configuration
  dnf: name=git state=latest
  become: yes

- name: Clone or pull the latest code
  git: repo={{ code_repository_url }}
        dest={{ app_dir }}
```

y agrega las siguientes variables a *group_vars/all*

```
# Github Code's Repo URL
code_repository_url: https://github.com/realpython/django-bootstrap

# App Directory
app_dir: /home/{{ deployer_user }}/{{app_name}}
```

*03_postgres.yml*
```
##
# Set up and configure postgres
##
- name: Install and configure db
  dnf: name={{item}} state=latest
  become: yes
  with_items:
    - postgresql-server
    - postgresql-contrib
    - postgresql-devel
    - python-psycopg2

- name: Run initdb command
  raw: postgresql-setup initdb
  become: yes

- name: Start and enable postgres
  service: name=postgresql enabled=yes state=started
  become: yes

- name: Create database
  postgresql_db: name={{ app_name }}
  become_user: postgres
  become: yes

- name: Configure a new postgresql user
  postgresql_user: db={{ app_name }}
                                name={{ db_user }}
                                password={{ db_password }}
                                priv=ALL
                                role_attr_flags=NOSUPERUSER
  become: yes
  become_user: postgres
  notify:
    - restart postgres
```

y en *group_vars/all*

```
# DB Configuration
db_url: postgresql://{{deployer_user}}:{{db_password}}@localhost/{{app_name}}
db_password: thisissomeseucrepassword
db_name: "{{ app_name }}"
db_user: "{{ deployer_user }}"
```

Cambia `db_password` con una contraseña segura.

Ahora crea un archivo *main.yml* en *handlers* con lo siguiente

```
- name: restart postgres
  service: name=postgresql state=restarted
  become: yes
```

*04_dependencies.yml*

```
##
# Set up all the dependencies in a virtualenv required by the Django app
##
- name: Create a virtualenv directory
  file: path={{ venv_dir }} state=directory

- name: Install dependencies
  pip:    requirements={{ app_dir }}/requirements.txt
          virtualenv={{ venv_dir }}
          virtualenv_python=python3.5

- name: Create the .env file for running ad-hoc python commands in our virtualenv
  template: src=env.j2 dest={{ app_dir }}/.env
  become: yes
```

y en *group_vars/all*

```
# Application Dependencies Setup
venv_dir: '/home/{{ deployer_user }}/envs/{{ app_name }}'
venv_python: '{{ venv_dir }}/bin/python3.5'
```

y crea un archivo *env.j2* en la carpeta templates

```
#!/bin/bash
export DEBUG="True"
export DATABASE_URL="postgresql://deployer:thisissomeseucrepassword@localhost/django_bootstrap"
export DJANGO_SECRET_KEY="changeme"
export DJANGO_SETTINGS_MODULE="config.settings.production"
```

> Ten mucho cuidado con las variables de ambiente y sus valores en *env.j2*, desde que son usadas por el proyecto.

*05_migrations.yml*
```
##
# Run db migrations and get all static files
##
- name: Make migrations
  shell: ". {{ app_dir }}/.env; {{ venv_python }} {{ app_dir }}/manage.py makemigrations "
  become: yes

- name: Migrate database
  django_manage: app_path={{ app_dir }}
                                 command=migrate
                                 virtualenv={{ venv_dir }}

- name: Get all static files
  django_manage: app_path={{ app_dir }}
                                 command=collectstatic
                                 virtualenv={{ venv_dir }}
  become: yes
```

*06_nginx.yml*

```
##
# Configure nginx web server
##
- name: Set up nginx config
  dnf: name=nginx state=latest
  become: yes

- name: Write nginx conf file
  template: src=django_bootstrap.conf dest=/etc/nginx/conf.d/{{ app_name }}.conf
  become: yes
  notify:
    - restart nginx
```

En *group_vars/all*

```
# Remote Server Details
server_ip: <remote-server-ip>
wsgi_server_port: 8000
```

y en *handlers/main.yml*

```
- name: restart nginx
  service: name=nginx state=restarted enabled=yes
  become: yes
```

Crea una plantilla llamada *django_bootstrap.conf* en *templates*

```
upstream app_server {
    server 127.0.0.1:{{ wsgi_server_port }} fail_timeout=0;
}

server {
    listen 80;
    server_name {{ server_ip }};
    access_log /var/log/nginx/{{ app_name }}-access.log;
    error_log /var/log/nginx/{{ app_name }}-error.log info;

    keepalive_timeout 5;

    # path for staticfiles
    location /static {
            autoindex on;
            alias {{ app_dir }}/staticfiles/;
    }

    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_redirect off;

        if (!-f $request_filename) {
            proxy_pass http://app_server;
            break;
        }
    }
}
``` 

*07_gunicorn.yml*

```
##
# Set up Gunicorn and configure systemd to execute gunicorn_start script
##
- name: Create a deploy directory
  file: path={{ deploy_dir }} state=directory
  become: yes

- name: Create the gunicorn_start script for running our app from systemd service
  template: src=gunicorn_start
                    dest={{ deploy_dir }}/gunicorn_start
  become: yes

- name: Make the gunicorn_start script executable
  raw: cd {{ deploy_dir }}; chmod +x gunicorn_start
  become: yes
```

y en *groups_vars/all*
```
# Deploy Dir in App Directory
deploy_dir: '{{ app_dir }}/deploy'

# WSGI Vars
django_wsgi_module: config.wsgi
django_settings_module: config.settings.production
django_secret_key: 'changeme'
database_url: '{{ db_url }}'
```

y en *templates/gunicorn_start*

```
#!/bin/bash

### Define script variables

# Name of the app
NAME='{{ app_name }}'
# Path to virtualenv
VIRTUALENV='{{ venv_dir }}'
# Django Project Directory
DJANGODIR='{{ app_dir }}'
# The user to run as
USER={{ deployer_user }}
# The group to run as
GROUP={{deployer_group }}
# Number of worker processes Gunicorn should spawn
NUM_WORKERS=3
# Settings file that Gunicorn should use
DJANGO_SETTINGS_MODULE={{django_settings_module}}
# WSGI module name
DJANGO_WSGI_MODULE={{ django_wsgi_module }}


### Activate virtualenv and create environment variables

echo "Starting $NAME as `whoami`"
# Activate the virtual environment
cd $VIRTUALENV
source bin/activate
cd $DJANGODIR
# Defining the Environment Variables
export DJANGO_SECRET_KEY='{{ django_secret_key }}'
export DATABASE_URL='{{ db_url }}'
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH


### Start Gunicorn

exec gunicorn ${DJANGO_WSGI_MODULE}:application \
        --name $NAME \
        --workers $NUM_WORKERS \
        --user=$USER --group=$GROUP \
        --log-level=debug \
        --bind=127.0.0.1:8000
```

*08_systemd.yml*

```
##
# Set up systemd for executing gunicorn_start script
##
- name: write a systemd service file
  template: src=django-bootstrap.service
                    dest=/etc/systemd/system
  become: yes
  notify:
    - restart app
    - restart nginx
```

Un nuevo template llamado *django-bootstrap.service*
```
#!/bin/sh

[Unit]
Description=Django Web App
After=network.target

[Service]
PIDFile=/var/run/djangoBootstrap.pid
User={{ deployer_user }}
Group={{ deployer_group }}
ExecStart=/bin/sh {{ deploy_dir }}/gunicorn_start
Restart=on-abort

[Install]
WantedBy=multi-user.target
```

y lo siguiente a *handlers/main.yml*

```
- name: restart app
  service: name=django-bootstrap state=restarted enabled=yes
  become: yes
```

*09_fix-502.yml*

```
##
# Fix the 502 nginx error post deployment
#
- name: Fix nginx 502 error
  raw: cd ~; cat /var/log/audit/audit.log | grep nginx | grep denied | audit2allow -M mynginx; semodule -i mynginx.pp
  become: yes
```

## Verificación

Ahora usaremos Ansible instalado en nuestro ambiente virtual  para realizar las pruebas

```
pip install ansible==2.1.3
```

Ahora creamos un nuevo archivo llamado *deploy_prod.sh* en la carpeta raiz del proyecto y aseguremonos de colocar la dirección IP correcta

```
#!/bin/bash

ansible-playbook ./prod/deploy.yml --private-key=./ssh_keys<server-ip>_prod_key -K -u deployer -i ./prod/hosts -vvv
```

y luego lo ejecutamos

```
sh deploy_prod.sh
```

Si existen errores, revisa la terminal para ver como arreglarlos. Una vez terminado podrás usar el script de despliegue y luego podrás visitar la IP para verificar que el sitio web de django está activo

asegurate de descomentar esta linea en *prod/roles/common/tasks/main.yml* si ves un mensaje de error 502, que indica que hay un problema entre nginx y gunicorn

```
# - include: 09_fix-502.yml
```

## Conclusión
Este post provee un conocimiento básico de como puedes automatizar la configuración de un servidor con Fabric y Ansible. Los libros de recetas de Ansible son muy poderosos desde que puedes automatizar casi cualquier tarea del servidor con un archivo YAML. Espero que ahora puedas empezar a automatizar tus tareas de servidor usando Ansible y sus libros de recetas.

Todo el código fuente se encuentra en [el repositorio oficial de Real Python](https://github.com/realpython/automated-deployments)

> La propiedad intelectual de este post pertenece a  [The Real Python](https://realpython.com/), para solicitar la remoción de este post, por favor comuníquese a [ma0@contraslash.com](mailto:ma0@contraslash.com)