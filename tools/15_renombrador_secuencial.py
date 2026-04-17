from pathlib import Path
import re

def texto_valido(texto: str) -> bool:
    """Verifica que el texto no contenga caracteres prohibidos por el sistema operativo."""
    if re.search(r'[<>:"/\\|?*\x00-\x1F]', texto):
        return False
    if not texto.strip():
        return False
    return True

def renombrado_secuencial(ruta_str: str, nuevo_nombre_base: str):
    ruta_base = Path(ruta_str)

    if not ruta_base.is_dir():
        print("❌ La ruta ingresada no es válida o no existe.")
        return

    # Diccionario para llevar la cuenta independiente por cada extensión
    contador_por_tipo = {}
    renombrados = 0
    errores = 0

    print(f"\n🚀 Iniciando renombrado masivo a: '{nuevo_nombre_base} (X).ext'")
    print("-" * 40)

    # Iteramos solo sobre los archivos de la carpeta principal (no carpetas ni subcarpetas)
    for archivo in ruta_base.iterdir():
        if archivo.is_file():
            ext = archivo.suffix.lower()

            # Aumentar el contador para esta extensión
            contador_por_tipo[ext] = contador_por_tipo.get(ext, 0) + 1

            # Formatear el nuevo nombre: NombreBase (1).ext
            nuevo_nombre = f"{nuevo_nombre_base} ({contador_por_tipo[ext]}){ext}"
            nueva_ruta = archivo.with_name(nuevo_nombre)

            # Evitar colisiones si el archivo por casualidad ya se llama así
            while nueva_ruta.exists() and nueva_ruta != archivo:
                contador_por_tipo[ext] += 1
                nuevo_nombre = f"{nuevo_nombre_base} ({contador_por_tipo[ext]}){ext}"
                nueva_ruta = archivo.with_name(nuevo_nombre)

            try:
                archivo.rename(nueva_ruta)
                print(f"✅ {archivo.name} -> {nuevo_nombre}")
                renombrados += 1
            except Exception as e:
                print(f"❌ Error al renombrar {archivo.name}: {e}")
                errores += 1

    print("-" * 40)
    print(f"🎉 Proceso completado. {renombrados} archivos renombrados.")
    if errores > 0:
        print(f"⚠️ Hubo errores en {errores} archivos.")

if __name__ == "__main__":
    print("--- 🏷️  RENOMBRADOR SECUENCIAL MASIVO ---")
    r = input("📁 Ingresa la ruta de la carpeta: ").strip().replace('"', '')

    n_base = input("📝 Ingresa el nuevo nombre base para los archivos: ").strip()

    if not texto_valido(n_base):
        print("❌ Error: El nombre ingresado está vacío o contiene caracteres inválidos (<> : \" / \\ | ? *).")
    else:
        renombrado_secuencial(r, n_base)