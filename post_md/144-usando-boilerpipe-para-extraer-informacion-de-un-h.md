Title: Usando Boilerpipe para extraer información de un HTML con Python
Date: 2017-01-25T18:21:53+00:00
Description: Usando Boilerpipe para extraer información de un documento html con Python
Tags: Python,Extraccion de Informacion
---
# Usando Boilerpipe para extraer información de un HTML con PythonPrimero nos aseguramos que tenemos Java instalados
Podemos descargar desde [el sitio oficial](https://java.com/en/download/) o usarl openjdk en ubuntu 14.04

```
sudo apt-get install openjdk-7-jdk
```

En ubuntu 16.04

```
sudo apt-get install openjdk-8-jdk
```

Nos aseguramos que JAVA_HOME esté definida.

En OSX

```
export JAVA_HOME=$(/usr/libexec/java_home -v 1.8)
```

en Ubuntu 14.04
```
export JAVA_HOME=”/usr/lib/jvm/java-7-openjdk-amd64/”
```

en Ubuntu 16.04
```
export JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64/"
```

Si estamos tabajando en un ambiente vitual, es útil colocarlo en 
`${VIRTUALENV_PATH}/bin/postactivate` o dejarlo para toda la sesión en `~/.profile` o `~/.bashrc`

Instalamos las dependencias

```
pip install jpype1
pip install chardet
```

Descargamos el binding de boilerpipe para python y lo instalamos

```
git clone https://github.com/misja/python-boilerpipe
cd python-boilerpipe
python setup.py install
```

Y luego probamos el funcionamiento con 
```
from boilerpipe.extract import Extractor
extractor = Extractor(extractor='ArticleExtractor', url='http://neuro.imm.dtu.dk/wiki/Boilerpipe')
extracted_text = extractor.getText()
```
