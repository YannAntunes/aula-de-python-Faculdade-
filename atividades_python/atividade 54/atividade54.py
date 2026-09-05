# 54. Crie um algoritmo que solicite ao usuario um numero e continue pedindo outro
# numero ate que um numero negativo seja inserido.

print("Digite numeros (um numero negativo encerrara o programa):")

while True:
    numero = float(input("Digite um numero: "))
    if numero < 0:
        print(f"Numero negativo ({numero}) detectado. Encerrando...")
        break
    else:
        print(f"Voce digitou: {numero}")
