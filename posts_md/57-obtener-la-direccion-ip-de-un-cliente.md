Title: Obtener la dirección IP de un cliente
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: Django
---
# Obtener la dirección IP de un cliente

Esta respuesta fue tomada de [aquí](http://stackoverflow.com/questions/4581789/how-do-i-get-user-ip-address-in-django)

```
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
```