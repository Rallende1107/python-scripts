import re
from pathlib import Path

# Envolvemos el import en un try-except por si ejecutas el script sin tener la librería instalada
try:
    import yt_dlp
except ImportError:
    print("❌ Falta la librería 'yt-dlp'. Instálala ejecutando: pip install yt-dlp")
    exit()

def limpiar_nombre(nombre: str) -> str:
    """Elimina caracteres inválidos para nombres de carpetas en Windows/Linux."""
    return re.sub(r'[\\/*?:"<>|]', "", nombre)

def descargar_media(video_url: str, carpeta_base_str: str):
    carpeta_base = Path(carpeta_base_str)

    ydl_opts_info = {
        'quiet': True,
        'extract_flat': 'in_playlist', # Acelera la extracción de info
        # 'cookiesfrombrowser': ('chrome',),  # 👈 Descomenta si necesitas videos privados
    }

    print("\n⏳ Obteniendo información de la URL...")
    try:
        with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
            info = ydl.extract_info(video_url, download=False)
    except Exception as e:
        print(f"❌ Error al leer la URL: {e}")
        return

    # Comprobamos si es una playlist
    es_playlist = 'entries' in info

    if es_playlist:
        nombre_playlist = limpiar_nombre(info.get('title', 'Playlist_Sin_Nombre'))
        carpeta_destino = carpeta_base / nombre_playlist
        print(f"🗂️  Playlist detectada: {nombre_playlist}")
    else:
        carpeta_destino = carpeta_base
        print(f"🎬 Video individual detectado: {info.get('title', 'Video')}")

    # Creamos las carpetas si no existen
    carpeta_destino.mkdir(parents=True, exist_ok=True)

    # yt-dlp requiere que outtmpl sea un string estándar, así que lo convertimos
    plantilla_salida = str(carpeta_destino / '%(title)s.%(ext)s')

    opciones_descarga = {
        'outtmpl': plantilla_salida,
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'ignoreerrors': True,
        # 'cookiesfrombrowser': ('chrome',),  # 👈 Descomenta si necesitas videos privados
    }

    print(f"⬇️  Iniciando descarga en: {carpeta_destino.resolve()}")
    print("-" * 40)

    try:
        with yt_dlp.YoutubeDL(opciones_descarga) as ydl:
            ydl.download([video_url])
        print("-" * 40)
        print("✅ Descarga completada.")
    except Exception as e:
        print(f"❌ Error durante la descarga: {e}")

if __name__ == "__main__":
    url = input("🔗 Ingresa la URL: ").strip()
    carpeta = input("📁 Carpeta de destino base: ").strip()
    descargar_media(url, carpeta)