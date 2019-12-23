import turtle, random

window = turtle.Screen()
bourder = turtle.Turtle()  # init object bourder
bourder.speed(0)
bourder.up()
bourder.hideturtle()
bourder.pensize(5)
bourder.color('green' )
bourder.begin_fill()
bourder.pencolor('red')
bourder.goto(300, 300)
bourder.down()
bourder.goto(300, -300)
bourder.goto(-300, -300)
bourder.goto(-300, 300)
bourder.goto(300, 300)
bourder.end_fill()

ball = turtle.Turtle()  # init the object ball
ball.shape('circle')    # form object
ball.color('blue')
ball.up()
randx = random.randint(-290, 290)
randy = random.randint(-290, 290)
ball.hideturtle()
ball.setposition(randx, randy)
ball.showturtle()
dx = 3                  # defen arrow: 1 add x,  -1 decr x
dy = 4
while True:
    x,y = ball.position()
    if x + dx >= 292 or x + dx <= -292:
        dx = -dx
    if y + dy >= 292 or y + dy <= -292:
        dy = -dy
    ball.goto(x+dx, y+dy)

window.mainloop()