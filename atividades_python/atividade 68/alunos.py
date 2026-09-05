# Modulo de gerenciamento de alunos
# Arquivo: alunos.py
# Atividade 68

import uuid
from validacoes import validar_nome, validar_email, validar_data_nascimento, validar_matricula


def gerar_matricula():
    """Gera uma matricula unica para cada aluno."""
    codigo = str(uuid.uuid4()).replace("-", "").upper()[:8]
    return f"MAT-{codigo}"


def cadastrar_aluno(alunos):
    """Cadastra um novo aluno no sistema."""
    print("\n--- CADASTRAR NOVO ALUNO ---")

    # Validar nome
    while True:
        nome_input = input("Nome: ")
        valido, resultado = validar_nome(nome_input)
        if valido:
            nome = resultado
            break
        print(f"  Erro: {resultado}")

    # Validar e-mail
    while True:
        email_input = input("E-mail: ")
        valido, resultado = validar_email(email_input)
        if valido:
            email = resultado
            break
        print(f"  Erro: {resultado}")

    # Validar data de nascimento
    while True:
        data_input = input("Data de nascimento (DD/MM/AAAA): ")
        valido, resultado = validar_data_nascimento(data_input)
        if valido:
            data_nascimento = resultado
            break
        print(f"  Erro: {resultado}")

    # Gerar matricula unica
    matricula = gerar_matricula()

    aluno = {
        "nome": nome,
        "email": email,
        "data_nascimento": data_nascimento,
        "matricula": matricula
    }

    alunos.append(aluno)
    print(f"\n  Aluno '{nome}' cadastrado com sucesso!")
    print(f"  Matricula gerada: {matricula}")


def atualizar_aluno(alunos):
    """Atualiza os dados de um aluno pelo numero de matricula."""
    if not alunos:
        print("\n  Nenhum aluno cadastrado.")
        return

    print("\n--- ATUALIZAR ALUNO ---")
    matricula_input = input("Digite a matricula do aluno: ")
    valido, resultado = validar_matricula(matricula_input, alunos)

    if not valido:
        print(f"  Erro: {resultado}")
        return

    aluno = resultado
    print(f"\n  Aluno encontrado: {aluno['nome']} (Matricula: {aluno['matricula']})")
    print("  O que deseja atualizar?")
    print("  1 - Nome")
    print("  2 - E-mail")
    print("  3 - Data de nascimento")

    opcao = input("  Escolha: ").strip()

    if opcao == "1":
        while True:
            novo_nome = input("  Novo nome: ")
            valido, resultado = validar_nome(novo_nome)
            if valido:
                aluno["nome"] = resultado
                print(f"  Nome atualizado para '{resultado}' com sucesso!")
                break
            print(f"  Erro: {resultado}")

    elif opcao == "2":
        while True:
            novo_email = input("  Novo e-mail: ")
            valido, resultado = validar_email(novo_email)
            if valido:
                aluno["email"] = resultado
                print("  E-mail atualizado com sucesso!")
                break
            print(f"  Erro: {resultado}")

    elif opcao == "3":
        while True:
            nova_data = input("  Nova data de nascimento (DD/MM/AAAA): ")
            valido, resultado = validar_data_nascimento(nova_data)
            if valido:
                aluno["data_nascimento"] = resultado
                print("  Data de nascimento atualizada com sucesso!")
                break
            print(f"  Erro: {resultado}")

    else:
        print("  Opcao invalida. Nenhuma alteracao feita.")


def remover_aluno(alunos):
    """Remove um aluno pelo numero de matricula."""
    if not alunos:
        print("\n  Nenhum aluno cadastrado.")
        return

    print("\n--- REMOVER ALUNO ---")
    matricula_input = input("Digite a matricula do aluno a ser removido: ")
    valido, resultado = validar_matricula(matricula_input, alunos)

    if not valido:
        print(f"  Erro: {resultado}")
        return

    aluno = resultado
    confirmacao = input(f"  Deseja remover o aluno '{aluno['nome']}'? (s/n): ").strip().lower()

    if confirmacao == "s":
        alunos.remove(aluno)
        print(f"  Aluno '{aluno['nome']}' removido com sucesso!")
    else:
        print("  Operacao cancelada.")


def listar_alunos(alunos):
    """Lista todos os alunos cadastrados."""
    print("\n--- LISTA DE ALUNOS ---")
    if not alunos:
        print("  Nenhum aluno cadastrado.")
        return

    print(f"  Total de alunos: {len(alunos)}")
    print("  " + "=" * 60)
    for i, aluno in enumerate(alunos, 1):
        print(f"\n  Aluno #{i}")
        print(f"  {'Matricula:':<20} {aluno['matricula']}")
        print(f"  {'Nome:':<20} {aluno['nome']}")
        print(f"  {'E-mail:':<20} {aluno['email']}")
        print(f"  {'Data de Nascimento:':<20} {aluno['data_nascimento']}")
        print("  " + "-" * 60)


def buscar_aluno(alunos):
    """Busca e exibe os dados de um aluno especifico pela matricula."""
    if not alunos:
        print("\n  Nenhum aluno cadastrado.")
        return

    print("\n--- BUSCAR ALUNO ---")
    matricula_input = input("Digite a matricula do aluno: ")
    valido, resultado = validar_matricula(matricula_input, alunos)

    if not valido:
        print(f"  Erro: {resultado}")
        return

    aluno = resultado
    print("\n  Aluno encontrado!")
    print("  " + "=" * 60)
    print(f"  {'Matricula:':<20} {aluno['matricula']}")
    print(f"  {'Nome:':<20} {aluno['nome']}")
    print(f"  {'E-mail:':<20} {aluno['email']}")
    print(f"  {'Data de Nascimento:':<20} {aluno['data_nascimento']}")
    print("  " + "=" * 60)
