# 20. Crie um programa que solicite ao usuario a temperatura em graus Celsius
# e converta para Fahrenheit.

celsius = float(input("Digite a temperatura em graus Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius} graus Celsius equivale a {fahrenheit:.2f} graus Fahrenheit")
