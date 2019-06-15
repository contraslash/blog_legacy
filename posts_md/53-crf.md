Title: CSRF Exempt en vistas basadas en clases
Date: 2016-01-29T06:42:23+00:00
Description: Usando el decorador csrf_exempt de Django para permitir POST a una vista basada en clases
Tags: Django,Seguridad
---
# CSRF Exempt en vistas basadas en clases

Esto es altamente peligroso, cabe aclarar, porque deja al sitio vulnerable a un [xss](https://es.wikipedia.org/wiki/Cross-site_scripting), pero igual para ambiente de pruebas es útil

```
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class MiVista(View):
	
    ...
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(MiVista, self).dispatch(request, *args, **kwargs)
        
        ...


```

Si lo que están haciendo son peticiones ajax desde un navegador, consideren usar [esto](https://docs.djangoproject.com/en/1.7/ref/contrib/csrf/#ajax) 

y si es un api para móviles, en serio, migren a [REST Framework](http://www.django-rest-framework.org/)