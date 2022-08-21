from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.color("blue")
        self.speed("fastest")
        self.shapesize(0.5, 0.5)
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
