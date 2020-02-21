---
title: "Modificando el origin de git"
date: "2016-05-20T02:43:45+00:00"
description: ""
tags: "Git"
---
# Modificando el origin de git

Este post es sacado de [aquí](https://help.github.com/articles/changing-a-remote-s-url/)

Primero se verifica cual es la url actual del remote
```
git remote -v
```

Luego se define la nueva ruta

```
git remote set-url oritin http://nueva.direccion/de/servidor/de/git
```

