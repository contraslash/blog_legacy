---
title: "Doble autenticación con python"
date: "2017-05-26T03:40:19+00:00"
description: "Implementar un segundo Factor de Autenticación con Python y Google Authenticator"
tags: "Seguridad"
---
# Doble autenticación con python

Debo confesar varias cosas cosas:

1. A pesar que me migré a Linode, aún conservo algunos servicios en Digital Ocean, solo porque me ha dado pereza terminar de migrarlos.
1. Me llamó mucho la atención que DO implementara un segundo facor de autenticación con [Google Authenticator](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2).
1. Siempre me han fascinado los tokens, si, ese pequeño dispositivo que muestra 6 números.

La seguridad es un factor importante para todos y como buena práctica en todos los manuales de seguridad, se recomienda tener un segundo factor de autenticación, así que por qué no implementar uno con python?

Existen un montón de referencias sobre cómo funcionan los Tokens, o mejor conocidos como Algoritmos de Contraseña única basados en HMAC (HMAC-Based One-Time Password Algorithm), y su implementación según el [RFC4226](https://tools.ietf.org/html/rfc4226) o Algoritmos de Contraseña única basados en el tiempo (Time-Based One-Time Password Algorithm), especificados en [RFC6238](https://tools.ietf.org/html/rfc6238). Por simplicidad abreviados como HOTP y TOTP. 

Los algoritmos son relativamente sencillos de implementar, pero para no reinventar la rueda, tomé la opción fácil e instalé [pyotp](https://github.com/pyotp/pyotp)

```
pip install pyotp
```

El uso de esta librería es tan fácil que da risa. Tan solo necesitamos nuestra  semilla (seed) en base 32, (la cual sospechosamente se parecerá a mi SECRET_KEY de mis proyectos en django) y luego preguntar por los números actuales.

```
import pyotp
import base64
SECRET_KEY = "a-z8a(^+jtp$m6bp6"57-uuv441=uc45%@q82flay%t#wv)s$41"
SECRET_KEY_BASE_32 = base64..b32encode(SECRET_KEY.encode()).decode()
totp = pyotp.TOTP(SECRET_KEY_BASE_32)
```

Después de jugar un poco con cadenas caracteres y cadenas de bytes podemos fácilmente preguntar por nuestra secuencia de 6 dígitos usando

```
totp.now()
```

Con esto nuestro servidor sabrá cual es el valor de la contraseña en cada momento del tiempo, solamente falta usar el mismo generador en un cliente para que nuestro usuario lo use.

Para esto, debemos entender un poco la implementación de Google Authenticator, que será el cliente escogido para esta labor.

Google Authenticator usa un formato URI para definir las claves, el cual está especificado en [esta página](https://github.com/google/google-authenticator/wiki/Key-Uri-Format). Brevemente el formato que debemos usar debe cumplir con la siguiente estructura:

```
otpauth://totp/<Nombre del sitio>:<cuenta que se autentica>?secret=<Llave en base 32>&issuer=<cuenta que se autentica>
```

O, para nosotros los mortales que seguimos este ejemplo

```
otpauth://totp/contraslash.com:ma0?secret=MEWXUODBFBPCW2TUOASG2NTCOA3DKNZNOV2XMNBUGE6XKYZUGUSUA4JYGJTGYYLZEV2CG53WFFZSINBR&issuer=ma0
```

Lo siguiente será generar un código QR, por fortuna, existe un módulo en python llamado [qrcode](https://pypi.python.org/pypi/qrcode) que hace el trabajo sucio por nosotros.

> Requerimos pillow que no se instala automáticamente como dependencia

```
pip install pillow
pip install qrcode
```

Para generar nuestro código QR ejecutamos el siguiente comando

```
qr "otpauth://totp/contraslash.com:ma0?secret=MEWXUODBFBPCW2TUOASG2NTCOA3DKNZNOV2XMNBUGE6XKYZUGUSUA4JYGJTGYYLZEV2CG53WFFZSINBR&issuer=ma0" > qr.png
```

Y ya tendremos nuestr código qr listo para ser leido por nuestro Google Authenticator

