from turtle import Turtle

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

# Texts
title = Text((0,150), "Lover's BreakOut", 55)

start_option = Text((0, 0), "START GAME", 25)
level_option = Text((0,-50), "ALL LEVELS", 25)
settings_option = Text((0,-100), "SETTINGS", 25)
exit_option = Text((0,-150), "EXIT GAME", 25)

# Selection Arrows
left_arrow = SelectionArrow((-105, 15), 0)
right_arrow = SelectionArrow((100, 15), 180)