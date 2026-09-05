# 12. Escreva um programa que peca ao usuario para escolher um modo de transporte
# (carro, bicicleta, a pe) e exiba uma mensagem com a velocidade media correspondente.

transporte = input("Escolha um modo de transporte (carro, bicicleta, a pe): ").strip().lower()

if transporte == "carro":
    print("A velocidade media de um carro e de aproximadamente 80 km/h.")
elif transporte == "bicicleta":
    print("A velocidade media de uma bicicleta e de aproximadamente 20 km/h.")
elif transporte == "a pe":
    print("A velocidade media a pe e de aproximadamente 5 km/h.")
else:
    print("Modo de transporte invalido.")
