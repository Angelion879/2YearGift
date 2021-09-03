# MAIN MENU GUI
import turtle
from GUIs import components
from gameWindow import win

left_arrow = None
right_arrow = None

# Texts
def draw_screen():
    global left_arrow, right_arrow
    title = components.Text((0,150), "Lover's BreakOut", 55)
    start_option = components.Text((0, 0), "START GAME", 25)
    level_option = components.Text((0,-50), "ALL LEVELS", 25)
    settings_option = components.Text((0,-100), "SETTINGS", 25)
    exit_option = components.Text((0,-150), "EXIT GAME", 25)

# Selection Arrows
    left_arrow = components.SelectionArrow((-115, 20), 0)
    right_arrow = components.SelectionArrow((115, 20), 180)



def import_functions():
    # Arrows Movement Functions

    def selection_arrows_go_up():
        global left_arrow, right_arrow
        if (left_arrow.ycor() < 20) and (right_arrow.ycor() < 20):
            new_left_Y = left_arrow.ycor() + 50
            new_right_Y = right_arrow.ycor() + 50
            left_arrow.sety(new_left_Y)
            right_arrow.sety(new_right_Y)

    def selection_arrows_go_down():
        if (left_arrow.ycor() > -130) and (right_arrow.ycor() > -130):
            new_left_Y = left_arrow.ycor() - 50
            new_right_Y = right_arrow.ycor() - 50
            left_arrow.sety(new_left_Y)
            right_arrow.sety(new_right_Y)

    # Choose Option Function

    def choose_option():
        if left_arrow.ycor() == 20:
            # Start game option
            win.reset()
            from levels import level01
            level01.draw_the_intro()

        elif left_arrow.ycor() == -30:
            # All Levels option
            win.reset()
            from GUIs import levelSelectGui
            levelSelectGui.draw_screen()
            levelSelectGui.import_functions()

        elif left_arrow.ycor() == -80:
            # Settings option
            win.reset()
            from GUIs import settingsGui
            settingsGui.draw_screen()
            settingsGui.import_functions()

        elif left_arrow.ycor() == -130:
            # Exit option
            turtle.bye()
            exit()

    # Key Binding

    win.onkeypress(selection_arrows_go_down, "Down")
    win.onkeypress(selection_arrows_go_up, "Up")
    win.onkeypress(choose_option, "space")