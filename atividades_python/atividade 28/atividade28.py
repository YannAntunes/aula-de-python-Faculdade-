# 28. Escreva um programa que peca ao usuario para inserir uma palavra e verifique
# se ela tem mais de 5 letras.

palavra = input("Digite uma palavra: ").strip()

if len(palavra) > 5:
    print(f"A palavra '{palavra}' tem {len(palavra)} letras, ou seja, mais de 5 letras.")
else:
    print(f"A palavra '{palavra}' tem {len(palavra)} letras, ou seja, nao tem mais de 5 letras.")
