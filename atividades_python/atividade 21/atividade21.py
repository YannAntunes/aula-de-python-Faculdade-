# 21. Escreva um algoritmo que peca ao usuario para digitar um numero e verifique
# se ele e maior, menor ou igual a 10.

numero = float(input("Digite um numero: "))

if numero > 10:
    print(f"O numero {numero} e maior que 10.")
elif numero < 10:
    print(f"O numero {numero} e menor que 10.")
else:
    print(f"O numero {numero} e igual a 10.")
