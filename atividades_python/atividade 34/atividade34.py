# 34. Escreva um programa que peca ao usuario um numero e verifique se ele
# e positivo, negativo ou zero.

numero = float(input("Digite um numero: "))

if numero > 0:
    print(f"O numero {numero} e positivo.")
elif numero < 0:
    print(f"O numero {numero} e negativo.")
else:
    print("O numero digitado e zero.")
