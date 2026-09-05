# 38. Escreva um programa que peca ao usuario para digitar sua altura em metros
# e verifique se ela e maior que 1.75.

altura = float(input("Digite sua altura em metros (ex: 1.75): "))

if altura > 1.75:
    print(f"Sua altura ({altura:.2f}m) e maior que 1,75m.")
else:
    print(f"Sua altura ({altura:.2f}m) nao e maior que 1,75m.")
