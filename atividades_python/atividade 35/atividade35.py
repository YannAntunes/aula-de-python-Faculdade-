# 35. Desenvolva um algoritmo que peca ao usuario para digitar dois numeros e verifique
# se a multiplicacao deles e igual a 20.

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

multiplicacao = numero1 * numero2

if multiplicacao == 20:
    print(f"A multiplicacao de {numero1} por {numero2} e igual a 20!")
else:
    print(f"A multiplicacao de {numero1} por {numero2} e {multiplicacao}, que nao e igual a 20.")
