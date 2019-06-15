Title: Autenticar OpenSSH sin contraseña
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: Linux
---
# Autenticar OpenSSH sin contraseñaEn el cliente 
`ssh-keygen -t rsa -b 2048 -v`

Luego
`ssh-copy-id -i .ssh/id_rsa.pub usuario@host`

nos autenticams y listo


`ssh -i .ssh/id_rsa usuario@host`