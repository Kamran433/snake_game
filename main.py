from turtle import Screen
from snake import Snake
# from score import Score
import time
# sc = Score()
sk = Snake()
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake-Game")
screen.tracer(0)
screen.listen()

while sk.t is True:
    screen.update()
    time.sleep(0.1)
    sk.move()
    if sk.head.distance(sk.food) <= 15:
        sk.food.hideturtle()
        sk.john.clear()
        sk.high()
        sk.john.clear()
        sk.extend()
        sk.foodx()
    sk.endgame()
    screen.onkey(sk.forv, "Up")
    screen.onkey(sk.back, "Down")
    screen.onkey(sk.right, "Right")
    screen.onkey(sk.left, "Left")
print(f"GAME-OVER!\nYour score is : {sk.score - 1}\nNew High-Score : {sk.max}")
screen.exitonclick()