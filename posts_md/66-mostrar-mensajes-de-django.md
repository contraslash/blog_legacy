Title: Mostrar Mensajes de Django
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: Django
---
# Mostrar Mensajes de Django```
{% if messages %}
<ul class="messages">
    {% for message in messages %}
    <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>
        {% if message.level == DEFAULT_MESSAGE_LEVELS.ERROR %}Important: {% endif %}
        {{ message }}
    </li>
    {% endfor %}
</ul>
{% endif %}
```