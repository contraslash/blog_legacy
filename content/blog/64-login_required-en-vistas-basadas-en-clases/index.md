---
title: "login_required en Vistas Basadas en Clases"
date: "2016-01-29T06:42:23+00:00"
description: ""
tags: "Django"
---
# login_required en Vistas Basadas en Clases

Tomado de [aquí](https://docs.djangoproject.com/en/1.8/topics/class-based-views/intro/#decorating-the-class)

```
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

class ProtectedView(TemplateView):
    template_name = 'secret.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProtectedView, self).dispatch(*args, **kwargs)
```

