from pathlib import Path

def limpiar_nombres_directorios(ruta_str: str, palabra: str):
    ruta_raiz = Path(ruta_str)
    if not ruta_raiz.is_dir():
        print("❌ La ruta no es válida.")
        return

    print(f"--- Limpiando la palabra '{palabra}' ---")

    for carpeta in ruta_raiz.iterdir():
        # Solo directorios y que contengan la palabra
        if carpeta.is_dir() and palabra in carpeta.name:
            nuevo_nombre = carpeta.name.replace(palabra, "").strip()

            if not nuevo_nombre:
                print(f"⚠️ Omitido: '{carpeta.name}' (quedaría sin nombre)")
                continue

            nueva_ruta = carpeta.with_name(nuevo_nombre)

            if nueva_ruta.exists():
                print(f"⚠️ Omitido: '{nuevo_nombre}' ya existe.")
                continue

            try:
                carpeta.rename(nueva_ruta)
                print(f"✅ {carpeta.name} -> {nuevo_nombre}")
            except Exception as e:
                print(f"❌ Error al renombrar {carpeta.name}: {e}")

if __name__ == "__main__":
    r = input("Ingresa la ruta de la carpeta: ").strip()
    p = input("Palabra a eliminar: ").strip()
    limpiar_nombres_directorios(r, p)