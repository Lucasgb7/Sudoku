import numpy as np
import turtle

cores = {
    1: "#00FFFF",
    2: "#FFD8B1",
    3: "#0000FF",
    4: "#FF00FF",
    5: "#808080",
    6: "#008000",
    7: "#00FF00",
    8: "#800000",
    9: "#000080",
    10: "#808000",
    11: "#800080",
    12: "#FF0000",
    13: "#C0C0C0",
    14: "#008080",
    15: "#FFFFFF",
    16: "#FFFF00"
}


# Desenha o tabuleiro
def drawTabuleiro(x, y, tamQuadrado, N, matriz):
    turtle.speed(0)
    # Posicao inicial
    turtle.penup()
    turtle.goto(x, y) # Posicao inicial do tabuleiro
    turtle.pendown()
    for i in range(1, N+1):
        # Desenha linha (i)
        for j in range(1, N+1):
            pos = matriz[(N - 1) - (i - 1)][(j - 1)]
            drawSquare(turtle.xcor(), turtle.ycor(), tamQuadrado, cores[pos], pos)
            turtle.setx(turtle.xcor() + tamQuadrado)

        turtle.penup()
        turtle.goto(x, turtle.ycor() + tamQuadrado)
        turtle.pendown()
    drawQuadrant(x, y, tamQuadrado, N)  # Desenhar a separacao de quadrante
    drawIndexPos(x, y, tamQuadrado, N)  # Desenha os indices para identificar cada posicao

# Desenha um bloco
def drawSquare(x, y, tamanho, cor, numero):
    # turtle.hideturtle()
    turtle.showturtle()
    turtle.penup()
    turtle.goto(x, y)   # Vai a posicao a ser desenhada
    turtle.pendown()
    turtle.fillcolor(cor)   # Preenche a cor
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(tamanho)
        turtle.left(90)
    turtle.end_fill()
    turtle.hideturtle()
    drawNum(x, y, tamanho, numero)  # Funcao para desenhar o numero dentro do quadrado


# Desenha os valores de cada posicao
def drawNum(x, y, tamQuadrado, numero):
    turtle.showturtle()
    turtle.penup()
    turtle.goto(x+tamQuadrado/2, (y+tamQuadrado/2)-10)  # Vai a posicao a ser desenhada (meio do quadrado)
    turtle.pendown()
    turtle.write(int(numero), align="center", font=("Arial", 12, "normal")) # Escreve numero
    turtle.penup()
    turtle.goto(x, y)
    turtle.hideturtle()


# Desenha um quadrante (sqrt(N))
def drawQuadrant(x, y, tamQuadrado, N):
    turtle.speed(0)
    turtle.pensize(5)
    raiz = int(np.sqrt(N))

    for i in range(raiz-1):
        turtle.penup()
        turtle.goto(x + ((i + 1) * raiz * tamQuadrado), (x-20))
        turtle.pendown()
        turtle.goto(x + ((i + 1) * raiz * tamQuadrado), -1*(x-20))

    for j in range(raiz-1):
        turtle.penup()
        turtle.goto((x-20), y + ((j + 1) * raiz * tamQuadrado))
        turtle.pendown()
        turtle.goto(-1*(x-20), y + ((j + 1) * raiz * tamQuadrado))

# Desenha os indicadores de posicao
def drawIndexPos(x, y, tamQuadrado, N):
    turtle.showturtle()
    turtle.penup()
    turtle.pencolor("black")
    turtle.pensize(5)
    turtle.speed(0)
    letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]

    for i in range(N):
        turtle.goto((x + tamQuadrado * i) + tamQuadrado / 2, y + (tamQuadrado * N) + 5)
        turtle.write(i+1, align="left", font=("Arial", 10, "normal"))

    for j in range(N):
        turtle.goto(x - 10, ((y + tamQuadrado * j) + tamQuadrado / 2) - 10)
        turtle.write(letras[(N-1) - j], align="center", font=("Arial", 10, "normal"))

    turtle.pendown()
    turtle.pensize(2)
    turtle.hideturtle()
