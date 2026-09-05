# 9. Crie um algoritmo que verifique se um numero inserido pelo usuario e par ou impar.

numero = int(input("Digite um numero: "))

if numero % 2 == 0:
    print(f"O numero {numero} e par.")
else:
    print(f"O numero {numero} e impar.")
