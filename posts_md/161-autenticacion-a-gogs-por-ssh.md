Title: Autenticación a Gogs por SSH
Date: 2017-03-17T15:02:48+00:00
Description: Guía corta para la autenticación por llaves SSH a un servidor Gogs
Tags: Git,Gogs,Continuous Integration,Automatic Deployment
---
# Autenticación a Gogs por SSHUno de los pasos mas importantes a la hora de realizar despliegue automático es que tu servidor pueda obtener los cambios en su rama respectiva sin necesidad de intervención humana, y por lo general nuestros repositorios son privados, de tal manera que autenticarse por SSH es una excelente opción.

Como primera instancia, en el cliente que recibirá los cambios, en este caso servidor de staging/testing/production debemos generar una llave SSH, para eso utilizamos el siguiente comando

```
ssh-keygen -t rsa -b 4096 -C "mail@example.com"
```

Aseguremonos de guardar las llaves en una ubicación que recordemos y que tenga un nombre apropiado. Por defecto se guardan en `~/.ssh/id_rsa`

Es importante que cuando nos pida la contraseña `paraphrase` lo dejemos vacío.

En al ubicación que hayamos escogido, ahora veremos dos archivos

1. {{nombre llave}}
1. {{nombre llave}}.pub

Copiaremos el contenido del archivo `<nombre llave>.pub` y lo pegaremos en Gogs en la siguiente ubicación:

Your Settings -> SSH Keys -> Add Key

En este formulario podremos colocarle un título a nuestra llave y podremos pegar el contenido.

A continuación habilitaremos la llave en nuestro servidor local con el comando

```
ssh-add {{nombre llave}}
```

> Si tenemos un problema de tipo 
  ```
  Could not open a connection to your authentication agent.
  ```
  Debemos ejecutar el siguiente comando habilitar el agente ssh
  ```
  eval `ssh-agent -s`
  ```

A continuación editaremos el archivo *~/.ssh/config* y añadiremos algo similar a esto

```
Host {{alias del sitio}} {{host del sitio}}
	HostName {{host del sitio}}
	IdentityFile {{ubicacion de la llave}}/{{nombre llave}}
	User {{usuario gogs}}
```

Les presento un ejemplo mas claro

```
Host gogs_server gogs.example.com
    HostName gogs.example.com
    IdentityFile ~/.ssh/id_rsa
    User admin
```

A continuación podremos clonar nuestro nuestro repositorio utilizando la dirección SSH, que debería verse similar a esto

```
git@gogs.example.com:admin/repo.git
```

Y de esta manera ya podremos ejecutar operaciones de git autenticandonos con el usuario que hemos definido.