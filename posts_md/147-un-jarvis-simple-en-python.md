Title: Un jarvis simple en Python
Date: 2017-02-06T17:22:23+00:00
Description: Un asistente conversacional sencillo en python
Tags: Python,Procesamiento de Lenguaje Natural
---
# Un jarvis simple en PythonSiempre mi motivación principal para estudiar programación fueron los agentes conversacionales, y creo que mi sueño se volvió parcialmente realidad en el momento que entregué mi tesis de pregrado.

Explorando la red me encontré con [este artículo](https://fossbytes.com/code-personal-assistant-using-python-programming/) de [FossBytes](https://fossbytes.com) donde crean un simple asistente conversacional que repite lo que entiende. Debo aclarar que funciona para inglés y que debería realizar unas configuraciones extras para que realice el mismo proceso en español, pero eso no será hoy. Por lo pronto los dejo con el código fuente, y un enlace al repositorio donde posiblemente en unos cuantos días encontrarán el código ajustado para el español

```
import speech_recognition
import pyespeak


speech_engine = pyespeak.ESpeak()


def speak(text):
    speech_engine.say(text)


print("starting recognizer")
recognizer = speech_recognition.Recognizer()
print("recognizer started")


def listen():
    with speech_recognition.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_sphinx(audio)
    except speech_recognition.UnknownValueError:
        print("Could not understand audio")
    except speech_recognition.RequestError as e:
        print("Recog Error; {0}".format(e))

    return ""

speak("Say something!")
speak("I heard you say " + listen())
```

Para tener este código funcional recomendamos clonar [este repositorio](https://github.com/contraslash/dummy-jarvis), instalar [espeak](http://espeak.sourceforge.net/download.html)

> Para mac, la mejor manera de tener espeak funcionando es usando [este repositorio](https://github.com/pettarin/espeakosx)

y ejecutar el siguiente código

```
pip install -r requirements.txt
git clone https://github.com/relsi/python-espeak
cd python-espeak
make install

cd ..
mkdir pyespeak
cp python-espeak/espeak/* pyespeak
```