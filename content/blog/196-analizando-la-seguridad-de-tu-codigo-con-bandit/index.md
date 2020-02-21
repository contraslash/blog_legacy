---
title: "Analizando la seguridad de tu código con Bandit"
date: "2018-04-12T14:41:07+00:00"
description: "Análisis estático de código Python buscando vulnerabilidades utilizando Bandit de OpenStack"
tags: "Python"
---
# Analizando la seguridad de tu código con Bandit

Continuando con herramientas de análisis de código estático, presentamos [Bandit](https://github.com/openstack/bandit), de [OpenStack](https://www.openstack.org/).

```shell
pip install bandit
```

El uso es bastante simple

```shell
bandit -r .
```

Podemos configurar para que solamente nos muestre posibles vulnerabilidades utilizando las banderas `-lll`

