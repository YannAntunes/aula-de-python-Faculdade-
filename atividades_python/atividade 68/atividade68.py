# 68. Crie uma nova versão do algoritmo 66, aplicando o conceito de módulos e dividindo as
# responsabilidades. Receberemos agora não somente o nome, mas simularemos um sistema de
# cadastro de alunos. Esta nova versão deve atender as novas funcionalidades a seguir:
#
# - Cada aluno cadastrado deve ter atrelado a seus dados pessoais (nome, e-mail, data de
#   nascimento, matrícula). No caso de matrícula, deve-se gerar uma matrícula única para
#   cada aluno cadastrado.
# - Cada um dos dados do aluno devem ser validados de forma que o código não quebre ao
#   serem informados valores incorretos.
# - Para atualizar qualquer dado do aluno, deve-se localizá-lo utilizando sua matrícula.
#   Valide de forma que o sistema não quebre ao ser inserido uma matrícula inválida.
# - Para remover um aluno, deve-se realizar esta ação usando sua matrícula. O sistema não
#   pode quebrar ao ser inserido uma matrícula errada.
# - Ao listar todos os alunos, mostre cada um de forma organizada e separada.
# - Crie uma funcionalidade que mostre os dados de um aluno específico usando apenas
#   sua matrícula.
#
# Módulos utilizados:
# - alunos.py: Contém as funções de CRUD (cadastrar, atualizar, remover, listar, buscar)
# - validacoes.py: Contém as funções de validação (nome, e-mail, data, matrícula)
# - menu.py: Contém as funções de exibição do menu
#
# Arquivo principal: atividade68.py

from menu import exibir_menu, obter_opcao
from alunos import cadastrar_aluno, atualizar_aluno, remover_aluno, listar_alunos, buscar_aluno

# Lista principal de alunos (banco de dados em memória)
alunos = []


def executar_opcao(opcao):
    """Executa a operação correspondente à opção escolhida."""
    if opcao == "1":
        cadastrar_aluno(alunos)
    elif opcao == "2":
        atualizar_aluno(alunos)
    elif opcao == "3":
        remover_aluno(alunos)
    elif opcao == "4":
        listar_alunos(alunos)
    elif opcao == "5":
        buscar_aluno(alunos)
    elif opcao == "0":
        return False
    else:
        print("\n  ✘ Opção inválida. Por favor, escolha uma opção do menu.")

    return True


# Loop principal do sistema
print("\nBem-vindo ao Sistema de Cadastro de Alunos!")

continuar = True
while continuar:
    exibir_menu()
    opcao = obter_opcao()

    if opcao == "0":
        print("\n  Encerrando o sistema. Até logo!")
        break

    continuar = executar_opcao(opcao)

    if continuar:
        input("\n  Pressione ENTER para continuar...")
