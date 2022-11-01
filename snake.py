import turtle
from turtle import Turtle, Screen
import random
TURT = [(0, 0), (-20, 0), (-40, 0)]
screen = Screen()
i = 0
class Snake:
    def __init__(self):
        self.man = Turtle()
        self.man.hideturtle()
        self.max = 0
        self.man.penup()
        self.man.goto(150, 280)
        self.turtlest = []
        self.snake()
        self.move()
        self.head = self.turtlest[0]
        self.t = True
        self.food = Turtle()
        self.john = Turtle()
        self.score = 0
        self.foodx()
        self.endgame()
        with open("score.txt", "r") as sc:
            self.max = int(sc.read())

    def snake(self):
        for pos in TURT:
           self.add_snake(pos)
    def add_snake(self, pos):
        turtles = Turtle("circle")
        turtles.penup()
        turtles.color("red")
        turtles.goto(pos)
        self.turtlest.append(turtles)
    def extend(self):
        self.add_snake(self.turtlest[-1].position())
    def move(self):
            for seg_num in range(len(self.turtlest) - 1, 0, - 1):
                new_x = self.turtlest[seg_num - 1].xcor()
                new_y = self.turtlest[seg_num - 1].ycor()
                self.turtlest[seg_num].goto(new_x, new_y)

            self.turtlest[0].forward(20)
    def forv(self):
      if self.head.heading() != 270:
          self.turtlest[0].setheading(90)
    def back(self):
      if self.head.heading() != 90:
        self.turtlest[0].setheading(270)
    def left(self):
      if self.head.heading() != 0:
        self.turtlest[0].setheading(180)
    def right(self):
      if self.head.heading() != 180:
        self.turtlest[0].setheading(0)
    def endgame(self):
      if self.turtlest[0].xcor() >= 300 or self.turtlest[0].ycor() >= 300 or self.turtlest[0].xcor() <= -300 or self.turtlest[0].ycor() <= -300:
          self.score = 1
          self.head.goto(0, 0)
          # self.t = False
      for i in range(1,len(self.turtlest)):
         if self.head.distance(self.turtlest[i]) <= 15:
             self.score = 1
             self.head.goto(0, 0)
             # self.t = False
    def foodx(self):
      self.john.color("white")
      self.man.color("white")
      self.john.hideturtle()
      self.john.penup()
      self.john.goto(0, 280)
      self.john.write(f"Score : {self.score}", align="center", font=("Arial", 18, "normal"))
      self.score+=1
      self.food.showturtle()
      self.food.shape("square")
      self.food.color("blue")
      self.food.speed("fastest")
      self.food.shapesize(0.5, 0.5)
      x = random.randint(-280, 280)
      y = random.randint(-280, 280)
      self.food.penup()
      self.food.goto(x, y)
    def high(self):
        self.man.write(f"High-score : {self.max}", align="center", font=("Arial", 18, "normal"))
        if self.score>=self.max:
            with open("score.txt", "w") as sc:
                sc.write(f"{self.max + 1}")
            self.man.clear()
            self.max = self.score
        self.man.write(f"High-score : {self.max}", align="center", font=("Arial", 18, "normal"))

