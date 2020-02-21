---
title: "¿Qué significan los tipos de registro DNS?"
date: "2017-09-07T15:14:58+00:00"
description: "Los tipos de registro DNS permiten identificar un nombre de dominio y relacionarlo con una dirección IP o un valor específico, los mas comunes son A, CNAME, NS, MX y TXT donde cada uno tiene su propio significado"
tags: "DNS"
---
# ¿Qué significan los tipos de registro DNS?

Desde hace tiempo que vengo involucrado con servidores DNS y muchas veces me preguntaba que significan ese montón de tipos de registros que hay, así que el día de hoy decidí investigar un poco mas mientras realizaba una migración de godaddy a AWS 53:

La especificación formal está definida en el [RFC 1035](https://tools.ietf.org/html/rfc1035) y ha sido modificada en múltiples ocaciones, pero en este documento podemos encontrar respuesta a lo que son los tipos de registro mas comunes:

- A
- NS
- CNAME
- MX
- TXT 

## A:

Son la sección final de todo proceso de resolución DNS, pues resuelven finalmente un nombre de dominio a una dirección IP.

Una forma práctica de ver un registro tipo A es un subdominio que apunta a una IP

## NS

Los tipo Name Servers apuntan a un servidor que hará el reproceso de resolución a un registro tipo A u otro.

Estos se refieren usualmente a nuestro servicio DNS en si, que resolverá definitiva o parcialmente el Dominio

## CNAME 

Al igual que los registros tipo A los registros CNAME pueden no causar un reproceso y resolver el dominio, pero también pueden reiniciar el proceso de resolución con un nombre nuevo de dominio, por esta razón son utilizados tradicionalmente como Alias

## MX

Son capaces re resolver finalmente un dominio, pero considerando un orden de prioridades, la especificación propia de este tipo de dominios se encuentra en el [RFC 974](https://tools.ietf.org/html/rfc974)

## TXT

Los registros TXT son los mas sencillos, pues no resulven a una IP sino que retornan un texto plano que puede ser interpretado por quien lo solicita de manera distinta

