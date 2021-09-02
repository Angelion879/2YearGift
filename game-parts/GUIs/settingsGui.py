from gameWindow import win
from GUIs import components

left_arrow = None
right_arrow = None

def draw_screen():
    settings_title = components.Text((0,150), "Settings", 55)
    
    warning_message = components.Text((0,0), "NO, THERE IS STILL\n NO SETTINGS HERE\nYET, BUT SINCE YOU\nARE HERE... HELLO!", 20)

    go_back = components.Text((0,-70), "BACK TO MENU", 25)

    left_arrow = components.SelectionArrow((-140, -50), 0)
    right_arrow = components.SelectionArrow((135, -50), 180)

def import_functions():
    def back_to_menu():
        win.reset()
        from GUIs import mainGui
        mainGui.draw_screen()
        mainGui.import_functions()

    win.onkeypress(back_to_menu, "space")