# 27. Crie um programa que solicite ao usuario tres numeros e exiba o maior deles.

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))
numero3 = float(input("Digite o terceiro numero: "))

if numero1 >= numero2 and numero1 >= numero3:
    maior = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    maior = numero2
else:
    maior = numero3

print(f"O maior numero entre {numero1}, {numero2} e {numero3} e: {maior}")
