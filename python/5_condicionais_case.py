# Case 

numero1 = 10
numero2 = 5
opcao = 1

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