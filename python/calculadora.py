
print('1 - Soma')
print('2 - Subtracao')
print('3 - Multiplicacao')
print('4 - Divisao')

opcao = int(input('Escolha uma opcao: '))

numero1 = float(input('Digite o primeiro numero: '))
numero2 = float(input('Digite o segundo numero: '))

match opcao:
    case 1:
        print(f'a soma : {numero1 + numero2}')
    case 2:
        print(f'a subtracao : {numero1 - numero2}')
    case 3:
        print(f'a multiplicacao : {numero1 * numero2}')
    case 4:
        print(f'a divisao : {numero1 / numero2}')
    case _:
        print('opcao invalida')