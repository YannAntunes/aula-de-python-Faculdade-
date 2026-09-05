# 43. Desenvolva um programa que pergunte ao usuario quantas vezes ele quer que uma mensagem
# seja exibida, e depois use um for para imprimir essa mensagem repetidas vezes.

vezes = int(input("Quantas vezes deseja exibir a mensagem? "))
mensagem = input("Digite a mensagem: ")

print(f"\nExibindo a mensagem {vezes} vez(es):")
for i in range(vezes):
    print(f"{i + 1}: {mensagem}")
