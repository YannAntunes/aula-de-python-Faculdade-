# 19. Escreva um algoritmo que peca ao usuario o nome de uma fruta e verifique
# se a fruta e uma maca.

fruta = input("Digite o nome de uma fruta: ").strip().lower()

if fruta == "maca":
    print("A fruta informada e uma maca!")
else:
    print(f"A fruta informada ({fruta}) nao e uma maca.")
