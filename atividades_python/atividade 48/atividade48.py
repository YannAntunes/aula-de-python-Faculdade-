# 48. Escreva um algoritmo que solicite ao usuario uma palavra e exiba cada
# letra da palavra em uma linha separada.

palavra = input("Digite uma palavra: ")

print(f"\nLetras da palavra '{palavra}':")
for letra in palavra:
    print(letra)
