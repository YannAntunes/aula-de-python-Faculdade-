# 69. Crie no algoritmo 67 as seguintes funcionalidades:
# - Informe ao usuário em caso de empate.
# - Crie uma forma de não permitir que um jogador jogue no mesmo lugar que já tenha
#   uma jogada realizada.
# - Atualmente o jogo encerra com o vencedor, ele agora também deve encerrar em caso
#   de empate.
# - Ao finalizar o jogo deve ser informado ao usuário uma mensagem solicitando uma nova
#   partida, o sistema deve reiniciar o jogo em caso de sim, e encerrar o programa em
#   caso de não.
# - Refatore a funcionalidade que verifica a vitória e pense em uma forma de simplificar
#   o código corrigido.

import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def criar_tabuleiro():
    return [[" " for _ in range(3)] for _ in range(3)]


def exibir_tabuleiro(tabuleiro):
    print("\n  ╔═══╦═══╦═══╗")
    for i, linha in enumerate(tabuleiro):
        print(f"  ║ {linha[0]} ║ {linha[1]} ║ {linha[2]} ║   ← {'ABC'[i]}")
        if i < 2:
            print("  ╠═══╬═══╬═══╣")
    print("  ╚═══╩═══╩═══╝")
    print("    1   2   3")
    print()


def verificar_vencedor(tabuleiro, jogador):
    """
    Verifica se o jogador atual venceu.
    Versão simplificada: verifica todas as linhas, colunas e diagonais
    usando uma única abordagem com transposição para colunas.
    """
    # Verifica linhas
    linhas_vencedoras = (
        # Linhas horizontais
        [tabuleiro[0], tabuleiro[1], tabuleiro[2]] +
        # Colunas (transposta)
        [[tabuleiro[i][j] for i in range(3)] for j in range(3)] +
        # Diagonais
        [[tabuleiro[i][i] for i in range(3)],
         [tabuleiro[i][2 - i] for i in range(3)]]
    )

    return any(all(cel == jogador for cel in linha) for linha in linhas_vencedoras)


def tabuleiro_cheio(tabuleiro):
    return all(tabuleiro[i][j] != " " for i in range(3) for j in range(3))


def obter_jogada(tabuleiro, jogador):
    """Solicita e valida a jogada do jogador atual."""
    linha_map = {"A": 0, "B": 1, "C": 2}
    col_map = {"1": 0, "2": 1, "3": 2}

    while True:
        try:
            jogada = input(f"  Jogador {jogador}, insira sua jogada (ex: A1, B2, C3): ").strip().upper()

            if len(jogada) < 2 or jogada[0] not in linha_map or jogada[1] not in col_map:
                print("  ⚠ Posição inválida! Use Letra (A-C) + Número (1-3). Ex: A1")
                continue

            linha = linha_map[jogada[0]]
            col = col_map[jogada[1]]

            if tabuleiro[linha][col] != " ":
                print(f"  ⚠ A posição {jogada} já está ocupada! Escolha outra posição.")
                continue

            return linha, col

        except Exception:
            print("  ⚠ Entrada inválida! Tente novamente.")


def jogar():
    """Executa uma partida completa do Jogo da Velha."""
    tabuleiro = criar_tabuleiro()
    jogadores = ["X", "O"]
    turno = 0

    while True:
        limpar_tela()
        jogador = jogadores[turno % 2]

        print(f"\n  === JOGO DA VELHA ===  Vez do Jogador {jogador}")
        exibir_tabuleiro(tabuleiro)

        linha, col = obter_jogada(tabuleiro, jogador)
        tabuleiro[linha][col] = jogador

        # Verificar vitória
        if verificar_vencedor(tabuleiro, jogador):
            limpar_tela()
            print(f"\n  === JOGO DA VELHA ===")
            exibir_tabuleiro(tabuleiro)
            print(f" Parabéns! O Jogador {jogador} venceu!")
            return

        # Verificar empate
        if tabuleiro_cheio(tabuleiro):
            limpar_tela()
            print(f"\n  === JOGO DA VELHA ===")
            exibir_tabuleiro(tabuleiro)
            print(" Empate! Nenhum jogador conseguiu vencer.")
            return

        turno += 1


# Programa principal
limpar_tela()
print("\n" + "=" * 35)
print("   BEM-VINDO AO JOGO DA VELHA!")
print("=" * 35)
print("\n  Como jogar:")
print("  - Use Letra + Número para jogar (ex: A1, B2, C3)")
print("  - Letras: A (linha 1), B (linha 2), C (linha 3)")
print("  - Números: 1 (coluna 1), 2 (coluna 2), 3 (coluna 3)")

while True:
    jogar()

    print()
    resposta = input("  Deseja jogar novamente? (s/n): ").strip().lower()
    if resposta == "s":
        limpar_tela()
        print("\n  Iniciando nova partida...")
    else:
        print("\n  Obrigado por jogar! Até a próxima.")
        break
