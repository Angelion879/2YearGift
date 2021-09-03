from GUIs import components
from bricks import Brick
from time import sleep

# First part: show the level's phrase
def draw_the_intro():
    for i in range(100,0,-10):
        color = "gray" + str(i)
        title = components.Text((0,150), "Lover's BreakOut", 55, color)
        sleep(0.1)
        title.clear()
    sleep(0.2)
    for i in range(0,100,10):
        color = "gray" + str(i)
        level_name = components.Text((0,0), "It all started with a brick...", 20, color)
        sleep(0.1)
        level_name.clear()
    level_name = components.Text((0,0), "It all started with a brick...", 20)
    sleep(3)
    level_name.clear()
    for i in range(100,0,-10):
        color = "gray" + str(i)
        level_name = components.Text((0,0), "It all started with a brick...", 20, color)
        sleep(0.1)
        level_name.clear()
    
# Second part: draw level and be playable