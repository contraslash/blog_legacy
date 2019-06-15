Title: Configurar SMTP con Gmail y Django
Date: 2016-03-14T16:24:19+00:00
Description: 
Tags: Django,SMTP
---
# Configurar SMTP con Gmail y Django

Agreguemos esto al **settings.py**
```
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_HOST_USER = 'myname@gmail.com'  
EMAIL_HOST_PASSWORD = 'mypassword'  
EMAIL_PORT = 587  
EMAIL_USE_TLS = True  
DEFAULT_FROM_EMAIL = 'nmyname@gmail.com'  
```