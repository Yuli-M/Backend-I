# Implementación Simple de RPC en Python

Un sistema ligero de Remote Procedure Call (RPC) implementado en Python utilizando sockets. Este proyecto te permite ejecutar funciones en un servidor remoto de manera sencilla, como si fueran locales.

## Prerequisitos

- **Python 3.6+**: tener Python instalado. 
- **Acceso a la Red**: los puertos especificados deben estar abiertos y no bloqueados por firewalls.

## Instalación

1. **Clonar el Repositorio**

   ```bash
   git clone https://github.com/Yuli-M/Backend-I.git 
   cd RPC

2. **Crear un Entorno Virtual (Opcional)**

  Entorno virtual para gestionar las dependencias.
  
  ```bash
  python3 -m venv venv
  source venv/bin/activate  
  ```
## Uso  
### Iniciando el Servidor
1. **Navegar al Directorio del Proyecto**
    Estar en el directorio raíz del proyecto.

2. **Ejecutar el Servidor**

    ```bash
    python server.py

El servidor comenzará a escuchar en localhost en el puerto 8080 por defecto.

### Ejecutando el Cliente

1. **Abrir una Nueva Ventana de Terminal**

2. **Navegar al Directorio del Proyecto**

3. **Ejecutar el Cliente**

    ```bash
    python cliente.py

Salida:

```bash

11
-1
Saludo
```


Esto demuestra la llamada a tres métodos remotos: add, sub y hi.

## Estructura del proyecto

**cliente.py:** El script del cliente que se conecta al servidor RPC y llama a métodos remotos.

**server.py:** El script del servidor que registra métodos y escucha solicitudes de clientes.

**rpc.py:** Contiene las clases RPCServer y RPCClient que manejan la funcionalidad central de RPC.




