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
### Levantamiento de la base de datos
Eecuta las sentencias SQL de [db.sql](/sql/db.sql) para crear las tablas necesarias para el proyecto

### Configuración de las variables de entorno
Crea un archivo .env donde configures los siguientes valores para conectar correctamente la base de datos
```bash
MYSQL_USER=
MYSQL_PASSWORD=
MYSQL_HOST=
MYSQL_DB=
```

## Rutas

- Ruta principal `/`: Se abre automaticamente al ejecutar la aplicación. Muestra el formulario para buscar personas por nombre y apellido
- Ruta `/search`: Es la ruta usada para buscar personas por nombre y appelido usando el metodo **POST** Devuelve el JSON requerido

## Vistas

### Index
![index](/docs/index_view.png)

### Persona encontrada
![persona_encontrada](/docs/persona_encontrada.png)
![true](/docs/true.png)

### Persona no encontrada
![persona_encontrada](/docs/persona_no_encontrada.png)
![true](/docs/false.png)

## Diseño de la base de datos
![Diagrama de base de datos](/docs/db_design.png)
- Uso de llaves primarias y llaves foraneas para mantener la integridad referencial


## Notas del proyecto

- Debido a la prontitud de la prueba y la fecha de esta (domingo) no tuve la capacidad de tiempo para realizar pruebas unitarias y hacer el deploy de la app (punto 5 y 7) sin embargo considero que con un dia mas de trabajo podria realizar exitosamente esos puntos.
- Para un proyecto mas grande elegiria una estructura de carpetas diferente enfocada en microservicios y en alguna arquitectura clean dependiendo de las necesidades del proyecto