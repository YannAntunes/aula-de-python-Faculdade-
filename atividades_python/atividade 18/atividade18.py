# 18. Faca um programa que peca ao usuario tres numeros e verifique se todos sao positivos.

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))
numero3 = float(input("Digite o terceiro numero: "))

if numero1 > 0 and numero2 > 0 and numero3 > 0:
    print("Todos os tres numeros sao positivos.")
else:
    print("Nem todos os numeros sao positivos.")
