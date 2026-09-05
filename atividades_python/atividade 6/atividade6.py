# 6. Desenvolva um programa que pergunte ao usuario uma operacao matematica (+, -, *, /)
# e dois numeros, e realize a operacao escolhida.

operacao = input("Digite a operacao matematica (+, -, *, /): ")
numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

if operacao == "+":
    resultado = numero1 + numero2
    print(f"Resultado: {numero1} + {numero2} = {resultado}")
elif operacao == "-":
    resultado = numero1 - numero2
    print(f"Resultado: {numero1} - {numero2} = {resultado}")
elif operacao == "*":
    resultado = numero1 * numero2
    print(f"Resultado: {numero1} * {numero2} = {resultado}")
elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"Resultado: {numero1} / {numero2} = {resultado}")
    else:
        print("Erro: Divisao por zero nao e permitida.")
else:
    print("Operacao invalida.")
