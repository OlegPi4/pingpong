import turtle

speed = 5
def moveUp():
    """
    движение вверх на 5 пикселей  при нажатии клавиши "Up"
    """
    x = pen.position()[0]
    y = pen.position()[1]
    pen.setposition(x, y+speed)

def moveDown():
    """
    движение вниз на 5 пикселей  при нажатии клавиши "Down"
    """
    x = pen.position()[0]
    y = pen.position()[1]
    pen.setposition(x, y-speed)

def moveLeft():
    """
    движение влево на 5 пикселей  при нажатии клавиши "Left"
    """
    x = pen.position()[0]
    y = pen.position()[1]
    pen.setposition(x-speed, y)

def moveRight():
    """
    движение вправо на 5 пикселей  при нажатии клавиши "Rigth"
    """
    x = pen.position()[0]
    y = pen.position()[1]
    pen.setposition(x+speed, y)
def change()  :
    """
    Изменение видимости черепашки клавишей "Spase"
    """
    if pen.isvisible():
        pen.up()
        pen.hideturtle()
    else:
        pen.down()
        pen.showturtle()

def speedUp():
    global speed
    speed += 1

def speedDown():
    global speed
    speed = max(0, speed-1)
window = turtle.Screen()
pen = turtle.Turtle()
window.onkey(moveUp, "Up")
window.onkey(moveDown, "Down")
window.onkey(moveLeft, "Left")
window.onkey(moveRight, "Right")
window.onkey(change, "a")
window.onkey(speedUp, "q")
window.onkey(speedDown, "z")

window.listen()
window.mainloop()