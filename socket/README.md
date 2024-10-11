# Proyecto de Comunicacion Cliente-Servidor con Sockets

Este proyecto implementa un sistema de comunicacion entre un cliente y un servidor usando sockets en Python. El servidor puede manejar multiples clientes simultaneamente y permite el intercambio de mensajes entre ellos. Ademas, incluye comandos para listar archivos (`ls`) y descargar archivos (`get`).

## Requisitos

Tener instalado Python 3. Se puede utilizar un entorno virtual para aislar las dependencias del proyecto

## Instalacion

1. **Clonar el repositorio**

   Clona el repositorio con el siguiente comando:
   
   ```bash
    git clone https://github.com/Yuli-M/Backend-I.git 
   cd socket

## Uso
### Ejecutar el servidor

  El servidor debe ser ejecutado primero para aceptar las conexiones de los clientes. El servidor estará escuchando en el puerto 7000 por defecto.

  - Ve a la carpeta del proyecto y ejecuta el servidor:

  ```bash
    python servidor.py
```
  Esto iniciará el servidor y comenzará a escuchar las conexiones entrantes.

### Ejecutar el cliente

  Una vez que el servidor esté en funcionamiento, puedes ejecutar el cliente para conectarte a el.

  - En otra terminal o ventana, ejecuta el cliente:

  ```bash
    python cliente-socket.py
```

  El cliente se conectara al servidor y podrás enviar mensajes o ejecutar comandos.

### Comandos del Cliente

  - Enviar mensajes: Ingresa un mensaje en el cliente y este será enviado a todos los clientes conectados, excepto al que lo envió.

  - Comando ls: Lista los archivos de un directorio. Puedes usarlo de la siguiente manera:

  ```bash
ls <directorio>
```

  Si no se especifica un directorio, listará los archivos del directorio actual.

- Comando get: Descarga un archivo desde el servidor. Ejemplo de uso:

```bash
get <nombre_archivo>
```

El archivo será descargado en la carpeta download del cliente.

- Salir: Para salir del cliente, escribe salir y se cerrará la conexión con el servidor.

## Notas

  Todos los archivos descargados por el cliente se guardarán en la carpeta download dentro del directorio donde se ejecuta el script del cliente.
  
  El servidor es capaz de gestionar múltiples clientes conectados de forma simultánea, permitiendo que se comuniquen entre ellos.

  
