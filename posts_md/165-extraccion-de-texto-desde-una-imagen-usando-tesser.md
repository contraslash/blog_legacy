Title: Extracción de texto desde una imagen usando Tesseract-OCR
Date: 2017-04-20T04:03:08+00:00
Description: Extracción de texto desde una imagen usando Tesseract-OCR
Tags: Extraccion de Informacion
---
# Extracción de texto desde una imagen usando Tesseract-OCRHace tiempo escribí un post sobre [Boilerpipe](http://blog.contraslash.com/usando-boilerpipe-para-extraer-informacion-de-un-h/), una herramienta para extraer texto de documentos html. Hoy mostraré [Tesseract](https://github.com/tesseract-ocr/tesseract) Un OCR.

Primero definamos OCR:

**O** ptical
**C** haracter
**R** ecognizer

Cuyo nombre traduce Reconocedor Óptico de Caracteres. Su principal objetivo es transformar imágenes  que contengan texto en texto.

Su instalación es bastante sencilla:

Ubuntu:

```
sudo apt install tesseract-ocr
```

OSX:

```
brew install tesseract
```

La ejecución del aplicativo es sencilla:

```
tesseract image.jpg -l spa outputtext.txt
```

Donde la bandera `-l` nos indica el lenguaje.

Si queremos transformar la imagen a un idioma que no esté presente por defecto, podemos decargar los modelos de lenguajes compilados del [este repositorio](https://github.com/tesseract-ocr/tessdata), y añadimos el argumento ` --tessdata-dir` que apuntará a la carpeta que contenga el modelo de lenguaje

```
tesseract image.jpg  --tessdata-dir /ruta/a/tessdata/ -l spa outputtext.txt 
```