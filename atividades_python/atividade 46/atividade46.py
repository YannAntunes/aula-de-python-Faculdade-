# 46. Desenvolva um programa que pergunte ao usuario para inserir 10 numeros e,
# ao final, exiba a media dos numeros inseridos.

soma = 0

print("Digite 10 numeros:")
for i in range(1, 11):
    numero = float(input(f"Numero {i}: "))
    soma += numero

media = soma / 10
print(f"\nA media dos 10 numeros e: {media:.2f}")
