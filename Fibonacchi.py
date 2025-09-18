from sympy import fibonacci
import time

n = 10000

inicio = time.time()

# Obtener el número 10000 de Fibonacci
fib_10000 = fibonacci(n)

fin = time.time()

print(f"F({n}) = {fib_10000}")
print(f"\nTiempo de ejecución: {fin - inicio:.6f} segundos")
