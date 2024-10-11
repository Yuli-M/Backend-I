# Proyecto Flask con PostgreSQL - Endpoint Usuarios y Torre

Este proyecto es una API simple utilizando Flask y PostgreSQL para gestionar usuarios. Existen dos endpoints principales: uno para obtener todos los usuarios y otro para obtener usuarios basados en su torre_id.
Requisitos

## Instalación de dependencias:

Tener instalados los siguientes paquetes:

  - Python 3.x
  - PostgreSQL
  - Librerías de Python (Flask y psycopg2)



## Configuración de la base de datos:

Crear un archivo database.ini en el directorio raíz del proyecto (ya está incluido en la carpeta endpointUsuarioTorre) con la siguiente estructura:
```bash
#ini

[postgresql]
host=localhost
database=torres
user=postgres
password=tu_password
```
 Reemplazar tu_password con tu contraseña de PostgreSQL.

 
 ## Configuración de la base de datos

Se debe tener una base de datos llamada torres con una tabla usuario. 


## Ejecución de la aplicación

Para ejecutar la API, primero el servidor de PostgreSQL debe estar en ejecución y que las credenciales en database.ini sean correctas.

Luego, ejecuta el archivo hello.py:

```bash

flask --app hello run

```
## Endpoints disponibles
   
Obtener todos los usuarios

  -Método: GET
  -Ruta: /usuarios
  -Descripción: Retorna una lista con todos los usuarios registrados en la base de datos.

Obtener usuarios por torre_id

  -Método: GET
  -Ruta: /usuarios/<int:torre_id>
  -Descripción: Retorna todos los usuarios con un determinado torre_id.


## Ejemplo de Uso

  Para obtener todos los usuarios,  hacer una petición GET a:

  ```bash
    http://localhost:8080/usuarios
```

Para obtener usuarios filtrados por torre_id, puedes hacer una petición GET a:

```bash
  http://localhost:8080/usuarios/<torre_id>


