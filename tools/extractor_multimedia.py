import shutil
from pathlib import Path

def extractor_media():
    print("--- 🎬 EXTRACTOR Y ORGANIZADOR MULTIMEDIA ---")

    src_input = input("📁 Directorio de origen: ").strip().replace('"', '')
    dst_input = input("📦 Directorio de destino: ").strip().replace('"', '')

    src_path = Path(src_input)
    dst_path = Path(dst_input)

    if not src_path.is_dir():
        print("❌ El directorio de origen no es válido.")
        return

    # 1. Elegir qué buscar
    print("\n¿Qué deseas extraer?")
    print("1. Solo Imágenes")
    print("2. Solo Videos")
    print("3. Ambos (Imágenes y Videos)")
    op_tipo = input("Selecciona (1-3): ").strip()

    ext_img = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}
    ext_vid = {'.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm'}

    extensiones = set()
    if op_tipo == "1": extensiones = ext_img
    elif op_tipo == "2": extensiones = ext_vid
    else: extensiones = ext_img.union(ext_vid)

    # 2. Elegir modo de renombrado
    print("\n¿Cómo deseas renombrarlos en el destino?")
    print("1. Mantener nombre original (puede haber conflictos)")
    print("2. Secuencia numérica (ej: img_1.jpg)")
    print("3. Usar ruta original (ej: Carpeta_Subcarpeta_foto.jpg)")
    op_nom = input("Selecciona (1-3): ").strip()

    # 3. Copiar o Mover
    print("\n¿Deseas Copiar o Mover los archivos?")
    print("1. Copiar (Seguro)")
    print("2. Mover (Borra del origen)")
    op_accion = input("Selecciona (1-2): ").strip()

    dst_path.mkdir(parents=True, exist_ok=True)
    contador = 1
    procesados = 0

    print("\n🚀 Iniciando proceso...")
    for archivo in src_path.rglob("*"):
        if archivo.is_file() and archivo.suffix.lower() in extensiones:

            # Lógica de renombrado
            if op_nom == "2":
                nuevo_nombre = f"media_{contador}{archivo.suffix.lower()}"
            elif op_nom == "3":
                # Crea un nombre basado en las carpetas padre relativas
                ruta_relativa = archivo.relative_to(src_path)
                nuevo_nombre = str(ruta_relativa).replace("\\", "_").replace("/", "_").replace(" ", "_")
            else:
                nuevo_nombre = archivo.name

            destino_final = dst_path / nuevo_nombre

            # Evitar sobreescribir si elegiste la opción 1 y hay nombres repetidos
            while destino_final.exists() and op_nom == "1":
                destino_final = dst_path / f"{destino_final.stem}_{contador}{archivo.suffix}"
                contador += 1

            try:
                if op_accion == "2":
                    shutil.move(str(archivo), str(destino_final))
                else:
                    shutil.copy2(str(archivo), str(destino_final))

                print(f"✔ {'Movido' if op_accion == '2' else 'Copiado'}: {nuevo_nombre}")
                procesados += 1
                contador += 1
            except Exception as e:
                print(f"❌ Error con {archivo.name}: {e}")

    print("-" * 30)
    print(f"✅ ¡Completado! {procesados} archivos procesados.")

if __name__ == "__main__":
    extractor_media()