# condicional If

idade = 10
acompanhado = False

# if idade >= 18:
#     print('Voce é maior de idade')
# else:
#     print('Voce não é maior de idade')

# if idade >=18:
#     print('Pode assistir ao filme')
# elif (idade >= 15) and (acompanhado == True):
#     print('Pode assistir ao filme, mas precisa estar acompanhado') 
# elif (idade >= 15) and (acompanhado == False):
#     print('Voce e menor e nao pode assistir ao filme') 
# else:
#     print('Voce nao pode assistir ao filme')

if idade >=18:
    print('Pode assistir ao filme')
elif idade >= 15:
    if acompanhado == True:
        print('Pode assistir ao filme, mas precisa estar acompanhado') 
elif idade >= 15:
    if acompanhado == False:
        print('Voce e menor e nao pode assistir ao filme') 
else:
    print('Voce nao pode assistir ao filme')