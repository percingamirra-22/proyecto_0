# Módulo para funcionalidades nuevas

from math import isqrt


# Verificar si es primo el número entero ingresado
def es_primo(n):
    """Verifica si un número entero positivo es primo."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("El argumento debe ser un número entero")
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


# Mostrar todos los números primos desde 1 hasta el entero digitado
def primos_hasta(limite):
    """Devuelve una lista con los primos desde 1 hasta limite (inclusive)."""
    if not isinstance(limite, int) or isinstance(limite, bool):
        raise TypeError("El argumento debe ser un número entero")
    if limite < 1:
        raise ValueError("El argumento debe ser un entero positivo")
    return [n for n in range(2, limite + 1) if es_primo(n)]


# Mostrar todos los números compuestos desde 1 hasta el entero digitado
def compuestos_hasta(limite):
    """Devuelve una lista con los compuestos desde 1 hasta limite (inclusive)."""
    if not isinstance(limite, int) or isinstance(limite, bool):
        raise TypeError("El argumento debe ser un número entero")
    if limite < 1:
        raise ValueError("El argumento debe ser un entero positivo")
    return [n for n in range(4, limite + 1) if not es_primo(n)]
