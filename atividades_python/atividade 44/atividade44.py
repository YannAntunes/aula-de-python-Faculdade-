# 44. Crie um programa que peca ao usuario 10 numeros e exiba apenas os numeros pares.

numeros_pares = []

print("Digite 10 numeros:")
for i in range(1, 11):
    numero = int(input(f"Numero {i}: "))
    if numero % 2 == 0:
        numeros_pares.append(numero)

if numeros_pares:
    print(f"\nNumeros pares digitados: {numeros_pares}")
else:
    print("\nNenhum numero par foi digitado.")
