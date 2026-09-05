# 13. Crie um algoritmo que solicite ao usuario um mes do ano (1 a 12) e exiba
# a estacao do ano correspondente.

mes = int(input("Digite o mes do ano (1 a 12): "))

if mes < 1 or mes > 12:
    print("Mes invalido. Digite um valor entre 1 e 12.")
elif mes in [12, 1, 2]:
    print(f"O mes {mes} corresponde ao Verao (no Brasil).")
elif mes in [3, 4, 5]:
    print(f"O mes {mes} corresponde ao Outono (no Brasil).")
elif mes in [6, 7, 8]:
    print(f"O mes {mes} corresponde ao Inverno (no Brasil).")
else:
    print(f"O mes {mes} corresponde a Primavera (no Brasil).")
