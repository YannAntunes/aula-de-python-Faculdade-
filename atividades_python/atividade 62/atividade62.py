# 62. Escreva um programa que solicite ao usuario para inserir 3 nomes e armazene-os
# em uma lista. Em seguida, imprima a lista completa.

nomes = []

print("Digite 3 nomes:")
for i in range(1, 4):
    nome = input(f"Nome {i}: ").strip()
    nomes.append(nome)

print(f"\nLista de nomes: {nomes}")
