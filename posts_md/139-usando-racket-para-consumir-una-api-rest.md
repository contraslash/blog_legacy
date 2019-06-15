Title: Usando Racket para consumir una API REST
Date: 2016-12-15T04:14:02+00:00
Description: A veces es necesario consumir los recursos de una api que usa la especificación REST desde nuestro programa escrito en Racket, es entonces cuando nos preguntamos ¿cómo podriamos hacerlo?
Tags: 
---
# Usando Racket para consumir una API REST

Consumir una API Rest en Racket es uno de los menesteres mas sencillos que un programador de este lenguaje puede imaginar, basta con importar un par de librerías para empezar a escribir el programa. En este post (¿si lo entienden?... post), vamos a usar la API pública de [jsonplaceholder](https://jsonplaceholder.typicode.com/) como ejemplo:

### Método Get
El método mas común en una API REST es el get, el cual te permite tomar toda la información disponible en ese endpoint. De esta forma podemos:

```
(require json)
(require net/url)

(call/input-url 
   (string->url "https://jsonplaceholder.typicode.com/albums")
   get-pure-port
   read-json
)

(call/input-url 
   (string->url "https://jsonplaceholder.typicode.com/posts/1")
   get-pure-port
   read-json
)
```

### Método Post
Este es uno de los métodos mas complicados, ya que no basta con usar la Url sino que tambien se debe agregar cierta información en el cuerpo del mensaje. 

El cuerpo del mensaje debe estar codificado en alguno de estos estandares:

* application/x-www-form-urlencoded (Por defecto)
* multipart/form-data
* text/plain

Así que si quieres transmitir información binaria o con un tamaño considerable deberias usar `multipart/form-data`. De lo contrario, usa `application/x-www-form-urlencoded`.


```
(require json)
(require net/url)
(require net/uri-codec)

(call/input-url 
   (string->url "https://jsonplaceholder.typicode.com/posts/")
   (lambda (url)
     (post-pure-port url
                     (string->bytes/utf-8 (alist->form-urlencoded
                                           (list (cons 'userId "1")
                                                 (cons 'title "Soy un titulo")
                                                 (cons 'body "Hola mundo"))))))
   read-json
)
```
### Métodos PUT, PATCH y DELETE

Los demas métodos se comportan muy parecido a GET y POST pero cambia el nombre de la función que crea el puerto (por ejemplo: put-pure-port, delete-pure-port).

```
(call/input-url 
   (string->url "https://jsonplaceholder.typicode.com/posts/1")
   (lambda (url)
     (put-pure-port url
                     (string->bytes/utf-8 (alist->form-urlencoded
                                           (list (cons 'userId "1")
                                                 (cons 'title "Soy un titulo")
                                                 (cons 'body "Hola mundo"))))))
   read-json
)
```
### Enviando un archivo
Enviar un archivo no es muy complejo, basta con codificar el cuerpo del post bajo `multipart/form-data`, lo veremos en el siguiente tutorial.

# Referencias
[Documentación oficial de racket](https://docs.racket-lang.org/net/url.html?q=put-pure-port#%28def._%28%28lib._net%2Furl..rkt%29._put-pure-port%29%29)