# 64. Crie uma lista com 10 numeros aleatorios e exiba apenas os numeros que sao
# multiplos de 3.

import random

numeros = [random.randint(1, 50) for _ in range(10)]

print(f"Lista de 10 numeros aleatorios: {numeros}")

multiplos_de_3 = [n for n in numeros if n % 3 == 0]

if multiplos_de_3:
    print(f"Numeros multiplos de 3: {multiplos_de_3}")
else:
    print("Nenhum numero multiplo de 3 foi encontrado na lista.")
