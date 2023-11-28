from entidades.biblioteca import Biblioteca
from entidades.libro import Libro


def guardar_en_archivo(biblioteca, archivo):
    """
    Guarda la información de la biblioteca en un archivo de texto, si no existe el archivo al guardar, se crea
    automáticamente. Para guardar se itera cada libro de la lista "Biblioteca"

    Parámetros:
    - biblioteca: Una instancia de la clase Biblioteca que contiene la colección de libros.
    - archivo: El nombre del archivo de texto en el que se guardará la información.
    """
    with open(archivo, 'w') as file:
        for libro in biblioteca.lista_libros:
            file.write(f"{libro.id},{libro.titulo},{libro.autor},{libro.año_publicacion}\n")


def cargar_desde_archivo(archivo):
    """
    Carga la información de la biblioteca desde un archivo de texto.

    Parámetros:
    - archivo: El nombre del archivo de texto del que se cargará la información.

    Retorna:
    Una instancia de la clase Biblioteca con la información cargada desde el archivo.
    """
    biblioteca = Biblioteca()
    try:
        with open(archivo, 'r') as file:
            for line in file:
                datos = line.strip().split(',')
                libro = Libro(int(datos[0]), datos[1], datos[2], int(datos[3]))
                biblioteca.agregar_libro(libro)
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no se encontró. Se creará uno nuevo.")
    return biblioteca
