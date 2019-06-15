Title: Python virtualenv
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: Django,Python
---
# Python virtualenv


Como bien saben, de momento soy novato con django, pero con la idea ingenieril de hacer las cosas bien, me encontré con que al igual que con node, python puede ser inmamable con las dependencias, y recomiendan mucho usar un concepto llamado virtualenv, que segun entiendo simplemente crea un ambiente aislado para instalar dependencias de python sin afectar otros proyectos.

Primero necesitamos pip

Ubuntu/Debian/like  
 `sudo apt-get install python-dev python-pip python-virtualenv`

Mac, primero necesitamos pip

https://pip.pypa.io/en/latest/installing.html

Bajamos get-pip.py lo ejecutamos y et viola

luego basta con ejecutar

`sudo pip install virtualenv`

Si usan windows les recomiendo suicidarse jajajajajajaja

Miento, no se suiciden, pero cambien de blog, xD

luego creamos un virtualenv

virtualenv nombreDelAmbiente

Ahora entramos en el

`./nombreDelAmbiente/bin/activate`

#NotaDelProgramador

a veces activate necesita permisos de ejecución

`chmod +x ./nombreDelAmbiente/bin/activate`

Ahora, en la consola veremos algo como

`(nombreDelAmbiente)NombredelPC:ruta/donde/estamos`

Esos parentesis nos dicen en que ambiente estamos

y listo, ahora podemos hacer cuanto pip install queramos, que quedará unicamente en nuestro ambiente,

#NotaDelProgramador

si trabajamos en varios equipos distintas, un

`pip freeze > requirementes.txt`

y luego un

`pip install -r requirements.txt`

en nuestros otros equipos, puede que no venga mal

#NotaDelProgramador

recuerden que el nuevo ambiente queda pelado como culo de bebe, no olviden instalar django al menos jajajajaa


