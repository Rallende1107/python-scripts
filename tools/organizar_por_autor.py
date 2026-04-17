import re
import shutil
from pathlib import Path

def reorganizar_carpetas(ruta_str: str):
    ruta_raiz = Path(ruta_str)
    if not ruta_raiz.is_dir():
        print("❌ La ruta no es válida.")
        return

    # Regex para: Nombre [Version] [Autor]
    patron = re.compile(r"^(.*?) \[(.*?)\] \[(.*?)\]$")

    for carpeta in ruta_raiz.iterdir():
        if carpeta.is_dir():
            match = patron.match(carpeta.name)
            if match:
                nombre, version, autor = match.groups()

                # Definimos la nueva estructura: Autor [Nombre] / Version
                # (Puedes ajustar el orden a tu gusto)
                ruta_nueva_base = ruta_raiz / f"{nombre} [{autor}]"
                ruta_version = ruta_nueva_base / version

                try:
                    ruta_version.mkdir(parents=True, exist_ok=True)

                    # Mover todo el contenido de la carpeta vieja a la nueva
                    for item in carpeta.iterdir():
                        shutil.move(str(item), str(ruta_version / item.name))

                    # Eliminar la carpeta original ahora que está vacía
                    carpeta.rmdir()
                    print(f"✅ Organizado: {carpeta.name} -> {ruta_nueva_base.name}/{version}")
                except Exception as e:
                    print(f"❌ Error procesando {carpeta.name}: {e}")

if __name__ == "__main__":
    r = input("Ingresa la ruta de la carpeta: ").strip()
    reorganizar_carpetas(r)