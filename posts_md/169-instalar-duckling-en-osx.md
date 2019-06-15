Title: Instalar Duckling en OSX
Date: 2017-05-21T13:38:23+00:00
Description: Inslatar Duckling, la librería para el procesamiento de lenguaje natural en Clojure en OSX
Tags: Procesamiento de Lenguaje Natural
---
# Instalar Duckling en OSX

[Duckling](https://duckling.wit.ai/) es una librería creada por [wit.ai](https://wit.ai) para realizar análisis de lenguaje, originalmente escrita en [Clojure](https://clojure.org/), un dialecto de Lisp implementado sobre la máquina virtual de Java. 

Para tener Duckling funcionando, primero debemos instalar Clojure, para lo cual usaremos como base el [este post](http://www.lispcast.com/clojure-mac)
TL;DR
```
curl https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein > lein
sudo mkdir -p /usr/local/bin/
sudo mv lein /usr/local/bin/lein
sudo chmod a+x /usr/local/bin/lein
export PATH=$PATH:/usr/local/bin
```
Podemos usar duckling directamente con clojure, como se muestra en la página oficial, pero usaremos el wrapper para python.

```
pip install duckling
```

Con lo cual podremos usar las funciones de Duckling en python


```
d = DucklingWrapper()
print(d.parse_time(u'Let\'s meet at 11:45am'))
```