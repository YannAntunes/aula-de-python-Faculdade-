# 25. Escreva um programa que peca ao usuario um numero de 0 a 20 e verifique
# se ele esta entre 10 e 15.

numero = float(input("Digite um numero de 0 a 20: "))

if 10 <= numero <= 15:
    print(f"O numero {numero} esta entre 10 e 15.")
else:
    print(f"O numero {numero} nao esta entre 10 e 15.")
