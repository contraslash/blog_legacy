Title: Reglas para desarrollar código seguro
Date: 2016-12-12T21:00:09+00:00
Description: Reglas para desarrollar código seguro para segmentos críticos del proyecto, basado en un artículo de Gerard J. Holzmann, del Laboratorio de código fiable de la NASA
Tags: Buenas Prácticas
---
# Reglas para desarrollar código seguroLas siguientes reglas están extraidas de [este artículo](http://spinroot.com/gerard/pdf/P10.pdf) de Gerard J. Holzmann. 

La mayoría de programadores siguen una guía de estilos para programar, pero usualmente estas guías no muestran la calidad del código. La mayoría de guías suelen estar enfocadas a un Lenguaje de programación o a un Framework en específico y presentan mas un manual de como debería verse en vez de cómo debería funcionar.

Las siguientes reglas están enfocadas a C, pero pueden extenderse con facilidad para otros Lenguajes de programación:

1. Restrinja todo su código a estructuras simples de control, evite la recursión directa o indirecta.
1. Todos los ciclos deben tener un límite superior, debería ser posible determinar que un programa no se ejecutará infinitamente con un chequeo básico. Si el límite de un ciclo no puede ser probado estáticamente, esta regla se considera violada.
1. No utilice localización dinámica de memoria después de la inicialización.
1. Cada función no debería ser mas larga de una hoja de papel, esto se traduce en un máximo de 60 líneas de código
1. La densidad de aserciones no debería sobrepasar dos por función, y siempre deberían ser consideradas como test booleanos
1. Los objetos que contienen datos deberían definirse en el ámbito mas pequeño posible.
1. El valor de retorno de cada función debe verificarse después de cada llamado y la validación de cada parámetro debe realizarse dentro de cada función
1. El código debería ser compilado frecuentemente desde el primer día de desarrollo, con todos los advertencias activadas.