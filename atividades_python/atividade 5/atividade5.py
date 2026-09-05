# 5. Faca um programa que solicite ao usuario dois numeros e verifique se ambos sao pares.

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

if numero1 % 2 == 0 and numero2 % 2 == 0:
    print("Ambos os numeros sao pares.")
else:
    print("Nem ambos os numeros sao pares.")
