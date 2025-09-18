import sys
sys.setrecursionlimit(20000)  # aumentar límite de recursión

from functools import lru_cache
import time

@lru_cache(maxsize=None)   # guarda resultados previos
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Calcular F(10000)
n = 10000

inicio = time.time()
resultado = fibonacci(n)
fin = time.time()

print(f"F({n}) = {resultado}")
print(f"\nTiempo de ejecución: {fin - inicio:.6f} segundos")
