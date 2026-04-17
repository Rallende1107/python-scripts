import shutil
from pathlib import Path

def vaciar_directorio(ruta_str: str):
    ruta = Path(ruta_str)

    if not ruta.is_dir():
        print("❌ Error: La ruta no existe o no es un directorio.")
        return

    print(f"\n⚠️  ATENCIÓN: Vas a borrar TODO el contenido de:")
    print(f"👉 {ruta.resolve()}")
    confirmacion = input("¿Estás 100% seguro? (s/n): ").strip().lower()

    if confirmacion != "s":
        print("🚫 Operación cancelada. Tus archivos están a salvo.")
        return

    print("-" * 30)
    for item in ruta.iterdir():
        try:
            # is_symlink() previene que borremos archivos a los que apunta un acceso directo
            if item.is_file() or item.is_symlink():
                item.unlink() # Borra el archivo
            elif item.is_dir():
                shutil.rmtree(item) # Borra la carpeta y todo su contenido
            print(f"✔ Borrado: {item.name}")
        except Exception as e:
            print(f"❌ Error borrando {item.name}: {e}")

    print("-" * 30)
    print("🏁 Carpeta vaciada con éxito.")

if __name__ == "__main__":
    r = input("Ingresa la ruta de la carpeta que quieres vaciar: ").strip()
    vaciar_directorio(r)