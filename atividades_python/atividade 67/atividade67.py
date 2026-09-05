# 67. Desenvolva um jogo da velha em python que funcione no terminal.

import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def criar_tabuleiro():
    return [[" " for _ in range(3)] for _ in range(3)]


def exibir_tabuleiro(tabuleiro):
    print("\n  Jogo da Velha")
    print("  -------------")
    print("    1   2   3")
    for i, linha in enumerate(tabuleiro):
        print(f"  {'ABC'[i]} {linha[0]} | {linha[1]} | {linha[2]}")
        if i < 2:
            print("   ---|---|---")
    print()


def verificar_vencedor(tabuleiro, jogador):
    # Verifica linhas e colunas
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)):
            return True
        if all(tabuleiro[j][i] == jogador for j in range(3)):
            return True
    # Verifica diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False


def tabuleiro_cheio(tabuleiro):
    return all(tabuleiro[i][j] != " " for i in range(3) for j in range(3))


def obter_jogada(tabuleiro, jogador):
    while True:
        try:
            jogada = input(f"Jogador {jogador}, insira sua jogada (ex: A1, B2, C3): ").strip().upper()
            if len(jogada) < 2:
                print("Entrada invalida! Use o formato Letra+Numero (ex: A1).")
                continue

            linha_map = {"A": 0, "B": 1, "C": 2}
            col_map = {"1": 0, "2": 1, "3": 2}

            linha_char = jogada[0]
            col_char = jogada[1]

            if linha_char not in linha_map or col_char not in col_map:
                print("Posicao invalida! Use letras A, B ou C e numeros 1, 2 ou 3.")
                continue

            linha = linha_map[linha_char]
            col = col_map[col_char]

            if tabuleiro[linha][col] != " ":
                print("Essa posicao ja esta ocupada! Escolha outra.")
                continue

            return linha, col
        except Exception:
            print("Entrada invalida! Tente novamente.")


def jogar():
    tabuleiro = criar_tabuleiro()
    jogadores = ["X", "O"]
    turno = 0

    while True:
        limpar_tela()
        exibir_tabuleiro(tabuleiro)

        jogador = jogadores[turno % 2]
        linha, col = obter_jogada(tabuleiro, jogador)
        tabuleiro[linha][col] = jogador

        if verificar_vencedor(tabuleiro, jogador):
            limpar_tela()
            exibir_tabuleiro(tabuleiro)
            print(f"Parabens! O Jogador {jogador} venceu!")
            break

        if tabuleiro_cheio(tabuleiro):
            limpar_tela()
            exibir_tabuleiro(tabuleiro)
            print("Empate! Nenhum jogador venceu.")
            break

        turno += 1


# Programa principal
print("=" * 30)
print("   BEM-VINDO AO JOGO DA VELHA!")
print("=" * 30)

jogar()
