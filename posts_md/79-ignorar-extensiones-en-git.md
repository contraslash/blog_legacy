Title: Ignorar extensiones en git
Date: 2016-02-16T18:19:24+00:00
Description: 
Tags: git
---
# Ignorar extensiones en gitPara ignorar algunas extensiones siempre, lo que haremos será crear un archivo *.gitignore_global* que funcionará como un archivo *.gitignore*, pero que se tendrá siempre en cuenta.

Luego añadiremos el archivo a la configuración de git

```
touch ~/.gitignore_global
git config --global core.excludesfile '~/.gitignore_global'
```