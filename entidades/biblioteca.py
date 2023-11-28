from entidades.libro import Libro

class Biblioteca:
    """
    La clase Biblioteca representa una colección de libros y proporciona
    métodos para agregar, buscar, actualizar, eliminar y mostrar libros.
    """

    def __init__(self):
        """
        Inicializa una instancia de la clase Biblioteca con una lista vacía de libros.
        """
        self.lista_libros = []

    def agregar_libro(self, libro):
        """
        Agrega un libro a la colección de la biblioteca.

        Parámetros:
        - libro: Una instancia de la clase Libro que se agregará a la biblioteca.
        """
        self.lista_libros.append(libro)

    def buscar_libro(self, id):
        """
        Busca un libro por su identificador en la colección de la biblioteca.

        Parámetros:
        - id: El identificador del libro a buscar.

        Retorna:
        Una instancia de la clase Libro si se encuentra, o None si no se encuentra.
        """
        for libro in self.lista_libros:
            if libro.id == id:
                return libro
        return None

    def actualizar_libro(self, id, nuevo_titulo, nuevo_autor, nuevo_año):
        """
        Actualiza la información de un libro en la colección de la biblioteca.

        Parámetros:
        - id: El identificador del libro a actualizar.
        - nuevo_titulo: El nuevo título del libro.
        - nuevo_autor: El nuevo autor del libro.
        - nuevo_año: El nuevo año de publicación del libro.
        """
        
        libro = self.buscar_libro(id)
        if libro:
            libro.titulo = nuevo_titulo
            libro.autor = nuevo_autor
            libro.año_publicacion = nuevo_año

    def eliminar_libro(self, id):
        """
        Elimina un libro de la colección de la biblioteca.

        Parámetros:
        - id: El identificador del libro a eliminar.
        """
        libro = self.buscar_libro(id)
        if libro:
            self.lista_libros.remove(libro)

    def mostrar_libros(self):
        """
        Muestra la información de todos los libros en la colección de la biblioteca.
        """
        for libro in self.lista_libros:
            libro.mostrar_info()
