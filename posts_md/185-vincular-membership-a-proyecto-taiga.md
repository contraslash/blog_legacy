Title: Vincular Membership a Proyecto Taiga
Date: 2017-10-05T21:16:08+00:00
Description: Crear membresías a proyectos con la consola de Django para un proyecto en TAIGA
Tags: Taiga
---
# Vincular Membership a Proyecto Taiga

Desde hace unos 4 meses que me dio la fiebre de los contenedores y quería volver todo un contenedor tuve la genial idea de poner [Taiga](https://taiga.io) en un contenedor, lo bueno fue que lo logré, lo malo es que tuve problemas épicos con los archivos estáticos y configuraciones de correo.

Para mitigar esto, me veo en la obligación de colocar este código para la vinculación de usuarios de una manera manual.

```
from taiga.users.models import User, Role
from taiga.projects import models
for p in models.Project.objects.all():
    print(p.id, p.name)
for u in User.objects.all():
    print(u.id, u)
for r in Role.objects.all()
for r in Role.objects.all().order_by("project"):
    print(r.id, r.project, r)

project_id = 4
user_id = 7
role_id = 21
p = models.Project.objects.get(pk=project_id)
u = User.objects.get(pk=user_id)
r = Role.objects.get(pk=role_id)

models.Membership.objects.create(project=p, user=u, role=r)
```