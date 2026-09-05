cavaleiros = ['Arthur', 'Lancelot', 'Gawain', 'Percival', 'Galahad']


# acressando elementos da lista por índice

cavaleiros.append('Tristão')

# acressando elementos da lista por extend

cavaleiros.extend(['Bors', 'Yann'])

# acressando elementos da lista por insert

cavaleiros.insert(0, 'Geraint')


for cavaleiro in cavaleiros:
    print(cavaleiro)

# removendo elementos da lista por pocição

cavaleiros.pop(1)
print(cavaleiros)

# removendo elementos da lista 

cavaleiros.remove('Yann')
print(cavaleiros)

# removendo elementos no final
cavaleiros.pop()
print(cavaleiros)

# limpando a lista

# cavaleiros.clear()  
# print(cavaleiros)

# # removenda da memoria a lista
# del cavaleiros
# print(cavaleiros)

# organizando a lista

# alfabeticamente ou numericamente
cavaleiros.sort()
print(cavaleiros)

# invertendo a lista
cavaleiros.reverse()
print(cavaleiros)

# verificando o tamanho da lista
print(len(cavaleiros))

# verificando o indice do elemento está na lista
print(cavaleiros.index('Percival'))

cavaleiros.pop(cavaleiros.index('Percival'))
print(cavaleiros)