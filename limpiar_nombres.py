from pathlib import Path

def procesar_nombres(ruta_str: str, buscar: str, reemplazo: str):
    ruta_raiz = Path(ruta_str)

    if not ruta_raiz.is_dir():
        print(f"❌ La ruta '{ruta_str}' no es un directorio válido.")
        return

    print(f"--- Iniciando limpieza en: {ruta_raiz.name} ---")

    contador = 0
    # rglob("*") busca archivos y carpetas recursivamente
    for item in ruta_raiz.rglob("*"):
        # Solo procesamos archivos para evitar romper rutas de carpetas mientras iteramos
        if item.is_file() and buscar in item.name:
            nuevo_nombre = item.name.replace(buscar, reemplazo)
            nueva_ruta = item.with_name(nuevo_nombre)

            try:
                item.rename(nueva_ruta)
                print(f"✅ Renombrado: {item.name} → {nuevo_nombre}")
                contador += 1
            except Exception as e:
                print(f"❌ Error al renombrar {item.name}: {e}")

    print(f"\n🎉 Proceso terminado. Se modificaron {contador} archivos.")

if __name__ == "__main__":
    r = input("Ruta de la carpeta: ").strip()
    print("\n💡 Tip: Para quitar espacios, presiona ESPACIO en 'Texto a buscar' y deja vacío el reemplazo.")
    b = input("Texto a buscar: ") # No usamos .strip() aquí para permitir buscar espacios
    m = input("Texto de reemplazo: ")

    procesar_nombres(ruta_str=r, buscar=b, reemplazo=m)