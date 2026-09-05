# 24. Desenvolva um algoritmo que pergunte ao usuario o nome de uma cidade e verifique
# se e a capital do Brasil.

cidade = input("Digite o nome de uma cidade: ").strip().lower()

if cidade == "brasilia":
    print("Sim! Brasilia e a capital do Brasil.")
else:
    print(f"Nao, {cidade.capitalize()} nao e a capital do Brasil. A capital e Brasilia.")
