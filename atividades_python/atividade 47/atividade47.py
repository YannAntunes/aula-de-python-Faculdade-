# 47. Crie um programa que peca ao usuario um numero e exiba a tabuada desse
# numero de 1 a 10.

numero = int(input("Digite um numero para ver a tabuada: "))

print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
