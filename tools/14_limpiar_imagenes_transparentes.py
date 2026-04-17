from pathlib import Path
from PIL import Image

def calcular_transparencia(imagen: Image.Image) -> float:
    """Devuelve el porcentaje de píxeles transparentes de la imagen."""
    if imagen.mode in ('RGBA', 'LA') or (imagen.mode == 'P' and 'transparency' in imagen.info):
        imagen = imagen.convert('RGBA')
        alfa = imagen.split()[-1] # Obtiene solo el canal Alpha

        total_pixeles = imagen.width * imagen.height
        # Cuenta los píxeles que no son completamente opacos (menor a 255)
        pixeles_transparentes = sum(1 for pixel in alfa.getdata() if pixel < 255)

        return (pixeles_transparentes / total_pixeles) * 100
    return 0.0

def limpiar_transparentes(ruta_str: str, umbral: float):
    ruta_base = Path(ruta_str)

    if not ruta_base.is_dir():
        print("❌ El directorio no es válido.")
        return

    extensiones = {'.png', '.webp', '.gif'} # Principalmente formatos que soportan transparencia
    procesadas = 0
    eliminadas = 0

    print(f"\n🔍 Buscando imágenes con más del {umbral}% de transparencia...")
    print("-" * 40)

    for archivo in ruta_base.rglob("*"):
        if archivo.is_file() and archivo.suffix.lower() in extensiones:
            procesadas += 1
            try:
                with Image.open(archivo) as img:
                    porcentaje = calcular_transparencia(img)

                if porcentaje >= umbral:
                    archivo.unlink()
                    print(f"👻 Eliminada: {archivo.name} ({porcentaje:.1f}% transparente)")
                    eliminadas += 1

            except Exception as e:
                print(f"❌ Error procesando {archivo.name}: {e}")

    print("-" * 40)
    print(f"✅ ¡Listo! Se procesaron {procesadas} imágenes y se eliminaron {eliminadas}.")

if __name__ == "__main__":
    print("--- 👻 LIMPIADOR DE IMÁGENES TRANSPARENTES ---")
    r = input("📁 Directorio de imágenes: ").strip().replace('"', '')

    try:
        u_input = input("🎚️ Umbral de transparencia para eliminar (1-99, Enter para 100%): ").strip()
        u = float(u_input) if u_input else 100.0
    except ValueError:
        print("❌ Debes ingresar un número válido.")
        exit()

    limpiar_transparentes(r, u)