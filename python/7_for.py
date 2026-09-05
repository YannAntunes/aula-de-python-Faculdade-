#laço de repetição for

for numero in range(10):
    print(numero)

# printando texto

palavra = "Yann"

for letra in palavra:
    letra = letra.upper()
    if letra == "Y":
        print("yeah")
    if letra == "a":
        print("aaaah")
    if letra == "n":
        print("uhuuuuu")
    if letra == "n":
        print("yeah")    


alunos = ["Yann", "Debora", "Victor"]

for indice, aluno in enumerate(alunos):
    print(indice, aluno)
    if (indice == 0):
        print("Yann é o melhor aluno da turma")