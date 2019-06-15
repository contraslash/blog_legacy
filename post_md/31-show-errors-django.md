Title: Mostrar errores Formularios Django
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: Django
---
# Mostrar errores Formularios Django
Tomado de [StackOverflow](http://stackoverflow.com/questions/14647723/django-forms-if-not-valid-show-form-with-error-message)
```
{% if form.errors %}
    {% for field in form %}
        {% for error in field.errors %}
            <div class="alert alert-error">
                <strong>{{ error|escape }}</strong>
            </div>
        {% endfor %}
    {% endfor %}
    {% for error in form.non_field_errors %}
        <div class="alert alert-error">
            <strong>{{ error|escape }}</strong>
        </div>
    {% endfor %}
{% endif %}
```