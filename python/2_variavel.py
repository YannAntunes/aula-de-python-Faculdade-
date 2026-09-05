# VARIAVEIS:

nome = 'y' \
'ann'
idade = 21
altura = 1.78   
vivo = True
nascimento = '2005-04-03'

# Verificar conteudo de variaveis

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('Vivo:', vivo)
print('Nascimento:', nascimento)

# concatenando variaveis

print('Seu nome e', nome, 'e voce tem', idade, 'anos de idade e mede', altura, 'metros de altura.')
print(f'sua idade é {idade} anos e voce nasceu em {nascimento}.')

# Verificando o tipo de variavel

print(type(nome))
print(type(idade))
print(type(altura))
print(type(vivo))
print(type(nascimento))

# exemplo de uso dos metodos de uma classe 

print(f'Conteudo original: {nome}')
print(f'Conteudo em maiusculo: {nome.upper()}')
print(f'Conteudo em capitalize: {nome.capitalize()}')


