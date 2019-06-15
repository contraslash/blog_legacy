Title: Registro de usuarios y confirmación por email en Django 2.0
Date: 2016-10-19T15:22:25+00:00
Description: Registro con confirmación vía correo electrónico con Gmail y Django
Tags: Django
---
# Registro de usuarios y confirmación por email en Django 2.0

Ha pasado mucho tiempo desde que publiqué [este artículo](http://blog.contraslash.com/user-registration-and-email-confirmation-in-django/), y recientemente recibí un correo solicitando ayuda con la implementación de esta funcionalidad.

Debo confesar que viendo en retrospectiva no está construido de la mejor manera y vale la pena hacer una reimplementación de ciertas cosas, que mencionaré a continuación.

Siguiendo la estructura del primer post, iniciaremos con la creación del formulario de registro, así que en nuestro archivo **forms.py** escribiremos lo siguiente:

```
#! /etc/bin/python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext as _

class UserForm(ModelForm):
    """
    Form wrapper for User in django.contril.auth
    """
    password = forms.CharField(widget=forms.PasswordInput, label=_('Password'))

    class Meta:

        model = User
        fields = (
            'email',
            'username',
            'password'
        )
        labels = {
            'email': _('Email'),
            'username': _('Username'),
            'password': _('Password'),
        }
        error_messages = {
            'username': {
                'required': _('Username field is required'),
                'invalid': _('Username field is invalid')
            },
            'password': {
                'required': _('Password field is required'),
                'invalid': _('Password field is invalid')
            }, }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'validate', 'required': 'required'}),
            'last_name': forms.TextInput(attrs={'class': 'validate', 'required': 'required'}),
            'email': forms.EmailInput(attrs={'class': 'validate', 'required': 'required'}),
            'username': forms.TextInput(attrs={'class': 'validate', 'required': 'required'}),
            'password': forms.TextInput(attrs={'class': 'validate', 'required': 'required'}),
        }

    def clean_email(self):
        """
        Verification for unique email
        :return: Email or raise exception
        """
        email = self.cleaned_data["email"]
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('duplicate email')

    def save(self, commit=True):
        """
        Custom save method for determine active and unactive users
        :param commit:
        :return:
        """
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.is_active = False
            user.save()
        return user
```

Lo primero rescatable de esta nueva implementación es el uso de `ugettext` con alias `_`, que nos va a permitir en un futuro traducir nuestros labels a otro idioma.
 
También el uso de clases personalizadas en nuestros inputs, en este caso estamos usando la clase validate, que se encuentra en la librería [Materializecss](http://materializecss.com/) que realiza algunas validaciones por nosotros y le da un buen aspecto a nuestros formularios

Lo siguiente son los validadores a nivel de input, en nuestro caso el método, que verifica si el correo ya ha sido registrado antes y retorna una excepción

Por último, se altera el flujo del método save, diciendo que el usuario no estará activo, y solo activaremos el usuario hasta que valide su cuenta 

Ahora crearemos un perfil para este usuario, en nuestro archivo **models.py** escribiremos lo siguiente

```
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db import IntegrityError

from . import conf as authentication_conf

class UserProfile(models.Model):
    """
    Model for extended information of User at django.contrib.auth
    """

    # One to one references to User Model
    user = models.OneToOneField(User)
    # Activation toke for email verification
    activation_token = models.CharField(max_length=40, blank=True)
    # Expiration date for activation token
    expiration = models.DateTimeField(blank=True, null=True)
    # Profile description
    profile = models.TextField()
    # Slug
    slug = models.SlugField()
    # profile_image
    image = models.ImageField(blank=True, null=True, upload_to=authentication_conf.UPLOAD_PROFILE_IMAGES)
    # youtube video
    youtube_url = models.URLField(blank=True, null=True)
    # cellphone
    cellphone = models.CharField(max_length=20, default="")

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.slug:
            self.slug = slugify(self.user.username)
        successful_save = False
        saved_object = None
        while not successful_save:
            try:
                saved_object = super(UserProfile, self).save(force_insert, force_update, using, update_fields)
                successful_save = True
            except IntegrityError:
                    self.slug = self.slug[:-4] + "-" + generate_random_string(4)
        return saved_object

    def __unicode__(self):
        return unicode(self.user)

def generate_random_string(n):
    """
    Generates a random string of length n
    :param n: Length of string
    :return: Random string
    """
    return ''.join(random.choice(string.ascii_lowercase) for a in range(n))

```

El modelo anteriormente creado nos da una función de perfil de usuario y nos da los elementos para agregar la funcionalidad de verificar el un usuario, ya que activation_token almacenara un registro único con el que un  usuario ingresará al sistema y cambiará el estado de su cuenta, esto se implentará acontinuación en nuestro archivo **views.py**

```
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import ugettext as _
from django.template.loader import get_template
from django.template.context import Context


from .forms import UserForm, User
from .models import UserProfile

from hashlib import sha1
from random import random
from datetime import datetime, timedelta

class SignUp(TemplateView):
    """
    Custom Sign up view. Sends a mail for email verification
    """
    template_name = 'authentication/sign-up.html'
    userform = UserForm(prefix='user')
    userformerrors = None

    def get_context_data(self, **kwargs):
        context = super(SignUp, self).get_context_data(**kwargs)
        print context
        if 'userform' not in context:
            context['userform'] = self.userform
        if 'userformerrors' not in context:
            context['userformerrors'] = self.userformerrors
        return context

    def post(self, request, *args, **kwargs):
        userform = UserForm(request.POST, prefix='user')
        if userform.is_valid():
            user = userform.save(commit=False)
            user.set_password(userform.cleaned_data['password'])
            user.save()
            username = userform.cleaned_data['username']
            email = userform.cleaned_data['email']
            salt = sha1(str(random())).hexdigest()[:5]
            activation_key = sha1(salt+email).hexdigest()
            key_expires = datetime.today() + timedelta(2)

            #Get user by username
            user = User.objects.get(username=username)

            # Create and save user profile
            activation_token = UserProfile(user=user, activation_token=activation_key, expiration=key_expires)
            activation_token.save()

            # Send email with activation key

            context = {
                'url': "http://%s/auth/sign-up-confirm/%s" % ('example.com',activation_key,)
            }

            email_subject = 'Account created successfully'
            email_body = "To activate your account, visit this link: " \
                         "http://%s/auth/sign-up-confirm/%s" \
                         % ('example.com',activation_key,)

            template = get_template('authentication/email-signup-confirmation.html')

            send_mail(
                email_subject,
                email_body,
                'sender_email@gmail.com',
                [email],
                fail_silently=False,
                html_message=template.render(context))
            # return reverse_lazy('index')
        self.userformerrors = userform.errors
        return render(request, self.template_name, self.get_context_data(**kwargs))

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse_lazy('index'))
        else:
            return render(request, self.template_name, self.get_context_data(**kwargs))


class SignUpConfirm(TemplateView):
    """
    Account verification view. Validates the token and activates the user for the platform
    """
    template_name = 'authentication/sign-up-confirm.html'

    def get(self, request, *args, **kwargs):

        if self.request.user.is_authenticated():
            HttpResponseRedirect(reverse_lazy('index'))
        try:
            activation_token = UserProfile.objects.get(activation_token=self.kwargs['token'])
        except UserProfile.DoesNotExist:
            return render(
                request,
                self.template_name,
                {
                    'status': _('Invalid URL')
                }
            )

        if activation_token.expiration < timezone.now():
            return render(
                request,
                self.template_name,
                {
                    'status': _('Expired URL')
                }
            )

        user = activation_token.user
        user.is_active = True
        user.save()
        return render(
            request,
            self.template_name,
            {
                'status': _('Your account has been activated, please log in')
            }
        )

```

En el archivo views tendremos 2 vistas, la primera de Registro, que en primera instancia crea un usuario, y luego genera un hash que servirá para activar el usuario, al final se envía un correo electrónico con el vínculo de activación

> Es importante que cambie  `example.com` y `sender_email@gmail.com` por valores reales. Para ambientes de desarrollo, puede usar `localhost` o `127.0.0.1`

La siguiente vista simplemente verica que el token exista y si existe, activa el usuario.

El archivo de **urls.py** debería quedar similar a esto
```
# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [

    # Sign Up
    url(
        r'sign-up/$',
        views.SignUp.as_view(),
        name='sign_up'
    ),
    url(
        r'sign-up-confirm/(?P<token>\w+)/$',
        views.SignUpConfirm.as_view(),
        name='sign_up_confirm'
    ),
]
```

Por último recuerde tener la configuración de su servidor SMTP en su archivo **settings.py**, que podría ser gmail
```
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'myname@gmail.com'
EMAIL_HOST_PASSWORD = 'mypassword'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'nmyname@gmail.com'
```

> Para habilitar el envío de correos electrónicos desde gmail, debe habilitar el acceso desde aplicaciones menos seguras, puede informarse mejor en [este enlace](https://support.google.com/accounts/answer/6010255?hl=es-419)

Por último los archivos de templates:

**sign-up.html**
```
{% extends "base.html" %}
{% load i18n %}
{% block title %}
    {% trans 'Sign up' %}
{% endblock %}

{% block content %}
    <div class="container center">
        <div class="row">
            <h1>{% trans 'Sign up' %}</h1>
        </div>
                {% if user.is_authenticated %}
                    {% if user.is_anonymous %}
                        {% trans 'Please activate your account'%}
                    {% else %}
                        {% blocktrans %}
                            You are logged as {{ user.username }}
                        {% endblocktrans %}
                        <a href="{% url 'log-out' %}">{% trans 'Log out' %}</a>
                    {% endif %}
                {%  else %}

                    {% if userformerrors %}
                        {{ userformerrors }}
                    {% endif %}
                    <form method="POST">
                    {%  csrf_token %}
                        {% for item in userform %}
                            <div class="input-field">
                                <label for="{{ item.name }}">{{ item.label }}</label>
                                {{ item }}
                            </div>
                        {% endfor %}

                      <button type="submit" class="btn waves-effect waves-light">
                          {% trans 'Sign up' %}
                          <i class="mdi-content-send right"></i>
                      </button>
                  </form>
                {%  endif %}

    </div>
{% endblock %}
```

y **sign-up-confirm.html**
```
{% extends "base.html" %}
{% load i18n %}
{% block title %}
    {% trans 'Sign up successfully' %}
{% endblock %}

{% block content %}
    <div class="container center">
        <div class="row">
            <h1>{% trans 'Sign up confirm' %}</h1>
        </div>
        <p>{{ status }}</p>
    </div>
{% endblock %}
```

El código fuente registrado aquí es una abstracción del [módulo de autenticación](http://git.contraslash.com/ma0/authentication-django) que usamos aquí en contraslash, siéntase libre de participar en el o usarlo para su proyecto