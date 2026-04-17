import shutil
from pathlib import Path

def fusionar_directorios(ruta_base_str: str, nombre_final: str):
    ruta_base = Path(ruta_base_str)

    if not ruta_base.is_dir():
        print("❌ Error: La ruta base no es válida.")
        return

    ruta_destino = ruta_base / nombre_final

    # 1. Preparar la carpeta de destino
    if ruta_destino.exists():
        print(f"⚠️  Vaciando carpeta de destino existente: {ruta_destino.name}")
        shutil.rmtree(ruta_destino)

    ruta_destino.mkdir(parents=True)
    print(f"\n📂 Consolidando archivos en: {ruta_destino.resolve()}")
    print("-" * 40)

    archivos_movidos = 0
    carpetas_procesadas = 0

    # 2. Iterar sobre las carpetas dentro de la ruta base
    for carpeta in ruta_base.iterdir():
        # Ignoramos si es un archivo suelto o si es la carpeta destino
        if carpeta.is_dir() and carpeta != ruta_destino:
            carpetas_procesadas += 1

            # 3. Mover el contenido
            for item in carpeta.iterdir():
                destino_item = ruta_destino / item.name

                # Manejo de conflictos (si el archivo ya existe)
                if destino_item.exists():
                    base = item.stem
                    ext = item.suffix
                    contador = 1
                    # Buscar un nombre que no exista
                    while destino_item.exists():
                        destino_item = ruta_destino / f"{base}_{contador}{ext}"
                        contador += 1

                # Mover el archivo/carpeta usando las rutas absolutas convertidas a string
                shutil.move(str(item.resolve()), str(destino_item.resolve()))
                archivos_movidos += 1

            # 4. Eliminar la carpeta original (ya debería estar vacía)
            try:
                carpeta.rmdir()
                print(f"✔ Fusionada y eliminada: {carpeta.name}")
            except Exception as e:
                print(f"⚠ No se pudo eliminar {carpeta.name} (¿Quedaron archivos ocultos?): {e}")

    print("-" * 40)
    print(f"✅ ¡Proceso terminado! Se movieron {archivos_movidos} elementos desde {carpetas_procesadas} carpetas.")

if __name__ == "__main__":
    r_base = input("📁 Introduce la ruta donde están las carpetas: ").strip()
    n_final = input("📦 Introduce el nombre para la nueva carpeta combinada: ").strip()

    fusionar_directorios(r_base, n_final)