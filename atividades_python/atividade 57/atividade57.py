# 57. Crie um programa que peca ao usuario para adivinhar um numero secreto entre 1 e 10.
# Continue pedindo ate que ele adivinhe o numero corretamente.

numero_secreto = 7  # Numero secreto predefinido

print("Bem-vindo ao jogo de adivinhacao!")
print("Tente adivinhar o numero secreto entre 1 e 10.")

tentativas = 0

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"Parabens! Voce adivinhou o numero {numero_secreto} em {tentativas} tentativa(s)!")
        break
    elif palpite < numero_secreto:
        print("Muito baixo! Tente um numero maior.")
    else:
        print("Muito alto! Tente um numero menor.")
