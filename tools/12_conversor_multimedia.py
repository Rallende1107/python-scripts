import os
from pathlib import Path

try:
    from PIL import Image
    from moviepy import VideoFileClip
except ImportError:
    print("❌ Faltan librerías necesarias.")
    print("Ejecuta: pip install Pillow moviepy")
    exit()

class ConversorMedia:
    def __init__(self):
        self.convertidos = 0
        self.omitidos = 0
        self.errores = 0
        self.archivos_originales = []  # Guardaremos los originales para borrarlos al final si el usuario quiere
        self.por_extension = {}

    def procesar_directorio(self, ruta_str, modo):
        ruta_base = Path(ruta_str)
        if not ruta_base.is_dir():
            print("❌ La ruta del directorio no es válida.")
            return

        ext_img = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif'}
        ext_vid = {'.mp4', '.avi', '.mov', '.mkv'}

        print("\n🚀 Iniciando conversión...")

        # rglob("*") recorre la carpeta y todas sus subcarpetas
        for archivo in ruta_base.rglob("*"):
            if not archivo.is_file():
                continue

            ext = archivo.suffix.lower()

            # Modo 1: Imágenes, Modo 2: Videos, Modo 3: Ambos
            if (modo in [1, 3] and ext in ext_img):
                self.convertir_imagen(archivo)
            elif (modo in [2, 3] and ext in ext_vid):
                self.convertir_video(archivo)

    def convertir_imagen(self, archivo: Path):
        try:
            nueva_ruta = archivo.with_suffix('.webp')

            if nueva_ruta.exists():
                print(f"⚠️ Omitido: {nueva_ruta.name} ya existe.")
                self.omitidos += 1
                return

            with Image.open(archivo) as img:
                img.save(nueva_ruta, 'WEBP')

            print(f"🖼️  Convertido: {archivo.name} -> {nueva_ruta.name}")
            self._registrar_exito(archivo, '.webp')

        except Exception as e:
            print(f"❌ Error con imagen {archivo.name}: {e}")
            self.errores += 1

    def convertir_video(self, archivo: Path):
        try:
            nueva_ruta = archivo.with_suffix('.webm')

            if nueva_ruta.exists():
                print(f"⚠️ Omitido: {nueva_ruta.name} ya existe.")
                self.omitidos += 1
                return

            print(f"⏳ Convirtiendo video (esto puede tardar): {archivo.name}")
            # logger=None evita que moviepy llene la consola de texto basura
            with VideoFileClip(str(archivo)) as clip:
                clip.write_videofile(str(nueva_ruta), logger=None)

            print(f"🎬 Convertido: {archivo.name} -> {nueva_ruta.name}")
            self._registrar_exito(archivo, '.webm')

        except Exception as e:
            print(f"❌ Error con video {archivo.name}: {e}")
            self.errores += 1

    def _registrar_exito(self, archivo_original: Path, nueva_ext: str):
        self.convertidos += 1
        self.archivos_originales.append(archivo_original)
        self.por_extension[nueva_ext] = self.por_extension.get(nueva_ext, 0) + 1

    def limpiar_originales(self):
        if not self.archivos_originales:
            return

        print("\n🗑️  Limpiando archivos originales...")
        for archivo in self.archivos_originales:
            try:
                archivo.unlink()
                print(f"✔ Eliminado: {archivo.name}")
            except Exception as e:
                print(f"❌ No se pudo eliminar {archivo.name}: {e}")

    def mostrar_resumen(self):
        print("\n" + "="*30)
        print("📊 RESUMEN DE CONVERSIÓN")
        print("="*30)
        print(f"✅ Convertidos exitosamente: {self.convertidos}")
        print(f"⚠️  Omitidos (ya existían): {self.omitidos}")
        print(f"❌ Errores: {self.errores}")

        if self.por_extension:
            print("\nDetalle por formato nuevo:")
            for ext, cant in self.por_extension.items():
                print(f"  {ext}: {cant} archivos")
        print("="*30)

def menu_principal():
    print("--- 🔄 CONVERSOR MULTIMEDIA (WebP / WebM) ---")
    print("1. Convertir Imágenes a WebP")
    print("2. Convertir Videos a WebM")
    print("3. Convertir Todo (Imágenes y Videos)")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ").strip()

    if opcion == "4":
        return
    if opcion not in ["1", "2", "3"]:
        print("❌ Opción inválida.")
        return

    ruta = input("📁 Ingresa la ruta del directorio: ").strip().replace('"', '')

    conversor = ConversorMedia()
    conversor.procesar_directorio(ruta, int(opcion))
    conversor.mostrar_resumen()

    if conversor.convertidos > 0:
        resp = input("\n¿Deseas ELIMINAR los archivos originales antiguos? (s/n): ").strip().lower()
        if resp == 's':
            conversor.limpiar_originales()
        else:
            print("📦 Los archivos originales se han conservado.")

if __name__ == "__main__":
    menu_principal()