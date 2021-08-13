# MAIN MENU GUI
import turtle
from turtle import Turtle, hideturtle
from gameWindow import win

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

# Arrows Movement Functions

def selection_arrows_go_up():
    if (left_arrow.ycor() < 15) and (right_arrow.ycor() < 15):
        new_left_Y = left_arrow.ycor() + 50
        new_right_Y = right_arrow.ycor() + 50
        left_arrow.sety(new_left_Y)
        right_arrow.sety(new_right_Y)

def selection_arroes_go_down():
    if (left_arrow.ycor() > -135) and (right_arrow.ycor() > -135):
        new_left_Y = left_arrow.ycor() - 50
        new_right_Y = right_arrow.ycor() - 50
        left_arrow.sety(new_left_Y)
        right_arrow.sety(new_right_Y)

# Choose Option Function

def choose_option():
    if left_arrow.ycor() == 15:
        # Start game option
        pass

    elif left_arrow.ycor() == -35:
        # All Levels option
        win.reset()
        from GUIs import levelSelectGui

    elif left_arrow.ycor() == -85:
        # Settings option
        win.reset()
        from GUIs import settingsGui

    elif left_arrow.ycor() == -135:
        # Exit option
        turtle.bye()
        exit()

# Key Binding

win.onkeypress(selection_arroes_go_down, "Down")
win.onkeypress(selection_arrows_go_up, "Up")
win.onkeypress(choose_option, "space")