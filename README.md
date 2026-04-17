# python-scripts

Colección de scripts en Python desarrollados como desafíos y proyectos
personales durante el tiempo libre. El objetivo de este repositorio es
automatizar tareas comunes y facilitar la gestión de archivos y
directorios.

## Autor
 - [@rallende](https://www.github.com/rallende1107)

## Scripts disponibles

### listar_directorios
Permite ingresar una ruta y muestra de forma ordenada todas las carpetas
contenidas en ese directorio. Utiliza generadores para optimizar el uso
de memoria y maneja errores comunes como rutas inexistentes o falta de permisos.

### limpiar_nombres
Herramienta de renombrado recursivo que permite reemplazar cadenas de
texto dentro de nombres de archivos y carpetas (incluyendo espacios).
Ideal para organizar grandes volúmenes de archivos de forma rápida.

### gestor_sufijos (añadir / quitar)
Permite gestionar nombres de archivos de forma masiva, agregando o
eliminando sufijos (etiquetas al final del nombre) de manera recursiva.

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
