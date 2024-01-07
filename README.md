# Proyecto de ejemplo de una aplicación en flask

Proyecto basado en una arquitectura de microservicios, enfocado a mantener una estructura de capas aisladas entre la base de datos, los servicios y las rutas 

## Instalación

### Creación de un entorno virtual
**Es necesario tener instalado [virtualenv](https://virtualenv.pypa.io/en/latest/) para esto**

En la carpeta del proyecto ejecutar el siguiente comando para instalar las dependencias necesarias en un entorno virtual

```bash
python -m virtualenv venv
```

### Instalación de dependencias
Ejecutar lo siguiente en la carpeta del proyecto

```bash
pip install -r requirements.txt
cd app
python main.py
```

## Rutas

- Ruta principal `/`: Se abre automaticamente al ejecutar la aplicación. Muestra el formulario para buscar personas por nombre y apellido
- Ruta `/search`: Es la ruta usada para buscar personas por nombre y appelido usando el metodo **POST** Devuelve el JSON requerido

## Vistas

### Index

## Diseño de la base de datos
![Diagrama de base de datos](/docs/db_design.png)
- Uso de llaves primarias y llaves foraneas para mantener la integridad referencial
