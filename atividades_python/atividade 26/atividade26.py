# 26. Desenvolva um algoritmo que peca ao usuario para inserir dois numeros e verifique
# se ambos sao multiplos de 5.

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

if numero1 % 5 == 0 and numero2 % 5 == 0:
    print(f"Ambos os numeros ({numero1} e {numero2}) sao multiplos de 5.")
else:
    print("Nem ambos os numeros sao multiplos de 5.")
