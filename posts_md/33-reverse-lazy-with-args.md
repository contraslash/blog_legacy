Title: Reverse Lazy with args
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: Django
---
# Reverse Lazy with args

Tomado de [StackOverflow](http://stackoverflow.com/questions/9879259/how-to-pass-url-parameter-to-reverse-lazy-in-django-urls-py)

en el response:
```
return reverse_lazy('resource-view',
                            kwargs={'param': param},
                            current_app='myapp')
```

y en urls.py 
```
urlpatterns = patterns('',
    url(r'^coolresource/(?P<param>\d+)/$', 
        RedirectSomewhere.as_view()),
)
```