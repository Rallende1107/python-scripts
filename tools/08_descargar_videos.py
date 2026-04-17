import os
import re
import subprocess
from pathlib import Path

# --- CONFIGURACIÓN DE REQUISITOS ---
# Si FFmpeg no está en tu PATH global, pon la ruta completa aquí:
# Ejemplo: "C:\\ffmpeg\\bin\\ffmpeg.exe"
FFMPEG_PATH = "ffmpeg"

try:
    import yt_dlp
except ImportError:
    print("❌ Error: La librería 'yt-dlp' no está instalada.")
    print("👉 Instálala con: pip install yt-dlp")
    exit()

def verificar_ffmpeg():
    """Comprueba si FFmpeg está accesible."""
    try:
        subprocess.run([FFMPEG_PATH, "-version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def limpiar_nombre(nombre: str) -> str:
    """Limpia caracteres inválidos para nombres de carpetas."""
    return re.sub(r'[\\/*?:"<>|]', "", nombre)

def descargar_multimedia(url: str, ruta_base_str: str):
    ruta_base = Path(ruta_base_str)

    if not verificar_ffmpeg():
        print("⚠️  Advertencia: No se detectó FFmpeg.")
        print("El video se descargará, pero la conversión a MP4 universal podría fallar.")

    # 1. Obtener información previa
    print("\n⏳ Analizando URL...")
    ydl_opts_info = {'quiet': True, 'extract_flat': 'in_playlist'}

    try:
        with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
            info = ydl.extract_info(url, download=False)
    except Exception as e:
        print(f"❌ Error al analizar la URL: {e}")
        return

    # 2. Configurar destino
    es_playlist = 'entries' in info
    if es_playlist:
        nombre_pl = limpiar_nombre(info.get('title', 'playlist'))
        ruta_destino = ruta_base / nombre_pl
        print(f"📂 Playlist detectada: {nombre_pl}")
    else:
        ruta_destino = ruta_base
        print(f"🎬 Video detectado: {info.get('title', 'video')}")

    ruta_destino.mkdir(parents=True, exist_ok=True)

    # 3. Opciones de descarga y post-procesamiento (Compatibilidad Total)
    opciones = {
        'outtmpl': str(ruta_destino / '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'ffmpeg_location': FFMPEG_PATH,
        # Forzar recodificación a formatos universales (H.264 y AAC)
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'postprocessor_args': [
            '-c:v', 'libx264',  # Video compatible con todo (H.264)
            '-c:a', 'aac',      # Audio compatible con todo (AAC)
            '-pix_fmt', 'yuv420p' # Necesario para compatibilidad con reproductores viejos
        ],
        'ignoreerrors': True,
    }

    # 4. Ejecución
    print(f"🚀 Iniciando descarga en: {ruta_destino.resolve()}")
    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
        print("\n✅ ¡Proceso completado con éxito!")
    except Exception as e:
        print(f"❌ Error durante la descarga: {e}")

if __name__ == "__main__":
    print("--- 📺 DESCARGADOR MULTIMEDIA PRO ---")
    u = input("🔗 Ingresa la URL (Video o Playlist): ").strip()
    r = input("📁 Carpeta de destino: ").strip().replace('"', '')

    descargar_multimedia(u, r)