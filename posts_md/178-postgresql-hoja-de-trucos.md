Title: PostgreSQL Hoja de Trucos
Date: 2017-09-04T14:01:45+00:00
Description: Hoja de trucos y atajos útiles para el manejo de PostgreSQL
Tags: PostgreSQL
---
# PostgreSQL Hoja de TrucosTraducido de [este gist](https://gist.github.com/Kartones/dd3ff5ec5ea238d4c546), 

Traducción realizada en [este gist](https://gist.github.com/ma0c/c444fa967a570dcfbedcb96b4a0bd909)

# PSQL

Palabras mágicas:
```bash
psql -U postgres
```
Si ejecutas con la bandera `-E`, describirá las consultas subyacentes que se realizan con los comandos `\` (genial para aprender).

La mayora de comandos `\d` soportan un parámetro adicional del `__schema__.name__` y aceptan comodines como `*.*`

- `\q`: Salir
- `\c __database__`: Conectarse a una base de datos
- `\d __table__`: Mostrar la definición de una tabla, incluyendo disparadores
- `\dt *.*`: Lista todas las tablas de todos los esquemas (Si no se coloca *.* solamente se buscaran los pertenecientes ap SEARCH_PATH)
- `\l`: Lista de las bases de datos
- `\dn`: Lista de los esquemas
- `\df`: Lista de las funciones
- `\dv`: Lista de las vistas
- `\df+ __function__` : Muestra el código SQL de una funcin
- `\x`: Da una salida mas elaborada mostrando los resultados de la consulta 

Relacionadas con usuarios:
- `\du`: Lista de usuarios
- `\du __username__`: Lista la información de un usuario si está presente
- `create user __username__ with password 'password'`: Crea un usuario __username__ con contrasea password
- `create role __test1__`: Crea un rol con un nombre de usuario específico
- `create role __test2__ noinherit login password __passsword__;`: Crea un rol con un usuario y contraseña
- `set role __test__;`: Cambia el rol de la sesión actual a `__test__`
- `grant __test2__ to __test1__;`: Permite a `__test1__` definir su rol como `__test2__`

## Configuración

- Comandos de gestin de servicio:
```
sudo service postgresql stop
sudo service postgresql start
sudo service postgresql restart
```

- Cambiar la verbosidad del log de Postgtgres:
  <br/>1) Primero edita el archivo de configuración, defone un log que te satisfaga, luego guarda y reinicia postgres:
```
sudo vim /etc/postgresql/9.x/main/postgresql.conf

# Uncomment/Change inside:
log_min_messages = debug5
log_min_error_statement = debug5
log_min_duration_statement = -1

sudo service postgresql restart
```
  2) Ahora puedes ver toneladas de detalles por cada sentencia, error e incluso tareas ejecutándose en segundo plano.
```
tail -f /var/log/postgresql/postgresql-9.x-main.log
```
  3) Se puede añadir quien ejecuto la sentencia en el log, editando el archivo `postgresql.conf`:
```
log_line_prefix = '%t %u %d %a '
```


## Consultas útiles
- `SELECT * FROM pg_proc WHERE proname='__procedurename__'`: Lista los procedimientos/funciones
- `SELECT * FROM pg_views WHERE viewname='__viewname__';`: Lista las vistas, incluidas las definiciones
- `SELECT pg_size_pretty(pg_total_relation_size('__table_name__'));`: Muestra la el espacio de tablas en uso.
- `SELECT pg_size_pretty(pg_database_size('__database_name__'));`: Muestra el espacio de base de datos en uso
- `show statement_timeout;`: Muestra el tiempo límite de finalización de la consulta.
- `SELECT * FROM pg_indexes WHERE tablename='__table_name__' AND schemaname='__schema_name__';`: Muestra los índices de las tablas
- Obtener todos los índices de todas las tablas de un esquema:
```sql
SELECT
   t.relname AS table_name,
   i.relname AS index_name,
   a.attname AS column_name
FROM
   pg_class t,
   pg_class i,
   pg_index ix,
   pg_attribute a,
    pg_namespace n
WHERE
   t.oid = ix.indrelid
   AND i.oid = ix.indexrelid
   AND a.attrelid = t.oid
   AND a.attnum = ANY(ix.indkey)
   AND t.relnamespace = n.oid
    AND n.nspname = 'kartones'
ORDER BY
   t.relname,
   i.relname
```
- Ejecutar datos:
  - Consutas a ser ejecutadas en una base de datos específica:
```sql
SELECT datname, application_name, pid, backend_start, query_start, state_change, state, query 
  FROM pg_stat_activity 
  WHERE datname='__database_name__';
```
  - Obtener todas las consultas a todas las bases de datos esperando por datos. 
```sql
SELECT * FROM pg_stat_activity WHERE waiting='t'
```
  - Consultas ejecutandose con su identificador de procesos:
```sql
SELECT pg_stat_get_backend_pid(s.backendid) AS procpid, 
  pg_stat_get_backend_activity(s.backendid) AS current_query
FROM (SELECT pg_stat_get_backend_idset() AS backendid) AS s;
```

Casting:
- `CAST (column AS type)` or `column::type`
- `'__table_name__'::regclass::oid`: Obtener el identificador dado el nombre de la tabla


## Herramientas
- [pg-top](http://ptop.projects.pgfoundry.org/): `top` para PG. `sudo apt-get install ptop` + `pg_top`
- [Búsqueda inversa en PG como la de Unix](https://dba.stackexchange.com/questions/63453/is-there-a-psql-equivalent-of-bashs-reverse-search-history):
```bash
$ echo "bind "^R" em-inc-search-prev" > $HOME/.editrc
$ source $HOME/.editrc
```