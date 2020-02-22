import turtle

#screen
wn = turtle.Screen()
wn.screensize(canvheight=600, canvwidth=800)
wn.bgcolor("beige")
wn.tracer(0)

#paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("black")
paddle.shapesize(stretch_len=5, stretch_wid=1, outline=7)
paddle.penup() #odstraní čáru
paddle.goto(0,-250)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.shapesize(2,2)
ball.penup()
ball.goto(0,0)
ball.dx = 0.1 # hýbe se o dva pixely
ball.dy = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player: 0 points", align="center", font=("Courier", 15, "normal"))

#function
def paddle_right():
    x = paddle.xcor()
    x += 20
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    x -= 20
    paddle.setx(x)


#Keyboard
wn.listen()
wn.onkeypress(paddle_right, "Right")
wn.onkeypress(paddle_left, "Left")

#score
score = 0

#main game
while True:
    wn.update()

    #ball move
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #bindings
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.xcor() > 348:
        ball.setx(348)
        ball.dx *= -1

    if ball.xcor() < -348:
        ball.setx(-348)
        ball.dx *= -1

    #get point
    if ball.ycor() < -290:
        ball.goto(0,0)
        ball.dy *= -1
        score += 1
        pen.clear()
        pen.write("Player: -{} points".format(score), align="center", font=("Courier", 15, "normal"))

    #paddle touch
    if (ball.ycor() < -220 and ball.ycor() > -230) and (ball.xcor() < paddle.xcor() + 40 and ball.xcor() > paddle.xcor() - 40):
        ball.sety(-220)
        ball.dy *= -1


