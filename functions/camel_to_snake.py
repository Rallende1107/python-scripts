import re

text = input("Ingresa texto (CamelCase):\n")

resultado = re.sub(r'([A-Z])', r'_\1', text)

print(resultado.lower())