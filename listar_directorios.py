import os
from pathlib import Path

def listar_directorios(ruta_input: str):
    """
    Función para listar carpetas usando generadores
    y manejo de errores.
    """
    ruta = Path(ruta_input)

    try:
        carpetas = (item.name for item in ruta.iterdir() if item.is_dir())

        print(f"\nContenido de: {ruta.resolve()}")

        for i, nombre in enumerate(sorted(carpetas), 1):
            print(f"{i}. 📁 {nombre}")

    except FileNotFoundError:
        print("Error: La ruta no existe.")
    except PermissionError:
        print("Error: No tienes permisos para leer esta carpeta.")

if __name__ == "__main__":
    # Esto asegura que el código solo se ejecute si lanzas este archivo directamente
    directorio  = input(str("Directorio a analizar: "))
    listar_directorios(directorio)