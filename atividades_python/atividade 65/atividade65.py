# 65. Escreva um programa que solicite ao usuario uma lista de 5 numeros e exiba
# o maior e o menor numero dessa lista.

numeros = []

print("Digite 5 numeros:")
for i in range(1, 6):
    numero = float(input(f"Numero {i}: "))
    numeros.append(numero)

print(f"\nLista de numeros: {numeros}")
print(f"Maior numero: {max(numeros)}")
print(f"Menor numero: {min(numeros)}")
