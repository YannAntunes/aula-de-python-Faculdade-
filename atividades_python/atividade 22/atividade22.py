# 22. Escreva um programa que peca ao usuario para inserir dois numeros e verifique
# se o primeiro e maior que o segundo.

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

if numero1 > numero2:
    print(f"O primeiro numero ({numero1}) e maior que o segundo ({numero2}).")
elif numero1 < numero2:
    print(f"O primeiro numero ({numero1}) nao e maior que o segundo ({numero2}).")
else:
    print(f"Os dois numeros sao iguais ({numero1}).")
