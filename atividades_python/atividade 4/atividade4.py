# 4. Crie um algoritmo que solicite ao usuário uma cor (vermelho, verde, azul) e exiba uma mensagem correspondente à cor escolhida.
cor = input("Digite uma cor (vermelho, verde, azul): ")
if cor.lower() == "vermelho":
    print("Você escolheu a cor vermelha!")
elif cor.lower() == "verde":
    print("Você escolheu a cor verde!")
elif cor.lower() == "azul":
    print("Você escolheu a cor azul!")
else:
    print("Cor não reconhecida.")