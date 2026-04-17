from pathlib import Path

def modificar_nombres(ruta_str: str):
    ruta_raiz = Path(ruta_str)

    if not ruta_raiz.is_dir():
        print("❌ Ruta inválida.")
        return

    palabra = input("📝 Ingresa la palabra a agregar: ").strip()
    separador = input("🔗 Ingresa el separador (_ o - o presiona Enter para ninguno): ").strip()
    if separador not in ['_', '-']: separador = ''

    print("\n¿Dónde deseas agregar la palabra?")
    print("1. Al inicio (Prefijo)")
    print("2. Al final (Sufijo)")
    modo = input("Selecciona (1/2): ").strip()

    contador = 0
    for archivo in ruta_raiz.rglob("*"):
        if archivo.is_file():
            nombre = archivo.stem
            ext = archivo.suffix

            if modo == "1":
                nuevo_nombre = f"{palabra}{separador}{nombre}{ext}"
            elif modo == "2":
                nuevo_nombre = f"{nombre}{separador}{palabra}{ext}"
            else:
                return

            nueva_ruta = archivo.with_name(nuevo_nombre)

            try:
                archivo.rename(nueva_ruta)
                print(f"✅ {archivo.name} -> {nuevo_nombre}")
                contador += 1
            except Exception as e:
                print(f"❌ Error en {archivo.name}: {e}")

    print(f"\n🎉 Proceso completado. Archivos modificados: {contador}")

if __name__ == "__main__":
    r = input("📁 Ruta de la carpeta: ").strip().replace('"', '')
    modificar_nombres(r)