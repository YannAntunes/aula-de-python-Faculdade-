# 55. Desenvolva um programa que peca ao usuario para inserir um numero maior que 100.
# Se o numero for menor ou igual a 100, continue pedindo ate que um numero maior que 100 seja inserido.

print("Por favor, insira um numero maior que 100.")

while True:
    numero = float(input("Digite um numero: "))
    if numero > 100:
        print(f"Parabens! Voce inseriu {numero}, que e maior que 100.")
        break
    else:
        print(f"O numero {numero} nao e maior que 100. Tente novamente.")
