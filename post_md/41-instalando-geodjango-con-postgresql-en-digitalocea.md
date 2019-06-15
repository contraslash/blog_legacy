Title: Instalando GeoDjango con Postgresql en DigitalOcean con Ubuntu 14.04
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: Django,Linux,Ubuntu,PostgreSQL,GeoDjango,Digital Ocean
---
# Instalando GeoDjango con Postgresql en DigitalOcean con Ubuntu 14.04
apt-get update
# Instalamos compiladores de C y otro utiles
sudo apt-get install build-essential
# Instalamos Postgres
sudo apt-get install postgresql postgresql-contrib
# Instalamos Postgres Server
sudo apt-get install postgresql-server-dev-9.3



# GEOS
sudo apt-get install binutils libproj-dev gdal-bin
wget http://download.osgeo.org/geos/geos-3.3.8.tar.bz2
tar xjf geos-3.3.8.tar.bz2
cd geos-3.3.8
./configure
make
sudo make install
cd ..

# Proj4
wget http://download.osgeo.org/proj/proj-4.8.0.tar.gz
wget http://download.osgeo.org/proj/proj-datumgrid-1.5.tar.gz

tar xzf proj-4.8.0.tar.gz
cd proj-4.8.0/nad
tar xzf ../../proj-datumgrid-1.5.tar.gz
cd ..
./configure
make
sudo make install
cd ../

# GDAL
wget http://download.osgeo.org/gdal/gdal-1.9.2.tar.gz
tar xzf gdal-1.9.2.tar.gz
cd gdal-1.9.2


./configure
make
sudo make install
cd ..

# Luego instalaremos POSTGIS
wget http://download.osgeo.org/postgis/source/postgis-2.1.5.tar.gz
tar xzf postgis-2.1.5.tar.gz
cd postgis-2.1.5
# Algunas librerías necesarias
sudo apt-get install libpq-dev libxml2-dev

./configure
make
sudo make install