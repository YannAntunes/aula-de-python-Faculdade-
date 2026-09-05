# 51. Crie um programa que peca ao usuario para inserir numeros ate que ele
# digite o numero 0. Ao final, exiba a soma de todos os numeros inseridos (exceto o 0).

soma = 0

print("Digite numeros (digite 0 para encerrar):")
while True:
    numero = float(input("Digite um numero: "))
    if numero == 0:
        break
    soma += numero

print(f"\nA soma de todos os numeros inseridos e: {soma}")
