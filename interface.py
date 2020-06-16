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


# Desenha um bloco
def quadrado(posx, posy, lado, cor):
    # turtle.hideturtle()
    turtle.showturtle()
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.pendown()
    turtle.fillcolor(cor)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(lado)
        turtle.left(90)
    turtle.end_fill()
    turtle.hideturtle()


# Desenha um tabuleiro
def tabuleiro(posx, posy, lado, N, matriz):
    turtle.speed(0)
    # Posicao inicial
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.pendown()
    for i in range(1, N + 1):
        # Desenha linha (i)
        for j in range(1, N + 1):
            quadrado(turtle.xcor(), turtle.ycor(), lado, cores[matriz[(N - 1) - (i - 1)][(j - 1)]])
            turtle.setx(turtle.xcor() + lado)

        turtle.penup()
        turtle.goto(posx, turtle.ycor() + lado)
        turtle.pendown()
    drawQuadrant(N, lado, posx, posy)
    drawIndexPos(posx, posy, lado, N)

# Desenha um quadrante (sqrt(N))
def drawQuadrant(N, tamSquare, posx, posy):
    turtle.speed(0)
    turtle.pensize(5)
    raiz = int(np.sqrt(N))
    if N == 16:
        for x in range(raiz):
            turtle.penup()
            turtle.goto(posx + ((x + 1) * 4 * tamSquare), -400)
            turtle.pendown()
            turtle.goto(posx + ((x + 1) * 4 * tamSquare), 400)

        for x in range(raiz):
            turtle.penup()
            turtle.goto(-400, posy + ((x + 1) * 4 * tamSquare))
            turtle.pendown()
            turtle.goto(400, posy + ((x + 1) * 4 * tamSquare))


# Creditos
def drawCreditos(string, posx, posy, fontsize):
    turtle.showturtle()
    turtle.penup()
    turtle.pencolor("black")
    turtle.pensize(5)
    turtle.speed(6)
    turtle.goto(posx, posy)
    turtle.write(string, align="left", font=("Arial", fontsize, "normal"))
    # turtle.pendown()
    turtle.hideturtle()
    turtle.pensize(2)


# Desenha os indicadores de posicao
def drawIndexPos(posx, posy, tamSquare, N):
    turtle.showturtle()
    turtle.penup()
    turtle.pencolor("black")
    turtle.pensize(5)
    turtle.speed(0)
    letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]

    for x in range(N):
        turtle.goto((posx + tamSquare * x) + tamSquare / 2, 370)
        turtle.write(x+1, align="left", font=("Arial", 10, "normal"))

    for x in range(N):
        turtle.goto(-390, ((posy + tamSquare * x) + tamSquare / 2) - 10)
        turtle.write(letras[(N-1) - x], align="center", font=("Arial", 10, "normal"))

    turtle.pendown()
    turtle.pensize(2)
    turtle.hideturtle()

# Desenha os valores de cada posicao
def drawPos(val, i, j):
    turtle.showturtle()
    turtle.penup()
    turtle.pencolor("black")
    turtle.pensize(5)
    turtle.speed(6)
    turtle.goto((-280 + 70 * i)+70/2,(-280 + 70 * j)+70/2)
    turtle.write(val, align="center", font=("Arial", 18, "normal"))
    #turtle.pendown()
    turtle.hideturtle()

def drawPath(i, j):
    turtle.showturtle()
    turtle.pencolor("black")
    turtle.pensize(5)
    turtle.speed(1)

    turtle.goto((-280 + 70 * i) + 70 / 2, (-280 + 70 * j) + 70 / 2)
    turtle.pendown()

##if __name__ == '__main__':
##tabuleiro(-380,-380, 48, 16,"white")
##turtle.done()
