# 37. Desenvolva um algoritmo que peca ao usuario para digitar um numero e verifique
# se ele e multiplo de 2 ou de 5.

numero = int(input("Digite um numero: "))

if numero % 2 == 0 and numero % 5 == 0:
    print(f"O numero {numero} e multiplo de 2 e de 5.")
elif numero % 2 == 0:
    print(f"O numero {numero} e multiplo de 2.")
elif numero % 5 == 0:
    print(f"O numero {numero} e multiplo de 5.")
else:
    print(f"O numero {numero} nao e multiplo de 2 nem de 5.")
