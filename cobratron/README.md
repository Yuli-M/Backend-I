# Sistema de gestion de pagos con postgresql
## Requisitos
- PostgreSQL 9.6 o superior.
- Tener acceso a un entorno de base de datos postgresql donde puedas ejecutar estos scripts.

## Pasos
- Clona este repositorio.
- Conéctate a tu base de datos postgresql.
- Ejecuta los scripts para crear las tablas y funciones en tu base de datos.
- Utiliza las funciones proporcionadas para crear clientes, aplicar pagos y generar reportes.

## Tablas
- clients - Esta tabla almacena la información básica de los clientes.
- payments - Esta tabla almacena los pagos realizados por cada cliente.

## Funciones
- create_client-Función para crear un nuevo cliente en la base de datos.
- apply_payments -Función para generar los pagos de un cliente en función de la frecuencia seleccionada (Semanal, Mensual, Trimestral, Semestral, Anual). Esta función calcula todas las fechas de pago hasta la fecha final y las inserta en la tabla payments.
- report_client-Función para generar un reporte de los pagos de un cliente, mostrando las fechas de pago y el estado del pago
- pay_payment- Función para marcar un pago como realizado. Cambia el estado de paid a TRUE si el monto del pago es igual o mayor al monto esperado.

## Entorno de Desarrollo
Este proyecto fue desarrollado y probado en:
- Sistema Operativo: Ubuntu 22.04.
- Docker: El proyecto se puede ejecutar en un contenedor.
- Base de Datos: PostgreSQL 16.4.
