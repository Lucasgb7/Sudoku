import interface as t
import numpy as np


def changeIndex(position, boardsize):
    'Converte a notação algébrica para formato index (x, y)'
    position = position.strip().lower()  # strip() -> remove os espacos em branco / lower() -> coloca em minusculo
    x = ord(position[0]) - ord('a')  # define a posicao x pelo Unicode (unicode(x)-unicode('a') = posicao x)
    y = int(position[1:]) - 1  # define a posicao y pelo numero digitado
    return x, y


valid = False
while not valid:  # Definicao de valores de tamanho e posicao inicial
    str_N = input("Defina o tamanho da matriz quadrada (N² = 4, 9 ou 16): ")
    N = int(str_N)
    start = input("Defina a posição inicial da distribuição dos valores (Ex.: A1): ")

    root = np.sqrt(N)
    if int(root + 0.5) ** 2 == N:
        if 1 < root <= 16: valid = True
    else:
        print('Digite um valor correto!')

tabuleiro = np.zeros((N, N))
print(tabuleiro)
posInicial = changeIndex(start, N)
print(posInicial)
