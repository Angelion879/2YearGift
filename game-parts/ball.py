from turtle import Turtle
from paddle import paddle
from time import sleep

ball = None

class Ball(Turtle):
    def __init__(self, position):
        super().__init__(shape='circle')
        self.speed(0)
        self.penup()
        self.color('white')
        self.goto(position)
        self.dx = 1
        self.dy = 1

def create_ball():
    global ball
    ball = Ball((0,-349))


def ball_movement():
    global ball
    #ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    

    if ball.xcor() > 435:
        ball.setx(435)
        ball.dx *= -1
    if ball.ycor() > 392:
        ball.sety(392)
        ball.dy *= -1
    if ball.xcor() < -444:
        ball.setx(-444)
        ball.dx *= -1
    if ball.ycor() < -400:
        ball.goto(0,-355)
        ball.dy *= -1
    
    # Paddle colision
    #if (ball.ycor() < -280 and ball.ycor() > -290) and (ball.xcor() < (paddle.xcor() +50) and ball.xcor() > (paddle.xcor() - 50)):
    #    ball.sety(-280)
    #    ball.dy *= -1