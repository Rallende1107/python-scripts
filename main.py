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
            nombre_base = script.replace(".py", "")

            # Cortamos el nombre en dos partes usando el primer guion bajo
            # Ejemplo: "01_listar_directorios" se convierte en ["01", "listar_directorios"]
            partes = nombre_base.split("_", 1)

            # Si la primera parte es un número, le agregamos un guion elegante
            if partes[0].isdigit() and len(partes) > 1:
                texto_restante = partes[1].replace("_", " ").title()
                nombre_limpio = f"{partes[0]} - {texto_restante}"
            else:
                # Si por alguna razón un archivo no tiene número, se formatea normal
                nombre_limpio = nombre_base.replace("_", " ").title()

            print(f"{i}. 🐍 {nombre_limpio}  [{script}]")

            # Guardamos la relación: { "1": "01_creador_carpetas.py", "2": "02_gestor_sufijos.py"... }
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