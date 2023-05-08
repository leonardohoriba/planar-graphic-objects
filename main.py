"""
5o ano - COMP 2023
Leonardo Horiba - 19411
Ten Marin - 19027
Cap Caique Nery - 20103
"""

import math

from PIL import Image

# As coordenadas de x e y estão em [0,200] x [-200,0].

def blackBackground():
    # Return black background 200x200
    return Image.new("1", (200, 200), color=0)

## Questao 1
def questao1():
    # Como a região esta definida entre [-1,1] x [-1,1], devemos realizar a transformacao
    # (x, y) -> (x/100-1, 1-y/100)
    img = blackBackground()
    (x, y) = img.size

    for a in range(x):
        for b in range(y):
            # Equacao da circunferencia para verificar a regiao de cada ponto em relacao a circunferencia
            p1 = (
                pow((a / 100 - 1) - 1 / 200, 2)
                + pow((1 - b / 100) - 1 / 200, 2)
                - pow(1, 2)
                < 0
            )
            p2 = (
                pow((a / 100 - 1) - 1 / 200, 2)
                + pow((1 - b / 100) + 1 / 200, 2)
                - pow(1, 2)
                < 0
            )
            p3 = (
                pow((a / 100 - 1) + 1 / 200, 2)
                + pow((1 - b / 100) - 1 / 200, 2)
                - pow(1, 2)
                < 0
            )
            p4 = (
                pow((a / 100 - 1) + 1 / 200, 2)
                + pow((1 - b / 100) + 1 / 200, 2)
                - pow(1, 2)
                < 0
            )
            # Análise de sinais
            if (1 - p1) * p4 + (1 - p3) * p2 + (1 - p2) * p1 + (1 - p4) * p3:
                img.putpixel((a, b), 1)

    # Salva o resultado na pasta output
    img.save("output/questao1.png")

## Questao 2a
def questao2a():
    # Como a região esta definida entre [-100,100] x [-100,100], devemos realizar a transformacao
    # (x, y) -> (x-100, 100-y)
    img = blackBackground()

    # Calculo da parametrizacao
    for t in range(1000):
        a = int((t / 10) * math.cos(t / 10))
        b = int((t / 10) * math.sin(t / 10))

        img.putpixel((a - 100, 100 - b), 1)

    # Salva o resultado na pasta output
    img.save("output/questao2a.png")

    ## Questao 2b
def questao2b():
    # Como a região esta definida entre [-100,100] x [-100,100], devemos realizar a transformacao
    # (x, y) -> (x-100, 100-y)
    img = blackBackground()
    t = 0

    # Calculo da parametrizacao
    while t <= 100:
        a = int(t * math.cos(t))
        b = int(t * math.sin(t))

        img.putpixel((a - 100, 100 - b), 1)
        t += 1 / math.sqrt(pow(t, 2) + 1)

    # Salva o resultado na pasta output
    img.save("output/questao2b.png")

## Questao 3
def questao3():
    # Como a região esta definida entre [0,1] x [0,1], devemos realizar a transformacao
    # (x, y) -> (x/200,1-y/200)
    img = blackBackground()
    (x, y) = img.size

    for a in range(x):
        for b in range(y):
            p1 = (a / 200) + (1 - b / 200) > 1
            p2 = pow(a / 200, 2) + pow(-b / 200, 2) - pow(1, 2) <= 0
            p3 = pow(a / 200 - 1, 2) + pow(1 - b / 200, 2) - pow(1, 2) <= 0

            if p1 * p2 * p3:
                img.putpixel((a, b), 1)

    # Salva o resultado na pasta output
    img.save("output/questao3.png")

## Questao 4
def questao4():
    # Como a região esta definida entre [-2,2] x [-2,2], devemos realizar a transformacao
    # (x, y) -> (x/50-2,2-y/50)
    img = blackBackground()
    (x, y) = img.size

    for a in range(x):
        for b in range(y):
            p1 = (
                pow((2 - b / 50) - 1 / 100, 2)
                - pow((a / 50 - 2) - 1 / 100, 3)
                + ((a / 50 - 2) - 1 / 100)
                < 0
            )
            p2 = (
                pow((2 - b / 50) + 1 / 100, 2)
                - pow((a / 50 - 2) + 1 / 100, 3)
                + ((a / 50 - 2) + 1 / 100)
                < 0
            )
            p3 = (
                pow((2 - b / 50) + 1 / 100, 2)
                - pow((a / 50 - 2) - 1 / 100, 3)
                + ((a / 50 - 2) - 1 / 100)
                < 0
            )
            p4 = (
                pow((2 - b / 50) - 1 / 100, 2)
                - pow((a / 50 - 2) + 1 / 100, 3)
                + ((a / 50 - 2) + 1 / 100)
                < 0
            )

            if (1 - p1) * p4 + (1 - p3) * p2 + (1 - p2) * p1 + (1 - p4) * p3:
                img.putpixel((a, b), 1)

    # Salva o resultado na pasta output
    img.save("output/questao4.png")

if __name__ == '__main__':
    questao1()
    questao2a()
    questao2b()
    questao3()
    questao4()