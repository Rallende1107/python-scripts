from pathlib import Path

def gestionar_sufijo(ruta_str: str, sufijo: str, modo: str):
    ruta_raiz = Path(ruta_str)

    if not ruta_raiz.is_dir():
        print("❌ Ruta inválida.")
        return

    print(f"\n--- Modo seleccionado: {'Añadir' if modo == '1' else 'Quitar'} sufijo ---")

    contador = 0
    for archivo in ruta_raiz.rglob("*"):
        if archivo.is_file():
            nombre = archivo.stem
            ext = archivo.suffix

            # --- LÓGICA PARA AÑADIR ---
            if modo == "1":
                if sufijo in nombre:
                    continue  # Evita duplicar si ya lo tiene
                nuevo_nombre_completo = f"{nombre}{sufijo}{ext}"

            # --- LÓGICA PARA QUITAR ---
            elif modo == "2":
                if sufijo not in nombre:
                    continue  # Salta si el archivo no tiene el sufijo
                # Reemplazamos el sufijo solo si está al final del nombre (antes de la extensión)
                if nombre.endswith(sufijo):
                    nuevo_nombre_sin_sufijo = nombre[: -len(sufijo)]
                    nuevo_nombre_completo = f"{nuevo_nombre_sin_sufijo}{ext}"
                else:
                    # Si el sufijo está en medio, también lo quitamos
                    nuevo_nombre_completo = f"{nombre.replace(sufijo, '')}{ext}"

            else:
                print("Opción no válida.")
                return

            nueva_ruta = archivo.with_name(nuevo_nombre_completo)

            try:
                archivo.rename(nueva_ruta)
                print(f"✅ {archivo.name} → {nuevo_nombre_completo}")
                contador += 1
            except Exception as e:
                print(f"❌ Error en {archivo.name}: {e}")

    print(f"\n🎉 Proceso completado. Archivos modificados: {contador}")

if __name__ == "__main__":
    r = input("📁 Ruta de la carpeta: ").strip()
    s = input("🏷️  Sufijo (ej: _v1, -copia): ").strip()
    print("\n¿Qué deseas hacer?")
    print("1. Añadir sufijo")
    print("2. Quitar sufijo")
    m = input("Selecciona (1 o 2): ").strip()

    gestionar_sufijo(ruta_str=r, sufijo=s, modo=m)