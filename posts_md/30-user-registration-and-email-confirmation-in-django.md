Title: Registro de usuarios y confirmación por email en Django
Date: 2016-01-29T06:42:23+00:00
Description: Registro y confirmación de usuarios en Django usando GMail
Tags: Django
---
# Registro de usuarios y confirmación por email en Django

> Le sugerimos visitar la  [versión 2.0](http://blog.contraslash.com/registro-de-usuarios-y-confirmacion-por-email-en-d/) de este post

##Fuente original: 
[User registration and email confirmation in Django](http://ipasic.com/article/user-registration-and-email-confirmation-django/) por Ivan Pasic

A pesar que hoy en día casi todo el mundo usa la applicación django-registration para proveer la funcionalidad de registro, tal vez algunos de ustedes todavía quieren aprender a crear por su cuenta o al menos aprender los proncipios básicos  de como  funciona esto.

Es por eso que trataré de explicarte como escribir tu propio formulario y vista de registro para un usuario y luego enviarle un email con un vínculo de activación, así el puede confirmar su dirección de correo electrónico cosa que a veces es muy importante.
>Nota: No estoy enseñando algo nuevo y diferente, la mayoría de estos principios son iguales que en django-registration, pero esta vez es solo para que tengas una idea de como aprender a hacerlo por ti mismo

Podemos utilizar el sistema de autenticación incluido en Django, pero nosotros podemos extenderlo y agregar algunos campos, como nombre, apellido, email, etc.

Así que primero creamos nuestro archivo forms.py con nuestra aplicación

######forms.py
```
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'E-mail address'}))
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')
```

Ahora vamos a extender el formulario de registro basándonos en el formulario UserCreationForm

Pero antes de comenzar a escribir nuestra vista, existen algunas cosas mas que debemos hacer con nuestro RegistrationForm.
Primero, probablemente queremos verificar si el email que el usuario a ingresado está siendo usado por otro usuario, y en ese caso levantar una excepción
Además de eso, probablemente también queremos que nuestro nuevo usuario registrado confirme su dirección de correo electrónico enviándole algún vínculo de activación, en el que el pueda dar click. Para eso necesitamos modificar nuestro método **form.save()**, el cual usaremos mas tarde para declarar que un usuario no esta activo, definiendo `is_active = False` 

Así que agregemos esto a nuestro forms.py
######forms.py
```
#clean email field
def clean_email(self):
    email = self.cleaned_data["email"]
    try:
        User._default_manager.get(email=email)
    except User.DoesNotExist:
        return email
    raise forms.ValidationError('email duplicado')

#modificamos el método save() así podemos definir  user.is_active a False la primera vez que se registra
def save(self, commit=True):        
    user = super(RegistrationForm, self).save(commit=False)
    user.email = self.cleaned_data['email']
    if commit:
        user.is_active = False # No está activo hasta que active el vínculo de verificación
        user.save()

    return user
```

Antes de escribir nuestras vistas, vamos a crear un modelo **UserProfile**, que está atado a **User**. Esto es importante y útil, porque aquí almacenaremos el token de activación y definiremos la fecha de vencimiento del token. Por ahora creemos el modelo, pronto entenderás de que estoy hablando.

######models.py
```
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today())
      
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural=u'Perfiles de Usuario'
```

Ahora podemos comenzar a escribir nuestra vistas.
Primero escribamos nuestro formulario de Registro.
 

######views.py
```
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from forms import *
from models import *
from django.template import RequestContext
from django.core.mail import send_mail
import hashlib, datetime, random
from django.utils import timezone

def register_user(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        args['form'] = form
        if form.is_valid(): 
            form.save()  # guardar el usuario en la base de datos si es válido
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            salt = hashlib.sha1(str(random.random())).hexdigest()[:5]            
            activation_key = hashlib.sha1(salt+email).hexdigest()            
            key_expires = datetime.datetime.today() + datetime.timedelta(2)

            #Obtener el nombre de usuario
            user=User.objects.get(username=username)

            # Crear el perfil del usuario                                                                                                                                 
            new_profile = UserProfile(user=user, activation_key=activation_key, 
                key_expires=key_expires)
            new_profile.save()

            # Enviar un email de confirmación
            email_subject = 'Account confirmation'
            email_body = "Hola %s, Gracias por registrarte. Para activar tu cuenta da clíck en este link en menos de 48 horas: http://127.0.0.1:8000/accounts/confirm/%s" % (username, activation_key)

            send_mail(email_subject, email_body, 'myemail@example.com',
                [email], fail_silently=False)

            return HttpResponseRedirect('/accounts/register_success')
    else:
        args['form'] = RegistrationForm()

    return render_to_response('user_profile/register.html', args, context_instance=RequestContext(request))
```

La mayoría de este código podría ser familiar para tí, si tienes algún conocimiento básico escribiendo formularios en Django, pero en lo que estamos interesados aquí es en la parte del token de autenticación y el envío de un correo electrónico.

Así, como puedes ver, si nuestro formulario es válido (no hay errores) entonces llamaremos al método **save()**, que previamente modificamos en **forms.py**

Eso creará nuestro nuevo usuario, pero ese usuario todavía no está activo, así que debemos generar algún token de activación que le podemoe enviar, con el que podrá activar su cuenta.

Para generar el token de activación, hemos utilizado los módulos **random** y **hashlib**, porque queremos un número aleatorio para generar un cifrado SHA1. Combinamos eso con la *sal* y el correo del usuario para obtener un token de activación que será enviado al usuario.

Pero antes de enviar el correo al usuario, queremos definir una fecha cuando el token de activación caduque. Así que vamos a definir un tiempo de vida, que en este caso es de 2 días. Si el usuario da click en el vínculo luego de dos días, el no podrá activar su cuenta.

Después de eso, vamos a crear y guardar un nuevo **UserProfile** que estará cibectadi al **User** que acabamos de crear y le pasaremos el token de activación y la fecha de vencimiento que acabamos de crear.

Después enviaremos el correo al usuario con su token de activación y algún texto apropiado, para eso usamos la función **send_mail** de Django. Si nunca has usado esta función te recomendamos leer mas de ella [aquí](https://docs.djangoproject.com/en/1.8/topics/email/)

De cualquier manera, es importante definir la configuración del envío de correos en **setting.py**, por ejemplo, si usas una cuenta de gmail, podría verse algo así

######settings.py
```
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'myname@gmail.com'
EMAIL_HOST_PASSWORD = 'mypassword'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'nmyname@gmail.com'
```

Nuestro registro.html podría verse así

######registro.html
```
{% extends "base.html" %}

{% block content %}            
<form class="form-signup" action="/accounts/sign_up/" method="post">{% csrf_token %}
    <h2>Crea tu cuenta</h2>
    <div class="fieldWrapper">
        <label>Nombre</label><br>
        {{ form.first_name }}
    </div>    
    <br>
    <div class="fieldWrapper">
        <label>Apellido</label><br>
        {{ form.last_name }}
    </div>    
    <br>
    <div class="fieldWrapper">    
        {{ form.email.errors }}            
        <label>E-mail</label><br>
        {{ form.email }}
    </div>    
    <br>
    <div class="fieldWrapper">
    {{form.errors.values.0}}                
        <label>Nombre de Usuario</label><br>
        {{ form.username }}
    </div>
    <br>
    <div class="fieldWrapper">        
        {{form.errors.values.1}}            
        <label>Contraseña</label><br>                    
        {{ form.password1 }}
    </div>
    <br>
    <div class="fieldWrapper">           
        <label>Contraseña de nuevo</label><br>
        {{ form.password2 }}
    </div>            
    <br></br>
    <input type="submit" name="submit" class="btn btn-primary" value="Crear cuenta">
</form>

{% endblock %}
```

Ahora definamos nuestra vista para activar una nueva cuenta.
Si tu quieres que esta vista funcione, es importante que definas tus urls para obtener el token de activación y pasarlo como argumento. mira el archivo **urls.py** al final de este tutorial para que tengas idea.	
######views.py
```
def register_confirm(request, activation_key):
    # Verifica que el usuario ya está logeado
    if request.user.is_authenticated():
        HttpResponseRedirect('/home')

    # Verifica que el token de activación sea válido y sino retorna un 404
    user_profile = get_object_or_404(UserProfile, activation_key=activation_key)

    # verifica si el token de activación ha expirado y si es así renderiza el html de registro expirado
    if user_profile.key_expires < timezone.now():
        return render_to_response('user_profile/confirm_expired.html')
    # Si el token no ha expirado, se activa el usuario y se muestra el html de confirmación
    user = user_profile.user
    user.is_active = True
    user.save()
    return render_to_response('user_profile/confirm.html')
```

Aquí está como yo configuré mi **urls.py**, por favor tengan cuidado de como van a definir sus urls y como van a llamar al HttpResponseRedirect en su **views.py**. Si llamas a un url que no existe, vas a tener un error. La mismca cosa con el token de activación del usuario. Si la url de activación no existe, el usuario no podrá tener una activación exitosa.

######urls.py
```
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

url(r'^sign_up/', ('yourappname.views.register_user')),
    url(r'^register_success/', ('yourappname.views.register_success')),
    url(r'^confirm/(?P<activation_key>\w+)/', ('yourappname.views.register_confirm')),
)
```

Eso es todo para este post, ahora tu deberías saber como crear y extender los formularios de registro con una confirmación de email :)

Espero que lo hayas encontrado entretenido y útil


>Si consideras que hay un error en la traducción o existe algo que se pueda mejorar, no dudes en mandarme un [email](mailto://ma0@contraslash.com)