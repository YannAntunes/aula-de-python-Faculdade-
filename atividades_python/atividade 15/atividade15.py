# 15. Escreva um programa que pergunte ao usuario uma idade e verifique se a pessoa
# e adolescente (entre 13 e 17 anos).

idade = int(input("Digite sua idade: "))

if 13 <= idade <= 17:
    print(f"Com {idade} anos, voce e adolescente.")
else:
    print(f"Com {idade} anos, voce nao e adolescente.")
