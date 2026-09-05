# 16. Desenvolva um programa que peca ao usuario um tipo de combustivel
# (gasolina, etanol, diesel) e exiba o preco correspondente por litro.

combustivel = input("Digite o tipo de combustivel (gasolina, etanol, diesel): ").strip().lower()

if combustivel == "gasolina":
    print("O preco da gasolina e R$ 5,89 por litro.")
elif combustivel == "etanol":
    print("O preco do etanol e R$ 3,79 por litro.")
elif combustivel == "diesel":
    print("O preco do diesel e R$ 6,09 por litro.")
else:
    print("Tipo de combustivel invalido.")
