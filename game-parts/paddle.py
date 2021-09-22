from turtle import Turtle

paddle = None

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__(shape='square')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.speed(0)
        self.penup()
        self.color('white')
        self.goto(position)

def create_paddle():
    paddle = Paddle((0, -370))

    def paddle_right():
        global paddle
        x = paddle.xcor()
        x+= 20
        paddle.setx(x)

    def paddle_left():
        global paddle
        x = paddle.xcor()
        x-=20
        paddle.setx(x)