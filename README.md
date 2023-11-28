# Biblioteca Virtual 📚

¡Bienvenido al proyecto de la Biblioteca Virtual! Este proyecto proporciona una implementación básica de una biblioteca en Python para gestionar libros. Aquí encontrarás una interfaz para realizar operaciones como agregar, actualizar, buscar, eliminar y mostrar información de los libros.

## Contenido 📋

- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instrucciones](#instrucciones)
- [Funciones Disponibles](#funciones-disponibles)
- [Decisiones de Diseño](#decisiones-de-diseño)

## Estructura del Proyecto 📁

El proyecto está organizado en las siguientes carpetas:

- **entidades**: Contiene las clases `Libro` y `Biblioteca`.

```plaintext
├── entidades
│   ├── biblioteca.py
│   └── libro.py
├── funciones
│   ├── metodos_de_archivo.py
│   └── operaciones_biblioteca.py
├── biblioteca.txt (opcional)
├── main.py
├── README.md
├── .idea
└── .git
```
## Instrucciones 🚀

### Requisitos Previos

Antes de comenzar, asegúrate de tener Python instalado en tu sistema.

### Apertura desde IDE

1. Clona este repositorio en tu sistema local.
2. Abre Visual Studio Code, PyCharm o el IDE que requieras para poder ejecutar código Python.
3. Abre el proyecto en el IDE escogido en el paso anterior.

### Ejecución

Para ejecutar el proyecto:

1. Encuentra el archivo `main.py` en el raiz del proyecto. 
2. Haz clic derecho en `main.py` y selecciona "Run Python File in Terminal" para ejecutar el programa principal.

## Funciones Disponibles 🚀

El programa te permite realizar las siguientes funciones:

1. **Agregar Libros:** Puedes agregar nuevos libros proporcionando información como el título, autor y año de publicación.

2. **Actualizar Libros:** Actualiza la información de un libro existente mediante su ID.

3. **Buscar Libros:** Busca un libro por su ID y muestra su información.

4. **Eliminar Libros:** Elimina un libro por su ID de la biblioteca.

5. **Mostrar Todos los Libros:** Muestra la información de todos los libros en la colección de la biblioteca.

## Documentación 📖

Este proyecto incluye documentación básica en los comentarios del código.

## Decisiones de Diseño 🛠️

Se ha implementado la clase `Libro` para representar los libros y la clase `Biblioteca` para gestionar la colección. 
Se ha buscado mantener el código claro y modular para facilitar la comprensión y el mantenimiento, motivo por el cual se
ha optado por la separación entre entidades y funciones que realiza el programa(directorios para entidades y funciones).

