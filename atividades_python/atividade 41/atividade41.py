# 41. Crie um programa que peca ao usuario um numero inteiro positivo e exiba
# todos os numeros de 1 ate o numero informado.

numero = int(input("Digite um numero inteiro positivo: "))

if numero <= 0:
    print("Por favor, digite um numero inteiro positivo.")
else:
    print(f"Numeros de 1 ate {numero}:")
    for i in range(1, numero + 1):
        print(i)
