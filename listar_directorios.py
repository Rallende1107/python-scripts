import os

# ruta = "K:\\Juegos\\XXX"

ruta = input("Ingresa el directorio: ")

carpetas = [
    nombre for nombre in os.listdir(ruta) if os.path.isdir(os.path.join(ruta, nombre))
]

for carpeta in carpetas:
    print(carpeta)

