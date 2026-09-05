# 50. Crie um programa que peca ao usuario para inserir um numero e, em seguida,
# exiba os numeros de 1 ate esse numero, mas de forma decrescente.

numero = int(input("Digite um numero: "))

if numero <= 0:
    print("Por favor, digite um numero positivo.")
else:
    print(f"\nContagem decrescente de {numero} ate 1:")
    for i in range(numero, 0, -1):
        print(i)
