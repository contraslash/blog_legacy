Title: Disqus y Django
Date: 2016-10-02T00:36:22+00:00
Description: Implementación de Disqus en Django
Tags: Django,Disqus
---
# Disqus y Django[Disqus](https://disqus.com) es una plataforma gratuita de comentarios muy famosa, que nos añadir fácilmente una funcionalidad de comentarios a nuestro sitio.

Desplegarlo junto con [django](https://djangoproject.com) me ha parecido muy sencillo,

Primero debemos crear una cuenta en disqus y luego crear un nuevo sitio, y luego get universal code, que nos dará un javascript que debe ser usado en los sitios que queremos que sean comentables.

Me pareció apropiado crear una aplicación muy sencilla que me sirva específicamente para este propósito, y usarlo templatetags, 

Aquí está el contenido de mis templatetags

**disqus_tags.py**

```python
from django import template

register = template.Library()


@register.inclusion_tag("disqus_plugin/disqus_html.html",)
def disqus_html():
    """
    Render HTMl from Disqus
    :return:
    """
    return {}


@register.inclusion_tag("disqus_plugin/disqus_js.html",)
def disqus_js(page_url, page_identifier):
    """
    Render JS from disqus
    :param page_url: Full page URL
    :param page_identifier: Unique Page identifier, Must be Unique
    :return:
    """
    return {
        'PAGE_URL': page_url,
        'PAGE_IDENTIFIER': page_identifier
    }
```

y claro, mis htmls
**disqus_html.html**
```html
<div id="disqus_thread"></div>
```

**disqus_js.html**
```html
<script>

/**
 *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
 *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables */

var disqus_config = function () {
    this.page.url = "{{ PAGE_URL }}";  // Replace PAGE_URL with your page's canonical URL variable
    this.page.identifier = "{{ PAGE_IDENTIFIER }}"; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
};

(function() { // DON'T EDIT BELOW THIS LINE
    var d = document, s = d.createElement('script');
    s.src = '//blogcontraslash.disqus.com/embed.js';
    s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
})();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
<script id="dsq-count-scr" src="//blogcontraslash.disqus.com/count.js" async></script>
```

Ahora viene lo mágico, este contenido será insertado en mis páginas de detalle del blog, una que posiblemente usted esté viendo en este momento, y para inyectar el contendo del URL de mi página uso un context processor, cuyo contenido está aquí

**context_processor.py**
```python
...
def site_name(request):
    site = SimpleLazyObject(lambda: get_current_site(request))
    protocol = 'https' if request.is_secure() else 'http'
    print site
    return {
        'site': site,
        'site_root': SimpleLazyObject(lambda: "{0}://{1}".format(protocol, site.domain)),
        'full_url': SimpleLazyObject(lambda: "{0}://{1}{2}".format(protocol, site.domain, request.path)),
        'path': SimpleLazyObject(lambda: "{0}".format(request.path)),
    }
...
```

y por último, la inyección en mi template

**detail_template.html**
```
{% block content %}
...
    {% disqus_html %}
...
{% endblock %}
{% block specific-js %}
...
    {% disqus_js full_url path %}
...
{% endblock %}

```
