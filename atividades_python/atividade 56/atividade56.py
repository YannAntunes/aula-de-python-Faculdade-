# 56. Escreva um programa que pergunte ao usuario quantas vezes ele quer que uma mensagem
# seja exibida, e utilize um laco while para exibir a mensagem a quantidade de vezes desejada.

vezes = int(input("Quantas vezes deseja exibir a mensagem? "))
mensagem = input("Digite a mensagem: ")

contador = 1
print(f"\nExibindo a mensagem {vezes} vez(es):")
while contador <= vezes:
    print(f"{contador}: {mensagem}")
    contador += 1
