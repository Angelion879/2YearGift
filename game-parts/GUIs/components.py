from turtle import Turtle, hideturtle

class Text(Turtle):
    def __init__(self, position, message, letter_size):
        super().__init__()
        self.speed(0)
        self.color('white')
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.write(message, align="center", font=("Courier", letter_size, "normal")) 

class SelectionArrow(Turtle):
    def __init__(self, position, direction):
        super().__init__(shape='arrow')
        self.speed(0)
        self.color('white')
        self.penup()
        self.goto(position)
        self.left(direction)
