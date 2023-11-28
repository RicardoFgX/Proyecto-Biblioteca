class Libro:
    """
    La clase Libro representa un libro con atributos como ID, título, autor y año de publicación.
    También proporciona un método para mostrar la información del libro.
    """

    def __init__(self, id, titulo, autor, año_publicacion):
        """
        Inicializa una instancia de la clase Libro con los atributos especificados.

        Parámetros:
        - id: El identificador único del libro.
        - titulo: El título del libro.
        - autor: El autor del libro.
        - año_publicacion: El año de publicación del libro.
        """
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    def mostrar_info(self):
        """
        Muestra la información del libro en la consola.

        Formato de salida:
        ID: [ID], Título: [Título], Autor: [Autor], Año de Publicación: [Año de Publicación]
        """
        print(f"ID: {self.id}, Título: {self.titulo}, Autor: {self.autor}, Año de Publicación: {self.año_publicacion}")
