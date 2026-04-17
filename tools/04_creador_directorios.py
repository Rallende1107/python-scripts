from pathlib import Path

def crear_desde_lista(ruta_base, nombres):
    """Lógica central para crear carpetas."""
    creadas = 0
    for nombre in nombres:
        nombre = nombre.strip()
        if not nombre: continue

        nueva_ruta = ruta_base / nombre
        try:
            nueva_ruta.mkdir(parents=True, exist_ok=True)
            print(f"✅ Creada: {nombre}")
            creadas += 1
        except Exception as e:
            print(f"❌ Error en {nombre}: {e}")
    return creadas

def main():
    print("--- 📂 GESTOR DE DIRECTORIOS PRO ---")

    # 1. Ruta destino
    r_input = input("📍 ¿Donde quieres crear las carpetas? (Ruta): ").strip()
    ruta_base = Path(r_input)

    if not ruta_base.exists():
        print("❌ La ruta base no existe.")
        return

    # 2. Menú de opciones
    print("\nSelecciona el origen de los nombres:")
    print("1. Escribir nombres manualmente (separados por comas)")
    print("2. Leer desde un archivo .txt")

    opcion = input("\nElije una opción (1/2): ").strip()

    nombres = []

    if opcion == "1":
        nombres = input("📝 Escribe los nombres: ").split(",")

    elif opcion == "2":
        txt_path = input("📄 Arrastra o pega la ruta del archivo .txt: ").strip().replace('"', '')
        archivo = Path(txt_path)
        if archivo.suffix == ".txt" and archivo.exists():
            # Leemos línea por línea
            with open(archivo, "r", encoding="utf-8") as f:
                nombres = f.readlines()
        else:
            print("❌ Archivo no válido o no encontrado.")
            return
    else:
        print("Opción inválida.")
        return

    # 3. Ejecución
    total = crear_desde_lista(ruta_base, nombres)
    print(f"\n✨ ¡Listo! Se procesaron {total} directorios.")

if __name__ == "__main__":
    main()