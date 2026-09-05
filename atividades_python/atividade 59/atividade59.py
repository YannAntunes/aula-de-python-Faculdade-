# 59. Escreva um programa que solicite ao usuario para digitar dois numeros e verifique se o
# primeiro e maior que o segundo. Continue pedindo numeros ate que o primeiro numero seja
# maior que o segundo.

print("Digite dois numeros onde o primeiro deve ser maior que o segundo.")

while True:
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))

    if numero1 > numero2:
        print(f"Correto! {numero1} e maior que {numero2}.")
        break
    else:
        print(f"O primeiro numero ({numero1}) nao e maior que o segundo ({numero2}). Tente novamente.")
