from turtle import Turtle

class Brick(Turtle):
    def __init__(self, position):
        super().__init__(shape='square')
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.speed(0)
        self.penup()
        self.color('white')
        self.goto(position)