import os
from pathlib import Path

def menu_dinamico():
    carpeta_tools = Path("tools")

    # 1. Validar que la carpeta tools exista
    if not carpeta_tools.exists() or not carpeta_tools.is_dir():
        print("❌ Error: No se encontró la carpeta 'tools'.")
        return

    while True:
        # 2. Buscar todos los archivos .py en la carpeta tools
        # Ignoramos archivos que empiecen con "__" (como __init__.py)
        scripts = [archivo.name for archivo in carpeta_tools.glob("*.py") if not archivo.name.startswith("__")]

        if not scripts:
            print("⚠️ No se encontraron scripts en la carpeta 'tools'.")
            break

        print("\n" + "="*50)
        print("   🛠️  MI CAJA DE HERRAMIENTAS PYTHON (AUTO)")
        print("="*50)

        # 3. Construir el menú y un diccionario de opciones automáticamente
        opciones = {}
        for i, script in enumerate(sorted(scripts), 1):
            # Formatear el nombre para que se vea más legible en el menú
            nombre_limpio = script.replace(".py", "").replace("_", " ").title()
            print(f"{i}. 🐍 {nombre_limpio}  [{script}]")

            # Guardamos la relación: { "1": "creador_carpetas.py", "2": "gestor_sufijos.py"... }
            opciones[str(i)] = script

        print("-" * 50)
        print("0. ❌ Salir")

        # 4. Pedir la opción al usuario
        seleccion = input(f"\n¿Qué herramienta quieres usar? (0-{len(scripts)}): ").strip()

        if seleccion == "0":
            print("\n👋 ¡Gracias por usar la caja de herramientas! Hasta luego.\n")
            break
        elif seleccion in opciones:
            script_elegido = opciones[seleccion]
            ruta_script = carpeta_tools / script_elegido

            print(f"\n🚀 Iniciando: {script_elegido}...")
            print("-" * 30)

            # 5. Ejecutar el script seleccionado
            os.system(f'python "{ruta_script}"')

            print("-" * 30)
            print("✅ Ejecución finalizada. Volviendo al menú principal...")
        else:
            print(f"\n❌ Opción no válida. Por favor, selecciona un número del 0 al {len(scripts)}.")

if __name__ == "__main__":
    menu_dinamico()