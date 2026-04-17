import os

def menu():
    while True:
        print("\n" + "="*40)
        print("   🛠️  MI CAJA DE HERRAMIENTAS PYTHON")
        print("="*40)
        print("1.-  Listar Directorios")
        print("2.-  Creador de Carpetas")
        print("3.-  Gestor de Sufijos (Añadir/Quitar)")
        print("4.-  Limpiar Nombres (Archivos y Carpetas)")
        print("5.-  Limpiar Nombres de Carpetas (Palabra específica)")
        print("6.-  Organizar por Autor (Regex)")
        print("-" * 40)
        print("0.-  Salir")

        opcion = input("\n¿Qué herramienta quieres usar? (0-6): ").strip()

        if opcion == "1":
            os.system("python tools/listar_directorios.py")
        elif opcion == "2":
            os.system("python tools/creador_carpetas.py")
        elif opcion == "3":
            os.system("python tools/gestor_sufijos.py")
        elif opcion == "4":
            os.system("python tools/limpiar_nombres.py")
        elif opcion == "5":
            os.system("python tools/limpiar_nombres_carpetas.py")
        elif opcion == "6":
            os.system("python tools/organizar_por_autor.py")
        elif opcion == "0":
            print("\n👋 ¡Gracias por usar la caja de herramientas! Hasta luego.\n")
            break
        else:
            print("\n❌ Opción no válida. Por favor, selecciona un número del 0 al 6.")

if __name__ == "__main__":
    menu()