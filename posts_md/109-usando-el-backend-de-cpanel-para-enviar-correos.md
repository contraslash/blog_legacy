Title: Usando el Backend de Cpanel para enviar Correos
Date: 2016-09-20T15:29:03+00:00
Description: Enviando Correos con Django desde CPanel
Tags: Django,CPanel
---
# Usando el Backend de Cpanel para enviar CorreosNunca he sido un gran fan de los hostings compartidos ni de CPanel, pero ya saben, cuando la tierra da limones, hay que hacer limonada.

Recientemente me encuentro trabajando en un proyecto donde usan CPanel como su proveedor de email corporativo y pues tocó configurarlo, y fue demasiado fácil.

Dejo el fruto del trabajo aquí abajo

*settings.py*
```
...
EMAIL_HOST = 'mail.example.com'
EMAIL_HOST_USER = 'info@example.com'
EMAIL_HOST_PASSWORD = 'MyUltr4$upp#rP@ss'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'info@example.com'
...
```

Y claro, el código para enviar el mail

```
email = EmailMessage(
     subject="Test Email",
     body="This is a test mail",
     from_email="info@example.com",
     to=["ma0@example.com"]
)
email.send(fail_silently=False)
```

>La aplicación Django no está ejecutándose en el servidor compartido y configurarla, al menos con CPanel, ha sido un trabajo que elegí posponer por la complejidad que me generó, al menos con ese proveedor de servidores compartidos