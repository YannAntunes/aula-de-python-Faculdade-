# 7. Escreva um programa que peca ao usuario uma nota de 0 a 10 e classifique a nota como
# "Baixa", "Media" ou "Alta" usando estrutura condicional if.

nota = float(input("Digite uma nota de 0 a 10: "))

if nota < 0 or nota > 10:
    print("Nota invalida. Digite um valor entre 0 e 10.")
elif nota < 5:
    print("Classificacao: Baixa")
elif nota < 7:
    print("Classificacao: Media")
else:
    print("Classificacao: Alta")
