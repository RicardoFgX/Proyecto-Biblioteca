from entidades.libro import Libro


def menu():
    """
    Muestra el menú de operaciones disponibles al usuario.
    """
    print("Operaciones disponibles:")
    print("1. Agregar libro")
    print("2. Actualizar libro")
    print("3. Buscar libro")
    print("4. Eliminar libro")
    print("5. Mostrar todos los libros")
    print("6. Salir")


def obtener_entero_input(mensaje):
    """
    Solicita al usuario un número entero a través de la entrada estándar.

    Parámetros:
    - mensaje: Un mensaje que se mostrará al usuario antes de solicitar la entrada.

    Retorna:
    Un número entero ingresado por el usuario.

    Ejemplos:
    >>> obtener_entero_input("Ingrese su edad: ")
    Ingrese su edad: 25
    25
    """
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Ingrese un número válido.")


def agregar_libro(biblioteca):
    """
    Solicita al usuario la información de un nuevo libro y lo agrega a la biblioteca si no existe.

    Parámetros:
    - biblioteca: Una instancia de la clase Biblioteca a la que se agregará el nuevo libro.
    """
    print("Ingrese la información del nuevo libro:")
    id = obtener_entero_input("ID: ")

    if biblioteca.buscar_libro(id) is not None:
        print(f"Ya existe un libro con la ID {id}. No se puede agregar el libro.")
    else:
        titulo = input("Título: ")
        autor = input("Autor: ")
        año_publicacion = obtener_entero_input("Año de Publicación: ")

        nuevo_libro = Libro(id, titulo, autor, año_publicacion)
        biblioteca.agregar_libro(nuevo_libro)
        print("Libro agregado con éxito.")


def actualizar_libro(biblioteca):
    """
    Permite al usuario actualizar la información de un libro en la biblioteca.

    Parámetros:
    - biblioteca: Una instancia de la clase Biblioteca en la que se actualizará el libro.
    """
    print("Lista de libros:")
    biblioteca.mostrar_libros()

    id = obtener_entero_input("Ingrese el ID del libro que desea actualizar: ")
    libro = biblioteca.buscar_libro(id)

    if libro:
        print("Ingrese la nueva información del libro:")
        nuevo_titulo = input("Nuevo Título: ")
        nuevo_autor = input("Nuevo Autor: ")
        nuevo_año = obtener_entero_input("Nuevo Año de Publicación: ")

        biblioteca.actualizar_libro(id, nuevo_titulo, nuevo_autor, nuevo_año)
        print("Libro actualizado con éxito.")
    else:
        print("Libro no encontrado.")
        print("Volviendo al menú principal...")


def buscar_libro(biblioteca):
    """
    Permite al usuario buscar un libro por su ID en la biblioteca.

    Parámetros:
    - biblioteca: Una instancia de la clase Biblioteca en la que se buscará el libro.
    """
    id = obtener_entero_input("Ingrese el ID del libro que desea buscar: ")
    libro = biblioteca.buscar_libro(id)

    if libro:
        print("Información del libro encontrado:")
        libro.mostrar_info()
    else:
        print("Libro no encontrado.")



def eliminar_libro(biblioteca):
    """
    Permite al usuario eliminar un libro por su ID de la biblioteca.

    Parámetros:
    - biblioteca: Una instancia de la clase Biblioteca de la que se eliminará el libro.
    """
    print("Lista de libros:")
    biblioteca.mostrar_libros()


    id = obtener_entero_input("Ingrese el ID del libro que desea eliminar: ")
    libro = biblioteca.buscar_libro(id)

    if libro:
        biblioteca.eliminar_libro(id)
        print("Libro eliminado con éxito.")
    else:
        print("Libro no encontrado.")
        print("Volviendo al menú principal...")

