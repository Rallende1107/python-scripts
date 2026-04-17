import re
from datetime import datetime
from pathlib import Path

def estandarizar_devlogs(ruta_base_str: str):
    ruta_base = Path(ruta_base_str)

    if not ruta_base.is_dir():
        print("❌ Error: La ruta no es válida.")
        return

    # Patrones de búsqueda
    patrones_antiguos = [
        re.compile(r"dev log (\d{2})\.(\d{2})\.(\d{4})", re.IGNORECASE),
        re.compile(r"dev log (\d{2})-(\d{2})-(\d{4})", re.IGNORECASE),
        re.compile(r"dev log (\d{2})(\d{2})(\d{4})", re.IGNORECASE)
    ]
    patron_nuevo = re.compile(r"dev log #(\d+) - (\d{2})\.(\d{2})\.(\d{4})", re.IGNORECASE)

    carpetas_antiguas = []
    numeracion_por_año = {}

    for carpeta in ruta_base.iterdir():
        if not carpeta.is_dir():
            continue

        # Revisar si ya tiene el formato nuevo para actualizar nuestro contador interno
        match_nuevo = patron_nuevo.match(carpeta.name)
        if match_nuevo:
            numero, dia, mes, año = match_nuevo.groups()
            año_int = int(año)
            numeracion_por_año[año_int] = max(numeracion_por_año.get(año_int, 0), int(numero))
            continue

        # Revisar formatos antiguos
        for patron in patrones_antiguos:
            match = patron.match(carpeta.name)
            if match:
                dia, mes, año = match.groups()
                fecha = datetime.strptime(f"{dia}.{mes}.{año}", "%d.%m.%Y")
                carpetas_antiguas.append((carpeta, fecha))
                break

    if not carpetas_antiguas:
        print("✅ No se encontraron carpetas con formato antiguo para renombrar.")
        return

    # Ordenar cronológicamente
    carpetas_antiguas.sort(key=lambda x: x[1])

    print("\n🚀 Estandarizando Dev Logs...")
    for carpeta, fecha in carpetas_antiguas:
        año = fecha.year
        numeracion_por_año[año] = numeracion_por_año.get(año, 0) + 1
        nuevo_nombre = f"Dev Log #{numeracion_por_año[año]} - {fecha.strftime('%d.%m.%Y')}"

        nueva_ruta = carpeta.with_name(nuevo_nombre)
        try:
            carpeta.rename(nueva_ruta)
            print(f"✅ Renombrado: '{carpeta.name}' → '{nuevo_nombre}'")
        except Exception as e:
            print(f"❌ Error con '{carpeta.name}': {e}")

    print("\n🎉 ¡Proceso completado!")

if __name__ == "__main__":
    ruta = input("📂 Ingresa la ruta de la carpeta de Dev Logs: ").strip().replace('"', '')
    estandarizar_devlogs(ruta)