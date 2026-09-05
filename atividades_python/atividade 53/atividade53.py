# 53. Escreva um programa que peca ao usuario um numero e exiba a contagem
# regressiva desse numero ate 1.

numero = int(input("Digite um numero para a contagem regressiva: "))

if numero <= 0:
    print("Por favor, digite um numero positivo.")
else:
    print(f"\nContagem regressiva de {numero} ate 1:")
    while numero >= 1:
        print(numero)
        numero -= 1
    print("Fim!")
