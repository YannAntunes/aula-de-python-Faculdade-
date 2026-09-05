# 23. Crie um algoritmo que peca ao usuario uma palavra e verifique se a palavra e "Python".

palavra = input("Digite uma palavra: ").strip()

if palavra.lower() == "python":
    print("A palavra digitada e Python!")
else:
    print(f"A palavra digitada ({palavra}) nao e Python.")
