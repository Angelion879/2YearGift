from GUIs import components
from gameWindow import win
from bricks import Brick
import ball as b
import paddle
from time import sleep

level_quote = "It all started with a brick..."
start = False
instruction = None
brick_1 = None

# First part: show the level's phrase
def draw_the_intro():
    global level_quote, instruction
    for i in range(100,0,-10):
        color = "gray" + str(i)
        title = components.Text((0,150), "Lover's BreakOut", 55, color)
        sleep(0.1)
        title.clear()
    sleep(0.3)
    for i in range(0,100,10):
        color = "gray" + str(i)
        level_name = components.Text((0,0), level_quote, 20, color)
        sleep(0.1)
        level_name.clear()
    level_name = components.Text((0,0), level_quote, 20)
    sleep(3)
    level_name.clear()
    for i in range(100,0,-10):
        color = "gray" + str(i)
        level_name = components.Text((0,0), level_quote, 20, color)
        sleep(0.1)
        level_name.clear()

    instruction = components.Text((0,0), "Press Space to start", 20)
    b.create_ball()
    paddle.create_paddle()
    build_bricks()
    win.onkeypress(start_game, "space")

def build_bricks():
    global brick_1
    brick_1 = Brick((0,250))


def start_game():
    global start, instruction
    start = True
    instruction.clear()
    level_loop()

# Second part: draw level and be playable
def level_loop():
    global start, brick_1
    #Start level
    if start:
        while start:
            b.ball_movement()
            if (b.ball.xcor(), b.ball.ycor()) == ((brick_1.xcor()), (brick_1.ycor()-19)):
                brick_1.hideturtle()
                break