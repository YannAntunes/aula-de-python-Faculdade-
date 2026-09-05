# 66. Escreva um algoritmo que forneca um menu para o usuario:
# 1 - Cadastrar nome
# 2 - Atualizar o nome
# 3 - Excluir
# 4 - Listar todos os cadastrados
# Ao final da operacao deve dar uma mensagem indicando o resultado da operacao e
# perguntando se deseja realizar outra operacao. O aplicativo apenas deve encerrar
# quando a opcao nao for inserida.

nomes = []


def exibir_menu():
    print("\n========== MENU ==========")
    print("1 - Cadastrar nome")
    print("2 - Atualizar nome")
    print("3 - Excluir nome")
    print("4 - Listar todos os cadastrados")
    print("==========================")


def cadastrar_nome():
    nome = input("Digite o nome a cadastrar: ").strip()
    if nome:
        nomes.append(nome)
        print(f"Nome '{nome}' cadastrado com sucesso!")
    else:
        print("Nome invalido. Operacao cancelada.")


def atualizar_nome():
    if not nomes:
        print("Nenhum nome cadastrado para atualizar.")
        return

    print("\nNomes cadastrados:")
    for i, nome in enumerate(nomes, 1):
        print(f"  {i}. {nome}")

    try:
        indice = int(input("Digite o numero do nome que deseja atualizar: ")) - 1
        if 0 <= indice < len(nomes):
            novo_nome = input(f"Digite o novo nome para substituir '{nomes[indice]}': ").strip()
            if novo_nome:
                nome_antigo = nomes[indice]
                nomes[indice] = novo_nome
                print(f"Nome '{nome_antigo}' atualizado para '{novo_nome}' com sucesso!")
            else:
                print("Nome invalido. Operacao cancelada.")
        else:
            print("Numero invalido. Operacao cancelada.")
    except ValueError:
        print("Entrada invalida. Digite um numero.")


def excluir_nome():
    if not nomes:
        print("Nenhum nome cadastrado para excluir.")
        return

    print("\nNomes cadastrados:")
    for i, nome in enumerate(nomes, 1):
        print(f"  {i}. {nome}")

    try:
        indice = int(input("Digite o numero do nome que deseja excluir: ")) - 1
        if 0 <= indice < len(nomes):
            nome_removido = nomes.pop(indice)
            print(f"Nome '{nome_removido}' excluido com sucesso!")
        else:
            print("Numero invalido. Operacao cancelada.")
    except ValueError:
        print("Entrada invalida. Digite um numero.")


def listar_nomes():
    if not nomes:
        print("Nenhum nome cadastrado.")
    else:
        print("\n====== NOMES CADASTRADOS ======")
        for i, nome in enumerate(nomes, 1):
            print(f"  {i}. {nome}")
        print(f"  Total: {len(nomes)} nome(s)")
        print("================================")


# Loop principal
while True:
    exibir_menu()
    opcao = input("Escolha uma opcao: ").strip()

    if opcao == "1":
        cadastrar_nome()
    elif opcao == "2":
        atualizar_nome()
    elif opcao == "3":
        excluir_nome()
    elif opcao == "4":
        listar_nomes()
    else:
        print("Opcao invalida. Encerrando o programa...")
        break

    continuar = input("\nDeseja realizar outra operacao? (s/n): ").strip().lower()
    if continuar != "s":
        print("Programa encerrado. Ate logo!")
        break
