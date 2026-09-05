# 45. Escreva um algoritmo que peca ao usuario para inserir 5 numeros e,
# ao final, exiba o maior numero inserido.

print("Digite 5 numeros:")
maior = None

for i in range(1, 6):
    numero = float(input(f"Numero {i}: "))
    if maior is None or numero > maior:
        maior = numero

print(f"\nO maior numero inserido foi: {maior}")
