import turtle, time, random
window = turtle.Screen()
pen = turtle.Turtle()
pen.speed(0)
def setcolorrandom():
    """
    формирование цвета случайным образом
    :return: возвращает кортеж из трех значений  от 0 до 1
    """
    a = random.random()
    b = random.random()
    c = random.random()
    return a, b, c
def setpos(x, y):
    """
    устанавливает черепашку на координаты x, y  без рисования линии
    """
    pen.up()
    pen.setposition(x, y)
    pen.down()
def painsqear(x, y, a, b, aa, bb, cc):
    """
    рисует и закрашивает прямоугольник x, y координата левого нижнего угла
    :param a: длина по х
    :param b: длина по у
    выбор цвета случайным образом
    """
    pen.hideturtle()
    pen.begin_fill()
    pen.color(aa, bb, cc)
    setpos(x, y)
    pen.goto(x, y+b)
    pen.goto(x+a, y+b)
    pen.goto(x+a, y)
    pen.goto(x,y)
    pen.end_fill()

def setka(lx, ly, n, m, h, w, a, b, c, aa, bb, cc, ws):
    """
    :param lx: координата нижнего левого угла
    :param ly: координата нижнего левого угла
    :param n: количество колонок
    :param m: количество строк
    :param a,b,c: задание цвета фона, значения от 0-1
    :param aa, bb, cc: задание цвета линии сетки, значения от 0-1
    :param ws: толщина линии
    :param h: высота
    :param w: ширина
    """
    window.bgcolor(a, b, c)
    pen.color(aa, bb, cc)
    pen.pensize(ws)
    pen.hideturtle()
    pen.speed(0)
    stepy = h/m
    stepx = w/n
    x = lx
    y = ly
    for k in range(m+1):
        setpos(x,y)
        pen.goto(x+w, y)
        y += stepy
    x = lx
    y = ly
    for k in range(n+1):
        setpos(x,y)
        pen.goto(x, y+h)
        x += stepx

def coleringsqear(lx, ly, n, m, h, w, a, b, c, ws=0):
    """
    зарисовка прямоугольников в поле nxn c дистанцией 3 пикселя
    :param Lx: начало по х (коорд. х чнижнего левого угла первого прямоугольника)
    :param Ly: начало по у  (коорд. у нижнего левого угла первого прямоугольника)
    :param n: колонок
    :param m: строк
    :param h: висота
    :param w: ширина
    :param a,b,c: цвет заливки, значения  от 0-1
    :param ws: ширина линий между квадратами
    """
    x = lx
    y = ly
    stepy = h / m
    stepx = w / n
    for l in range(m):
        for k in range(n):
            painsqear(x+ws, y+ws, stepx-ws-2, stepy-ws-2, a, b, c)
            x += stepx
        y += stepy
        x = lx
time.sleep(1)

pen.speed(1000)
setka(-200, -200, 6, 11, 150, 390, 0.2, 0.6, 0.6, 0.9, 0.3, 0.3, 2)
coleringsqear(-200, -200, 6, 11, 150, 390, 0.5, 0.1, 0.1, ws=2)


window.mainloop()
