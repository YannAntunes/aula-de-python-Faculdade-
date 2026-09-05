# 10. Crie um algoritmo que solicite ao usuario uma idade e verifique se ela e maior ou igual a 18.

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print(f"Com {idade} anos, voce e maior de idade.")
else:
    print(f"Com {idade} anos, voce e menor de idade.")
