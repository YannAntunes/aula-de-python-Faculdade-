# 30. Faca um programa que pergunte ao usuario a idade e verifique se ele pode
# votar (idade maior ou igual a 16).

idade = int(input("Digite sua idade: "))

if idade >= 16:
    print(f"Com {idade} anos, voce pode votar.")
else:
    print(f"Com {idade} anos, voce ainda nao pode votar. A idade minima e 16 anos.")
