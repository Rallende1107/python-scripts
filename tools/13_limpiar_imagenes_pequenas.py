from pathlib import Path


try:
    from PIL import Image
except ImportError:
    print("❌ Falta la librería Pillow.")
    print("Ejecuta: pip install Pillow")
    exit()

def limpiar_imagenes_pequenas(ruta_str: str, minimo_px: int):
    ruta_base = Path(ruta_str)

    if not ruta_base.is_dir():
        print("❌ El directorio no es válido.")
        return

    extensiones = {'.png', '.jpg', '.jpeg', '.webp', '.bmp'}
    eliminadas = 0
    errores = 0

    print(f"\n🔍 Buscando imágenes con ancho o alto menor a {minimo_px}px...")
    print("-" * 40)

    for archivo in ruta_base.rglob("*"):
        if archivo.is_file() and archivo.suffix.lower() in extensiones:
            try:
                with Image.open(archivo) as img:
                    ancho, alto = img.size

                # Si es más pequeña que el mínimo, se elimina
                if ancho < minimo_px or alto < minimo_px:
                    archivo.unlink()
                    print(f"🗑️ Eliminada: {archivo.name} ({ancho}x{alto})")
                    eliminadas += 1

            except Exception as e:
                print(f"❌ Error al leer {archivo.name}: {e}")
                errores += 1

    print("-" * 40)
    print(f"✅ Proceso terminado. Se eliminaron {eliminadas} imágenes pequeñas.")
    if errores > 0:
        print(f"⚠️ Hubo {errores} archivos que no se pudieron leer.")

if __name__ == "__main__":
    print("--- 🧹 LIMPIADOR DE IMÁGENES PEQUEÑAS ---")
    r = input("📁 Directorio de imágenes: ").strip().replace('"', '')

    try:
        m = int(input("📏 Tamaño mínimo permitido en píxeles (ej: 100): ").strip())
    except ValueError:
        print("❌ Debes ingresar un número válido.")
        exit()

    limpiar_imagenes_pequenas(r, m)