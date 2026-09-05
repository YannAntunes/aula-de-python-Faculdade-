# 17. Crie um programa que solicite ao usuario dois numeros e exiba a soma,
# subtracao, multiplicacao e divisao entre eles.

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

print(f"\nResultados das operacoes:")
print(f"Soma:           {numero1} + {numero2} = {numero1 + numero2}")
print(f"Subtracao:      {numero1} - {numero2} = {numero1 - numero2}")
print(f"Multiplicacao:  {numero1} * {numero2} = {numero1 * numero2}")

if numero2 != 0:
    print(f"Divisao:        {numero1} / {numero2} = {numero1 / numero2}")
else:
    print("Divisao:        Nao e possivel dividir por zero.")
