import turtle

wn = turtle.Screen()
wn.title("Pong by Verča")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_A = 0
score_B = 0



#Paddle A
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("green")
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.penup()
paddle_A.goto(-350,0)

#Paddle B
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("yellow")
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.penup()
paddle_B.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx = 0.15 # hýbe se o dva pixely
ball.dy = 0.15
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("PlayerA: 0  PlayerB: 0", align="center", font=("Courier", 24, "normal"))

#Function
def paddle_A_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)

def paddle_A_down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)

def paddle_B_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)

def paddle_B_down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)

#Keyboard binding
wn.listen()
wn.onkeypress(paddle_A_up, "w")
wn.onkeypress(paddle_A_down, "s")
wn.onkeypress(paddle_B_up, "Up")  #klávesy
wn.onkeypress(paddle_B_down, "Down")

#main game loop

while True:
    wn.update()

    #ball move
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_A += 1
        pen.clear()
        pen.write("PlayerA: {}  PlayerB: {}".format(score_A, score_B), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_B += 1
        pen.clear()
        pen.write("PlayerA: {}  PlayerB: {}".format(score_A, score_B), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball touch
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_B.ycor() + 40 and ball.ycor() > paddle_B.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() < -350) and (ball.ycor() > paddle_A.ycor() - 40 and ball.ycor() < paddle_A.ycor()  +40):
        ball.dx *= -1