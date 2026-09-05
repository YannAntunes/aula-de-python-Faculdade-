# 58. Desenvolva um algoritmo que solicite ao usuario uma palavra e continue pedindo
# outra palavra ate que ele digite "sair".

print("Digite palavras (digite 'sair' para encerrar):")

while True:
    palavra = input("Digite uma palavra: ").strip().lower()
    if palavra == "sair":
        print("Programa encerrado. Ate logo!")
        break
    else:
        print(f"Voce digitou: {palavra}")
