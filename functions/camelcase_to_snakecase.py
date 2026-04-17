text = input("Ingresa texto (CamelCase):\n")

resultado = ""

for i, letra in enumerate(text):
    if letra.isupper():
        if i != 0:  # 👈 evita "_" al inicio
            resultado += "_"
        resultado += letra.lower()
    else:
        resultado += letra

print(resultado)