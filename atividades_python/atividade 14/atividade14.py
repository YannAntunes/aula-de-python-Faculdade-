# 14. Desenvolva um algoritmo que peca ao usuario para digitar dois numeros e verifique
# se a soma deles e maior que 100.

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

soma = numero1 + numero2

if soma > 100:
    print(f"A soma ({soma}) e maior que 100.")
else:
    print(f"A soma ({soma}) nao e maior que 100.")
