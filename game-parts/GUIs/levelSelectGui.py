from gameWindow import win
from GUIs import components

left_arrow = None
right_arrow = None

def draw_screen():
    global left_arrow, right_arrow

    level_select_title = components.Text((0,200), "All Levels", 55)

    spoiler_alert = components.Text((0,100), "SPOILER ALERT:", 40)

    spoiler_alert_message = components.Text((-5,-20), "HERE ARE A LOT OF SPOILERS\nOF THE GAME, DO YOU REALLY\n     WANT TO CONTINUE?\n", 20)

    continue_option = components.Text((0,-150), "YES, PLEASE!", 25)
    go_back_option = components.Text((0,-200), "NO! GO BACK!", 25)

    left_arrow = components.SelectionArrow((-135, -130), 0)
    right_arrow = components.SelectionArrow((130, -130), 180)


def write_the_poem():
    level_select_title = components.Text((0,200), "All Levels", 55)

    poem_title = components.Text((0,140),"A PLayable Poem:", 30)

    #A item per verse just because I can & its easier to align
    level_1 = components.Text((0,100), "It all started with a brick", 15)
    level_2 = components.Text((0,80), "And my face", 15)
    level_3 = components.Text((0,60), "And the idea that both would colide one day", 15)
    level_4 = components.Text((0,40), "For the joke that your hand would never reach my head", 15)
    level_5 = components.Text((0,20), "and some other things I said that never made sense", 15)
    level_6 = components.Text((0,0), "turns out I was wrong", 15)
    level_7 = components.Text((0,-20), "and the whole you made it to my brain", 15)

    level_8 = components.Text((0,-60), "and now we are here", 15)
    level_9 = components.Text((0,-80), "together, after two whole years", 15)
    level_10 = components.Text((0,-100), "I love you, with all my heart...", 15)
    level_11 = components.Text((0,-120), "and soul :P", 15)
    level_12 = components.Text((0,-140), "And I hope that someday", 15)
    level_13 = components.Text((0,-160), "we share our last names", 15)
    level_14 = components.Text((0,-180), "and a place", 15)
    level_15 = components.Text((0,-200), "just for me and you", 15)
    final = components.Text((0,-240), "❤", 25)

    go_back = components.Text((0,-300), "BACK TO MENU", 25)

    left_arrow = components.SelectionArrow((-140, -280), 0)
    right_arrow = components.SelectionArrow((135, -280), 180)

def import_functions():
    # Arrows Movement Functions

    def selection_arrows_go_up():
        global left_arrow, right_arrow

        if (left_arrow.ycor() < -130) and (right_arrow.ycor() < -130):
            new_left_Y = left_arrow.ycor() + 50
            new_right_Y = right_arrow.ycor() + 50
            left_arrow.sety(new_left_Y)
            right_arrow.sety(new_right_Y)

    def selection_arrows_go_down():
        if (left_arrow.ycor() > -180) and (right_arrow.ycor() > -180):
            new_left_Y = left_arrow.ycor() - 50
            new_right_Y = right_arrow.ycor() - 50
            left_arrow.sety(new_left_Y)
            right_arrow.sety(new_right_Y)

    # Choose Option Function

    def choose_option():
        if left_arrow.ycor() == -130:
            # Show whole poem
            win.reset()
            write_the_poem()

        elif left_arrow.ycor() == -180 or -280:
            win.reset()
            from GUIs import mainGui
            mainGui.draw_screen()
            mainGui.import_functions()

    # Key Binding

    win.onkeypress(selection_arrows_go_down, "Down")
    win.onkeypress(selection_arrows_go_up, "Up")
    win.onkeypress(choose_option, "space")