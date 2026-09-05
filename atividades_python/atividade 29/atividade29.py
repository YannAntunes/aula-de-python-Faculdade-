# 29. Crie um algoritmo que pergunte ao usuario um numero e verifique se ele
# e multiplo de 3.

numero = int(input("Digite um numero: "))

if numero % 3 == 0:
    print(f"O numero {numero} e multiplo de 3.")
else:
    print(f"O numero {numero} nao e multiplo de 3.")
