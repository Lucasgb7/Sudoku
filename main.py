import numpy as np
import turtle
import interface as it


def solucionar(tabuleiro):
    'Faz as delimitações de busca'
    find = findEmpty(tabuleiro)
    if not find:  # Todas as posicoes ocupadas
        return True
    else:
        x, y = find  # linha e coluna

    for num in range(1, N + 1):  # numeros possiveis no tabuleiro
        if verifica(tabuleiro, num, (x, y)): # verifica se o espaco esta ocupado com o mesmo numero da sequencia (seguindo a logica do Sudoku)
            tabuleiro[x][y] = num

            if solucionar(tabuleiro):  # terminou
                return True

            tabuleiro[x][y] = 0

    return False


def verifica(tabuleiro, num, pos):
    'Faz as delimitações de busca'
    raiz = int(np.sqrt(N))  # dependendo do tamanho do tabuleiro sua raiz sera diferente
    # Verifica cada linha
    for i in range(len(tabuleiro[0])):
        if tabuleiro[pos[0]][i] == num and pos[1] != i:  # se a linha possui valor igual ao numero a ser inserido
            return False

    # Verifica cada coluna
    for i in range(len(tabuleiro)):
        if tabuleiro[i][pos[1]] == num and pos[0] != i:  # se a coluna possui o valor igual ao ser inserido
            return False

    # Verifica o quadrante
    quadrante_x = pos[1] // raiz
    quadrante_y = pos[0] // raiz
    for i in range(quadrante_y * raiz, quadrante_y * raiz + raiz):
        for j in range(quadrante_x * raiz, quadrante_x * raiz + raiz):
            if tabuleiro[i][j] == num and (i, j) != pos:  # se o valor esta inserido no quadrante
                return False

    return True


def findEmpty(tabuleiro):
    'Encontra uma posição que esteja vazia no tabuleiro'
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[0])):
            if tabuleiro[i][j] == 0:
                return i, j  # linha, coluna

    return None


def changeIndex(position, boardsize):
    'Converte a notação algébrica para formato index (x, y)'
    position = position.strip().lower()  # strip() -> remove os espacos em branco / lower() -> coloca em minusculo
    x = ord(position[0]) - ord('a')  # define a posicao x pelo Unicode (unicode(x)-unicode('a') = posicao x)
    y = int(position[1:]) - 1  # define a posicao y pelo numero digitado
    return x, y


if __name__ == '__main__':

    valid = False
    while not valid:  # Definicao de valores de tamanho e posicao inicial
        str_N = input("Defina o tamanho da matriz quadrada (N² = 4, 9 ou 16): ")
        N = int(str_N)
        start = input("Defina a posição inicial da distribuição dos valores (Ex.: A1 [A= Linha | 1= Coluna]): ")
        posInicial = changeIndex(start, N)  # Converte a posicao definida para x, y
        tabuleiro = np.zeros((N, N))    # Cria uma matriz NxN com zeros
        root = np.sqrt(N)   # Raiz do tamanho do tabuleiro
        if int(root + 0.5) ** 2 == N:
            if 1 < root <= 16:
                if tabuleiro[posInicial[0]][posInicial[1]] == 0:
                    valid = True
                else:
                    print('Posição já ocupada!')
        else:
            print('Digite um valor correto!')



    print("Tabuleiro Inicial: ")
    print(tabuleiro)
    tabuleiro[posInicial[0]][posInicial[1]] = 1
    if solucionar(tabuleiro):
        print("--------------------------------------------")
        print("Solução:")
        print(tabuleiro)
    else:
        print("Não exite uma solução!")

    if N == 16:
        it.drawTabuleiro(-370, -380, 46, N, tabuleiro)  # Pos_inicial_x, Pos_inicial_y, tamQuadrado, tamTabuleiro, matriz do tabuleiro
    elif N == 9:
        it.drawTabuleiro(-210, -210, 46, N, tabuleiro)
    elif N == 4:
        it.drawTabuleiro(-95, -95, 46, N, tabuleiro)

    turtle.done()
