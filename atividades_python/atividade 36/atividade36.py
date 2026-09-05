# 36. Crie um programa que solicite ao usuario um numero de 1 a 12 e exiba
# o mes correspondente.

meses = {
    1: "Janeiro", 2: "Fevereiro", 3: "Marco", 4: "Abril",
    5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
    9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
}

numero = int(input("Digite um numero de 1 a 12: "))

if numero in meses:
    print(f"O mes {numero} e {meses[numero]}.")
else:
    print("Numero invalido. Digite um valor entre 1 e 12.")
