from funciones.operaciones_biblioteca import menu, agregar_libro, actualizar_libro, buscar_libro, eliminar_libro
from funciones.metodos_de_archivo import cargar_desde_archivo, guardar_en_archivo


def main():
    """
    Función principal que gestiona la interacción del usuario con la biblioteca.

    Carga una biblioteca desde un archivo, muestra un menú de operaciones disponibles
    y realiza las operaciones seleccionadas por el usuario. Permite agregar, actualizar,
    buscar, eliminar y mostrar libros, así como guardar la biblioteca en un archivo al salir.
    Para esta última opción se realiza al salir del programa, ya se por el menú o de forma abrupta.

    """
    archivo = "biblioteca.txt"
    biblioteca = cargar_desde_archivo(archivo)

    try:
        while True:
            menu()
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                agregar_libro(biblioteca)
            elif opcion == '2':
                actualizar_libro(biblioteca)
            elif opcion == '3':
                buscar_libro(biblioteca)
            elif opcion == '4':
                eliminar_libro(biblioteca)
            elif opcion == '5':
                biblioteca.mostrar_libros()
            elif opcion == '6':
                guardar_en_archivo(biblioteca, archivo)
                print("Saliendo del programa. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")
    except KeyboardInterrupt:
        print("\nPrograma interrumpido. ¡Hasta luego!")
        guardar_en_archivo(biblioteca, archivo)


if __name__ == "__main__":
    main()
