# 63. Desenvolva um algoritmo que peca ao usuario para inserir 5 numeros, adicione-os
# a uma lista e, depois, exiba a soma de todos os numeros na lista.

numeros = []

print("Digite 5 numeros:")
for i in range(1, 6):
    numero = float(input(f"Numero {i}: "))
    numeros.append(numero)

soma = sum(numeros)
print(f"\nLista de numeros: {numeros}")
print(f"Soma de todos os numeros: {soma}")
