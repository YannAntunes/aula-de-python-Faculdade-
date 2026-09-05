# 42. Escreva um algoritmo que solicite ao usuario 5 numeros inteiros e calcule
# a soma desses numeros.

soma = 0

print("Digite 5 numeros inteiros:")
for i in range(1, 6):
    numero = int(input(f"Numero {i}: "))
    soma += numero

print(f"\nA soma dos 5 numeros e: {soma}")
