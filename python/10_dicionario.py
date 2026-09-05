Aluno = {
    "nome": "Yann",
    "idade": 21,
    "email": "yann@example.com"
}

print(Aluno)
print(type(Aluno))

print(Aluno["nome"])
print(Aluno["email"])

print(f'O aluno {Aluno["nome"]} tem {Aluno["idade"]} anos e seu email é {Aluno["email"]}.')


Clientes = [
{
    "nome": "Yann",
    "idade": 21,
    "email": "yann@example.com",
    "telefone": ["1234-5678", "9876-5432"]
},
{
    "nome": "Debora",
    "idade": 26,
    "email": "debora@example.com",
    "telefone": ["5555-1234", "5555-5678"]
},
{
    "nome": "Victor",
    "idade": 22,
    "email": "victor@example.com",
    "telefone": ["9999-1234", "9999-5678"]
}
]

print(Clientes[1]["telefone"][1])