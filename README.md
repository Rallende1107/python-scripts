# python-scripts

Colección de scripts en Python desarrollados como desafíos y proyectos
personales durante el tiempo libre. El objetivo de este repositorio es
automatizar tareas comunes y facilitar la gestión de archivos y
directorios.

## Autor
 - [@rallende](https://www.github.com/rallende1107)

## Scripts disponibles

### 1.- Listar Directorios
Permite ingresar una ruta y muestra de forma ordenada todas las carpetas
contenidas en ese directorio. Utiliza generadores para optimizar el uso
de memoria y maneja errores comunes como rutas inexistentes o falta de permisos.

### 2.- Limpiar Nombres
Herramienta de renombrado recursivo que permite reemplazar cadenas de
texto dentro de nombres de archivos y carpetas (incluyendo espacios).
Ideal para organizar grandes volúmenes de archivos de forma rápida.

### 3.- Gestor Prefijos/Sufijos
Permite agregar prefijos o sufijos a los nombres de archivos de forma masiva y recursiva, incluyendo soporte para separadores personalizados (_, -). Ideal para etiquetar lotes de archivos.

### 4.- Creador de Directorios
Utilidad para la creación de directorios que soporta entrada manual y carga de nombres desde archivos externos (.txt).

### 5.- Reorganizador Estructural por autor (Regex)
Reestructura directorios que siguen el formato Nombre [Versión] [Autor]. El script extrae los datos mediante expresiones regulares, crea una nueva jerarquía basada en el autor y mueve el contenido a subcarpetas de versión, eliminando los directorios originales vacíos. Ideal para organizar librerías o assets de forma jerárquica.

### 6.- Limpiar nombre de Carpetas
Filtra y renombra directorios en el nivel principal de una ruta eliminando palabras específicas. Incluye validaciones de seguridad para evitar nombres vacíos o colisiones con carpetas ya existentes, asegurando una limpieza de nombres rápida y sin pérdida de datos.


### 7.- Vaciador de Directorios
Utilidad destructiva pero segura para vaciar completamente un directorio sin eliminar la carpeta raíz. Cuenta con un sistema de confirmación de usuario, elimina recursivamente subcarpetas y limpia archivos regulares y enlaces simbólicos.

### 8.- Descargar videos
Descargador de videos y listas de reproducción optimizado con yt-dlp. Detecta automáticamente si la URL pertenece a un video individual o una playlist, creando una subcarpeta sanitizada para organizar las descargas, y fusiona la mejor calidad de video y audio en formato MP4.

### 9.- Fusionar directorios
Consolida el contenido de múltiples subdirectorios en una sola carpeta principal. Elimina automáticamente las carpetas de origen vacías y previene la pérdida de datos renombrando inteligentemente los archivos si detecta nombres duplicados.

### 10.- Extractor Multimedia
Herramienta todo-en-uno para la extracción y organización de archivos multimedia. Permite buscar imágenes o videos de forma recursiva, copiarlos o moverlos a un destino único, y renombrarlos automáticamente usando una secuencia numérica o su ruta de origen para evitar conflictos.

### 11.- Estandarizar DevLogs
Herramienta de organización cronológica para bitácoras de desarrollo (Dev Logs). Escanea carpetas con múltiples formatos de fecha, las ordena temporalmente y las renombra con un estándar limpio (Dev Log #X - DD.MM.YYYY), manteniendo un contador independiente para cada año.

### 12.- Conversor Multimedia
Potente conversor de medios que transforma imágenes a formato WebP y videos a WebM de forma masiva. Utiliza Pillow y MoviePy para optimizar el peso de los archivos de un directorio completo, con opciones para limpieza automática de los archivos originales.



## Requisitos
-   Python 3.14.0
-   pip 26.0.1

## Cómo ejecutar el proyecto

1.  Clonar el repositorio
   `git clone https://github.com/Rallende1107/python-scripts.git`

2.  Entrar al directorio del proyecto `cd python-scripts`

3.  Crear un entorno virtual `python -m venv venv`

4.  Activar el entorno virtual

Windows: venv

Linux / macOS: source venv/bin/activate

5.  Instalar dependencias `pip install -r requirements.txt`

6.  Ejecutar un script python nombre_del_script.py
