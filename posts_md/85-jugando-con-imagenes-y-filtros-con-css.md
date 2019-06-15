Title: Jugando con imagenes y filtros con CSS
Date: 2016-05-19T02:31:01+00:00
Description: 
Tags: CSS,HTML5
---
# Jugando con imagenes y filtros con CSS

Siempre me ha parecido muy curioso ese efecto en algunas páginas de dejar algunas imágenes en su footer en blanco y negro y al pasarles el mouse por encima se agrandan un poco y toman su escala de colores.

Tomando [esta base](http://jsfiddle.net/27Syr/1206/) y [este post](http://stackoverflow.com/questions/7273927/image-greyscale-with-css-re-color-on-mouse-over), obtuve muy buenos resultados.

Las clases css simplificadas son:
```
 .image {
                    height: 100%;
}

.image img {
                    -webkit-transition: all 1s ease; /* Safari and Chrome */
                    -moz-transition: all 1s ease; /* Firefox */
                    -o-transition: all 1s ease; /* IE 9 */
                    -ms-transition: all 1s ease; /* Opera */
                    transition: all 1s ease;

                    filter: url("data:image/svg+xml;utf8,<svg xmlns=\'http://www.w3.org/2000/svg\'><filter id=\'grayscale\'><feColorMatrix type=\'matrix\' values=\'0.3333 0.3333 0.3333 0 0 0.3333 0.3333 0.3333 0 0 0.3333 0.3333 0.3333 0 0 0 0 0 1 0\'/></filter></svg>#grayscale"); /* Firefox 3.5+ */
                    filter: gray; /* IE6-9 */
                    -webkit-filter: grayscale(100%); /* Chrome 19+ & Safari 6+ */
}

.image:hover img {
                    -webkit-transform:scale(1.25); /* Safari and Chrome */
                    -moz-transform:scale(1.25); /* Firefox */
                    -ms-transform:scale(1.25); /* IE 9 */
                    -o-transform:scale(1.25); /* Opera */
                     transform:scale(1.25);
                    filter: none;
                    -webkit-filter: grayscale(0%);
 }
```
Y la implementación en HTML

```
<div class="image">
    <img src="alguna/url.png">
</div>
```
Muy simple y bastante linsto