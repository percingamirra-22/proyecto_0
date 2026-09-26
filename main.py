# Programa básico de Números Primos en Python
from funciones import primos_hasta

LIMITE = 100

print(f"Números primos entre 1 y {LIMITE}:")
for primo in primos_hasta(LIMITE):
    print(primo)
