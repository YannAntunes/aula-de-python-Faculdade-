# 49. Desenvolva um programa que peca ao usuario para inserir 7 numeros e,
# ao final, exiba quantos desses numeros sao maiores que 10.

contagem = 0

print("Digite 7 numeros:")
for i in range(1, 8):
    numero = float(input(f"Numero {i}: "))
    if numero > 10:
        contagem += 1

print(f"\nQuantidade de numeros maiores que 10: {contagem}")
