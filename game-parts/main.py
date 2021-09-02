from GUIs import mainGui
from gameWindow import win

win.listen()
mainGui.draw_screen()
mainGui.import_functions()

while True:

    win.update()
    