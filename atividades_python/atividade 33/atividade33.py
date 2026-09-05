# 33. Crie um programa que solicite ao usuario o valor de um produto e calcule
# o desconto de 10%.

valor = float(input("Digite o valor do produto: R$ "))

desconto = valor * 0.10
valor_final = valor - desconto

print(f"\nValor original:    R$ {valor:.2f}")
print(f"Desconto (10%):    R$ {desconto:.2f}")
print(f"Valor com desconto: R$ {valor_final:.2f}")
