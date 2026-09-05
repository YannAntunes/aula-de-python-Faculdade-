# 40. Escreva um programa que peca ao usuario para inserir tres numeros e verifique
# se todos sao iguais.

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))
numero3 = float(input("Digite o terceiro numero: "))

if numero1 == numero2 == numero3:
    print("Todos os tres numeros sao iguais!")
else:
    print("Os numeros nao sao todos iguais.")
