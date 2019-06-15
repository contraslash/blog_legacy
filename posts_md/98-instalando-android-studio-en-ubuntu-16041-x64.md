Title: Instalando android studio en ubuntu 16.04.1 x64 
Date: 2016-08-30T20:40:32+00:00
Description: 
Tags: Android
---
# Instalando android studio en ubuntu 16.04.1 x64 

Instalamos estos paquetes
```
sudo apt-get install lib32z1 lib32ncurses5 libbz2-1.0:i386 lib32stdc++6
```

Instalamos java
```
sudo apt-get install default-jdk
```
Descargamos Android Studio desde el [sitio oficial](https://developer.android.com/studio/index.html)

El vinculo de descarga es [este](https://dl.google.com/dl/android/studio/ide-zips/2.1.3.0/android-studio-ide-143.3101438-linux.zip)

Y descargamos el SDK de Android, el vinculo directo de descarga es [este](https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz)

Descomprima ambos archivos

```
mkdir -p ~/Android

cd ~/Android

wget https://dl.google.com/dl/android/studio/ide-zips/2.1.3.0/android-studio-ide-143.3101438-linux.zip

unzip android-studio-ide-143.3101438-linux.zip

wget https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz

tar -xzvf android-sdk_r24.4.1-linux.tgz

```

agregue las siguientes lineas al final de su archivo .bashrc

```
echo "export ANDROID_HOME=~/Android/android-sdk-linux" >> ~/.bashrc
echo "export PATH=${PATH}:~/Android/android-sdk-linux/tools:~/Android/android-studio/bin"  >> ~/.bashrc
```

Ahora ejecute Androd Studio

```
~/Android/android-studio/bin/studio.sh
```

Y cuando aparezca el wizard, seleccione como carpeta del SDK la carpeta ~/Android/android-sdk-linux

Android Studio descargara todas las dependencias necesarias para ejecutar su primer proyecto 