Title: Recuperación de contraseña personalizada
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: Django
---
# Recuperación de contraseña personalizada

Tomado de [garmoncheg](http://garmoncheg.blogspot.com.au/2012/07/django-resetting-passwords-with.html)

Tenía que hacer  una tarea recientemente. Se trataba de agregar una mecanismo para recuperar contraseña en un proyecto de django. Nosotros teníamos nuestro propio sistema de registro funcionando ....
Era un proyecto del sector corporativo, así que no podías irte registrando por ti mismo. Administradores, probablemente con sincronización  LDAP, registraban tu email/login en el sistema. Así que tenías que definir tu propia contraseña. Por razones de seguridad, no podías registrarte. Punto.

Primero, traté de encontrar una decisión estándar, así que revisé [django-registration](https://pypi.python.org/pypi/django-registration/) y [django password-reset](https://github.com/brutasse/django-password-reset). Estas eran unas increibles herramientas para instalar y  continuar, pero necesitaba una solución un poco mas compleja,  y la idea de que tu propia bicicleta es siempre mejor, así que me decidí por usar el administrador de django y ví que estaban las harramientas para ser usadas sin perder tiempo. Actualmente django.contrib.auth hace parte de Dajgno, pero tiene la UI del admin de django. Tu puedes encontrar las herramientas que necesitas aquí:


- password_reset
- password\_reset\_done 
- password\_reset\_confirm 
- password\_reset\_complete 

Para usar este método, primero debes:
### 1. Confiturar el email:
Tu proyecto de Django, tipicamente tiene espacio para variables de correo SMTP en **settings.py**. Usualmente tu necesitas esto en producción para enviar errores a los administradores de errores **500** y/o alertas del sistema. Para nuestras necesitades, python tiene su propio servidor de email. Yo prefiero usar esto para propositos de *degug*, así que una buena manera de usar esto únicamente en caso de debug es agregando esta líneas en **settings.py**:
######settings.py
```
if DEBUG:
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_USE_TLS = False
    DEFAULT_FROM_EMAIL = 'testing@example.com'
```
Aquí tu tendrás tu propio servidor de email en un puerto alternativo. Para producción podrías entrar las configuraciones de Sendmail (o cualquiera que uses)

Ahora tu podrías ser capaz de iniciar el servidor ejecutando en el servidor:

`python -m smtpd -n -c DebuggingServer localhost:1025`


### 2.Confirurar las Urls:
######urls.py
```
urlpatterns = patterns('',
    url(r'^user/password/reset/$', 
        'django.contrib.auth.views.password_reset', 
        {'post_reset_redirect' : '/user/password/reset/done/'},
        name="password_reset"),
    (r'^user/password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
    (r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : '/user/password/done/'}),
    (r'^user/password/done/$', 
        'django.contrib.auth.views.password_reset_complete'),
    # ...
)
```

> - Django 1.6 y superior requiere uidb64 en lugar de uidb36
 
### 3. Agregar 

Tu tienes templates para recuperar las contraseñas. 
Django tiene los templates del administrador aquí, pero creo que tu podrías querer templates personalizados a tus necesidades, así que básicamente lo que tienes que hacer es sobreescribir esos templates, especificando tus templates en el path de django. Los templates de Django son:

- registration/password_reset_form.html
- registration/password_reset_done.html
- registration/password_reset_confirm.html
- registration/password_reset_complete.html

Template del email

- registration/password_reset_email.html 

Colocaré abajo los templates que yo he usado, de acuerdo con la filosofía de *baterías incluidas* de Django


######registration/password_reset_form.html 
```
{% extends "base.html" %}

{% block title %}Reset Password{% endblock %}

{% block content %}
<p>Especifique su email para enviarle las instrucciones para la recuperación de contraseña.</p>

<form action="" method="post">
    <div style="display:none">
        <input type="hidden" value="{{ csrf_token }}" name="csrfmiddlewaretoken">
    </div>
     {{ form.email.errors }}
    <p><label for="id_email">Dirección de correo electrónico:</label> {{ form.email }} <input type="submit" value="Recuperar contraseña" /></p>
</form>
{% endblock %}
```
######registration/password_reset_done.html 
```
{% extends "base.html" %}

{% block title %}Recuperación de contraseña exitosa{% endblock %}

{% block content %}
<p>Hemos enviado las instrucciones de como recuperar la contraseña a la dirección de correo electrónico especificada</p>
<p>Estarás recibiendo el correo proto.</p>
{% endblock %}
```

######registration/password_reset_confirm.html 
```
{% extends "base.html" %}
{% block title %}Definir nueva contraseña{% endblock %}

{% block content %}
    {% if validlink %}
        <p>Por favor ingrese su nueva contraseña dos veces.<br />
          Así podremos verificar que es correcta.</p>
        <form action="" method="post">
            <div style="display:none">
                <input type="hidden" value="{{ csrf_token }}" name="csrfmiddlewaretoken">
            </div>
            <table>
                <tr>
                    <td>{{ form.new_password1.errors }}
                        <label for="id_new_password1">Nueva contraseña:</label></td>
                    <td>{{ form.new_password1 }}</td>
                </tr>
                <tr>
                    <td>{{ form.new_password2.errors }}
                        <label for="id_new_password2">Confirmar contraseña:</label></td>
                    <td>{{ form.new_password2 }}</td>
                </tr>
                <tr>
                    <td></td>
                    <td><input type="submit" value="Cambiar mi contraseña" /></td>
                </tr>
            </table>
        </form>
    {% else %}
        <h1>Recuperación de contraseña fallida</h1>
        <p>El vínculo de recuperación de contraseña es inválido, <br />
        Posiblemente ya ha sido usado <br />
        Por favor solicite una nueva contraseña.</p>
    {% endif %}
{% endblock %}
```

######registration/password_reset_complete.html 
```
{% extends "base.html" %}

{% block title %}Password reset complete{% endblock %}

{% block content %}
<p>Tu contraseña ha sido definida. Ya puedes iniciar sesión de nuevo</p>
<p><a href="{{ login_url }}">Iniciar sesión</a></p>
{% endblock %}
```

######registration/password_reset_email.html 
```
{% autoescape off %}
Está recibiendo este correo porque solicitó un cambio de contraseña en {{ site_name }}.

Por favor vaya a esta página y configure su nueva constreña
{% block reset_link %}
{{ protocol }}://{{ domain }}{% url django.contrib.auth.views.password_reset_confirm uidb36=uid, token=token %}
{% endblock %}

Su nombre de usuario en caso que lo haya olvidado: {{ user.username }}

Gracias por usar nuestro sitio!

El equipo{{ site_name }}.

{% endautoescape %}
```
Así que tu estás teniendo un sistema de recuperación de contraseña *fuera de la caja*, usando las herrramientas incluidas en Django, con poco tiempo.

Comentame!
 >Si crees que la traducción puede mejorar o tienes alguna opinión, envíame un [correo](mailto://ma0acollazos@gmail.com)