# Programa básico de Números Primos en Python
# Digamos que deseo imprimir los números primos entre 1 y 100


def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


print("Números primos entre 1 y 100:")
for num in range(1, 101):
    if es_primo(num):
        print(num)
