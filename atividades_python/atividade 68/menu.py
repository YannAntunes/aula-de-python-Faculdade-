# Módulo de menu para o sistema de cadastro de alunos
# Arquivo: menu.py
# Atividade 68


def exibir_menu():
    """Exibe o menu principal do sistema."""
    print("\n" + "=" * 45)
    print("   SISTEMA DE CADASTRO DE ALUNOS")
    print("=" * 45)
    print("  1 - Cadastrar novo aluno")
    print("  2 - Atualizar dados de um aluno")
    print("  3 - Remover aluno")
    print("  4 - Listar todos os alunos")
    print("  5 - Buscar aluno por matrícula")
    print("  0 - Encerrar o programa")
    print("=" * 45)


def obter_opcao():
    """Obtém a opção do usuário do menu."""
    return input("  Escolha uma opção: ").strip()
