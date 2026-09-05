# 60. Crie um programa que peca ao usuario um numero e exiba todos os divisores desse numero.

numero = int(input("Digite um numero inteiro positivo: "))

if numero <= 0:
    print("Por favor, digite um numero inteiro positivo.")
else:
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)

    print(f"\nDivisores de {numero}: {divisores}")
