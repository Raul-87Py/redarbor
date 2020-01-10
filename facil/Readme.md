#crear subnet

$ docker network create --subnet 121.18.0.0/24 pystacknet


#Crear my-sql container:

- descargar contenedor
	version:8.0.18
- generar volumensi no existe

	$ docker volume create mysql-db-data

- arrancar contenedor my-sql
	docker run  -p 27017:27017 --net pystacknet --ip 121.18.0.17

	$ docker run -d -p 33060:3306 --name mysql-db  -e MYSQL_ROOT_PASSWORD=secret --mount src=mysql-db-data,dst=/var/lib/mysql mysql

Y de esta forma ya estamos trabajando con contenedores, como pudieron ver se instaló el Workbench para hacer una conexión vía HTTP y así como lo hacemos al 127.0.0.1:33060 lo podemos hacer a un contenedor remoto.

#arrancr api:

