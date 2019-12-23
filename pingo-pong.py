import turtle
from random import choice, randint
window = turtle.Screen()
window.title("Ping-Pong")
window.setup(width=1.0, height=1.0)
window.bgcolor(0.2, 0.2, 0.2)
window.tracer(1.0)
border = turtle.Turtle()
border.speed(0)
border.color('green')
border.begin_fill()
border.goto(-500, 300)
border.goto(500, 300)
border.goto(500, -300)
border.goto(-500, -300)
border.goto(-500, 300)
border.end_fill()

border.goto(0, 300)
border.color('white')
border.setheading(270)
for i in range(25):
    if i%2 == 0:
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()
border.hideturtle()

rocket_a = turtle.Turtle()
rocket_a.color('white')
rocket_a.shape('square')
rocket_a.shapesize(stretch_wid=5, stretch_len=1)
rocket_a.penup()
rocket_a.goto(-470, 0)
def move_up_a():
    y = rocket_a.ycor()  # определение координаті у объєкта
    if y <= 240:
        rocket_a.sety(y + 10)
    else:
        rocket_a.set(y)
def move_down_a():
    y = rocket_a.ycor()  # определение координаті у объєкта
    if y >= -240:
        rocket_a.sety(y - 10)
    else:
        rocket_a.sety(y)

rocket_b = turtle.Turtle()
rocket_b.color('white')
rocket_b.shape('square')
rocket_b.shapesize(stretch_wid=5, stretch_len=1)
rocket_b.penup()
rocket_b.goto(470, 0)
def move_up_b():
    y = rocket_b.ycor()  # определение координаті у объєкта
    if y <= 240:
        rocket_b.sety(y + 10)
    else:
        rocket_b.set(y)
def move_down_b():
    y = rocket_b.ycor()  # определение координаті у объєкта
    if y >= -240:
        rocket_b.sety(y - 10)
    else:
        rocket_b.sety(y)

ball = turtle.Turtle()
ball.shape('circle')
ball.speed(0  )
ball.color('red')
ball.penup()
window.listen()
window.onkeypress(move_up_a, "w")
window.onkeypress(move_down_a, "s")
window.onkeypress(move_up_b, "Up")
window.onkeypress(move_down_b, "Down")
ball.dx = 3
ball.dy = -3
while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() >= 290:
        ball.dy = -ball.dy
    if ball.ycor() <= -290:
        ball.dy = -ball.dy
    if ball.xcor() >= 490:
        ball.goto(0,randint(-150, 150))
        ball.dx = choice([-5, -4, -3, 3, 4, 5])
        ball.dy = choice([-5, -4, -3, 3, 4, 5])
    if ball.xcor() <= -490:
        ball.goto(0,randint(-150, 150))
        ball.dx = choice([-5, -4, -3, 3, 4, 5])
        ball.dy = choice([-5, -4, -3, 3, 4, 5])

    if ball.ycor() >= rocket_b.ycor() - 50 and ball.ycor() <= rocket_b.ycor() + 50 and \
        ball.xcor() >= rocket_b.xcor() - 20 and ball.xcor() <= rocket_b.xcor() + 20:
        ball.dx = -ball.dx
    if ball.ycor() >= rocket_a.ycor() - 50 and ball.ycor() <= rocket_a.ycor() + 50 and \
            ball.xcor() >= rocket_a.xcor() - 20 and ball.xcor() <= rocket_a.xcor() + 20:
        ball.dx = -ball.dx

window.mainloop()

