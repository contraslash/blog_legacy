Title: Instalando Freeling
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: PLN
---
# Instalando FreelingPrimero:
 ```sudo apt-get install libboost-regex-dev libicu-dev
 sudo apt-get install libboost-system-dev libboost-program-options-dev
 ```
 
 pero resulta que tambien necesito 
 
 `sudo apt-get install libboost-thread-dev`
 
 Luego, si sale algo como 
`undefined reference to boost::system::generic_category`

toca `make distclean`
editar `src/automake_options.am`
colocar en las lineas del boost_old
```
if BOOST_OLD
  ADD_FL_DEPS=-lboost_thread$(MT) -lboost_system$(MT)
else
  ADD_FL_DEPS=-lboost_system$(MT)
endif
```
 
 y luego 
 
 ```aclocal; autoconf; automake -a;
 ./configure
 make
 sudo make install 
 ```
 y ya
 :D 