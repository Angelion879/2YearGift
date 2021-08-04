from turtle import Turtle

class Ball(Turtle):
    def __init__(self, position):
        super().__init__(shape='circle')
        self.speed(0)
        self.penup()
        self.color('white')
        self.goto(position)

ball = Ball((0,-344))