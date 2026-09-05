# 1. Crie um programa que pergunte ao usuário um número de 1 a 3 e exiba o nome correspondente ao número (1: "um", 2: "dois", 3: "três").
numero = int(input("Digite um número de 1 a 3: "))

if numero == 1:
    print("um")
elif numero == 2:
    print("dois")
elif numero == 3:
    print("três")
else:
    print("Número inválido.")