Title: Un tutorial de Ansible
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: Aprovisionamiento,Ansible
---
# Un tutorial de Ansible> Basado en [este post](https://serversforhackers.com/an-ansible-tutorial)

>Ansible es una herramienta de configuración automática de servidores Agent Free que funciona sobre SSH

Considero que el principal atractivo de [Ansible](http://www.ansible.com/) es Agent Free, que quiero decir con esto: que no necesito instalar ruby y un cliente en el servidor que quiero aprovisionar antes de aprovisionar, como con [Chef](https://www.chef.io/) o [Puppet](https://puppetlabs.com/), en lugar de eso, solo necesita un python 2.6+ y un servidor ssh, lo que viene casi que por defecto instalado en las imágenes predeterminadas que nos ofrecen nuestros IaaS favoritos.

###Instalando Ansible
###### Ubuntu
```
sudo apt-add-repository -y ppa:ansible/ansible
sudo apt-get update
sudo apt-get install -y ansible
```

######Mac
```
pip install ansible
```

###Host
Aclaremos algo: esto del aprovisionamiento automático solo es divertido cuando son muchos equipos, o no?

Nuestro archivo de configuración de host estará compuesto por una lista de ips o nombres de dominio identificables  por nuestra máquina (1 por línea), que de ahora en adelante llamaremos maestro.

Podemos crear grupos de hosts colocando líneas que indiquen el nombre del grupo

```
mail.example.com

[webservers]
foo.example.com
bar.example.com

[dbservers]
one.example.com
two.example.com
three.example.com
``` [aprende mas de Inventories](http://docs.ansible.com/ansible/intro_inventory.html)

###Comandos AdHoc
Como cualquier herramienta medianamente decente, tenemos nuestro API por consola.

Prueba estos comandos

```
ansible all -m shell -a "ifconfig"
ansible all -m ping
ansible webservers -s -m apt -a "pkg=apache2 state=installed update_cache=true"
```
>El primer parametro especifica el grupo

>-m Especifica el módulo [módulos](http://docs.ansible.com/ansible/list_of_all_modules.html)

>-s Los comando se ejecutan como superusuario

>-k Pide la contraseña 

>-i Especifica un archivo de host

>--private-key Especifica el archivo con la llave publica para la conexión

>-a Argumentos para el módulo